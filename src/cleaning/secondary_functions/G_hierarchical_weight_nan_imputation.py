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

##Funcion de imputacion de datos NAN en WEIGHT
def imputar_weight_nan_jerarquico(df, specie_col='specie', race_col='race', age_col='age', weight_col='weight', mostrar_log=True):
    log = []

    # Trata valores 0.0 como NaN
    df[weight_col] = df[weight_col].replace(0.0, pd.NA)

    try:
        media_esp_raza_edad = df.groupby([specie_col, race_col, age_col])[weight_col].mean()
        media_esp_raza = df.groupby([specie_col, race_col])[weight_col].mean()
        media_esp = df.groupby(specie_col)[weight_col].mean()
        media_global = df[weight_col].mean()
    except Exception as e:
        print("⚠️ Error al calcular medias por grupo:", e)
        return df

    def imputar_fila(row):
        try:
            if pd.notna(row[weight_col]):
                return row[weight_col]

            clave1 = (row[specie_col], row[race_col], row[age_col])
            if clave1 in media_esp_raza_edad:
                imputado = media_esp_raza_edad[clave1]
                nivel = "especie + raza + edad"
            elif (row[specie_col], row[race_col]) in media_esp_raza:
                imputado = media_esp_raza[(row[specie_col], row[race_col])]
                nivel = "especie + raza"
            elif row[specie_col] in media_esp:
                imputado = media_esp[row[specie_col]]
                nivel = "especie"
            else:
                imputado = media_global
                nivel = "global"

            if mostrar_log:
                log.append((row[specie_col], row[race_col], row[age_col], round(imputado, 2), nivel))

            return imputado

        except Exception as e:
            print(f"❌ Error al imputar fila: {row.to_dict()}")
            print("   → Detalle del error:", e)
            return media_global

    try:
        df[weight_col] = df.apply(imputar_fila, axis=1)
    except Exception as e:
        print("⚠️ Error al aplicar imputaciones:", e)
        return df

    if mostrar_log:
        print("\n📋 Imputación jerárquica de pesos[Kg]:")
        for specie, race, age, valor, nivel in log:
            print(f"→ {specie} / {race} / edad {age}: imputado con {nivel} = {valor}")

    return df