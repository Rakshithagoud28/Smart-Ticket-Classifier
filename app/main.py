import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from utils import classify_ticket, find_similar_tickets, get_solution

from groq_api.resolver import get_solution_from_groq

st.set_page_config(page_title="Smart Helpdesk Resolver", layout="centered")
st.title("🛠 Smart Helpdesk Ticket Classifier")

ticket_text = st.text_area("📜 Enter a new IT support ticket:")

if st.button("🚀 Analyze Ticket"):
    if ticket_text.strip() == "":
        st.warning("Please enter a ticket message.")
    else:
        category, urgency = classify_ticket(ticket_text)
        st.success(f"✅ Category: `{category}` | Urgency: `{urgency}`")

        st.subheader("🔎 Similar Past Issues")
        similar = find_similar_tickets(ticket_text)
        for i, t in enumerate(similar):
            st.write(f"**{i+1}.** _{t}_")
            st.caption(f"💡 Solution: {get_solution(t)}")

        st.subheader("🤖 Suggested Fix (Groq AI)")
        with st.spinner("Thinking..."):
            suggestion = get_solution_from_groq(ticket_text)
            st.info(suggestion)