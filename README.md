# ishkarim-rag

> **Hybrydowe wyszukiwanie RAG — FTS5 + embeddingi + RRF, działa w pełni offline na CPU**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Wyszukiwanie semantyczne po dużych bazach wiedzy
- Łączenie wyszukiwania leksykalnego (BM25) z semantycznym (embeddingi) przez RRF fusion
- Deterministyczne, powtarzalne wyniki — te same wyniki przy tym samym zapytaniu

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-rag

# Demo (10 sekund)
python projects/ishkarim-rag/demo.py
```

## Użycie w kodzie

```python
import ishkarim_rag as m

# Wszystkie 235 katalogi wiedzy obszaru 'rag'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_rag.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Firmowa baza wiedzy z semantycznym wyszukiwaniem (offline, dane nie opuszczają sieci)
- System Q&A nad dokumentacją techniczną produktu
- Narzędzie dla researcherów / analityków do przeszukiwania notatek

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 235 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_rag.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_rag_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_rag.py --quick
```

## Struktura projektu

```
ishkarim-rag/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 235 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_rag/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_rag.py         ← testy jednostkowe
│   └── test_rag_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_rag.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 235 katalogów wiedzy obszaru `rag`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
