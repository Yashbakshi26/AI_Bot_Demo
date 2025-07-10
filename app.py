import streamlit as st
import pandas as pd
import requests
import openai
import os

# --- CONFIG ---
SNOV_CLIENT_ID = st.secrets.get("SNOV_CLIENT_ID", "your-client-id-here")
SNOV_CLIENT_SECRET = st.secrets.get("SNOV_CLIENT_SECRET", "your-client-secret")
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", "your-openai-key")

openai.api_key = OPENAI_API_KEY

# --- STREAMLIT UI ---
st.title("🎯 AI-Powered Lead Generation Demo")
st.write("Enter the target details and get a list of enriched leads.")

industry = st.text_input("Industry", "SaaS")
role = st.text_input("Target Role", "CTO")
location = st.text_input("Location", "United States")
use_case = st.text_input("Use Case (for outreach message)", "AI-based lead gen tool")

if st.button("🔍 Generate Leads"):
    with st.spinner("Fetching leads..."):

        # --- 1. Get SNOV Access Token (Mocked) ---
        def get_snov_token():
            return "mocked-access-token"

        token = get_snov_token()

        # --- 2. Fetch Leads (Mocked API Call) ---
        def fetch_leads():
            return [
                {"name": "Alice Chen", "role": "CTO", "company": "TechNova", "email": "alice@technova.com", "linkedin": "linkedin.com/in/alicechen"},
                {"name": "Brian Patel", "role": "VP Engineering", "company": "CloudSprout", "email": "brian@cloudsprout.io", "linkedin": "linkedin.com/in/brianpatel"},
            ]

        leads = fetch_leads()

        # --- 3. GPT Enrichment ---
        enriched = []
        for lead in leads:
            prompt = (
                f"Why would a {lead['role']} at {lead['company']} in {industry} be interested in {use_case}? "
                "Write a 1-line personalized hook."
            )
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=60,
                )
                hook = response["choices"][0]["message"]["content"].strip()
            except Exception as e:
                hook = f"[GPT Error] {str(e)}"

            enriched.append({**lead, "hook": hook})

        # --- 4. Display Table ---
        df = pd.DataFrame(enriched)
        st.dataframe(df)

        # --- 5. CSV Download ---
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, "leads.csv", "text/csv")
