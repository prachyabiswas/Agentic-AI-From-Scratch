# Agentic AI Crash Course — My Notes & Practice

This repo documents my own notes, explanations, and hands-on code while following the free
YouTube course **["Agentic AI Crash Course using LangChain"](https://www.youtube.com/watch?v=D74el9mvNak)**
by [Codebasics](https://codebasics.io/) (Dhaval Patel).

The goal: start from "what is Generative AI" and end up having actually built two end-to-end
agentic applications (a shopping agent, and a telecom RAG chatbot) — and leave behind a repo
clear enough that any beginner with basic Python knowledge can read it top to bottom and
reproduce everything themselves.

> **Status:** work in progress, built module by module as I go through the video. Current
> progress and what's coming next: [`docs/00_course_roadmap.md`](docs/00_course_roadmap.md).

## Quick start

```bash
git clone https://github.com/prachyabiswas/agentic-ai-crash-course.git
cd agentic-ai-crash-course
uv sync                          # or: python -m venv .venv && pip install -e .
cp .env.example .env             # then fill in your API keys
jupyter notebook
```

Full walkthrough: [`docs/01_environment_setup.md`](docs/01_environment_setup.md) and
[`docs/05_api_key_setup.md`](docs/05_api_key_setup.md). Something not working?
[`docs/09_troubleshooting_faq.md`](docs/09_troubleshooting_faq.md).

## How this repo is organized

```
docs/   - my notes on the theory (one file per concept, read in numeric order)
code/   - one folder per hands-on module, matching the course's structure, each with its own README
```

### Theory notes (`docs/`)

| # | Topic |
|---|-------|
| 00 | [Course roadmap / progress tracker](docs/00_course_roadmap.md) |
| 01 | [Generative AI vs. Traditional AI](docs/01_generative_ai_vs_traditional_ai.md) |
| 02 | [Transformer architecture](docs/02_transformer_architecture.md) |
| 03 | [LLM parameters — temperature, top-k, top-p, context window](docs/03_llm_parameters.md) |
| 04 | [LLMs explained with an analogy (stochastic parrot, RLHF)](docs/04_llm_analogy_explained.md) |
| 05 | [API key setup](docs/05_api_key_setup.md) |
| 06 | [What is LangChain?](docs/06_what_is_langchain.md) |
| 07 | [Workflow vs. agent](docs/07_workflow_vs_agent.md) |
| 08 | [RAG theory](docs/08_rag_theory.md) |
| 09 | [Troubleshooting / FAQ](docs/09_troubleshooting_faq.md) |

### Hands-on code (`code/`)

| Module | What it is | Status |
|---|---|---|
| [01_simple_llm_calling](code/01_simple_llm_calling) | First LLM calls via LangChain — system/human messages, temperature, switching providers | ✅ |
| [02_health_analysis](code/02_health_analysis) | A two-stage LLM *workflow*: blood report → flagged values → diet plan, plus a Streamlit UI | ✅ |
| [03_vector_db](code/03_vector_db) | ChromaDB basics — semantic search on raw text | ✅ |
| [04_rag_basics](code/04_rag_basics) | Full RAG pipeline: load → chunk → embed → retrieve → generate | 🟡 in progress |
| [extras](code/extras) | Small standalone utilities (list available Gemini models) | ✅ |

Chapters I haven't reached in the video yet (AI agents, ReAct loop, multimodal agents,
evaluation, guardrails, and the two capstone projects) are tracked in the roadmap and will get
their own `docs/` notes and `code/` modules as I work through them.

## Credit

All course content, teaching structure, and original example code are from **Codebasics /
Atliq** — go watch the [full video](https://www.youtube.com/watch?v=D74el9mvNak) and check out
their [AI engineering cohort](https://codebasics.io/) if you want to go deeper than a crash
course. See [`NOTICE.md`](NOTICE.md) for full attribution. Everything in `docs/` is my own
write-up, and the code in `code/` is my own practice implementation while learning from the
course.
