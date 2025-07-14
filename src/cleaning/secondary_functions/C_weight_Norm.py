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


def normalizacion_peso(df):
    """
    Normaliza las columnas 'weight' y 'weight_unit' en un DataFrame,
    convirtiendo 'g' y 'lb' a 'Kg'.

    Args:
        df (pd.DataFrame): DataFrame con las columnas 'weight' y 'weight_unit'.

    Returns:
        pd.DataFrame: DataFrame con las columnas de peso normalizadas.
    """
    if df is None or df.empty:
        return None

    # Asegurarse de que las columnas 'weight' y 'weight_unit' existan
    if 'weight' not in df.columns or 'weight_unit' not in df.columns:
        print("Las columnas 'weight' o 'weight_unit' no se encuentran en el DataFrame.")
        return df

    # Convertir la columna 'weight' a tipo numérico, manejando errores
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')

    # Convertir la columna 'weight_unit' a minúsculas para facilitar la comparación
    df['weight_unit'] = df['weight_unit'].str.lower()

    # Definir factores de conversión a Kg
    conversion_factors = {
        'g': 0.001,  # gramos a kilogramos
        'lb': 0.453592  # libras a kilogramos
    }

    # Iterar sobre las filas y aplicar la conversión
    for index, row in df.iterrows():
        unit = row['weight_unit']
        weight = row['weight']

        if pd.notna(weight) and unit in conversion_factors:
            df.at[index, 'weight'] = weight * conversion_factors[unit]
            df.at[index, 'weight_unit'] = 'kg' # Cambiar la unidad a Kg

    return df

# Ejemplo de uso (asumiendo que df_limpio_esp es tu DataFrame actual)
#df_limpio_esp = normalizacion_peso(df_limpio_esp)
 #display(df_limpio_esp.head())