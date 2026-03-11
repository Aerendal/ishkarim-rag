"""
rag.py — fragmenty kodu z WORK.md dla obszaru rag.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 4 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: FTS5 mikro‑bench: pomiar mJ - op z RAPL — CPU‑only
# Każdy repeat startuje od pustej bazy!
for repeat in range(N):
    db = ":memory:"  # lub tmpfs
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("CREATE VIRTUAL TABLE t USING fts5(body, tokenize='unicode61')")
    E_before = read_energy()
    conn.executemany("INSERT INTO t VALUES(?)", batch)
    conn.commit()
    E_after = read_energy()
    results.append((E_after - E_before) / len(batch))

# ────────────────────────────────────────────────────────────

# Source: Główne źródła i ograniczenia FTS5
PRAGMAS = ["journal_mode","synchronous","temp_store","cache_size","mmap_size","foreign_keys"]

def verified_config(db_path, out_path):
    conn = sqlite3.connect(db_path)
    cfg["sqlite_version"] = conn.execute("SELECT sqlite_version()").fetchone()[0]
    cfg["sqlite_source_id"] = conn.execute("SELECT sqlite_source_id()").fetchone()[0]
    cfg["compile_options"] = [r[0] for r in conn.execute("PRAGMA compile_options")]
    cfg["pragmas"] = {p: conn.execute(f"PRAGMA {p}").fetchone()[0] for p in PRAGMAS}
    # + smoke test: CREATE FTS → INSERT → MATCH 'kot' → zapisz hits
    Path(out_path).write_text(json.dumps(cfg, ensure_ascii=False, indent=2))

# ────────────────────────────────────────────────────────────

# Source: Testy niezmienników i offsetów FTS5_04
def utf8_slice(text: str, byte_off: int, byte_len: int) -> str:
    b = text.encode("utf-8")
    frag = b[byte_off: byte_off + byte_len]
    return frag.decode("utf-8")  # przecięcie UTF-8 → wyjątek = FAIL

# ────────────────────────────────────────────────────────────

# Source: Wizualne interfejsy bazy wiedzy i relacji
# Stabilne ID węzłów
make_node_id("Module", "qa", "core.storage")  # → "Module:qa:core.storage"
make_edge_id("DEPENDS_ON", src, dst)           # → "DEPENDS_ON:src->dst:<sha1>"

# Deterministyczne sortowanie przed eksportem (KLUCZOWY patch)
nodes.sort(key=lambda n: n.id)
edges.sort(key=lambda e: e.id)

# Incremental: stable_hash(src) porównywany przed nadpisaniem
