"""
fts5.py — fragmenty kodu z WORK.md dla obszaru rag.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 3 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: FTS5 mikro‑bench: pomiar mJ - op z RAPL — CPU‑only
def read_energy_uj(zone_path):
    return int(open(f"{zone_path}/energy_uj").read())

before = read_energy_uj("/sys/class/powercap/intel-rapl:0")
# ... operacje FTS5 ...
after = read_energy_uj("/sys/class/powercap/intel-rapl:0")
max_range = int(open(f"{zone_path}/max_energy_range_uj").read())
delta_uj = after - before
if delta_uj < 0:
    delta_uj += max_range  # wrap-around
mj_per_op = (delta_uj / 1000) / ops_count

# ────────────────────────────────────────────────────────────

# Source: Lematyzacja w czasie zapytania z Morfeusz2 i plWordNet
from apsw.fts5 import SynonymTokenizer
morf = morfeusz2.Morfeusz()
def variants_for_query_token(token):
    token = unicodedata.normalize("NFC", token).strip()
    lemmas = {ana[2][1] for ana in morf.analyse(token)}
    syns = plwordnet_synonyms_from_db(token)
    result = [token] + sorted(lemmas - {token}) + sorted(syns - {token})
    return tuple(result)
tok = SynonymTokenizer(get=variants_for_query_token)
con.register_fts5_tokenizer("pl_syn", tok)

# ────────────────────────────────────────────────────────────

# Source: Lokalny deterministyczny RAG na CPU_02
# Atomowy zapis CAS
tmp_fd, tmp_name = tempfile.mkstemp(prefix="cas_", dir=str(self.tmp_dir))
# ... zapis ...
os.replace(tmp_name, dst_path)   # atomowy rename w obrębie FS

# Deterministyczna normalizacja
def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", text)
    return text

# Run Registry - stabilny JSON
def stable_json(obj): 
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",",":"))

# Tie-break FTS5
SELECT seg_id, bm25(docs_fts) AS bm25_score
FROM docs_fts WHERE docs_fts MATCH ?
ORDER BY bm25_score ASC, doc_key ASC  -- deterministyczne remisy
