# API Key Setup

Every notebook in this repo calls an LLM over an API, so you need at least one API key
before anything will actually run. I set up two, so I always have a free backup.

## Option A — Google AI Studio (Gemini / Gemma models)

1. Go to https://aistudio.google.com/ and sign in.
2. Click **API keys** → **Create API key**.
3. Pick (or create) a Google Cloud project, give the key a name, and generate it.
4. Treat the key like a password — don't commit it or share it.
5. Google's free tier has rate limits (requests per minute and per day) — check the
   "rate limit" page in AI Studio so you know how many calls you can make before you'd need
   to pay. This course stays well inside the free tier.

## Option B — Groq Cloud (fast, OpenAI/Llama/Qwen-style open models)

1. Go to https://console.groq.com/ and sign in with Google or email.
2. Go to **API keys** → **Create API key**, give it a name, generate it.
3. Groq also has a generous free tier, and is useful as a backup if you ever hit Google's
   rate limit.

## Put the keys in `.env`

```bash
cp .env.example .env
```

Then edit `.env` and paste in your keys:

```
GOOGLE_API_KEY=AIza...
GROQ_API_KEY=gsk_...
```

You don't need both — if you're only using Gemini models, the Google key alone is enough,
and vice versa for Groq. `.env` is already in `.gitignore`, so it never gets committed.

Every notebook starts with:

```python
from dotenv import load_dotenv
load_dotenv()
```

which reads `.env` and sets the keys as environment variables for that process — that's all
the LangChain model classes need to authenticate.

Next: [docs/06_rag_theory.md](06_rag_theory.md), or jump straight into the first hands-on
notebook at [code/01_simple_llm_calling](../code/01_simple_llm_calling).
