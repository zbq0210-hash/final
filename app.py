import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from xiaoliu_ren import generate_result, get_meaning
from baseline import get_baseline
from prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()
client = OpenAI()

st.set_page_config(
    page_title="Xiaoliu Ren Reflective Assistant",
    page_icon="🌙",
    layout="wide"
)

st.title("🌙 Xiaoliu Ren Reflective Assistant")

st.write(
    "This app uses Xiaoliu Ren as a culturally inspired symbolic system "
    "to support reflection. It is not a prediction tool and should not replace personal judgment."
)

question = st.text_area(
    "What uncertain situation would you like to reflect on?",
    placeholder="Example: Should I take this internship or wait for a better opportunity?"
)

if st.button("Generate Reflection"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        result = generate_result()
        meaning = get_meaning(result)
        baseline_output = get_baseline(result)

        user_prompt = build_user_prompt(question, result, meaning)

        with st.spinner("Generating reflection..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.4,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ]
            )

        genai_output = response.choices[0].message.content

        st.subheader("Xiaoliu Ren Result")
        st.info(f"**{result}** — {meaning}")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Baseline: Fixed Template")
            st.write(baseline_output)

        with col2:
            st.subheader("GenAI: Personalized Reflection")
            st.write(genai_output)

        st.caption(
            "Note: The baseline gives a static explanation. The GenAI version adapts the interpretation to the user's specific question."
        )