import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("meviy Tech Assistant")
openai_api_key = st.secrets["OPENAI_API_KEY"]

def generate_response(input_text):
model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "How can I resolve an error with my model?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
