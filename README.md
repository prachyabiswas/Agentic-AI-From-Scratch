# Agentic AI From Scratch

My own hands-on build-up of Generative AI, RAG, and agentic AI concepts using LangChain —
starting from "what is Generative AI" at the very basics, working through transformers, LLM
parameters, retrieval-augmented generation, and (as I keep building this out) all the way to
working autonomous agents.

The goal: a repo clear enough that any beginner with basic Python knowledge can read it top to
bottom and reproduce everything themselves — real explanations in my own words, plus working
code for every concept, not just theory.

> **Status:** work in progress, built module by module. Current progress and what's coming
> next: [`docs/00_roadmap.md`](docs/00_roadmap.md).

## Quick start

```bash
git clone https://github.com/prachyabiswas/Agentic-AI-From-Scratch.git
cd Agentic-AI-From-Scratch
uv sync                          # or: python -m venv .venv && pip install -e .
cp .env.example .env             # then fill in your API keys
python scripts/check_setup.py    # confirms packages + keys are wired up correctly
jupyter notebook
```

Full walkthrough: [`docs/01_environment_setup.md`](docs/01_environment_setup.md) and
[`docs/05_api_key_setup.md`](docs/05_api_key_setup.md). Something not working?
[`docs/09_troubleshooting_faq.md`](docs/09_troubleshooting_faq.md).

## How this repo is organized

```
docs/   - my notes on the theory (one file per concept, read in numeric order)
code/   - one folder per hands-on module, each with its own README
```

### Theory notes (`docs/`)

| # | Topic |
|---|-------|
| 00 | [Roadmap / progress tracker](docs/00_roadmap.md) |
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

What's still ahead — AI agents, the ReAct loop, multimodal agents, evaluation, guardrails, and
two full capstone projects (a shopping agent, a telecom RAG chatbot) — is tracked in the
roadmap and will get its own `docs/` notes and `code/` modules as I keep building.
