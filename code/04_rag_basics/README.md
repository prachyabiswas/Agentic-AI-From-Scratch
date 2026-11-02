# 04 — RAG Basics (end to end)

🟡 **In progress** — I've built a first working pass through this, but I'm still partway
through the "RAG — Hands On" chapter in the video, so this will get refined. See
[`docs/00_course_roadmap.md`](../../docs/00_course_roadmap.md) for current status.

## What's in here

`rag_demo.ipynb` wires together everything from [RAG theory](../../docs/08_rag_theory.md) and
[vector DB basics](../03_vector_db) into one working pipeline against `telecom_guide.pdf`:

1. Load the PDF (`PyPDFLoader`)
2. Split it into overlapping chunks (`RecursiveCharacterTextSplitter`)
3. Embed the chunks locally (`all-MiniLM-L6-v2`) and store them in Chroma
4. Sanity-check the retriever alone
5. Build the full chain: retriever → prompt → LLM (Groq), using LCEL
6. Ask it a question end to end
7. Inspect exactly which chunks were retrieved for a harder question (useful for debugging
   retrieval quality before blaming the LLM)

## Run it

Needs `GROQ_API_KEY` in `.env` (see
[`docs/05_api_key_setup.md`](../../docs/05_api_key_setup.md)). The embedding model downloads
locally on first run (~90 MB), no embedding API key needed.

```bash
jupyter notebook rag_demo.ipynb
```

## What I still want to add

- A persistent (disk-backed) vector store instead of rebuilding it in-memory every run
- An interactive question loop
- A similarity-score threshold so it says "I don't know" on weak matches instead of guessing

Next: once I'm through the AI Agent chapters in the video, `code/05_single_agent` onward.
