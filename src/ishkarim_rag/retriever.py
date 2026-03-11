"""
retriever.py — kod wyekstrahowany z WORK.md dla obszaru rag.

Zawiera 2 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Aktualizacja z 18–22 lutego - RRF jako standard w ekosystemie
@dataclass(frozen=True)
class QueryPlan:
    query_id: str           # sha256(query_text + canonical_filters)
    query_text: str
    filters: Dict[str, object]
    retrievers: List[RetrieverSpec]
    fusion: FusionSpec

@dataclass(frozen=True)
class FusionSpec:
    method: Literal["rrf"] = "rrf"
    rrf_k: int = 60
    tie_break: Literal["doc_id"] = "doc_id"

# Source: Lekki harness CPU + siatka ablacji BEIR
# Siatka ablacji — parametry
fts_variants    = [tokenizer × remove_diacritics]
retriever_space = {topk_bm25: [50,200], topk_dense: [50,200], w_title: [0.5,1.0,2.0]}
fusion_space    = [rrf(k=10), rrf(k=60), combsum+minmax, combmnz+minmax, borda]
