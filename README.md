# 🛠 Smart Helpdesk Ticket Classifier & Resolver

An AI-powered solution that automates the classification, prioritization, and resolution of IT support tickets using NLP, vector search, and Groq LLM.

---

## 🚩 Problem Statement

Large companies receive hundreds of helpdesk tickets daily — issues like _"WiFi not working"_ or _"System overheating."_  
Manually processing them slows down IT teams and delays resolution time.

---

## ✅ Solution

This Smart Helpdesk system:
- Automatically classifies each ticket (e.g., **Network**, **Hardware**, **Software**, etc.)
- Predicts its **urgency** (High / Medium / Low)
- Finds **similar past issues** using **FAISS vector search**
- Suggests the **best fix** using **Groq LLM**

---

## 🔍 Sample Use Case

> A user enters:  
> _"My laptop screen is flickering."_  

✅ The app responds:
- **Category:** Hardware  
- **Urgency:** High  
- 🔎 **Similar Past Issues:**  
  - “Monitor not turning on”  
  - “Display issue with HDMI”  
- 🤖 **Groq Suggested Fix:**  
  _"Check display drivers or connect to external monitor to isolate issue."_  

---

## 🧠 Tech Stack

| Component       | Tool/Library                | Purpose                          |
|----------------|-----------------------------|----------------------------------|
| Frontend       | Streamlit                   | Interactive web app              |
| Classifier     | scikit-learn, spaCy         | Category & urgency prediction    |
| Embeddings     | sentence-transformers       | Ticket encoding                  |
| Vector Search  | FAISS                       | Find similar past issues         |
| LLM            | Groq API                    | Generate AI-based ticket fix     |
| Backend        | Python                      | Logic and orchestration          |
| Storage        | CSV, Pickle                 | Tickets and vector data          |

---


---

## ⚙️ How to Run Locally

git clone https://github.com/Rakshithagoud28/Smart-Ticket-Classifier.git
cd Smart-Ticket-Classifier
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
GROQ_API_KEY = "your-groq-api-key"
streamlit run app/main.py


Built with ❤️ by Rakshitha Goud
Inspired by the latest AI-powered helpdesk automation trends.