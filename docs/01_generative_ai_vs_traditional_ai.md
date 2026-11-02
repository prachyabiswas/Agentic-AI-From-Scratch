# Generative AI vs. Traditional AI

## What is Generative AI?

Generative AI is AI that *creates new content* — text, images, audio, video, or code — by
learning patterns from huge amounts of existing data, instead of just classifying or scoring
something that already exists. When you type a prompt into ChatGPT, Claude, or Gemini, a
**large language model (LLM)** underneath is what actually generates the response. The "large"
part refers to how these models are trained on massive datasets (Wikipedia, books, news
articles, code, and so on) and end up with billions to trillions of internal parameters.

## Traditional AI didn't disappear — it's still everywhere

Before chatbots went mainstream, AI was already doing useful work, just not by *generating*
anything. A classic example: your bank's fraud-detection system. It looks at a transaction and
outputs a label — fraud or not fraud — using lightweight statistical models like **XGBoost** or
**Random Forest**. That's classification, not generation, and it's been in production for
20–30 years.

## The bigger picture: AI → ML → Deep Learning → Transformers

It helps to see how these pieces nest inside each other:

```
Artificial Intelligence (AI)
├── Rule-based systems (if/else logic, regex, classic robotics control)
└── Machine Learning (ML)
    ├── Statistical ML (XGBoost, Random Forest — the fraud-detection kind)
    └── Deep Learning (neural networks)
        ├── CNN (convolutional neural networks — mostly images)
        ├── RNN (recurrent neural networks — sequences, now mostly superseded)
        └── Transformer  ← the architecture behind modern LLMs
```

- **AI**, broadly, means getting a computer to do something humans are normally good at —
  driving, reading and understanding text, writing, even robotics.
- **ML** is the subset of AI where the system learns patterns from data rather than following
  hand-written rules.
- **Deep learning** is the subset of ML built on neural networks.
- The **Transformer** architecture (introduced in Google's 2017 paper *"Attention Is All You
  Need"*) is the specific neural network design that made the current wave of generative AI
  possible.

Generative AI is essentially the class of applications built on top of transformer-based
models.

## Seeing a transformer work, visually

A great way to build intuition is the [Transformer Explainer](https://poloclub.github.io/transformer-explainer/)
interactive visualization. You type a sentence, and it shows — step by step — how the model
tokenizes the input, computes self-attention across tokens, and predicts the single most
likely *next* token. That's genuinely all a language model is doing at each step: given
everything so far, predict what comes next, one token at a time.

Next: [docs/02_transformer_architecture.md](02_transformer_architecture.md) digs a bit deeper
into tokens, embeddings, and self-attention.
