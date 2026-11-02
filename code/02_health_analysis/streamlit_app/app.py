"""Blood Work Analyzer — a small Streamlit UI around the two-stage pipeline
from ../blood_work_analysis.ipynb.

Run with: streamlit run app.py   (from inside this folder, with .venv active)
"""

from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(page_title="Blood Work Analyzer", layout="wide")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("Blood Work Analyzer")
st.caption("Not medical advice — for learning purposes only.")

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Blood Work Report")
    blood_report = st.text_area(
        label="Paste your report below",
        height=450,
        placeholder="Paste a blood work report here...",
        label_visibility="collapsed",
    )
    analyze_clicked = st.button("Analyze", type="primary", use_container_width=True)

with right_col:
    st.subheader("Health Summary")
    health_box = st.empty()

    st.subheader("Suggested Diet Plan")
    diet_box = st.empty()

if analyze_clicked:
    if not blood_report.strip():
        st.warning("Please paste a blood work report before analyzing.")
    else:
        with st.spinner("Analyzing..."):
            # Stage 1: extract and flag abnormal values
            extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or
NORMAL based on the reference ranges provided in the report.

Format your response as:
- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""
            extracted_values = llm.invoke(extraction_prompt).text

            # Stage 2: health summary and diet plan, clearly split into two sections
            diet_prompt = f"""
You are a nutritionist. Based on the blood work analysis below, provide two clearly separated
sections:

SECTION 1 - HEALTH SUMMARY:
Write 4-5 lines explaining the patient's condition in simple, non-technical language.

SECTION 2 - DIET PLAN:
List foods to eat more of and foods to avoid. Keep it practical and concise.

Blood Work Analysis:
{extracted_values}
"""
            full_response = llm.invoke(diet_prompt).text

        if "SECTION 2" in full_response:
            parts = full_response.split("SECTION 2")
            health_summary = parts[0].replace("SECTION 1 - HEALTH SUMMARY:", "").replace("SECTION 1", "").strip()
            diet_plan = ("SECTION 2" + parts[1]).replace("SECTION 2 - DIET PLAN:", "").replace("SECTION 2", "").strip()
        else:
            health_summary, diet_plan = full_response, ""

        health_box.markdown(health_summary)
        diet_box.markdown(diet_plan if diet_plan else full_response)
