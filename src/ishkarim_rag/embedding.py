"""
embedding.py — kod wyekstrahowany z WORK.md dla obszaru rag.

Zawiera 3 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Demo hybrydowe: SQLite FTS5 + sqlite‑vec z RRF i ranx
doc_id = hashlib.sha256(text.encode()).hexdigest()[:16]
chunk_id = hashlib.sha256(f"{doc_id}:{seq}:{chunk_text}".encode()).hexdigest()[:16]
embedding_blob = struct.pack(f'<{len(vec)}f', *vec)  # float32 LE

# Source: Porównanie FTS5 (BM25) i FAISS-CPU KNN
SEED = 42
N = 20000    # liczba dokumentów/wektorów
D = 256      # wymiar embeddingów
K = 10       # top-k
Q = 200      # liczba zapytań
WARMUPS = 5
COLD_REPEATS = 3
PIN_CORE = 2

# Source: Prosty monitoring dryfu embeddingów na CPU_04
{
  "series_key": str,          # deterministyczny, stabilny
  "obs_id": str,              # sha256(...) — idempotentne
  "ts_utc": float,            # UNIX timestamp (event-time)
  "embedding": list[float],   # lub None (loguj tylko skalary)
  "source_type": str,         # "user_query" | "doc_chunk" | ...
  "embedding_model_id": str,
  "tokenizer_id": str,
  "pipeline_version": str
}
