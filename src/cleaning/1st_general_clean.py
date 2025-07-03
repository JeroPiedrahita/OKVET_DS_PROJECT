import os
import pandas as pd

# ------------------------------
# Función de limpieza general
# ------------------------------
def limpieza_general(df):
    if df is None or df.empty:
        return None
    
    #Eliminar columnas deleted_at, waiting_room_shift_id, dx
    columnas_a_eliminar = ["deleted_at", "waiting_room_shift_id", "dx"]
    df = df.drop(columns=[col for col in columnas_a_eliminar if col in df.columns], errors='ignore')

    df.columns = df.columns.str.strip().str.lower()
    df.replace(["", " ", "N/A", "n/a", "--"], pd.NA, inplace=True)
    df = df.dropna(axis=1, how='all')

    if df.empty:
        return None

    umbral_columnas = int(df.shape[1] * 0.65)
    df = df[df.isnull().sum(axis=1) <= umbral_columnas]
    df.reset_index(drop=True, inplace=True)

    # Convertir automáticamente columnas que parecen ser fechas (CON PALABRAS CLAVE)
    posibles_fechas = [col for col in df.columns if any(keyword in col for keyword in ['fecha', 'date', 'created', 'updated', "deworming", "consult_at", "start", "end", "birth", "admission", "discharge"])]
    for col in posibles_fechas:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Ordenar si están presentes
    orden_cols = [col for col in ["updated_at", "created_at"] if col in df.columns]
    if orden_cols:
        df = df.sort_values(by=orden_cols, ascending=False).reset_index(drop=True)

    # Rellenar texto faltante con "NA"
    for col in df.select_dtypes(exclude=['number']).columns:
        df[col] = df[col].fillna("NA")

    return df


# ------------------------------
# Rutas y configuración
# ------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(script_dir, "../.."))
data_dir = os.path.join(base_dir, "data")

# ------------------------------
# Inicializar estructuras de almacenamiento
# ------------------------------
dfs_originales = []
dfs_limpios = []
nombres_dataframes = []

# ------------------------------
# Procesar todos los archivos Excel
# ------------------------------
for archivo in os.listdir(data_dir):
    if archivo.endswith(".xlsx"):
        nombre_base = os.path.splitext(archivo)[0]  # sin la extensión
        ruta = os.path.join(data_dir, archivo)

        # Leer la única hoja (ej. "Sheet 1")
        df_original = pd.read_excel(ruta)
        dfs_originales.append(df_original)

        # Aplicar limpieza sin imputar
        df_limpio = limpieza_general(df_original.copy())
        dfs_limpios.append(df_limpio)

        # Crear nombre dinámico para el DataFrame limpio
        nombre_df = f"df_{nombre_base}"
        globals()[nombre_df] = df_limpio  # Variable con nombre dinámico

        nombres_dataframes.append(nombre_df)

# ------------------------------
# Confirmar resultados
# ------------------------------
print("✔ Se cargaron y procesaron los siguientes DataFrames:")
for nombre in nombres_dataframes:
    print(f" - {nombre}")



print("\n🧾 Vista previa de cada DataFrame limpio:\n")

for nombre, df in zip(nombres_dataframes, dfs_limpios):
    print(f"🔹 {nombre}")
    print(df.head())  # Muestra las primeras 5 filas
    print("-" * 40)
