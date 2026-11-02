# What is LangChain?

LangChain is the main framework used throughout this repo for calling LLMs and building both
agentic and non-agentic AI applications. It's genuinely common to see it listed as a required
skill in GenAI engineer job postings, so it's worth learning properly rather than treating it
as just another library.

## It's an ecosystem, not one single tool

- **LangChain** — the core framework: wrappers around LLM providers (Google, Groq, OpenAI,
  etc.), prompt templates, chains, and tools to build both simple pipelines and full agents.
- **LangGraph** — for building more reliable, controllable agents with explicit state and
  low-level control over the execution graph.
- **LangSmith** — observability, evaluation, and deployment tooling: trace every LLM call,
  inspect prompts/responses, debug chains in production.

A comparison that stuck with me: LangChain is like shooting photos in a DSLR's **auto mode** —
a few lines of code and you get a working agent. LangGraph is more like full **manual mode** —
more setup, but precise, low-level control over exactly how the agent reasons and moves between
steps. Different tools for different levels of control, not a strict "better vs worse."

For now I'm mostly working with plain LangChain in this repo, since the goal is to get the core
concepts solid before reaching for the extra control LangGraph offers.

Next: [code/01_simple_llm_calling](../code/01_simple_llm_calling) — the first real LangChain
code in this repo.
