import streamlit as st
from gmail_to_sheet import process_emails

st.set_page_config(page_title="AI Gmail PDF Summarizer")

st.title("📧 AI Gmail PDF Summarizer")

st.write(
    "Fetch Gmail emails, extract PDF attachments, and generate AI summaries."
)

if st.button("Fetch Emails"):
    with st.spinner("Reading Gmail and generating summaries..."):
        result = process_emails()

    st.success(result)