"""
extracted.py — kod wyekstrahowany z WORK.md dla obszaru rag.

Zawiera 84 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Agentowe RAG - LangGraph 1.0.6 i nowe dema IBM-Microsoft
# Minimalny executor grafowy (offline, zero deps)
class GraphExecutor:
    def run(self, state: dict) -> dict:
        current = self.entry
        while True:
            fn = self.nodes[current]
            attempt = 0
            while True:
                start = time.time()
                try:
                    result = fn(state)
                    state.update(result)
                    break
                except Exception as e:
                    attempt += 1
                    if attempt > self.max_retries:
                        raise NodeError(f"Node '{current}' failed") from e
            if current == self.finish:
                return state
            current = self.edges.get(current)

# Source: Benchmarki lokalne: FTS5 + wektory
# NIGDY nie dziel na poziomie chunka — dziel po source_doc_id
source_ids = list(set(chunk['source_path'] for chunk in chunks))
random.shuffle(source_ids)  # seed stały!
train_ids = source_ids[:70%]; dev_ids = ...; test_ids = ...

# Source: Czy coś pokona RRF? Wyniki i plan testów
# query-level split, nie doc-level
from sklearn.model_selection import GroupKFold
gkf = GroupKFold(n_splits=5)
for train_idx, test_idx in gkf.split(X, y, groups=query_ids): ...

# Source: Demo hybrydowe: SQLite FTS5 + sqlite‑vec z RRF i ranx
from ranx import Qrels, Run, evaluate, compare
qrels = Qrels.from_dict({"q1": {"doc1": 1, "doc2": 0}})
run_hyb = Run.from_dict({"q1": {"doc1": 0.9, "doc2": 0.4}})
results = evaluate(qrels, run_hyb, metrics=["ndcg@10", "recall@100"])
report = compare([run_lex, run_vec, run_hyb], qrels, stat_test="student", random_seed=42)

# Source: Deterministic local RAG with CPU‑only indexing
def check_gate_b(golden, run, epsilon=1e-6):
    for qid, exp_docids in golden.items():
        got_docids = run.get(qid, [])
        if got_docids != exp_docids:
            return {"status": "FAIL", "qid": qid}
    return {"status": "OK"}

# Source: Deterministic local RAG with CPU‑only indexing
def atomic_symlink_swap(link_path: Path, target: Path) -> None:
    tmp = link_path.with_name(link_path.name + ".tmp")
    if tmp.exists() or tmp.is_symlink():
        tmp.unlink()
    tmp.symlink_to(target)
    os.replace(tmp, link_path)  # atomowe na tym samym filesystemie

# Source: Deterministyczne indeksy JSONB w SQLite
# Atomowy zapis artefaktów
def atomic_write_text(path, text):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# Source: Deterministyczne lokalne RAG z SQLite i Soar
cand = window.rfind("\n\n", back, rel_target + 1)  # preferencja podwójny newline
if cand == -1: cand = window.rfind("\n", back, rel_target + 1)
if cand == -1: cand = window.rfind(" ", back, rel_target + 1)
# fallback: twarde cięcie na target_end

# Source: Deterministyczne lokalne RAG z SQLite i Soar
dst = sqlite3.connect(str(out_path))
con.backup(dst, pages=0)  # cały backup; nie używaj VACUUM INTO (problemy z bindingami)
dst.close()

# Source: Deterministyczny RRF i stabilne metryki
dataset_id = sha256_hex(canon_json_bytes(dataset_manifest_without_id))
run_id     = sha256_hex(canon_json_bytes({dataset_id, config_id, eligibility_sha256,
                                          gates_sha256, pipeline_version, code_build_id,
                                          env_fingerprint}))

# Source: Deterministyczny harness fuzji rankingów w Pythonie
def canonical_sort(doc2score):
    return sorted(doc2score.items(), key=lambda kv: (-kv[1], kv[0]))

def sha256_lines(lines):
    h = hashlib.sha256()
    for l in lines:
        h.update((l + "\n").encode("utf-8"))
    return h.hexdigest()

# Source: Deterministyczny harness fuzji rankingów w Pythonie
from ranx import Run, fuse

def fuse_and_canon(runs, norm, method, params):
    fused = fuse(runs, norm=norm, method=method, params=params)
    per_qid = {}
    for qid in fused.run.keys():
        doc2score = fused.get_run(qid)
        canon = canonical_sort(doc2score)
        ordered_ids = [d for d, _ in canon]
        per_qid[qid] = {
            "ordered_ids": ordered_ids,
            "sha256": sha256_lines(ordered_ids),
            "top10": ordered_ids[:10],
        }
    return per_qid

# Source: Deterministyczny harness fuzji rankingów w Pythonie
import os
for k in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS",
          "VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(k, "1")

# Source: Deterministyczny harness fuzji rankingów w Pythonie
def test_quality_gate_ndcg10_not_regress():
    ref_ndcg = ...  # z baseline
    for vdir in sorted(base.iterdir()):
        cur_ndcg = json.loads((vdir/"metrics_aggregate.json").read_text())["aggregate"]["nDCG@10"]
        assert cur_ndcg >= ref_ndcg - 0.01

# Source: Dobór k z uwzględnieniem budżetu CPU
import numpy as np
def bootstrap_ci(mrr_scores, n_boot=1000, alpha=0.05):
    boot = [np.mean(np.random.choice(mrr_scores, len(mrr_scores))) for _ in range(n_boot)]
    return np.percentile(boot, [100*alpha/2, 100*(1-alpha/2)])

# Source: Dostrajanie SQLite FTS w indeksowaniu wiedzy agentów
# Normalizacja app-side
def normalize_pl(text):
    text = text.replace('_', ' ').replace('-', ' ')
    # camelCase split, diakrytyki → ascii (opcjonalnie)
    return text.lower().strip()

# Source: Dwa krótkie demka i skrypty bench do uruchomienia
PROFILES = {
  "baseline_safe":  {"journal_mode":"WAL","synchronous":"NORMAL","wal_autocheckpoint":1000,"cache_size":-200000},
  "wal_latency":    {"journal_mode":"WAL","synchronous":"NORMAL","wal_autocheckpoint":200, "cache_size":-200000},
}

# Source: Eksperyment z kwantyzacją embeddingów
def quantize_int8_per_row(E, eps=1e-12):
    maxabs = np.max(np.abs(E), axis=1)
    scales = np.maximum(maxabs / 127.0, eps).astype(np.float32)
    Q = np.rint(E / scales[:, None]).clip(-127, 127).astype(np.int8)
    return Q, scales

# Source: Energo-metryka CPU-only dla FTS-bench
class PowercapZone:
    path: str; name: str; max_range_uJ: Optional[int]

def _energy_delta(prev_uJ, now_uJ, max_range_uJ):
    # Poprawna obsługa wrap-around
    if now_uJ >= prev_uJ: return now_uJ - prev_uJ
    return (max_range_uJ - prev_uJ) + now_uJ

# API: meter.begin() → wykonaj batch → result = meter.end()
# result: {e_run_uJ, t_run_ns, sensor_metadata}

# Source: Energo-metryka CPU-only dla FTS-bench
def measure(cmd_run, cmd_idle, n_ops, repeats=7):
    idle_uJ = statistics.median([run_batch(cmd_idle, 0).uJ for _ in range(5)])
    runs = [run_batch(cmd_run, n_ops) for _ in range(repeats)]
    net_uJ = [max(0, r.uJ - idle_uJ) for r in runs]
    # Zwraca: mJ/op p50/p95, lat_ms/op p50/p95, throughput_kops p50/p95

# Source: Ewaluacja i wersjonowanie indeksów w deterministycznym RAG
s = s.replace("\r\n", "\n")
s = re.sub(r"[ \t]+", " ", s)
s = re.sub(r"\n{3,}", "\n\n", s)
return s.strip()

# Source: FTS5  - mikropomiarowy harness z konfiguracją CI
# bench/fts_harness.py
meter = EnergyMeter()          # z energy_meter.py
meter.begin()
run_fts_batch(conn, queries, n=N_OPS)
result = meter.end()           # {e_run_uJ, t_run_ns, sensor_metadata}
record = {
    "run_id": uuid4().hex,
    "commit": GIT_SHA,
    "sqlite_version": conn.execute("SELECT sqlite_version()").fetchone()[0],
    "tokenizer": TOKENIZER,
    "n_ops": N_OPS,
    "mj_op": result.e_net_uJ / 1000 / N_OPS,
    "lat_ms_op": result.t_run_ns / 1e6 / N_OPS,
}

# Source: FTS5 brak nowych poprawek offsetów i highlightów_04
def render_highlight(text: bytes, hits, pre="<b>", post="</b>"):
    hits = sorted(hits, key=lambda x: (x[0], -x[1]))
    merged = []
    for s,e in hits:
        if not merged: merged.append([s,e])
        else:
            ls,le = merged[-1]
            if s <= le: merged[-1][1] = max(le, e)
            else: merged.append([s,e])
    out = []; pos = 0
    for s,e in merged:
        out.append(html.escape(text[pos:s].decode("utf-8")))
        out.append(pre + html.escape(text[s:e].decode("utf-8")) + post)
        pos = e
    out.append(html.escape(text[pos:].decode("utf-8")))
    return "".join(out)

# Source: FTS5 i reranking wektorowy — wzorce CPU‑first_04
@dataclass
class RunResult:
    t_fts_ms: float; t_knn_ms: float; t_fuse_ms: float
    n_candidates: int; k: int; union_size: int; final_size: int

def timed(fn):
    t0 = time.perf_counter(); out = fn()
    return (time.perf_counter() - t0) * 1000.0, out
# bench(): warmup + N iteracji; summarize(): median/p90 per (scenario, qid)

# Source: FreshRSS 1.28 delivers better search and sorting
# Flow: FreshRSS → normalizacja → SQLite canonical record
record = {
    "doc_id": sha256(url + title),
    "url": ..., "title": ..., "source": ...,
    "published_at": ..., "fetched_at": ...,
    "length": len(content_text),
    "tags": [...],
    "content_text": cleaned,
    "meta_json": {...}
}

# Source: Fuzja rankingów ranx — RRF i CombMNZ lokalnie
# per-qid metryki z ranx
evaluate(qrels, run, metrics, return_mean=True,
         save_results_in_run=True, make_comparable=True)
scores_per_qid = run.scores["ndcg@10"]  # dict qid→float

# Paired randomization test (deterministyczny)
deltas = [fused_scores[qid] - baseline_scores[qid] for qid in qids]
observed = sum(d > 0 for d in deltas) / len(deltas)

# Source: GraphQLite: grafowe rozszerzenie SQLite z Cypher
# Ładowanie rozszerzenia (tylko zaufany tryb lokalny)
conn.enable_load_extension(True)
conn.load_extension("./libgraphqlite.so")
conn.enable_load_extension(False)
conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS graph USING graph()")

# Source: Główne źródła i ograniczenia FTS5
# Simple (kontrolowany AST, tylko tokeny + OR):
match_expr = " OR ".join(f'"{t}"' for t in tokenize(user_input))
# Advanced (pełna składnia + limity):
if advanced and len(user_input) < MAX_QUERY_LEN:
    match_expr = user_input  # + progress handler timeout

# Source: Harness deterministyczny FTS5 dla CI
# bounds check
if start < 0 or end > len(body) or start >= end:
    offsets_mismatches += 1

# snippet oracle (wzorzec, nie równość literalna)
SNIP_PATTERNS = [("jaźń", r".*<b>jaźń</b>.*"), ("emoji", r".*<b>emoji</b>.*"), ...]

# logical hash
logical_hash = sha256_text(json.dumps(logical_payload, ensure_ascii=False, sort_keys=True))

# Source: Hybrid RAG w praktyce: BM25 + wektory + RRF
def make_chunk_id(doc_id: str, start: int, end: int, chunk_text: str) -> str:
    h = hashlib.sha256(chunk_text.encode("utf-8")).hexdigest()[:16]
    return f"{start:08d}-{end:08d}-{h}"

# Source: Hybrid RAG w praktyce: BM25 + wektory + RRF
def l2_normalize(x: np.ndarray, eps=1e-12) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    return x / np.maximum(norms, eps)

# Source: Hybrydowe wyszukiwanie SQLite + Tantivy_04
with sqlite_conn:
    sqlite_conn.execute("INSERT INTO docs_latest ... ON CONFLICT DO UPDATE ...")
    sqlite_conn.execute("INSERT INTO doc_events(doc_id, event_type, payload_json, created_utc) VALUES ...")
# indexer reads outbox:
for event in fetch_pending_events(conn):
    writer.delete_term(Term.from_field_text("doc_id", event.doc_id))
    writer.add_document(...)
writer.commit()
reader.reload()
mark_events_done(conn, event_ids)
save_checkpoint(conn, tantivy_generation, last_event_id)

# Source: Hybrydowy stack FTS5 + wektory
fts = [(rid, rank) ...]   # SELECT rowid, rank FROM chunks_fts ...
vec = [(rid, rank) ...]   # ANN wynik z sqlite-vec
k = 60
scores = {}
for rid, r in fts: scores[rid] = scores.get(rid, 0) + 1/(k + r)
for rid, r in vec: scores[rid] = scores.get(rid, 0) + 1/(k + r)
top = sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:50]  # tie-break doc_id

# Source: Interfejsy semantyczne do baz wiedzy_001
@dataclass(frozen=True)
class ExplainSignals:
    vector_hit: bool; text_hit: bool
    vec_score: Optional[float]; txt_score: Optional[float]
    vec_norm: Optional[float]; txt_norm: Optional[float]
    vec_contrib: Optional[float]; txt_contrib: Optional[float]
    notes: Optional[str]

# Source: Kendall τ jako miara stabilności rankingu
# Pseudokod τ-b
ids = sorted(intersect(A.keys(), B.keys()))
rankA = rank_positions(A, ids)
rankB = rank_positions(B, ids)
for each pair {i,j}:
  sA = sign(rankA[i] - rankA[j])
  sB = sign(rankB[i] - rankB[j])
  if sA==0 or sB==0: ties++
  elif sA==sB: con++
  else: dis++
tau = (con-dis) / sqrt((con+dis+tiesA)*(con+dis+tiesB))

# Source: Klocki do mikro‑benchmarków retrievalu
energy_before = int(open("/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj").read())
# ... operacja ...
energy_after = int(open("/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj").read())
energy_mj = (energy_after - energy_before) / 1e3

# Source: Kompatybilność: sqlite‑vec, sqlite‑vss, sqlite‑vector
import struct, hashlib
def to_blob(vec_list: list[float]) -> bytes:
    blob = struct.pack(f"<{len(vec_list)}f", *vec_list)
    return blob  # len == dim * 4

def vec_sha256(blob: bytes) -> bytes:
    return hashlib.sha256(blob).digest()

# Source: Lekki pakiet microbenchów dla sqlite‑vec i hybrid SQL_04
random.seed(args.seed)                      # deterministyczny seed
queries.sort(key=lambda x: x[0])            # sort po qid
# warmup_runs=3, measure_runs=12, batch per próbka
samples = run_scenario(conn, sql, params, warmup=3, runs=12)
# zapis: samples_sec + p50/p95/p99 + parametry do results.jsonl

# Source: Lekki pakiet microbenchów dla sqlite‑vec i hybrid SQL_04
meter = pyRAPL.Measurement(tag); meter.begin()
# ... operacja ...
meter.end()
j = meter.export_as_json()  # total_pkg [µJ], dram [µJ]

# Source: Lematyzacja i synonimy PL w FTS5
@lru_cache(maxsize=200_000)
def lemma_of_token(tok): ...  # morf.analyse(tok) → pierwsza baza → lower
def lemmatize_text(text): ...  # TOKEN_RE.finditer → lemma_of_token
def ingest_many(db, rows): ...  # BEGIN; INSERT docs_fts; COMMIT

# Source: Lematyzacja w czasie zapytania z Morfeusz2 i plWordNet
@dataclass(frozen=True)
class SearchRequest:
    query: str; mode: Literal["literal","advanced"] = "literal"
    expansion: Literal["none","lemmas","lemmas_syns"] = "lemmas_syns"
    ranking: Literal["strict_only","strict_expanded_fused"] = "strict_expanded_fused"
    k_final: int = 20; time_budget_ms: float = 5.0

# Source: Lokalne demo hybrydowego RAG w SQLite
def fts_safe_query(user_text: str) -> str:
    tokens = user_text.strip().split()
    return " AND ".join('"' + t.replace('"','""') + '"' for t in tokens) or '""'

# Source: Lokalny graf wiedzy z wizualizacją_04
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns([{"label": "TECH", "pattern": "SQLite"},
                    {"label": "TECH", "pattern": "Litestream"}])

# Source: Lokalny wzorzec hybrydowy- FTS5 + BM25 + Embeddingi
def cosine(q_blob: bytes, d_blob: bytes) -> float:
    q = np.frombuffer(q_blob, dtype=np.float32)
    d = np.frombuffer(d_blob, dtype=np.float32)
    return float(np.dot(q, d))  # normy=1 → iloczyn skalarny = cosine
con.create_function("cosine", 2, cosine)

# Source: Lokalny wzorzec hybrydowy- FTS5 + BM25 + Embeddingi
def pack_f32(vec: np.ndarray) -> bytes:
    assert vec.dtype == np.float32
    return vec.tobytes()
def l2_normalize(vec): return vec / (np.linalg.norm(vec) + 1e-12)
def unpack_f32(blob: bytes): return np.frombuffer(blob, dtype=np.float32)

# Source: Metryki spójności i pokrycia dla lokalnych testów RAG
def nli_label(premise, hypothesis):
    inputs = tok(premise, hypothesis, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = mdl(**inputs).logits
    probs = torch.softmax(logits, dim=-1).squeeze()
    idx = int(torch.argmax(probs))
    return ["contradiction","neutral","entailment"][idx], probs.tolist()

# Source: Metryki spójności i pokrycia dla lokalnych testów RAG
import ir_measures
from ir_measures import nDCG, Recall
metrics = ir_measures.calc([nDCG@10, Recall@20], qrels, run)

# Source: Metryki spójności i pokrycia dla lokalnych testów RAG
assert recall_at_10 >= baseline_recall_at_10 * 0.95, \
    f"Recall@10 regression: {recall_at_10:.3f} < {baseline_recall_at_10:.3f}"
assert contradiction_rate <= 0.10, f"NLI contradiction_rate too high: {contradiction_rate:.2%}"

# Source: Mikro‑benchmark FTS5 krok po kroku
start = time.perf_counter()
cur.execute("SELECT rowid FROM fts WHERE fts MATCH ? LIMIT ?", [q, k])
cur.fetchall()
elapsed = time.perf_counter() - start

# Source: Minimalny lokalny skrypt ewaluacyjny i ryzyka
per_mut_seed = int(hashlib.sha256(
    f"{global_seed}|{base_qid}|{mutation_type}|{i}".encode()
).hexdigest(), 16) % 2**32
random.seed(per_mut_seed)

# Source: Minimalny lokalny skrypt ewaluacyjny i ryzyka
from ir_measures import read_trec_qrels, read_trec_run, calc_aggregate
import ir_measures as ir
qrels = read_trec_qrels('qrels.tsv')
run   = read_trec_run('run.tsv')
print(calc_aggregate([ir.Recall@10, ir.nDCG@10], qrels, run))

# Source: Minimalny lokalny skrypt ewaluacyjny i ryzyka
def norm_text(s):
    import unicodedata
    s = unicodedata.normalize("NFKC", s)
    return " ".join(s.strip().split())

# qid_mut format: f"{base_qid}-{mutation_type}-{i:02d}"
# run format: topicid Q0 docid rank score run-tag (6 kolumn)

# Source: Mini‑korpus FTS5 z testami offsetów PL_04
def find_all_spans(hay_bytes, needle_bytes):
    out, i = [], 0
    while True:
        j = hay_bytes.find(needle_bytes, i)
        if j < 0: break
        out.append((j, j + len(needle_bytes)))
        i = j + 1
    return out

# Dla TOKEN: filtruj po is_token_boundary()
# Dla SUBSTRING: zwróć wszystkie spans bez filtrowania

# Source: New research on AI memory models_04
# Minimalny kontrakt memory_item (plik 1/8):
{
  "content": "...",
  "type": "episodic|semantic|procedural",
  "source": "tool|user|assistant",
  "confidence": 0.85,
  "valid_from_utc": "2026-01-01T00:00:00Z",
  "valid_to_utc": null,
  "status": "active|stale|superseded|retracted",
  "version": 1,
  "logical_id": "uuid-stable"
}

# Reguła R4 (konflikt):
# Jeśli istnieje active (subject, predicate) z innym object
# → nowa wersja + poprzedni.status = "superseded" + krawędź "contradicts"

# Graf DAG: krawędzie typowane (plik 3/8):
# depends_on, derived_from, corrected_by, supersedes, causes
# Reguła: src.ts ≤ dst.ts (DAG w obrębie wątku)

# Source: Nowe wydanie sqlite‑vec z wbudowanymi benchmarkami
PROFILE_MEMORY = {"journal_mode": "memory", "cache_size": -64000}
PROFILE_WAL    = {"journal_mode": "WAL", "synchronous": "NORMAL",
                  "cache_size": -32000, "wal_autocheckpoint": 0}

# Source: Nowe wydanie sqlite‑vec z wbudowanymi benchmarkami
for page_sz in [4096, 8192, 16384]:
    for chunk_sz in [64, 256, 1024]:
        run_bench(page_size=page_sz, chunk_size=chunk_sz, n_vecs=50000, dim=384)

# Source: Nowości: RAG i inżynieria wiedzy
chunk_id = "chk_" + sha256_hex(
    f"{doc_id}|{profile_hash}|{start}|{end}|{text_sha256}".encode()
)[:32]

# Source: Obsługa polskich znaków w SQLite FTS5
# ASCII-fold łącznie z ł→l
import unicodedata
def ascii_fold(text: str) -> str:
    text = text.lower()
    text = text.replace('ł', 'l').replace('Ł', 'l')
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

# Source: Obsługa polskich znaków w SQLite FTS5
_PL_EXTRA = str.maketrans({"ł": "l", "Ł": "L"})
def fold_ascii_pl(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.translate(_PL_EXTRA)
    return s.lower()

# Source: Odmładzanie RAG z zachowaniem determinizmu
# Metryki świeżości
fresh_pct = fresh_count / total_topk_count * 100
stale_hit = stale_count / total_topk_count * 100
drift_rate = drifted_count / refreshed_count * 100

# Source: Porównanie FTS5 (BM25) i FAISS-CPU KNN
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
random.seed(SEED); np.random.seed(SEED)
psutil.Process(os.getpid()).cpu_affinity([PIN_CORE])

# Source: RAG w SQLite: FTS5 + Vector + AI lokalnie
def canonical_json(obj) -> str:  # JCS RFC 8785: sort kluczy, brak spacji, Decimal dla liczb
def hash_json(obj) -> str:        # SHA-256(canonical_json_bytes(obj))
def hash_keyed(parts: list[tuple[str, bytes]]) -> str:  # name\0len\0bytes dla złożonych kluczy
cache_key = hash_keyed([("user_text", normalize_user_text(q).encode()), ("params", canonical_json_bytes(params)), ...])

# Source: RAG‑TUI — terminalowy inspektor chunków
# Kalibracja progu similarity
def pick_threshold(scores_pos, scores_neg, target_recall=0.90, neg_percentile=0.95):
    t_neg = np.percentile(scores_neg, neg_percentile * 100)
    for t in np.linspace(t_neg, 1.0, 200):
        recall = np.mean(scores_pos >= t)
        if recall >= target_recall:
            return float(t)
    return float(t_neg)

# Source: Receptura lokalnego RAG z metrykami CPU-cost
# Deterministyczny wybór indeksu (canary)
h = int(hashlib.sha256(query.encode()).hexdigest(), 16) % 100
if h < router_cfg["canary_pct"]:
    return router_cfg["canary"]
return router_cfg["primary"]

# Source: Retro podgląd FTS5 — live TUI_04
START, END = "⟦", "⟧"

def parse_highlight_to_rich(s):
    out = Text(); plain_chars = []; spans = []
    i = 0; plain_pos = 0; in_hit = False; hit_start = None
    while i < len(s):
        if s.startswith(START, i):
            in_hit = True; hit_start = plain_pos; i += len(START); continue
        if s.startswith(END, i):
            in_hit = False
            if hit_start is not None: spans.append((hit_start, plain_pos))
            i += len(END); continue
        ch = s[i]
        plain_chars.append(ch)
        out.append(ch, style="bold red" if in_hit else "")
        plain_pos += 1; i += 1
    return "".join(plain_chars), out, spans

# Source: Retro podgląd FTS5 — live TUI_04
def on_input_changed(self, event):
    self._last_query = event.value
    if self._debounce_timer: self._debounce_timer.stop()
    self._debounce_timer = self.set_timer(0.15, self._run_query, pause=False)

# Source: SQLite 3.51.2 naprawia potencjalny deadlock w interfejsie unix
# Weryfikacja SHA3-256 tarballa (bez zewnętrznych narzędzi)
import hashlib, pathlib
def sha3_256_file(p):
    h = hashlib.sha3_256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

# Source: Semantic interfaces and flow visualization for knowledge bases
# SecurityPolicy — path guard
def assert_path_allowed(self, path: str) -> None:
    ap = os.path.abspath(path)
    for root in self.allowed_roots:
        if ap == os.path.abspath(root) or ap.startswith(os.path.abspath(root) + os.sep):
            return
    raise PermissionError(f"Path not allowed by policy: {ap}")

# Source: Semantic interfaces and flow visualization for knowledge bases
# FTS fallback w NLU
if vq_text:
    return QueryIR(..., vq=VectorQuery(text=vq_text, topk=topk), tq=None)
query_text = _extract_query_text_fallback(text)
if query_text:
    return QueryIR(..., vq=None, tq=TextQuery(text=query_text, topk=topk))

# Source: Semantyczne interfejsy i AI w symulacjach gier
import sqlglot
from sqlglot import exp

def validate_sql_ast(sql, schema_obj, dialect="sqlite"):
    tables_def = {t["name"]: set(t.get("columns", [])) for t in schema_obj.get("tables", [])}
    tree = sqlglot.parse_one(sql, read=dialect)
    used_tables = {t.name for t in tree.find_all(exp.Table)}
    unknown_tables = [t for t in used_tables if t not in tables_def]
    # ... walidacja aliasów i kolumn

# Source: Semantyczne interfejsy i AI w symulacjach gier
CheckItem(key="validation_loop", weight=2.0,
  positive_markers=("parse","AST","EXPLAIN","dry run","repair loop","iterative"),
  negative_markers=("one-shot","single pass","direct generation"))

# Source: Szablony repozytoriów FTS5 z Morfeusz2_04
import morfeusz2
m = morfeusz2.Morfeusz()
def pl_lemmas(text):
    return [interp[2].split(':')[0] for _,_,interp in m.analyse(text)]

# Source: Szablony repozytoriów FTS5 z Morfeusz2_04
recall@5 delta >= -0.01          # quality gate
page_count growth <= 0.15        # cost gate (lemma=first)
match_p95 growth <= 0.20         # latency gate

# Source: Szablony repozytoriów FTS5 z Morfeusz2_04
ALPH = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
PUNC = " -–—''.,:;()[]\n\t"
rng = random.Random(12345)
# 300–500 próbek, 0–2048 znaków; sprawdza base==overlay surface stream

# Source: Szybkie testy jakości embeddingów_04
# Deterministyczna normalizacja
def l2_normalize(x, eps=1e-12):
    n = np.linalg.norm(x, axis=1, keepdims=True)
    return x / np.maximum(n, eps)

# Deterministyczny Top-k z tie-breakiem
order = np.lexsort((idx, -scores))  # tie-break by doc_id

# Verdict z root_cause_hint
if drift["p50"] < t.emb_cos_p50_min: return "FAIL", "DETERMINISM"
if nnc["rbo_mean"] < t.nnc_rbo_mean_min: return "FAIL", "METRIC_NORMALIZATION"
if ann["recall@10"] < t.ann_vs_exact_recall10_min: return "FAIL", "ANN_PARAMS"

# Source: TREC‑ToT — fuzja BM25 i gęstych modeli (RRF)
def write_trec_run(path, runs, tag="myrun"):
    for qid, docs in runs.items():
        for rank, (docid, score) in enumerate(docs, start=1):
            f.write(f"{qid} Q0 {docid} {rank} {score:.6f} {tag}\n")

# Source: Test CI dla stabilności offsets() i snippet() w języku polskim
# Probe matrix (z pliku 01.md)
def test_probe_matrix():
    queries = ["żarł OR jaźń"]
    results = {
        "unicode61": run_mode("unicode61", queries),
        "icu":        run_mode("icu", queries),
        "custom":     run_mode("custom", queries),
    }
    assert results["unicode61"]["offsets"] == EXPECTED["unicode61"]["offsets"]

# Source: Test CI dla stabilności offsets() i snippet() w języku polskim
# Mapowanie byte-offset → char-index (z pliku 08.md)
def build_utf8_byte_to_char_map(s: str) -> list[int]:
    b = s.encode("utf-8", errors="strict")
    m = [0] * (len(b) + 1)
    i_char = 0; i = 0
    while i < len(b): ...  # O(n), deterministyczne
    return m

# Source: Wbudowany tokenizer Morfologik FSA dla FTS5
import sys, pathlib
data = pathlib.Path(sys.argv[1]).read_bytes()
hexbytes = ",".join(f"0x{b:02x}" for b in data)
pathlib.Path(sys.argv[2]).write_text(
    f'#include <stddef.h>\nconst unsigned char kFsa[] = {{ {hexbytes} }};\n'
    f'const size_t kFsaSize = sizeof(kFsa);\n')

# Source: Wykrywanie dryfu semantycznego dokumentów
def detect_drift(prev_vecs, curr_vecs, tau, model_changed):
    sims = [cos_sim(prev_vecs[cid], v) for cid, v in curr_vecs.items() if cid in prev_vecs]
    tau_eff = tau - 0.02 if model_changed else tau
    return {"flag": mean(sims) < tau_eff, "mean": mean(sims), "median": median(sims)}

# Source: Wzorce CPU→GPU dla energooszczędnego lokalnego RAG‑a
if gap_score >= threshold and doc_count >= min_docs:
    route_to_gpu(task)
else:
    return cpu_result

# Source: Wzorzec idempotentnego ingestu FTS5
for row in new_rows:
    new_hash = sha256(row['title'] + ' ' + row['body'])
    cur.execute("SELECT text_hash FROM docs WHERE id=?", (row['id'],))
    existing = cur.fetchone()
    if existing is None:
        cur.execute("INSERT INTO docs(id,title,body,text_hash) VALUES(?,?,?,?)",
                    (row['id'], row['title'], row['body'], new_hash))
    elif existing[0] != new_hash:
        cur.execute("UPDATE docs SET title=?,body=?,text_hash=? WHERE id=?",
                    (row['title'], row['body'], new_hash, row['id']))
    # else: brak zmiany, pomijamy (idempotencja)

# Source: Zbieranie przykładów przez rozbieżność rankingów
def disagreement_score(rank_a, rank_b, k):
    ra = rank_a if rank_a is not None else (k + 1)
    rb = rank_b if rank_b is not None else (k + 1)
    return float(abs(ra - rb))

# Source: Zwinne i deterministyczne RAG-i w SQLite
# Normalizacja PL (przed INSERT i przy zapytaniu)
import unicodedata
def normalize(text: str, fold_diacritics: bool = True) -> str:
    t = unicodedata.normalize('NFC', text).casefold()
    if fold_diacritics:
        t = t.translate(PL_FOLD_TABLE)
    return t
