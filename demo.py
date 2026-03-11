#!/usr/bin/env python3
"""
demo.py — demo ishkarim-rag

Hybrydowe wyszukiwanie RAG — FTS5 + embeddingi + RRF, działa w pełni offline na CPU

Uruchomienie:
    python projects/ishkarim-rag/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[2] / "src"))
import sqlite3

DB = pathlib.Path(__file__).parents[2] / "tools" / "search.db"
if not DB.exists():
    print("Zbuduj najpierw indeks: python3 scripts/build_index.py"); exit(1)

query = "hybrid RAG SQLite FTS5"
with sqlite3.connect(DB) as con:
    rows = con.execute(
        "SELECT name, snippet(docs_fts,-1,'>>','<<','...',20) FROM docs_fts WHERE docs_fts MATCH ? ORDER BY rank LIMIT 5",
        (query,)
    ).fetchall()

print(f"Zapytanie: {query!r}\n")
for i, (name, snippet) in enumerate(rows, 1):
    print(f"  #{i} {name}")
    print(f"     {snippet[:120]}\n")

