import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data/tickets.csv")
X = df["ticket_text"]
y_category = df["category"]
y_urgency = df["urgency"]

pipeline_cat = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])
pipeline_cat.fit(X, y_category)

pipeline_urg = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])
pipeline_urg.fit(X, y_urgency)

with open("models/ticket_classifier.pkl", "wb") as f:
    pickle.dump({"category_model": pipeline_cat, "urgency_model": pipeline_urg}, f)

print("✅ Models trained and saved.")
