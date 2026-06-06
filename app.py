import streamlit as st
import webbrowser
from gmail_to_sheet import process_emails

st.set_page_config(page_title="AI Gmail PDF Summarizer")

st.title("📧 AI Gmail PDF Summarizer")
if "sheet_opened" not in st.session_state:
    webbrowser.open(
        "https://docs.google.com/spreadsheets/d/1DnDzJlIe-uaeaMkT0e8m-YNXW7yPmWUQtXA_h0XpMng/edit"
    )
    st.session_state.sheet_opened = True

st.write(
    "Fetch Gmail emails, extract PDF attachments, and generate AI summaries."
)

if st.button("Fetch Emails"):
    with st.spinner("Reading Gmail and generating summaries..."):
        result = process_emails()

    st.success(result)