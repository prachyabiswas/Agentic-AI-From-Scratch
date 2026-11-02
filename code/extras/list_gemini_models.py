"""Small utility: list every Gemini/Gemma model your Google API key currently has access to.

Useful whenever a notebook's hard-coded model string (e.g. "gemini-2.5-flash") starts
returning a 404 - model names get renamed/retired fairly often, so it's worth checking the
live list instead of guessing.

Run with: python list_gemini_models.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name.removeprefix("models/"))
