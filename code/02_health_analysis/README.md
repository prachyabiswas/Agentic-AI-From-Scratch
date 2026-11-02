# 02 — Health Analysis (a Workflow, not an Agent)

A small but genuinely useful first project: paste in a blood report, get a plain-language
summary and a diet plan back out. See
[`../../docs/07_workflow_vs_agent.md`](../../docs/07_workflow_vs_agent.md) for why this is
called a **workflow** rather than an agent.

## What's in here

- `blood_work_analysis.ipynb` — the notebook version, two LLM calls chained together
  (extract abnormal values → write a summary + diet plan)
- `sample_blood_work.txt` — synthetic sample report to test with (fictional patient, not real
  data)
- `streamlit_app/app.py` — the same pipeline wrapped in a small web UI

## Run the notebook

```bash
jupyter notebook blood_work_analysis.ipynb
```

## Run the Streamlit app

```bash
cd streamlit_app
streamlit run app.py
```

Paste the contents of `../sample_blood_work.txt` into the left box (or your own report in the
same format) and click **Analyze**.

## The pipeline

```
raw report  ->  [LLM: extract + flag HIGH/LOW/NORMAL]  ->  [LLM: summary + diet plan]  ->  output
```

Two focused prompts, not one giant one — each step is easier to get right, and Stage 2 never
has to re-parse the raw report text.

Next: [`../03_vector_db`](../03_vector_db) — the hands-on vector database chapter.
