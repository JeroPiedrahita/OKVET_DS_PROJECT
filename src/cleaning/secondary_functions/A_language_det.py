##Importar librerias a usar
import pandas as pd
from nltk.corpus import stopwords
from langdetect import detect, DetectorFactory
import spacy

def detect_language(text):
    """Detects the language of the input text."""
    if pd.isna(text) or text.strip() == "":
        return None  # Return None for empty or missing text
    try:
        # Langdetect might raise an error for very short or ambiguous text
        lang = detect(text)
        return lang
    except:
        return None  # Return None if detection fails