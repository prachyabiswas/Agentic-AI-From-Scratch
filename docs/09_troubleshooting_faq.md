# Troubleshooting / FAQ

Things that tripped me up, in case they trip you up too.

**`ModuleNotFoundError` for something like `langchain_google_genai`**
Your virtual environment isn't active, or `uv sync` / `pip install -e .` hasn't been run yet.
Check [docs/01_environment_setup.md](01_environment_setup.md).

**`AssertionError` / API key errors when a notebook runs**
`.env` is missing or doesn't have the right key name. Copy `.env.example` to `.env` (at the
repo root, or inside the specific module folder if it has its own) and fill in real keys — see
[docs/05_api_key_setup.md](05_api_key_setup.md). Also double check you didn't leave stray
quotes around the key value.

**A model name gives a 404 / "model not found"**
Model names get renamed or retired over time. Run
[`code/extras/list_gemini_models.py`](../code/extras/list_gemini_models.py) to see what your
key currently has access to, and swap the model string in the notebook.

**Hit a rate limit on the free tier**
Google AI Studio's free tier caps requests per minute and per day. Either wait a bit, or switch
that notebook cell to use Groq instead (see [docs/05_api_key_setup.md](05_api_key_setup.md)).

**Streamlit app won't start / "command not found: streamlit"**
Make sure your virtual environment is active (`source .venv/bin/activate`) in the *same*
terminal you're running `streamlit run` from, and that you're running it from inside the
module's folder (e.g. `code/02_health_analysis/streamlit_app/`).

**The embedding model download in `code/04_rag_basics` is slow**
`all-MiniLM-L6-v2` downloads once (~90 MB) and is cached locally after that — the first run
will always be the slowest.

**Jupyter opens but I don't see my notebook**
Launch `jupyter notebook` from inside the specific module folder (e.g.
`code/01_simple_llm_calling/`), not from the repo root — otherwise you'll have to click through
folders to find it, which is fine too, just slower.

Didn't find your issue here? Open an issue on this repo, or check
[docs/00_roadmap.md](00_roadmap.md) for where a given topic's notes and code live.
