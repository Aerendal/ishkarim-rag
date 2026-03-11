"""
ishkarim_rag — moduł z obszaru rag.

Hybrydowe wyszukiwanie RAG: FTS5 BM25 + embeddingi + RRF fusion. Lokalne, deterministyczne, CPU-first.

Źródła: 235 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "rag"



MODULES: list[str] = [
    '20‑minutowy eksperyment dla odzyskania impetu',
    'Adaptacyjna fuzja z wagami zależnymi od zapytania',
    'Advances in Long‑Lived Agent Architectures',
    'Agenci narracyjni w pętli RAG',
    'Agent TODO PoC CPU-only i bezpieczeństwo',
    'Agent TODO jako kontrolowany automat pracy',
    'Agent TODO z dokumentów ekstrakcja i audyt',
    'Agentowe RAG - LangGraph 1.0.6 i nowe dema IBM-Microsoft',
    'Aktualizacja z 18–22 lutego - RRF jako standard w ekosystemie',
    'Architektura deterministycznych systemów RAG',
    'Archiwum Hacker News 22\u202fGB w przeglądarce',
    'Audyt zmian RAG przez semantyczne diffy',
    'BM25 i embeddingi — przewodnik strojenia',
    'Benchmarki CPU‑first dla SQLite RAG',
    'Benchmarki lokalne: FTS5 + wektory',
    'Bezpieczne VACUUM i REBUILD przy migracjach WAL',
    'Bezpieczne migracje i sanity-check dla FTS5',
    'Blueprinty dla sub‑sekundowego RAG',
    'Brak offsets() w FTS5 — jak wyjaśnić trafienia',
    'CLI do inspekcji offsetów i diffów FTS5',
    'CPU‑First Design for Local AI Systems',
    'CPU‑Only AGI: Key Developments',
    'CUBO  - RAG CPU-first z pełną powtarzalnością',
    'CUBO: mierzalny benchmark hybrydowy BM25+dense',
    'Checklist audytu tokenizacji FTS5',
    'Chroma 1.4.1 — prywatne sieci i GroupBy w RAG',
    'Crawler jako ekstraktor grafów dziedzinowych',
    'Czy coś pokona RRF? Wyniki i plan testów',
    'Demo hybrydowe: SQLite FTS5 + sqlite‑vec z RRF i ranx',
    'Detektory osieroconych rekordów FTS5',
    'Deterministic local RAG with CPU‑only indexing',
    'Deterministic offline RAGs for reproducible results',
    'Deterministyczne indeksy JSONB w SQLite',
    'Deterministyczne lokalne RAG z SQLite i Soar',
    'Deterministyczne polityki remisów w BEIR',
    'Deterministyczne łączenie wyników: struktura i zabezpieczenia',
    'Deterministyczny RAG na CPU z mini-zbiorem',
    'Deterministyczny RAG z SQLite FTS5 i Tantivy',
    'Deterministyczny RRF i stabilne metryki',
    'Deterministyczny harness fuzji rankingów w Pythonie',
    'Deterministyczny lokalny RAG i jego odświeżanie',
    'Deterministyczny lokalny RAG na CPU',
    'Deterministyczny mikro‑harness FTS5: inwarianty i szybka lista kontrolna',
    'Dobór k z uwzględnieniem budżetu CPU',
    'Dobór wymiarów embeddingów w SQLite',
    'Dokumenty jako graf YAML SQLite Graphviz_04',
    'Dostrajanie SQLite FTS w indeksowaniu wiedzy agentów',
    'Dwa krótkie demka i skrypty bench do uruchomienia',
    'Eksperyment z kwantyzacją embeddingów',
    'Energo-metryka CPU-only dla FTS-bench',
    'Ewaluacja i wersjonowanie indeksów w deterministycznym RAG',
    'FRTR‑Bench — multimodalne testy RRF',
    'FTS5  - mikropomiarowy harness z konfiguracją CI',
    'FTS5 brak nowych poprawek offsetów i highlightów_04',
    'FTS5 i reranking wektorowy — wzorce CPU‑first_04',
    'FTS5 micro‑benchmarki dla wydajności_02',
    'FTS5 mikro‑bench: pomiar mJ - op z RAPL — CPU‑only',
    'FTS5 z\u202fICU i\u202fmorfologią polską — powtarzalne testy',
    'FTS5 — notatki patchowe i przepisy PRAGMA_04',
    'Federacyjny RAG na SQLite',
    'Fraktalny słownik: trzy krótkie prompty do rozbudowy grafu pojęć',
    'Fresh RAG & knowledge-engineering hits',
    'FreshRSS 1.28 delivers better search and sorting',
    'Fuzja RRF i ranx — gotowy kod OSS',
    'Fuzja rankingów ranx — RRF i CombMNZ lokalnie',
    'GraphQLite: grafowe rozszerzenie SQLite z Cypher',
    'GraphRAG — nowe dema i repo',
    'Główne źródła i ograniczenia FTS5',
    'Harness deterministyczny FTS5 dla CI',
    'Hybrid Knowledge Graph + RAG in SQLite',
    'Hybrid RAG w praktyce: BM25 + wektory + RRF',
    'Hybrydowe RAG+FTS i ontologie w SQLite',
    'Hybrydowe wyszukiwanie FTS + wektory w SQLite',
    'Hybrydowe wyszukiwanie SQLite + Tantivy_04',
    'Hybrydowy RAG w SQLite FTS5 + wektory w jednym pliku',
    'Hybrydowy RAG z deterministycznym filtrem leksykalnym FTS5',
    'Hybrydowy stack FTS5 + wektory',
    'ICU 78.2 i wpływ na tokenizację FTS5',
    'IRB — automatyczny benchmark faktualności RAG',
    'Interfejsy semantyczne Cytoscape.js i YASGUI',
    'Interfejsy semantyczne do baz wiedzy_001',
    'Interfejsy semantyczne z wizualną ścieżką dowodową',
    'Iteracyjny agent TODO‑→akcja dla dokumentów',
    'Kendall τ jako miara stabilności rankingu',
    'Kiedy dodać wektory do BM25',
    'Kiedy rozbudować BM25 o warstwę wektorową',
    'Klocki do mikro‑benchmarków retrievalu',
    'Kompatybilność: sqlite‑vec, sqlite‑vss, sqlite‑vector',
    'Korzystanie z Prism OpenAI',
    'LangFlow RAG review',
    'Lekki harness CPU + siatka ablacji BEIR',
    'Lekki harness do CombMNZ i BordaFuse',
    'Lekki pakiet microbenchów dla sqlite‑vec i hybrid SQL_04',
    'Lematyzacja i synonimy PL w FTS5',
    'Lematyzacja w czasie zapytania z Morfeusz2 i plWordNet',
    'Lokalne RAG‑i oparte na deterministycznych mini‑stackach',
    'Lokalne demo hybrydowego RAG w SQLite',
    'Lokalne ewaluacje BEIR i tokenizacja dla PL',
    'Lokalny RAG deterministyczny na SQLite_02',
    'Lokalny RAG deterministyczny: wzorzec i test odtwarzalności',
    'Lokalny RAG z FTS5 i RRF w jednym pliku_04',
    'Lokalny deterministyczny RAG na CPU_02',
    'Lokalny graf wiedzy z wizualizacją_04',
    'Lokalny harness ewaluacji retrievalu',
    'Lokalny hybrydowy retriever RAG + FTS + SQLite',
    'Lokalny pipeline QMD: FTS5, wektory i reranking',
    'Lokalny wzorzec hybrydowy- FTS5 + BM25 + Embeddingi',
    'Mapowanie dystansu i deterministyczne sortowanie wyników',
    'Metryki spójności i pokrycia dla lokalnych testów RAG',
    'Mikrotest wag BM25 w SQLite FTS5',
    'Mikrotesty - usuwanie sekcji, negatywne retrievale, drift',
    'Mikro‑benchmark FTS5 krok po kroku',
    'Minimalny lokalny skrypt ewaluacyjny i ryzyka',
    'Minimalny mikrobenchmark BM25 embed→rerank z RAPL',
    'Minimalny, deterministyczny pipeline FTS5-wektory-RRF',
    'Mini‑korpus FTS5 z testami offsetów PL_04',
    'Narzędzia do oceny RAG‑a i\u202ftestów odporności',
    'New - Local RAG  and DevOps Docs',
    'New GraphRAG & RAG integrations',
    'New research on AI memory models_04',
    'Normalizacja diakrytyków w wyszukiwaniu FTS5',
    'Now: Advances in Long‑Lived Agents',
    'Now: CPU‑Only AGI & Agent Research',
    'Nowe RAG i integracje grafowe',
    'Nowe badania — normalizacja wyników i znaczenie determinizmu',
    'Nowe badania: lokalne, CPU‑only AGI',
    'Nowe dema interfejsów semantycznych_04',
    'Nowe frameworki RoutIR i TEMPO dla RAG',
    'Nowe porównania strategii chunkowania w RAG',
    'Nowe prace i narzędzia RAG',
    'Nowe prace i narzędzia RAG (lokalne)',
    'Nowe praktyczne interfejsy semantyczne',
    'Nowe wydanie sqlite‑vec z wbudowanymi benchmarkami',
    'Nowości: RAG i inżynieria wiedzy',
    'Nowości: lokalne systemy RAG',
    'Nowy benchmark energetyczny RAG (styczeń 2026)',
    'Nowy klaster RAGFTS sqlite-vec i sqlite-lembed',
    'Nowy preprint cross-document topic-aligned chunking',
    'Obsługa polskich znaków w SQLite FTS5',
    'Odmładzanie RAG z zachowaniem determinizmu',
    'Ontologie i hybrydy FTS+wektory',
    'OpenLLMetry i OpenTelemetry GenAI — szybki start',
    'Pełny obieg LinkML → SQL z odwracalnymi migracjami',
    'Pięć lekkich narzędzi do debugowania RAG offline',
    'Plan testu: WAL, VACUUM i miękkie usuwanie TTL',
    'Polska tokenizacja i wierność snippetów w FTS5',
    'Pomiar energii w RAG: wskazówki ICSE‑SEIS 2026',
    'Pomiar ‘gap rate’ w zbiorze pivotów',
    'Poniedziałkowe Monitory: semantyka KB i AI w grach',
    'Poprawki FTS5: bezpieczeństwo i stabilność indeksów',
    'Porównanie FTS5 (BM25) i FAISS-CPU KNN',
    'Porównanie hybryd RAG z silnikami serwerowymi',
    'Porównanie tokenizerów polskich: ICU, Unicode61, Morfologik',
    'Połączenie sqlite-rag z AgentPrism jako lokalny inspektor',
    'Praktyczny hybrydowy RAG w SQLite z RRF_02',
    'Projektowanie gry filozoficznej',
    'Prosty monitoring dryfu embeddingów na CPU_04',
    'Prototypy semantycznych interfejsów CLI',
    'Przepis na mini‑microbench do retrievalu',
    'Przełomy AI w symulacjach fiz‑chem',
    'QUOKA — selektywne K - V dla szybszego prefillu',
    'QuackIR — powtarzalne benchmarki BEIR na SQLite i DuckDB',
    'RAG Persistence and Archival Integrity',
    'RAG w SQLite: FTS5 + Vector + AI lokalnie',
    'RAG z pełnym śledzeniem źródeł',
    'RAGExplorer  - wizualna analiza konfiguracji retrievalu',
    'RAGTrace: wizualny audyt retrievalu',
    'RAG‑TUI — terminalowy inspektor chunków',
    'RRF + RAG: zestaw testowy do ewaluacji',
    'Recepta na mikrobenchmark CPU dla hybryd SQLite',
    'Receptura FTS5 dla języka polskiego i kodu',
    'Receptura lokalnego RAG z metrykami CPU-cost',
    'Repozytoria do szybkiego startu z FTS5',
    'Retro podgląd FTS5 — live TUI_04',
    'Ryzyka bezpieczeństwa modeli open‑source',
    'SQL-only hybryda - RRF i LSE w SQLite',
    'SQLite 3.51.2 naprawia potencjalny deadlock w interfejsie unix',
    'SQLite 3.51.2 nowe funkcje JSONB i rozszerzenia',
    'SQLite z JSONB: dynamiczny mózg schematu',
    'SSM kontra RWKV modele pamięci długiego kontekstu',
    'Samonaprawiające się audyty w SQLite',
    'Schedulery CPU↔GPU: kTransformers i HybriMoE',
    'Seedowanie RAG pivotami dla szybszego startu',
    'Semantic Highlighting for Efficient RAG_02',
    'Semantic interfaces and flow visualization for knowledge bases',
    'Semantic interfaces: Practical roundup',
    'Semantyczne interfejsy i AI w symulacjach gier',
    'Skrócony schemat dla embeddingów',
    'Smarter quantization makes CPUs competitive again',
    'Stabilna kalibracja LSE i softmax w SQLite',
    'Strojenie BM25 w SQLite pod kontekst',
    'Struktura dokumentu FTS',
    'Sygnały z ekosystemu FTS5 - regresje i aktywność',
    'Synchronizacja grafów z SQLite JSONB',
    'Szablon budżetu energetycznego dla retrievalu',
    'Szablony SPEC‑ONLY i GOVERNANCE jako baza AI',
    'Szablony dokumentów technicznych AI',
    'Szablony repozytoriów FTS5 z Morfeusz2_04',
    'Szybkie testy jakości embeddingów_04',
    'TREC‑ToT — fuzja BM25 i gęstych modeli (RRF)',
    'Taguj wersje embeddingów, by uniknąć dryfu',
    'Test CI dla stabilności offsets() i snippet() w języku polskim',
    'Testowanie Embeddingów w Shadow Index',
    'Testowanie offsetów w morfologicznych tokenizerach',
    'Testy ICU i unicode61 dla FTS5',
    'Testy niezmienników i offsetów FTS5_04',
    'Tokenizacja polska: unicode61, ICU i lematyzacja',
    'Tokenizery FTS5 unicode61 ICU i własne podejścia_04',
    'Trwała pamięć agentów i pętle CPU‑first',
    'Tryby przechowywania FTS5 i ich kompromisy',
    'Unikaj wycieków w ewaluacji wyszukiwania',
    'Unstructured  - lokalne PDF→JSON-Markdown (Feb 2026)',
    'VelesDB 1 4 — lokalny silnik fuzji rankingów_04',
    'Wax  - jednoplikowy hybrydowy RAG na urządzeniu',
    'Wbudowany tokenizer Morfologik FSA dla FTS5',
    'Wizualne interfejsy bazy wiedzy i relacji',
    'Wykrywaj anomalie przez dryf embeddingów',
    'Wykrywanie dryfu semantycznego dokumentów',
    'Wzorce CPU→GPU dla energooszczędnego lokalnego RAG‑a',
    'Wzorce RRF dla hybrydowego RAG w SQLite',
    'Wzorce hybrydowe RAG w SQLite_05',
    'Wzorzec idempotentnego ingestu FTS5',
    'Zastosowanie języka Julia',
    'Zautomatyzowany harness micro‑benchmarków FTS5',
    'Zbieranie przykładów przez rozbieżność rankingów',
    'Zestaw audytowy deterministycznej fuzji hybrydowej',
    'Zestawy benchmarków dla faktualności i pokrycia dokumentów',
    'Znajdź jedno źródło tarcia',
    'Zwinne i deterministyczne RAG-i w SQLite',
    'Zwinne lokalne RAG w SQLite',
    'beads_viewer — przeglądarka grafów w Go + WASM',
    'qmd  - lokalny CLI RAG od Tobi Lütkego',
    'sift‑kg — lokalne CLI do budowy grafu wiedzy',
    'tldw_chatbook — terminalowy eksplorator semantyczny',
    'Łączenie BM25 i Embeddingów przez RRF',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "rag"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
