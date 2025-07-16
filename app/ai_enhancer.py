from langdetect import detect
from deep_translator import GoogleTranslator
from langcodes import Language  # ✅ Convert lang code to full language name
from textblob import TextBlob
from groq_api.resolver import get_solution_from_groq

def detect_and_translate(text):
    lang_code = detect(text)
    lang_name = Language.get(lang_code).language_name()  # ✅ Get full name
    if lang_code != 'en':
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated, lang_name
    return text, lang_name

def summarize_ticket(text):
    return get_solution_from_groq(f"Summarize this IT ticket: {text}")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Frustrated/Urgent"
    else:
        return "Neutral"
