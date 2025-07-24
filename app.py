# === 📄 app.py ===
import streamlit as st
from utils.extract import extract_text
from agent.auditor_agent import audit_policy

st.set_page_config(page_title="Policy Audit AI", layout="wide")
st.title("📘 Policy Audit AI")

uploaded_file = st.file_uploader("Upload a policy document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)
    st.subheader("📄 Extracted Text Preview")
    st.text_area("Text", text[:2000], height=300)

    if st.button("🧠 Run Audit"):
        with st.spinner("Auditing with AI..."):
            result = audit_policy(text)
            st.success("Audit Complete!")

            st.subheader("📋 Audit Report")
            st.json(result)

            if st.button("📥 Download Report"):
                import json
                import datetime
                st.download_button("Download", json.dumps(result, indent=2), file_name=f"audit_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.json")

