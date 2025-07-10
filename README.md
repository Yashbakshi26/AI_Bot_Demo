# 🧠 AI-Powered Lead Generation Demo

This Streamlit app showcases a **Custom GPT-powered lead enrichment tool** designed for B2B lead generation services.

## 🚀 Features

- Enter **industry, role, location, and use case**
- Fetch a small list of **B2B leads**
- Automatically **generate a personalized hook** for each lead using GPT-4
- View and **download a CSV file** with enriched data

## 🔧 Setup

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/leadgen_streamlit.git
cd leadgen_streamlit
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Add Streamlit secrets**  
Create a `.streamlit/secrets.toml` file:

```toml
SNOV_CLIENT_ID = "your-client-id"
SNOV_CLIENT_SECRET = "your-client-secret"
OPENAI_API_KEY = "your-openai-key"
```

4. **Run the app**  
```bash
streamlit run app.py
```

## 🤖 What does the custom GPT do?

It generates a **1-line personalized outreach hook** for each lead using OpenAI GPT-4, based on:

- The lead’s role and company
- The industry
- The use case you provide

Example:
> *"As a CTO at TechNova in the SaaS space, you're likely exploring AI tools that streamline outbound – here's one tailored for that."*

## 📦 To Deploy on Streamlit Cloud

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Connect your repo and deploy!

---

📬 Need help customizing or deploying? Reach out on [Fiverr Demo Page].
