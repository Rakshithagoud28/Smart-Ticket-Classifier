from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_solution_from_groq(ticket_text):
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # ✅ Use this for now
        messages=[
            {"role": "system", "content": "You are an expert IT support engineer."},
            {"role": "user", "content": f"Suggest a fix for this issue: {ticket_text}"}
        ]
    )
    return response.choices[0].message.content
