###Funcion de limpieza especifica de los datos
#---------------------------------------------
#Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
#---------------------------------------------
#Llamado a la funcion de limpieza general
from src.cleaning.general_clean import limpieza_general
#---------------------------------------------
#Funcion de limpieza especifica de los datos
def limpieza_especifica(df, hoja_nombre):
    """
    Aplica reglas de limpieza específicas según el nombre de la hoja.
    Args:
        df (pd.DataFrame): DataFrame original ya procesado por limpieza_general().
        hoja_nombre (str): Nombre de la hoja (o archivo) que indica las reglas a aplicar.

    Returns:
        pd.DataFrame: DataFrame limpio y transformado.
    """
    hoja = hoja_nombre.lower().strip()

    if hoja == "citas":
     
      if "summary" in df.columns:
            split_cols = df["summary"].str.split("-", n=1, expand=True)
            df["tipo_consulta"] = split_cols[0].str.strip()
            df["veterinaria"] = split_cols[1].str.strip() if split_cols.shape[1] > 1 else ""
    #"Revisar como se rellenan los campos de veterinaria si estan tipo NAN o vacios"
      #Eliminar la columna "description"
      #CONFIRMAR ELIMINACION DE LA COLUMNA DESCRIPTION
      if "description" in df.columns:
        df = df.drop(columns=["description"])

      # Calcular la diferencia en horas entre 'end' y 'start'
      if "start" in df.columns and "end" in df.columns:
          df["tiempo_de_consulta"] = (df["end"] - df["start"]).dt.total_seconds() / 3600

      ##Eliminacion de la columna event_id, comments, form_id, form_type y Variables
      columnas_a_eliminar_citas = ["event_id", "comments", "form_id", "form_type", "variables", "responsible_id"]
      df = df.drop(columns=[col for col in columnas_a_eliminar_citas if col in df.columns], errors='ignore')

      ## HAY ERRORES EN EL CAMBIO DE LAS FECHAS-CAMBIA CALENDAR_ID Y QUITA LA HORA EN START Y END


    elif hoja == "consultas":
        if "dosis" in df.columns:
            df["dosis"] = df["dosis"].fillna(0).astype(int)
        if "vacuna" in df.columns:
            df["vacuna"] = df["vacuna"].str.strip().str.upper()



    # Agrega más hojas específicas según las necesidades...

    return df


