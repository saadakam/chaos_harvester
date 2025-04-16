import streamlit as st
import openai

st.set_page_config(page_title="🧠 Chaos Harvester", layout="centered")
st.title("🧪 Autonomous Research Assistant")

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.markdown("Paste raw scientific or research-related text below:")
input_text = st.text_area("🔍 Input Text", height=300)

if st.button("Harvest Insights"):
    if input_text.strip() == "":
        st.warning("Please paste some text.")
    else:
        with st.spinner("Processing..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a research analyst. Your job is to extract meaningful insights from academic or unstructured scientific text."},
                    {"role": "user", "content": f"""Analyze the following text:\n\n{input_text}\n\nYour Tasks:\n1. Provide a summary\n2. List key contributions\n3. Identify weaknesses or missing parts\n4. Suggest future work directions"""}
                ]
            )
            st.markdown("### 🧠 Insights:")
            st.write(response['choices'][0]['message']['content'])
