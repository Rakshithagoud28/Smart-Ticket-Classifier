def get_solution_from_groq(ticket_text):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an expert IT support assistant."},
            {"role": "user", "content": f"Suggest a fix for this helpdesk ticket: {ticket_text}"}
        ]
    )
    return response.choices[0].message.content.strip()
