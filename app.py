import streamlit as st
from gmail_to_sheet import process_emails

st.set_page_config(
    page_title="AI Gmail PDF Summarizer",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

h1, h2, h3, h4, h5, h6 {
    color: white !important;
}
section[data-testid="stSidebar"] {
    background-color: #f8fafc;
}

section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

div.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    font-size: 20px;
    font-weight: bold;

    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
}

div.stButton > button:hover {
    background-color: #1d4ed8 !important;
    color: white !important;
}

[data-testid="stMetricValue"] {
    font-size: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style='text-align:center;'>📧 AI Gmail PDF Summarizer</h1>

<h4 style='text-align:center;color:lightgray;'>
Extract PDF attachments • Generate AI summaries • Save to Google Sheets
</h4>
""", unsafe_allow_html=True)

st.divider()

with st.sidebar:
    st.title("⚙️ Dashboard")

    st.markdown("---")

    st.subheader("🤖 AI Model")
    st.success("Llama 3.2 3B")

    st.subheader("📊 Google Sheet")
    st.link_button(
        "Open Google Sheet",
        "https://docs.google.com/spreadsheets/d/1DnDzJlIe-uaeaMkT0e8m-YNXW7yPmWUQtXA_h0XpMng/edit",
        use_container_width=True
    )

    st.markdown("---")

    st.caption(
        "Fetch PDF attachments from Gmail, generate AI summaries using Llama 3.2, and automatically save results to Google Sheets."
    )

if st.button("🚀 Fetch & Summarize PDFs"):
    with st.spinner("Reading Gmail and generating summaries..."):
        result = process_emails()

    st.balloons()
    st.success(
        f"✅ Added {result['new_pdfs']} new PDF emails"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📄 PDFs Processed",
        result["total_pdfs"]
    )

    col2.metric(
        "🆕 New PDFs Added",
        result["new_pdfs"]
    )

    col3.metric(
        "🔒 Password Protected",
        result["password_protected"]
    )