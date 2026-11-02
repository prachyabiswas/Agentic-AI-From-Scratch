# Workflow vs. Agent

Worth pinning down early — this is a real distinction, not just terminology.

## Workflow

A fixed sequence of LLM calls (and/or other steps) wired together by *your* code. You decide
the order, you decide what each call sees as input. The LLM never decides what happens next —
it just does the one task it's asked to do at each step, then control returns to your code.

`code/02_health_analysis` is a workflow: step 1 always extracts values, step 2 always writes a
diet plan from step 1's output. There's no branching, no decision-making by the model about
what to do next — just two fixed calls in a fixed order.

## Agent

An AI agent is given a goal and a set of **tools**, and it decides *for itself*, at each step,
what to do next — which tool to call, with what arguments, whether it has enough information to
answer yet, or whether it needs to take another action first. The control flow isn't
hand-written by you; it emerges from the model reasoning about the current state.

This repo doesn't have agent code yet — that's the next big chunk of this project (agent
fundamentals, the ReAct loop, and a hands-on single-agent build), which I haven't gotten to
yet. I'll fill in `code/05_single_agent` and the rest of `docs/` as I build it out.

## Why this distinction matters in practice

Workflows are predictable, cheap, and easy to debug — great when the steps genuinely are
always the same. Agents are more flexible and can handle problems you didn't explicitly
anticipate, but that flexibility comes with less predictability, higher cost (more LLM calls,
possibly in a loop), and the need for guardrails to keep them on track. Picking the simplest
tool that solves the problem — workflow before agent — is a real design decision, not a
cop-out.

Next: [docs/06_what_is_langchain.md](06_what_is_langchain.md) if you haven't read it yet, or
[docs/08_rag_theory.md](08_rag_theory.md) for the RAG chapter.
