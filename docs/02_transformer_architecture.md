# Transformer Architecture (Just Enough to Be Dangerous)

I'm not trying to re-derive the "Attention Is All You Need" paper here — just capturing the
intuition that actually matters for using LLMs well.

## Tokens, not words

A model doesn't see words — it sees **tokens**, which are often sub-word pieces. A short
sentence can easily break into more tokens than you'd expect (word pieces, punctuation, even
single letters sometimes get their own token). You can see this yourself at the
[OpenAI tokenizer playground](https://platform.openai.com/tokenizer) — type a sentence and
watch it get chopped into colored token chunks.

This matters practically because:
- API pricing is per token, not per word or per request.
- Context window limits (see [docs/03_llm_parameters.md](03_llm_parameters.md)) are measured
  in tokens.

## Embeddings and self-attention, in one paragraph

Each token gets converted into a vector (a list of numbers) called an **embedding**, which
captures something about its meaning. Inside a transformer block, **self-attention** lets
every token "look at" every other token in the input and figure out which ones are most
relevant to predicting what comes next — e.g. in *"I'm hungry, I need some ___"*, the words
"hungry" and "need" strongly influence that the next token is probably food-related, not
"bicycle" or "sky". Stack many of these attention blocks (a modern LLM has dozens) and you get
a model that can track long, complex relationships across an entire passage.

## The model is doing one thing, repeatedly: predict the next token

After all that attention computation, the final layer produces a probability distribution
over the entire vocabulary for "what token comes next" — e.g. after *"I'm"*, the token "am"
might get ~99% probability. The model samples from that distribution (how it samples is
controlled by the generation parameters — see the next doc), appends the chosen token, and
repeats the whole process for the next position. That's the entire generation loop.

## Why this is trained on "all the internet"

These statistical patterns only become useful because the model has seen an enormous amount of
text — Wikipedia, books, news, code. If you say "I'm hungry, I need some ___", the training
data overwhelmingly continues with food-related words, essentially never with "computer" or
"sky", so the model's learned probabilities reflect that.

Next: [docs/03_llm_parameters.md](03_llm_parameters.md) — temperature, top-k, top-p, and
context window, i.e. the knobs that control *how* the model samples from that next-token
distribution.
