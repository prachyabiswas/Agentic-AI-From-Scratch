# Environment Setup

Steps I used to set up a clean Python environment for this repo.

## Prerequisites

- Python 3.11+
- A code editor — I used VS Code
- Basic Python knowledge — that's genuinely the only prerequisite

## 1. Install `uv`

`uv` is a fast alternative to `pip` for managing Python projects and virtual environments.
Install instructions for your OS: https://docs.astral.sh/uv/getting-started/installation/

## 2. Clone this repo and sync dependencies

```bash
git clone https://github.com/prachyabiswas/Agentic-AI-From-Scratch.git
cd Agentic-AI-From-Scratch
uv sync
```

`uv sync` reads `pyproject.toml` and installs every dependency (LangChain, ChromaDB,
Streamlit, etc.) into a project-local virtual environment (`.venv/`).

If you'd rather use plain `pip`:

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -e .
```

## 3. Activate the environment

```bash
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

## 4. Run the notebooks

```bash
jupyter notebook
```

Open any notebook inside `code/<module>/` and run the cells top to bottom.

## 5. Run a Streamlit app (where one exists)

```bash
streamlit run code/<module>/streamlit_app/app.py
```

Next: [docs/05_api_key_setup.md](05_api_key_setup.md) to configure the LLM API keys you'll
need before any of the notebooks can actually call a model.
