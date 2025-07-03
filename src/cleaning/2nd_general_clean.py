import os
import pandas as pd

def limpieza_general(df):
    # Quitar espacios de nombres de columnas y ponerlas en minúscula
    df.columns = df.columns.str.strip().str.lower()

    # Eliminar filas completamente vacías
    df = df.dropna(how='all')

    # Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how='all')

    # Eliminar Columnas created_at, updated_at, deleted_at
    columnas_a_eliminar = ["created_at", "updated_at", "deleted_at"]
    df = df.drop(columns=[col for col in columnas_a_eliminar if col in df.columns])

    # Reemplazar valores nulos estándar
    df.replace(["", " ", "N/A", "n/a", "--"], pd.NA, inplace=True)

    # Resetear el índice si es necesario
    df.reset_index(drop=True, inplace=True)

    return df

# 1. Obtener ruta del directorio donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Subir a la raíz del proyecto
base_dir = os.path.abspath(os.path.join(script_dir, "../.."))

# 3. Ir a la carpeta "data"
data_dir = os.path.join(base_dir, "data")

# 4. Obtener todos los archivos .xlsx de esa carpeta
archivos = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".xlsx")]

# 5. Leer y limpiar cada archivo
for archivo in archivos:
    print(f"\n📂 Procesando archivo: {os.path.basename(archivo)}")

    excel = pd.ExcelFile(archivo)
    for hoja in excel.sheet_names:
        print(f"  ➤ Hoja: {hoja}")
        df = pd.read_excel(archivo, sheet_name=hoja)
        df_limpio = limpieza_general(df)

        # Aquí podrías guardar, analizar, o visualizar el df_limpio si quieres
        print(f"    ✔ Columnas después de limpieza: {df_limpio.columns.tolist()}")
