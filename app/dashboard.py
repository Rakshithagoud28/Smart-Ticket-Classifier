import streamlit as st
import pandas as pd
import plotly.express as px

def render_dashboard():
    st.header("📊 Ticket Insights Dashboard")

    if "history" not in st.session_state or len(st.session_state.history) == 0:
        st.warning("No ticket data available. Please analyze at least one ticket.")
        return

    # Convert session history to DataFrame
    df = pd.DataFrame(st.session_state.history)

    # 🔢 Number of tickets
    st.metric("Total Tickets Analyzed", len(df))

    # 📂 Category Distribution
    st.subheader("📁 Categories")
    fig1 = px.pie(df, names="category", title="Ticket Categories")
    st.plotly_chart(fig1, use_container_width=True)

    # 💬 Sentiment Distribution (Fix Here ✅)
    st.subheader("💬 Sentiment")
    sentiment_counts = df["sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["sentiment", "count"]  # Rename for clarity
    fig2 = px.bar(sentiment_counts, x="sentiment", y="count", title="Sentiment Distribution")
    st.plotly_chart(fig2, use_container_width=True)

    # 🔥 Urgency Breakdown
    st.subheader("⚠️ Urgency Levels")
    urgency_counts = df["urgency"].value_counts().reset_index()
    urgency_counts.columns = ["urgency", "count"]
    fig3 = px.bar(urgency_counts, x="urgency", y="count", title="Urgency Levels")
    st.plotly_chart(fig3, use_container_width=True)
