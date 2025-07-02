import pandas as pd

def limpiar_datos(df, columnas_fechas=None, rellenos = None, eliminar_cols = True):
    
    # Eliminar columnas innecesarias
    if eliminar_cols:
        df.dropna(axis=1, how='all', inplace=True)

    # Convertir columnas de fecha a datetime
    if columnas_fechas:
        for col in columnas_fechas:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')


    # Imputar valores nulos

    if rellenos: 
        for col, valor in rellenos.items():
            if col in df.columns:
                df[col] = df[col].fillna(valor)
    return df


#
def clean_dataframe(df):
    df_cleaned = df.copy()

    # Eliminar columnas con todos los valores nulos
    df_cleaned.dropna(axis=1, how='all', inplace=True)

    # Eliminar columnas que contienen 'dx', 'deleted_at' o 'waiting_room_shift_id'
    cols_to_drop = [col for col in df_cleaned.columns if any(keyword in col for keyword in ['dx', 'deleted_at', 'waiting_room_shift_id'])]
    df_cleaned.drop(columns=cols_to_drop, inplace=True)

    # Convertir columnas de fecha a tipo datetime
    for col in df_cleaned.columns:
        if any(kw in col.lower() for kw in ['date', 'at']):
            try:
                df_cleaned[col] = pd.to_datetime(df_cleaned[col], errors='coerce')
            except:
                pass

    # Imputar columnas de tipo texto con pocos valores únicos
    for col in df_cleaned.select_dtypes(include='object'):
        if df_cleaned[col].isnull().sum() > 0 and df_cleaned[col].nunique() < 10:
            df_cleaned[col].fillna('No reportado', inplace=True)

    return df_cleaned
