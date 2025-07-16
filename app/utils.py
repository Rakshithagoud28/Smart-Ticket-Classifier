import pickle
import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from deep_translator import GoogleTranslator  # ✅ Added for translation

# Load trained models
with open("models/ticket_classifier.pkl", "rb") as f:
    models = pickle.load(f)

category_model = models["category_model"]
urgency_model = models["urgency_model"]

# Load embedding model & FAISS index
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("models/vector_index.faiss")

# Load ticket embeddings and original ticket data
with open("data/ticket_embeddings.pkl", "rb") as f:
    ticket_data = pickle.load(f)

df = pd.read_csv("data/tickets.csv")

def classify_ticket(text):
    category = category_model.predict([text])[0]
    urgency = urgency_model.predict([text])[0]
    return category, urgency

def find_similar_tickets(text, top_k=3):
    vector = embedding_model.encode([text])
    D, I = index.search(np.array(vector).astype("float32"), top_k)
    results = []
    for i in I[0]:
        if i < len(df):
            issue = df.iloc[i]["ticket_text"]
            solution = df.iloc[i]["solution"]
            results.append((issue, solution))
    return results

def get_solution(ticket_text):
    row = df[df["ticket_text"] == ticket_text]
    if not row.empty:
        return row["solution"].values[0]
    return "Solution not found."

def translate_to_english(text):
    """
    Detects and translates the input ticket text to English using Deep Translator.
    Useful for multi-language support.
    """
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        return text  # Fallback to original if translation fails
