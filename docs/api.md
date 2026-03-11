# API — ishkarim_rag

> Hybrydowe wyszukiwanie RAG: FTS5 BM25 + embeddingi + RRF fusion.

## Moduł główny: `ishkarim_rag`

```python
import ishkarim_rag
```

### Publiczne atrybuty

| Atrybut | Typ | Opis |
|---------|-----|------|
| `__version__` | `str` | Wersja pakietu (np. `"0.1.0"`) |
| `__area__` | `str` | Nazwa obszaru tematycznego (`"rag"`) |
| `MODULES` | `list[str]` | Lista 303 nazw katalogów-źródeł |

### `load_knowledge_index(root=None) → list[dict]`

Zwraca listę rekordów metadanych dla wszystkich katalogów-źródeł obszaru.

**Parametry:**
- `root` — ścieżka do katalogu głównego repozytorium (opcjonalne, autodiscovery jeśli `None`)

**Zwraca:** listę słowników z kluczami:
```python
{
    "name":     str,   # nazwa katalogu (np. "Hybrid RAG w SQLite")
    "doc_id":   str,   # identyfikator (np. "DOC-RAG-0042")
    "maturity": str,   # FROZEN | DECISION | DRAFT
    "area":     str,   # "rag"
}
```

**Przykład:**
```python
import ishkarim_rag

docs = ishkarim_rag.load_knowledge_index()
print(f"Znaleziono {len(docs)} katalogów")

# Filtruj po dojrzałości
frozen = [d for d in docs if d["maturity"] == "FROZEN"]
print(f"FROZEN: {len(frozen)}")
```

---

## Moduł: `ishkarim_rag.utils`

```python
from ishkarim_rag.utils import read_work_md, extract_tags, extract_python_blocks
```

### `def read_work_md(dir_path: str | Path) -> str:`

Wczytuje WORK.md z podanego katalogu.

### `def extract_tags(dir_path: str | Path) -> dict:`

Parsuje TAGS.md i zwraca słownik metadanych.

### `def extract_python_blocks(work_md: str) -> list[str]:`

Wyodrębnia bloki ```python z tekstu Markdown.


---

## Snippety kodu: `ishkarim_rag.snippets`

Fragmenty kodu wyekstrahowane z WORK.md (referencyjne, nie produkcyjne):

- `snippets/bm25.py`
- `snippets/rag.py`
- `snippets/extracted.py`
- `snippets/rerank.py`
- `snippets/fts5.py`
- `snippets/rrf.py`
- `snippets/embedding.py`
- `snippets/retriever.py`

### Jak używać snippetów

```python
# Snippety są dostępne jako pliki .py w katalogu snippets/
# Możesz je przeglądać, kopiować fragmenty do własnych projektów

import importlib.util, pathlib
snippet_path = pathlib.Path(ishkarim_rag.__file__).parent / "snippets" / "retrieved_snippet.py"
# Przeczytaj jako tekst (bezpieczniejsze niż import dla fragmentów z błędami):
print(snippet_path.read_text())
```

---

## Rozszerzenia i zależności opcjonalne

```bash
# Podstawowe (bez ML)
pip install -e "projects/ishkarim-rag"

# Z modelami embeddings (dla RAG)
pip install -e "projects/ishkarim-rag[rag]"

# Z narzędziami SQLite
pip install -e "projects/ishkarim-rag[sqlite]"

# Środowisko deweloperskie (z pytest)
pip install -e "projects/ishkarim-rag[dev]"
```

---

## Uruchomienie testów

```bash
# Testy jednostkowe (bez danych repo)
pytest projects/ishkarim-rag/tests/test_rag.py -v

# Testy domenowe (wymagają repo Ishkarim)
pytest projects/ishkarim-rag/tests/test_rag_domain.py -v

# Wszystkie testy
pytest projects/ishkarim-rag/tests/ -v

# Z pokryciem kodu
pytest projects/ishkarim-rag/tests/ --cov=ishkarim_rag --cov-report=term-missing
```

---

## Benchmarki

```bash
python projects/ishkarim-rag/benchmarks/bench_rag.py
```

*Wygenerowano automatycznie przez `scripts/enrich_projects.py`*
