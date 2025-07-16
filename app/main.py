import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils import classify_ticket, find_similar_tickets
from groq_api.resolver import get_solution_from_groq
from app.ai_enhancer import detect_and_translate, summarize_ticket, analyze_sentiment
from app.dashboard import render_dashboard

# Set up session storage for dynamic dashboard
if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="Smart Helpdesk Resolver", layout="centered")
st.title("🛠 Smart Helpdesk Ticket Classifier")

# 📝 Ticket input section
ticket_text = st.text_area("📜 Enter a new IT support ticket:")

if st.button("🚀 Analyze Ticket"):
    if ticket_text.strip() == "":
        st.warning("⚠️ Please enter a ticket message.")
    else:
        # 0️⃣ Detect Language & Translate
        translated_text, lang_name = detect_and_translate(ticket_text)
        if lang_name.lower() != "english":
            st.info(f"🌍 Detected language: **{lang_name}** → translated to English for analysis.")

        # 1️⃣ Summarize Ticket
        summary = summarize_ticket(translated_text)
        st.write(f"📝 **Summary**: `{summary}`")

        # 2️⃣ Sentiment Analysis
        sentiment = analyze_sentiment(translated_text)
        st.write(f"💬 **Sentiment**: `{sentiment}`")

        # 3️⃣ Classify Category & Urgency
        category, urgency = classify_ticket(translated_text)
        st.success(f"✅ **Category**: `{category}` | **Urgency**: `{urgency}`")

        # 4️⃣ Show Similar Past Issues
        st.subheader("🔎 Similar Past Issues")
        similar_tickets = find_similar_tickets(translated_text)
        for i, (issue, solution) in enumerate(similar_tickets):
            st.markdown(f"**{i+1}.** _{issue}_")
            st.caption(f"💡 Solution: {solution}")

        # 5️⃣ AI Suggested Fix
        st.subheader("🤖 Suggested Fix (Groq AI)")
        with st.spinner("Thinking..."):
            suggestion = get_solution_from_groq(translated_text)
            st.info(suggestion)

        # ✅ 6️⃣ Save data to session for dashboard
        st.session_state.history.append({
            "ticket": ticket_text,
            "summary": summary,
            "sentiment": sentiment,
            "category": category,
            "urgency": urgency
        })

# 📊 Optional Dashboard
st.divider()
if st.button("📊 View Dashboard"):
    render_dashboard()
