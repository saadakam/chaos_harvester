import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("🧠 Chaos Harvester: Research Assistant")

# --- OpenAI Client Init ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Text Input ---
input_text = st.text_area("🔍 Paste raw research text below:", height=300)

if st.button("🧪 Analyze"):
    if not input_text.strip():
        st.warning("Please paste some text first.")
    else:
        with st.spinner("Harvesting insights from chaos..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a research analyst. Extract structured insights from chaotic text."},
                    {"role": "user", "content": f"""Text:\n{input_text}\n\nTasks:\n1. Summarize it.\n2. Extract key points.\n3. List weaknesses/gaps.\n4. Suggest future work."""}
                ]
            )
            st.markdown("### 🧠 Insights")
            st.write(response.choices[0].message.content)
