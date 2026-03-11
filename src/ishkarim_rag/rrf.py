"""
rrf.py — kod wyekstrahowany z WORK.md dla obszaru rag.

Zawiera 16 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Adaptacyjna fuzja z wagami zależnymi od zapytania
w, meta = policy.weights(q, runs)
  ranked = fuse_rrf(q, runs, weights_map=w)
  ranked = clamp_and_renorm(ranked)

# Source: Aktualizacja z 18–22 lutego - RRF jako standard w ekosystemie
def rrf_fuse(ranked_lists, k=60, per_list_weight=None):
    scores = {}
    for li, hits in enumerate(ranked_lists):
        w = float(per_list_weight[li]) if per_list_weight else 1.0
        for rank, hit in enumerate(hits, start=1):
            scores[hit.doc_id] = scores.get(hit.doc_id, 0.0) + w * (1.0 / (k + rank))
    return sorted(scores.items(), key=lambda x: (-x[1], x[0]))  # deterministyczny tie-break

# Source: Benchmarki lokalne: FTS5 + wektory
def rrf(rankings: dict[str, list[int]], k0: int = 60) -> dict[int, float]:
    scores = {}
    for method_ranks in rankings.values():
        for rank, doc_id in enumerate(method_ranks, 1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k0 + rank)
    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

# Source: Czy coś pokona RRF? Wyniki i plan testów
if challenger_ndcg > baseline_ndcg + threshold and p_value < 0.05:
    active_method = challenger
else:
    active_method = "rrf"   # fallback

# Source: Demo hybrydowe: SQLite FTS5 + sqlite‑vec z RRF i ranx
def rrf(rankings: dict[str, list[str]], k: int = 60) -> dict[str, float]:
    scores = {}
    for run_name, doc_ids in rankings.items():
        for rank, doc_id in enumerate(doc_ids, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return dict(sorted(scores.items(), key=lambda x: (-x[1], x[0])))

# Source: Deterministic local RAG with CPU‑only indexing
def rrf_fuse(per_source: dict, weights: dict, k=60, topk=20):
    scores, prov = {}, {}
    for src_name, hits in per_source.items():
        w = weights.get(src_name, 1.0)
        for rank, (doc_id, raw_score) in enumerate(hits):
            scores[doc_id] = scores.get(doc_id, 0.0) + w / (k + rank + 1)
            prov.setdefault(doc_id, []).append((src_name, rank, raw_score))
    return sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:topk], prov

# Source: Deterministyczny RAG z SQLite FTS5 i Tantivy
# Deterministyczne ID dokumentu
import hashlib
def make_doc_id(canonical_key: str) -> str:
    return hashlib.sha256(canonical_key.encode()).hexdigest()

def make_chunk_id(doc_version_id: str, chunk_index: int, chunk_hash: str) -> str:
    key = f"{doc_version_id}:{chunk_index}:{chunk_hash}"
    return hashlib.sha256(key.encode()).hexdigest()

# RRF score
def rrf_score(ranks: list[int], k: int = 60) -> float:
    return sum(1.0 / (k + r) for r in ranks)

# Source: Fuzja RRF i ranx — gotowy kod OSS
# Deterministyczna fuzja RRF
fused = fuse(runs=runs, method="rrf", params={"k": 60}, norm=None)

# Kanonizacja: sort + re-rank
items.sort(key=lambda x: (-float(x[1]), str(x[0])))
for r, (doc_id, _) in enumerate(items, start=1):
    scores[str(doc_id)] = -float(r)

# Source: Lokalny harness ewaluacji retrievalu
from ranx import Qrels, Run, fuse, evaluate
qrels = Qrels.from_file("data/qrels.trec")
runs = [Run.from_file(f, kind="trec") for f in run_files]
rrf = fuse(runs, method="rrf", params={"k": 60})
cmz = fuse(runs, method="combmnz")
print(evaluate(qrels, rrf, ["ndcg@10", "recall@10", "mrr@10"]))

# Source: Nowe badania — normalizacja wyników i znaczenie determinizmu
def rrf_score(ranks: list[int], k: int = 60) -> float:
    return sum(1.0 / (k + r) for r in ranks)

# Total order: sort by (fused_score DESC, stable_doc_id ASC)
results.sort(key=lambda x: (-x.fused_score, x.stable_doc_id))

# Source: Nowe frameworki RoutIR i TEMPO dla RAG
# Weighted RRF
def weighted_rrf(rankings, weights, k=60):
    scores = defaultdict(float)
    for name, r in rankings.items():
        w = weights.get(name, 1.0)
        for idx, doc_id in enumerate(r, start=1):
            scores[doc_id] += w * (1.0 / (k + idx))
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# Context packing + citation validation
packed = pack_context(ranked_chunks, ctx_limit_tokens=8192, ...)
prompt, sid_map = build_prompt(question, packed)
text = llm.generate(prompt)
ok, bad = validate_citations(text, set(sid_map.keys()))

# Source: QuackIR — powtarzalne benchmarki BEIR na SQLite i DuckDB
def _rrf_fuse(sparse_ranked, dense_ranked, rrf_k, Kh):
    # tie-breaker: doc_id ASC
    scored = {d: 1/(rrf_k+pos) for pos,d in enumerate(sparse_ranked, 1)}
    for pos, d in enumerate(dense_ranked, 1):
        scored[d] = scored.get(d, 0) + 1/(rrf_k+pos)
    return sorted(scored.keys(), key=lambda d: (-scored[d], d))[:Kh]

# Source: Semantic interfaces and flow visualization for knowledge bases
# Hybrid fuse plan (planner.py)
ops.append(Op("adaptive_vector_candidates", {"vq": ir.vq, "topk": topk, "c0": 300, "cmax": 2000, "growth": 2.0}))
ops.append(Op("fts_candidates", {"tq": ir.tq, "max": limits.max_candidates}))
ops.append(Op("rank_fuse_rrf", {"k": 60}))
ops.append(Op("sql_filter_candidates_ranked", {"filters": ir.filters}))
ops.append(Op("sql_fetch_ranked", {"select": ir.select, "topk": topk}))
return Plan(ops=ops, strategy="hybrid_fuse")

# Source: Sygnały z ekosystemu FTS5 - regresje i aktywność
def rrf_fuse(fid, broad, k=60, prefer_source="fid"):
    rf = {h.docid: i+1 for i, h in enumerate(fid)}
    rb = {h.docid: i+1 for i, h in enumerate(broad)}
    docids = sorted(set(rf.keys()) | set(rb.keys()))
    # score = sum(1/(k+rank)) per source

# Source: Wzorce RRF dla hybrydowego RAG w SQLite
def rrf_fuse(fts_ranks, vec_ranks, k_rrf=60, w_fts=1.0, w_vec=1.0):
    scores = {}
    for rank, chunk_id in enumerate(fts_ranks, 1):
        scores[chunk_id] = scores.get(chunk_id, 0) + w_fts / (k_rrf + rank)
    for rank, chunk_id in enumerate(vec_ranks, 1):
        scores[chunk_id] = scores.get(chunk_id, 0) + w_vec / (k_rrf + rank)
    return sorted(scores, key=lambda x: (-scores[x], x))  # tie-break po chunk_id

# Source: Zwinne lokalne RAG w SQLite
# chunk_key — deterministyczny, niezależny od kolejności ingestu
chunk_key = sha256(f"{doc_key}:{chunk_ord}:{sha256(chunk_text)}")
chunk_id = int(chunk_key[:15], 16) & 0x7FFFFFFFFFFFFFFF  # bez high-bit

# index_meta — strict mode
meta = conn.execute("SELECT backend,dim,chunker,vec_enabled,model_fingerprint FROM index_meta").fetchone()
if meta != expected:
    raise RuntimeError("index_meta mismatch — przebuduj indeks")

# Tie-break w zapytaniu (deterministyczny)
ORDER BY rrf_score DESC, chunk_id ASC
