# 03 — Vector DB Basics

Hands-on with [ChromaDB](https://www.trychroma.com/) on its own, before wiring it into a full
RAG chain in the next module. Goal: actually *see* semantic (meaning-based) search work, as
opposed to exact keyword matching.

## Run it

```bash
jupyter notebook vector_db_basics.ipynb
```

No API key needed for this one — Chroma's default in-memory client handles embedding locally.

## What it demonstrates

Four short documents are added to a collection (two about tech companies, one about the fruit
"apple", one about NASA). Querying with phrases that share *no keywords* with the right
document — "a query related to Elon Musk", "I love iPad", "tips for improving health" — still
correctly retrieves the semantically related document each time. That's the core trick vector
databases enable, and it's exactly what step 1 and step 2 of
[RAG theory](../../docs/08_rag_theory.md) depend on.

Next: [`../04_rag_basics`](../04_rag_basics).
