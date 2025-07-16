# groq_api/resolver.py

import os
from openai import OpenAI  # ✅ Correct import for Groq API usage

# ✅ Initialize Groq-compatible client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")  # Make sure this is set in your .env or Streamlit secrets
)

def get_solution_from_groq(ticket_text):
    """
    Uses Groq's LLaMA3 model to suggest a fix for the ticket.
    """
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an expert IT support assistant."},
                {"role": "user", "content": f"Suggest a fix for this helpdesk ticket: {ticket_text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"❌ Error from Groq API: {str(e)}"
