# RAG Theory (Retrieval-Augmented Generation)

RAG shows up in a huge share of real GenAI projects — it's the standard way to make an LLM
answer questions about information it was never trained on: your company's HR policy, a
product manual, internal tickets, anything private or too recent to be in the model's training
data.

## The open-book-exam mental model

A plain LLM is like a very well-read student walking into a *closed-book* exam on a topic it
never studied — it'll guess, and sometimes that guess is confidently wrong (a hallucination).
Hand that same student the right reference material during an *open-book* exam, and suddenly
it can give accurate, grounded answers — not because it became smarter, but because it now has
the right source in front of it. RAG is exactly this: give the LLM the relevant snippet of your
own documents *as part of the prompt*, right before it answers.

## Why not just paste the whole document in?

For a short document, you could literally paste it into the prompt alongside the question and
it would work fine. The problem is scale: a 3,000-page policy document is far more tokens than
any context window can hold, and even when it *would* fit, sending the entire document on
every single question is slow and needlessly expensive — you're paying per token for mostly
irrelevant text. RAG's job is to find and send only the *relevant* slice.

## The two-step RAG pipeline

### Step 1 — Indexing (done once, offline, whenever your documents change)

1. **Chunk** your documents into smaller pieces (see `code/04_rag_basics` for a concrete
   `chunk_size` / `chunk_overlap` example). Smaller, focused chunks retrieve more precisely
   than whole pages.
2. **Embed** each chunk — convert it into a vector (a list of numbers) that captures its
   *meaning*, using an embedding model (e.g. `sentence-transformers/all-MiniLM-L6-v2`, or a
   hosted option like `text-embedding-3-small`).
3. **Store** all those vectors in a **vector database** (Chroma, Qdrant, Milvus are common
   choices). Unlike a normal database that matches exact values, a vector DB finds entries that
   are *semantically similar* — searching for "a company that leads in electric vehicles" can
   return a chunk about Tesla, even without the word "Tesla" appearing in the query.

### Step 2 — Retrieval (done on every user question)

1. Embed the incoming **question** with the *same* embedding model used for indexing.
2. Run a similarity search against the vector DB to pull back the top-k most relevant chunks
   (you choose k — e.g. the top 2, top 5).
3. Stuff those chunks into the prompt as context, alongside the original question, and send
   that combined prompt to the LLM. A good system prompt explicitly tells the model to answer
   *only* from the provided context.

```
documents --chunk--> chunks --embed--> vectors --store--> [ Vector DB ]
                                                                 ^
                                                                 | similarity search
question ------------------embed---------------------------> top-k chunks --> prompt --> LLM --> answer
```

## Why bother — two real benefits

1. **Fewer hallucinations.** The model is grounded in your actual source text instead of
   guessing from general training knowledge, so answers are far more likely to be accurate —
   and when the retrieved context genuinely doesn't contain the answer, a well-written prompt
   will have the model say so instead of making something up.
2. **Lower cost.** Sending only the 2-5 relevant chunks instead of an entire document means
   dramatically fewer tokens per call — and LLM APIs bill per token.

Next: [`code/03_vector_db`](../code/03_vector_db) for hands-on practice with a vector database
on its own, before wiring up the full RAG chain in
[`code/04_rag_basics`](../code/04_rag_basics).
