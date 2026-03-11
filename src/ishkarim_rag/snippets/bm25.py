"""
bm25.py — fragmenty kodu z WORK.md dla obszaru rag.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 12 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: CUBO  - RAG CPU-first z pełną powtarzalnością
def route(query_features) -> Tier:
    if has_entity_id(query_features):   return Tier.BM25_ONLY
    if is_short(query_features):        return Tier.HOT_HYBRID
    if hits_semantic_cache(query):      return Tier.CACHE
    if cold_available:                  return Tier.FULL_HYBRID
    return Tier.HOT_HYBRID

# ────────────────────────────────────────────────────────────

# Source: Deterministyczny RAG na CPU z mini-zbiorem
# Inkrementalny sync — sprawdź sha1
def sha1_hex(s: str) -> str:
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

# Priorytety w rankingu BM25 (SQL)
# rank = bm25(...) + prio_lambda * (max_prio - source.priority)
# ORDER BY rank, doc_id, chunk_id   -- deterministyczny tie-break

# Atomowy snapshot
def atomic_write_text(path, text):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# ────────────────────────────────────────────────────────────

# Source: Fraktalny słownik: trzy krótkie prompty do rozbudowy grafu pojęć
def resolve(query_text, threshold=0.5):
    norm = variant_norm(query_text)
    rows = db.execute(
        "SELECT canonical_id, bm25(variants_fts) AS score "
        "FROM variants_fts WHERE variant_norm MATCH ? "
        "ORDER BY score LIMIT 10", [norm]).fetchall()
    # Grupuj po canonical_id, sprawdź kolizje
    ...

# ────────────────────────────────────────────────────────────

# Source: Klocki do mikro‑benchmarków retrievalu
def rrf_score(rank, k=60): return 1.0 / (k + rank)
combined = defaultdict(float)
for r, (doc_id, _) in enumerate(bm25_results): combined[doc_id] += rrf_score(r)
for r, (doc_id, _) in enumerate(dense_results): combined[doc_id] += rrf_score(r)
final = sorted(combined.items(), key=lambda x: (-x[1], x[0]))  # tie-break by id

# ────────────────────────────────────────────────────────────

# Source: Lekki harness CPU + siatka ablacji BEIR
# Stabilne sortowanie w BM25 run (mergesort = stable)
idxs = np.argsort(-scores, kind="mergesort")

# Identyfikator eksperymentu z konfiguracji
exp_id = hashlib.sha256(stable_json(config).encode()).hexdigest()[:12]

# Fuzja RRF przez ranx
fused_rrf = fuse([bm25_run, dense_run], method="rrf", params={"k": 60})
metrics = evaluate(qrels_r, fused_rrf, metrics=["ndcg@10", "recall@100"])

# ────────────────────────────────────────────────────────────

# Source: Lekki harness do CombMNZ i BordaFuse
from ranx import Run, Qrels, fuse, evaluate
combmnz = fuse([bm25, splade, e5], method="combmnz")
borda   = fuse([bm25, splade, e5], method="borda")
rrf     = fuse([bm25, splade, e5], method="rrf", k=60)
evaluate(qrels, run, metrics=["ndcg@10","map@100"])

# ────────────────────────────────────────────────────────────

# Source: Lokalny harness ewaluacji retrievalu
sql = """
    SELECT d.doc_id, bm25(docs_fts, 1.0, 0.5) AS s
    FROM docs_fts JOIN docs d ON d.rowid = docs_fts.rowid
    WHERE docs_fts MATCH ? AND {where}
    ORDER BY s LIMIT ?
"""
# Wynik: score = float(-s)  ← negacja bo bm25() mniejszy = lepszy

# ────────────────────────────────────────────────────────────

# Source: Lokalny hybrydowy retriever RAG + FTS + SQLite
# Dual-index router (uproszczony)
def search(query, k_fts=200, k_final=20):
    cands = con.execute(
        "SELECT d.id, bm25(docs_fts) AS score FROM docs_fts "
        "JOIN docs d ON d.id=docs_fts.rowid WHERE docs_fts MATCH ? "
        "ORDER BY score LIMIT ?", (query, k_fts)).fetchall()
    q = embed(query).astype("float32")
    scored = [(cosine(q, vecs[r["id"]]), r) for r in cands if r["id"] in vecs]
    scored.sort(reverse=True, key=lambda x: x[0])
    return [r for _, r in scored[:k_final]]

# Próg "nie wiem"
c1 = max_cosine  # 0..1
c2 = min(1, len(hits)/k_final)
c3 = 1 - missing_vec_ratio
confidence = max(0, min(1, 0.7*c1 + 0.2*c2 + 0.1*c3))
if confidence < 0.4:
    return {"mode": "dont_know", "hypothesis": ..., "gaps": ...}

# ────────────────────────────────────────────────────────────

# Source: Minimalny, deterministyczny pipeline FTS5-wektory-RRF
def hybrid_search(query, k_rrf=60, k_fts=50, k_vec=50):
    fts = db.query("SELECT doc_id, bm25(...) AS score FROM documents_fts
                    WHERE ... MATCH ? ORDER BY score LIMIT ?", [query, k_fts])
    vec = db.query("SELECT doc_id, distance FROM documents_vec
                    WHERE embedding MATCH ? AND k = ?", [qvec, k_vec])
    rrf = {}
    for rank, row in enumerate(fts, 1): rrf[row.doc_id] += 1/(k_rrf+rank)
    for rank, row in enumerate(vec, 1): rrf[row.doc_id] += 1/(k_rrf+rank)
    return sorted(rrf.items(), key=lambda x: (-x[1], x[0]))

# ────────────────────────────────────────────────────────────

# Source: Smarter quantization makes CPUs competitive again
sql = """
SELECT c.chunk_id, c.doc_id, c.text, c.start_char, c.end_char,
       bm25(chunks_fts) AS score
FROM chunks_fts
JOIN chunks c ON c.chunk_id = chunks_fts.rowid
WHERE chunks_fts MATCH ?
ORDER BY score LIMIT ?;"""

# ────────────────────────────────────────────────────────────

# Source: Wzorce hybrydowe RAG w SQLite_05
def rrf_score(rank: int, k: int = 60) -> float:
    return 1.0 / (k + rank)

def hybrid_search(fts_candidates, embed_query_fn, load_vec_fn, top_k=8, rrf_k=60):
    qv = embed_query_fn(query_text)
    cands = [Cand(chunk_id=cid, bm25=bm) for cid, bm in fts_candidates]
    for c in cands:
        c.cos = cosine(qv, load_vec_fn(c.chunk_id))
    for i, c in enumerate(sorted(cands, key=lambda x: x.bm25), 1):
        c.rank_bm = i
    for i, c in enumerate(sorted(cands, key=lambda x: -x.cos), 1):
        c.rank_vec = i
    for c in cands:
        c.rrf = rrf_score(c.rank_bm, rrf_k) + rrf_score(c.rank_vec, rrf_k)
    return sorted(cands, key=lambda x: -x.rrf)[:top_k]

# ────────────────────────────────────────────────────────────

# Source: Zestaw audytowy deterministycznej fuzji hybrydowej
def rrf(ranks_bm25: list, ranks_dense: list, k=60, scale=1_000_000) -> list:
    scores = {}
    for rank, doc_id in enumerate(ranks_bm25, 1):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    for rank, doc_id in enumerate(ranks_dense, 1):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    # kwantyzacja → int dla stabilnego total order
    quantized = {doc_id: round(s * scale) for doc_id, s in scores.items()}
    # total order: malejący score_int, tie-break rosnący doc_id
    return sorted(quantized.items(), key=lambda x: (-x[1], x[0]))
