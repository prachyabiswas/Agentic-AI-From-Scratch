# Changelog

Rough log of how this repo got built, in case it's useful context for anyone following along.

## Round 1 — through "RAG Theory" / start of "Vector DB — Hands On"

- Repo scaffold: README, LICENSE, NOTICE (attribution), `.gitignore`, `pyproject.toml`
- Environment + API key setup guides
- Theory notes: Generative AI vs. Traditional AI, transformer architecture, LLM generation
  parameters, the stochastic-parrot analogy for LLMs, what LangChain is, workflow vs. agent,
  RAG theory
- Hands-on code: simple LLM calling, a two-stage blood-work-analysis workflow (notebook +
  Streamlit app), ChromaDB basics, a first pass at an end-to-end RAG pipeline
- Beginner troubleshooting/FAQ doc, a `scripts/check_setup.py` sanity checker

See [`docs/00_course_roadmap.md`](docs/00_course_roadmap.md) for exactly which video chapters
are covered so far and what's still ahead (AI agents, ReAct loop, multi-agent and multimodal
agents, evaluation, guardrails, and the two capstone projects).

## Round 2 — planned

Once I'm further through the video: agent chapters, both capstone projects (shopping agent,
telecom RAG chatbot), and a polish pass tying the whole repo together.
