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

def imputar_peso_faltante(df, weight_col='weight', specie_col='specie',
                          race_col='race', age_col='age', rango_edad=5,
                          metodo='mean'):
    """
    Imputa solo los valores faltantes en la columna de peso según especie, raza y grupo de edad.

    Parámetros:
    - df: DataFrame original.
    - weight_col: Columna con el peso.
    - specie_col: Columna con la especie.
    - race_col: Columna con la raza.
    - age_col: Columna con la edad.
    - rango_edad: Rango de edad para agrupar (ej. cada 5 años).
    - metodo: 'mean' o 'median' para calcular el valor de imputación.

    Retorna:
    - DataFrame con la columna de peso imputada solo en los valores faltantes.
    """
    df = df.copy()

    def imputar_fila(fila):
        if pd.isna(fila[weight_col]) or (isinstance(fila[weight_col], str) and fila[weight_col].strip() == ''):
            grupo_edad = (fila[age_col] // rango_edad) * rango_edad
            filtro = (
                (df[specie_col] == fila[specie_col]) &
                (df[race_col] == fila[race_col]) &
                ((df[age_col] // rango_edad) * rango_edad == grupo_edad) &
                (~df[weight_col].isna()) &
                (df[weight_col] != '')
            )
            valores = df.loc[filtro, weight_col]
            if metodo == 'mean':
                imputado = valores.astype(float).mean()
            elif metodo == 'median':
                imputado = valores.astype(float).median()
            else:
                raise ValueError("Método inválido. Usa 'mean' o 'median'.")
            return imputado
        else:
            return fila[weight_col]

    df[weight_col] = df.apply(imputar_fila, axis=1)

    return df
