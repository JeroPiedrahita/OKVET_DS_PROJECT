import pandas as pd
import os

''' __file__ → Es el nombre del archivo actual (1st_data_checking.py)
os.path.abspath(__file__) → Convierte ese nombre de archivo en una ruta absoluta completa
os.path.dirname(...) → Extrae solo el directorio donde está el archivo (sin incluir el archivo mismo)'''

# Obtener ruta absoluta del directorio donde está el script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

'''
os.path.join(script_dir, "../..") → Une la ruta del script con dos niveles hacia arriba (.. significa "subir un directorio")
os.path.abspath(...) → Convierte esa ruta relativa en una ruta absoluta'''


# Subir dos niveles desde src/cleaning → llegar a la raíz del proyecto
base_dir = os.path.abspath(os.path.join(script_dir, "../.."))

# Construir ruta a la carpeta 'data'
data_dir = os.path.join(base_dir, "data")

# Crear rutas absolutas a los archivos Excel
archivos = [
    os.path.join(data_dir, "citas.xlsx"),
    os.path.join(data_dir, "mascotas.xlsx"),
    os.path.join(data_dir, "consultas.xlsx"),
    os.path.join(data_dir, "desparasitaciones.xlsx")
]

# Lista de columnas típicas que podrían repetirse
columnas_repetidas = ["id", "nombre", "fecha", "peso", "created_at", "updated_at", "deleted_at", ""]

def revisar_hoja(nombre_archivo):
    excel = pd.ExcelFile(nombre_archivo)
    resultados = []

    for hoja in excel.sheet_names:
        df = pd.read_excel(nombre_archivo, sheet_name=hoja)
        resultado = {
            "Archivo": os.path.basename(nombre_archivo),
            "Hoja": hoja,
            "¿Tiene encabezados?": "Sí" if not df.columns.str.contains("Unnamed").all() else "No",
            "¿Tiene filas vacías?": "Sí" if df.isnull().all(axis=1).any() else "No",
            "¿Nombres de columnas inconsistentes?": "Sí" if df.columns.duplicated().any() else "No",
            "¿Celdas con espacios o símbolos?": "Sí" if df.astype(str).apply(lambda x: x.str.contains(r"\s|--|N/A", na=False)).any().any() else "No",
            "¿Valores tipo texto donde deberían ser números o fechas?": "Sí" if any(df.dtypes == object) else "No",
            "¿Columnas comunes como id, nombre, etc.?": "Sí" if any(col in df.columns.str.lower() for col in columnas_repetidas) else "No"
        }
        resultados.append(resultado)
    
    return resultados

# Aplicar revisión a todos los archivos
resumen = []
for archivo in archivos:
    resumen.extend(revisar_hoja(archivo))

# Mostrar los resultados en formato tabular
df_resumen = pd.DataFrame(resumen)
print(df_resumen)
