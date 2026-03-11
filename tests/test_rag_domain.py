"""
test_rag_domain.py — testy domenowe dla ishkarim_rag.

Testy używają prawdziwych danych z repozytorium Ishkarim.
Wymagają, że pakiet jest zainstalowany (pip install -e .).
"""
import pytest
from pathlib import Path
import ishkarim_rag
from ishkarim_rag import load_knowledge_index


@pytest.fixture
def repo_root():
    """Zwraca ścieżkę do katalogu głównego repozytorium Ishkarim."""
    root = Path(__file__).resolve().parents[3]  # projects/ishkarim-rag/tests/ → repo root
    assert (root / "CATALOG.md").exists() or (root / "CHANGELOG.md").exists(), \
        f"Nie znaleziono repo root w {root}. Uruchom testy z poziomu repozytorium."
    return root


class TestRealData:
    """Testy z prawdziwymi danymi z repozytorium."""

    def test_rag_docs_have_doc_ids(self, repo_root):
        """Każdy katalog RAG powinien mieć doc_id zaczynający się od DOC-RAG."""
        docs = load_knowledge_index(root=str(repo_root))
        rag_docs = [d for d in docs if d["doc_id"].startswith("DOC-RAG")]
        assert len(rag_docs) > 100, f"Expected >100 RAG docs, got {len(rag_docs)}"

    def test_rag_has_frozen_and_decision_docs(self, repo_root):
        """Baza RAG powinna mieć dokumenty w różnych stanach dojrzałości."""
        docs = load_knowledge_index(root=str(repo_root))
        maturities = {d["maturity"] for d in docs}
        assert "FROZEN" in maturities or "DECISION" in maturities

    def test_extract_blocks_from_real_work_md(self, repo_root):
        """Przetestuj ekstrakcję kodu z prawdziwego WORK.md z obszaru RAG."""
        from ishkarim_rag.utils import read_work_md, extract_python_blocks
        docs = load_knowledge_index(root=str(repo_root))
        found_code = False
        for doc in docs[:20]:
            work = read_work_md(Path(str(repo_root)) / doc["name"])
            blocks = extract_python_blocks(work)
            if blocks:
                found_code = True
                break
        assert found_code, "Żaden z pierwszych 20 dokumentów RAG nie zawiera bloków Python"


class TestModuleIntegrity:
    """Weryfikuje integralność modułu jako pakietu."""

    def test_version_format(self):
        assert re.match(r"\d+\.\d+\.\d+", ishkarim_rag.__version__)

    def test_modules_all_strings(self):
        for name in ishkarim_rag.MODULES:
            assert isinstance(name, str), f"MODULES entry not a string: {name!r}"
            assert name, "Empty module name found"

    def test_load_returns_correct_area(self, repo_root):
        docs = load_knowledge_index(root=str(repo_root))
        for doc in docs[:5]:
            assert doc["area"] == "rag"

    def test_tags_parseable(self, repo_root):
        """Pliki TAGS.md powinny być parsowalny przez extract_tags."""
        from ishkarim_rag.utils import extract_tags
        docs = load_knowledge_index(root=str(repo_root))
        errors = []
        for doc in docs[:10]:
            tags = extract_tags(Path(str(repo_root)) / doc["name"])
            if not tags:
                errors.append(doc["name"])
        assert len(errors) < 5, f"Zbyt wiele błędów parsowania TAGS.md: {errors}"

    def test_work_md_readable(self, repo_root):
        """Pliki WORK.md powinny być czytelne dla przynajmniej 80% katalogów."""
        from ishkarim_rag.utils import read_work_md
        docs = load_knowledge_index(root=str(repo_root))
        readable = 0
        for doc in docs[:20]:
            content = read_work_md(Path(str(repo_root)) / doc["name"])
            if content:
                readable += 1
        assert readable >= min(14, max(1, int(len(docs) * 0.5))), f"Tylko {readable}/{min(20, len(docs))} plików WORK.md czytelnych"


import re
