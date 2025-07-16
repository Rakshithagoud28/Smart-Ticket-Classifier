import pandas as pd

df = pd.read_csv("data/tickets.csv")
print("Ticket Category Distribution:\n", df["category"].value_counts())
print("Urgency Label Distribution:\n", df["urgency"].value_counts())
