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


def imputar_weight_por_media(df, specie_col='specie', race_col='race', weight_col='weight', mostrar_log=True):
    log_imputaciones = []

    def limpiar_grupo(grupo):
        # Excluir NaN antes de calcular cuartiles
        datos_validos = grupo[weight_col].dropna()

        q1 = datos_validos.quantile(0.25)
        q3 = datos_validos.quantile(0.75)
        iqr = q3 - q1
        limite_inf = q1 - 1.5 * iqr
        limite_sup = q3 + 1.5 * iqr

        # Calcular media solo con valores válidos
        media = datos_validos[(datos_validos >= limite_inf) & (datos_validos <= limite_sup)].mean()

        # Contar y reemplazar solo valores extremos, no NaN
        def corregir(x):
            if pd.isna(x):
                return x
            return media if x < limite_inf or x > limite_sup else x

        grupo[weight_col] = grupo[weight_col].apply(corregir)

        cantidad_outliers = ((datos_validos < limite_inf) | (datos_validos > limite_sup)).sum()
        if mostrar_log:
            grupo_id = (grupo[specie_col].iloc[0], grupo[race_col].iloc[0])
            log_imputaciones.append((grupo_id, cantidad_outliers, round(media, 2)))

        return grupo

    df_corregido = df.groupby([specie_col, race_col], group_keys=False).apply(limpiar_grupo)

    if mostrar_log:
        print("\n📋 Outliers corregidos por grupo (sin tocar NaN):")
        for (specie, race), cantidad, media in log_imputaciones:
            print(f"→ {specie} / {race}: {cantidad} valores corregidos con media = {media}")

    return df_corregido