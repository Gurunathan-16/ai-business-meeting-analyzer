import streamlit as st
from analyzer import analyze_meeting

st.set_page_config(
    page_title="AI Business Meeting Analyzer",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    st.title("📊 Meeting Analyzer")

    st.markdown("### Features")

    st.write("✅ Executive Summary")
    st.write("✅ Decisions")
    st.write("✅ Action Items")
    st.write("✅ Risks")
    st.write("✅ Participant Analysis")
    st.write("✅ Project Status")

    st.divider()

    st.info("Powered by Google Gemini")

st.title("📊 AI Business Meeting Analyzer")
st.markdown("Upload a meeting transcript and let AI extract key business insights.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt"]
)

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Meeting Transcript")

    with st.expander("View Transcript"):
        st.text(transcript)

    if st.button("🚀 Analyze Meeting", use_container_width=True):
        with st.spinner("Analyzing meeting..."):
            result = analyze_meeting(transcript)
        st.success("Analysis Complete!")
        st.markdown(result)