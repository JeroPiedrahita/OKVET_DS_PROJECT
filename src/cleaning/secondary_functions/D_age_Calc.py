##Importar librerias a usar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import date
import re
import string
import nltk
from nltk.corpus import stopwords
import spacy
from langdetect import detect, DetectorFactory
import spacy

from datetime import date

def calcular_edad(fecha_nacimiento):
    """Calcula la edad en años dada una fecha de nacimiento."""
    if pd.isna(fecha_nacimiento):
        return pd.NA
    today = date.today()
    # Handle potential future dates
    if fecha_nacimiento.date() > today:
        return 0
    return today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

#df_limpio_esp['age_in_years'] = df_limpio['birth_at'].apply(calcular_edad)

#display(df_limpio_esp[['name', 'birth_at', 'age_in_years']].head())