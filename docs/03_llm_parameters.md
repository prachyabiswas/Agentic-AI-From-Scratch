# LLM Generation Parameters

These are the knobs that control how a model samples the *next token* from its predicted
probability distribution.

## Temperature

- **Temperature = 0** → deterministic. The model (almost) always picks the single
  highest-probability token. Same prompt in, same answer out. Good for factual /
  precise tasks (data extraction, classification, code).
- **Higher temperature** (e.g. 0.7–1.0) → the model is more willing to pick lower-probability
  tokens, producing more varied, "creative" output. Good for taglines, poems, brainstorming,
  pitch decks — anything where you want variety rather than a single "correct" answer.

I tested this directly in `code/01_simple_llm_calling` — the exact same tagline prompt run at
`temperature=0` vs `temperature=1` produces a safe, predictable line at 0 and a noticeably
more playful one at 1.

## Top-K sampling

Instead of considering the model's entire vocabulary, top-k sampling restricts the choice to
only the **k** most likely next tokens, then samples randomly among just those k. For example
with `k=3`, if the top three candidate tokens are "am" (51%), "need" (20%), "have" (10%), the
model picks randomly among those three (renormalizing their probabilities) and ignores
everything else — including other words that might individually have had a non-trivial
probability, but didn't make the top 3.

## Top-P (nucleus) sampling

Top-p works differently: instead of a fixed count of tokens, it keeps adding candidates — in
order of probability, highest first — until their *cumulative* probability crosses a threshold
**p** (e.g. `p=0.9`), then samples from just that set. So if "hat" (35%), "mat" (30%), "bat"
(20%) and "car" (10%) sum to 95% — past the 0.9 threshold after "car" — those four are the
pool to sample from, regardless of how many tokens that turned out to be. This adapts better
than top-k to situations where the model is very confident (few tokens needed to hit 90%) vs.
very uncertain (many tokens needed).

## Context window

The context window is the maximum number of **tokens** (input + output + any earlier turns in
the conversation) a model can process in a single call. If you keep chatting, each new message
you send actually re-sends the relevant prior conversation too, so the token count accumulates
turn over turn.

Rough reference points (these numbers move fast, so always check the current docs for whatever
model you're using):

| Model | Context window |
|---|---|
| GPT-4o | 128K tokens |
| GPT-5.3 | 400K tokens |
| Claude Opus 4.6 | 1M tokens |

Practical implication: if you're feeding a model a huge document (a 3,000-page policy PDF, for
example), you cannot just paste the whole thing in, even with a huge context window — it would
be too many tokens and too expensive per call. That's exactly the problem **RAG** solves — see
[docs/08_rag_theory.md](08_rag_theory.md).

Next: [docs/04_llm_analogy_explained.md](04_llm_analogy_explained.md) for a simpler mental
model of what an LLM actually is.
