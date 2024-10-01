import streamlit as st
from summary_model import summarize_text

st.title("Text Summarization App")

input_text = st.text_area("Enter the text you want to summarize:", height=300)

if st.button("Summarize"):
    if input_text:
        summary = summarize_text(input_text)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error("Please enter some text to summarize.")