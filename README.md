# ishkarim-rag

> Hybrydowe wyszukiwanie RAG: FTS5 BM25 + embeddingi + RRF fusion. Lokalne, deterministyczne, CPU-first.

## Instalacja

```bash
pip install -e projects/ishkarim-rag
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-rag
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_rag as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **235 katalogów** obszaru `rag`:

- `20‑minutowy eksperyment dla odzyskania impetu`
- `Adaptacyjna fuzja z wagami zależnymi od zapytania`
- `Advances in Long‑Lived Agent Architectures`
- `Agenci narracyjni w pętli RAG`
- `Agent TODO PoC CPU-only i bezpieczeństwo`
- `Agent TODO jako kontrolowany automat pracy`
- `Agent TODO z dokumentów ekstrakcja i audyt`
- `Agentowe RAG - LangGraph 1.0.6 i nowe dema IBM-Microsoft`
- … i 227 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### 20‑minutowy eksperyment dla odzyskania impetu

# WORK: 20‑minutowy eksperyment dla odzyskania impetu
## 0-Metadane
- Katalog: 20‑minutowy eksperyment dla odzyskania impetu
- Pliki: 14 (bez placeholderów; pliki 1–14 zawierają treść, 15–60 są puste)
- Tagi: sprint, 3-warianty, FTS5, benchmark, SQLite, DoD-lite, decyzje, produktywność

### Adaptacyjna fuzja z wagami zależnymi od zapytania

# WORK: Adaptacyjna fuzja z wagami zależnymi od zapytania
## 0-Metadane
- Katalog: Adaptacyjna fuzja z wagami zależnymi od zapytania
- Pliki: 18 (bez placeholderów)
- Tagi: RAG, fuzja-rankingów, wagi-adaptacyjne, RRF, QPP, bandit, supervised, kalibracja, offline-pipeline, harness, NDCG, TREC

### Advances in Long‑Lived Agent Architectures

# WORK: Advances in Long‑Lived Agent Architectures
## 0-Metadane
- Katalog: Advances in Long‑Lived Agent Architectures
- Pliki: 20 (bez placeholderów; pliki 21–60 puste)
- Tagi: long-lived-agents, persistent-memory, lifecycle, SQLite, FTS5, offline, checkpointing, replay, self-maintenance, retrieval, hash-chain


## Struktura projektu

```
ishkarim-rag/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 235 katalogów-źródeł
├── src/
│   └── ishkarim_rag/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_rag.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-rag/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
