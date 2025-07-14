##Importar librerias a usar
import pandas as pd
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords_es = set(stopwords.words('spanish'))
stopwords_en = set(stopwords.words('english'))


from langdetect import detect, DetectorFactory
import spacy
nlp_es = spacy.load("es_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

from src.cleaning.secondary_functions.H_clean_text import clean_text
from src.cleaning.secondary_functions.A_language_det import detect_language

# Set a seed for reproducibility
def clean_with_stopwords_and_lemmatization(text):
    """
    Cleans text by detecting language, removing stopwords, and applying lemmatization.
    """
    if pd.isna(text) or text.strip() == "" or text == "NA":
        return text # Return original value for empty, missing, or "NA" text

    language = detect_language(text)

    if language == 'es':
        doc = nlp_es(text)
        lemmatized = [token.lemma_ for token in doc if token.text.lower() not in stopwords_es]
    elif language == 'en':
        doc = nlp_en(text)
        lemmatized = [token.lemma_ for token in doc if token.text.lower() not in stopwords_en]
    else:
        # Handle other languages or detection failures (e.g., return original text or empty string)
        return text # Return original text if language is not Spanish or English

    return " ".join(lemmatized).strip()