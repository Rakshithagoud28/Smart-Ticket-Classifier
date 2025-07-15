import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
import pickle
import os

df = pd.read_csv("data/tickets.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(df["ticket_text"].tolist(), show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "models/vector_index.faiss")

with open("data/ticket_embeddings.pkl", "wb") as f:
    pickle.dump({"ids": df["id"].tolist(), "texts": df["ticket_text"].tolist()}, f)

print("✅ FAISS index and embeddings saved.")
