# Changelog

Rough log of how this repo got built.

## Round 1 — through RAG theory and the start of vector DB / RAG hands-on

- Repo scaffold: README, LICENSE, `.gitignore`, `pyproject.toml`
- Environment + API key setup guides
- Theory notes: Generative AI vs. Traditional AI, transformer architecture, LLM generation
  parameters, the stochastic-parrot analogy for LLMs, what LangChain is, workflow vs. agent,
  RAG theory
- Hands-on code: simple LLM calling, a two-stage blood-work-analysis workflow (notebook +
  Streamlit app), ChromaDB basics, a first pass at an end-to-end RAG pipeline
- Beginner troubleshooting/FAQ doc, a `scripts/check_setup.py` sanity checker

See [`docs/00_roadmap.md`](docs/00_roadmap.md) for exactly what's covered so far and what's
still ahead (AI agents, the ReAct loop, multi-agent and multimodal agents, evaluation,
guardrails, and two capstone projects).

## Round 2 — planned

Agent fundamentals and the ReAct loop, both capstone projects (a shopping agent, a telecom RAG
chatbot), and a polish pass tying the whole repo together.
