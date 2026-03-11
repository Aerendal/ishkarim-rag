"""
rerank.py — fragmenty kodu z WORK.md dla obszaru rag.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 3 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Dobór k z uwzględnieniem budżetu CPU
for k_retrieve in [20, 50, 100, 200]:
    for k_rerank in [5, 10, 20, 50]:
        if k_rerank > k_retrieve:
            continue
        mrr, recall, ndcg = eval_quality(dataset, k_retrieve, k_rerank)
        t_p50, t_p95, cpu_peak, rss = eval_perf(k_retrieve, k_rerank)
        log_result(k_retrieve, k_rerank, mrr, recall, ndcg, t_p50, t_p95, cpu_peak, rss)

# ────────────────────────────────────────────────────────────

# Source: Dobór k z uwzględnieniem budżetu CPU
def is_hard_query(top_scores, fts_hits):
    low_top1 = top_scores[0] < threshold_low
    small_margin = (top_scores[0] - top_scores[1]) < margin_min
    no_fts = fts_hits == 0
    return low_top1 or small_margin or no_fts

k_rerank = k_rerank_hard if is_hard_query(...) else k_rerank_default

# ────────────────────────────────────────────────────────────

# Source: Kiedy rozbudować BM25 o warstwę wektorową
plateau = (delta_ndcg_10_20 < epsilon_ndcg and delta_ndcg_20_50 < epsilon_ndcg)
recall_growing = delta_recall_10_50 >= min_recall_gain
if plateau and recall_growing:
    enable_vector_reranker()
