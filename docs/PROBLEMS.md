# PROBLEMS — ishkarim-rag

> Hybrydowe wyszukiwanie RAG — FTS5 + embeddingi + RRF, działa w pełni offline na CPU

## ✅ Co ten projekt rozwiązuje

- ✅ Wyszukiwanie semantyczne po dużych bazach wiedzy **bez GPU i bez chmury**
- ✅ Łączenie wyszukiwania leksykalnego (BM25) z semantycznym (embeddingi) przez RRF fusion
- ✅ Deterministyczne, powtarzalne wyniki — te same wyniki przy tym samym zapytaniu
- ✅ Indeksowanie setek dokumentów w jednym pliku SQLite (< 10 MB na 843 docs)
- ✅ Filtrowanie wyników po obszarach tematycznych

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Generowanie odpowiedzi — to RAG *retrieval*, nie ma LLM w pętli
- ❌ Real-time indexing — zmiana dokumentu wymaga przebudowy indeksu (`build_index.py`)
- ❌ Multi-modal search — tylko tekst, nie obrazy/audio
- ❌ Skalowalność do milionów dokumentów — SQLite ma ograniczenia przy ~100k+
- ❌ Wyszukiwanie cross-językowe bez dodatkowej konfiguracji tokenizera

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **Embeddingi all-MiniLM-L6-v2 (384-dim)** — dokładniejsze modele (np. BGE-M3) dają lepsze wyniki kosztem RAM i czasu
- ⚠️ **FTS5 tokenizer unicode61** nie rozumie polskiej fleksji — lematyzacja wymaga Morfeusz2 (patrz `ishkarim-nlp`)
- ⚠️ **RRF k=60** nie jest dostrojony pod ten korpus — można ulepszyć przez ablację BEIR
- ⚠️ **search.db** nie aktualizuje się automatycznie po zmianach w WORK.md — wymaga ręcznego `python3 scripts/build_index.py`
- ⚠️ **Brak cache wyników** — każde zapytanie odczytuje bazę; dla prod dodaj Redis/lru_cache

---

## 🎯 Przypadki użycia

- 🎯 Firmowa baza wiedzy z semantycznym wyszukiwaniem (offline, dane nie opuszczają sieci)
- 🎯 System Q&A nad dokumentacją techniczną produktu
- 🎯 Narzędzie dla researcherów / analityków do przeszukiwania notatek
- 🎯 Fundament pod RAG-pipeline z własnym LLM (llama.cpp / Ollama)

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
