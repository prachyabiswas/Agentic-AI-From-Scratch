"""Quick sanity check for beginners: run this after `uv sync` + filling in `.env` to confirm
everything is wired up correctly *before* opening a notebook.

Run with: python scripts/check_setup.py
"""

import importlib
import os
import sys

from dotenv import load_dotenv

load_dotenv()

REQUIRED_PACKAGES = [
    "langchain",
    "langchain_google_genai",
    "langchain_groq",
    "langchain_chroma",
    "langchain_huggingface",
    "chromadb",
    "streamlit",
    "dotenv",
]

print("Checking required packages are installed...")
missing = []
for pkg in REQUIRED_PACKAGES:
    try:
        importlib.import_module(pkg)
        print(f"  [ok]  {pkg}")
    except ImportError:
        print(f"  [MISSING]  {pkg}")
        missing.append(pkg)

print("\nChecking API keys in .env...")
keys = {
    "GOOGLE_API_KEY": "needed for code/01, code/02",
    "GROQ_API_KEY": "needed for code/01 (Groq example), code/04",
}
missing_keys = []
for key, note in keys.items():
    if os.getenv(key):
        print(f"  [ok]  {key}")
    else:
        print(f"  [MISSING]  {key}  ({note})")
        missing_keys.append(key)

if missing or missing_keys:
    print("\nSomething still needs fixing before the notebooks will run.")
    print("See docs/01_environment_setup.md and docs/05_api_key_setup.md.")
    sys.exit(1)

print("\nAll set. Open any notebook in code/ and start running cells.")
