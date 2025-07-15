import pickle
import faiss
from sentence_transformers import SentenceTransformer
import pandas as pd

with open("models/ticket_classifier.pkl", "rb") as f:
    models = pickle.load(f)

category_model = models["category_model"]
urgency_model = models["urgency_model"]

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("models/vector_index.faiss")

with open("data/ticket_embeddings.pkl", "rb") as f:
    ticket_data = pickle.load(f)

df = pd.read_csv("data/tickets.csv")

def classify_ticket(text):
    category = category_model.predict([text])[0]
    urgency = urgency_model.predict([text])[0]
    return category, urgency

def find_similar_tickets(text, top_k=3):
    vector = embedding_model.encode([text])
    D, I = index.search(vector, top_k)
    results = [ticket_data["texts"][i] for i in I[0]]
    return results

def get_solution(ticket_text):
    row = df[df["ticket_text"] == ticket_text]
    if not row.empty:
        return row["solution"].values[0]
    return "Solution not found."