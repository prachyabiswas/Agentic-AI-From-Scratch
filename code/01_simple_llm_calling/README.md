# 01 — Simple LLM Calling

The "hello world" of this course: verify your API keys work and make your first programmatic
call to an LLM through LangChain.

## What's in here

`call_llm.ipynb` covers, in order:
1. A single `.invoke()` call to a Gemini model
2. System vs. human messages (and why separating them matters)
3. The `temperature` parameter, same prompt at `0` vs `1`
4. Swapping to a different provider (Groq) with almost no code changes

## Run it

Make sure you've done [`docs/05_api_key_setup.md`](../../docs/05_api_key_setup.md) first (a
`.env` file with at least `GOOGLE_API_KEY`, ideally `GROQ_API_KEY` too), then:

```bash
jupyter notebook call_llm.ipynb
```

## Why this matters before anything else

Every later module in this repo — the health analysis pipeline, RAG, agents — is built out of
exactly this one operation, called repeatedly with different prompts and wired together. Get
comfortable with `.invoke()`, system/human messages, and temperature here first.
