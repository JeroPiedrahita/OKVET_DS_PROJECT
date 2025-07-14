

### ***Español:***

Esta carpeta contiene el código fuente del proyecto OKVET_DS_PROJECT.
Se encuentra organizado por módulos que permiten una fácil reutilización, mantenimiento y escalabilidad del sistema.
Cada subcarpeta representa un componente funcional del proyecto (limpieza, análisis, reportes, visualización, etc.).

***Estructura:***

- cleaning/: limpieza y preprocesamiento de los archivos .xlsx crudos.
- eda/: análisis exploratorio y cálculos estadísticos.
- reporting/: generación de informes automáticos (PDF, Excel, etc.).
- app/: futura interfaz gráfica (Streamlit, Dash o FastAPI).

***Instrucciones:***

1. Instalar dependencias: conda env create -f environment.yml
2. Ejecutar: python -m src.cleaning.00_general_cleaning
3. Explorar notebooks dentro de /notebooks.

---------------------------------------------------------------------------

### ***English:***

This folder contains the source code for the OKVET_DS_PROJECT.
It's organized into modular subfolders to allow for maintainability, reusability, and future scalability.
Each submodule corresponds to a functional part of the pipeline (cleaning, analysis, reporting, visualization, etc.).

***Structure:***

- cleaning/: data preprocessing and cleaning of raw Excel files.
- eda/: exploratory data analysis and statistical summaries.
- reporting/: automatic report generation (PDF, Excel, etc.).
- app/: future graphical user interface (e.g., Streamlit, Dash, or FastAPI).

***Instructions:***

1. Install dependencies: conda env create -f environment.yml
2. Run: python -m src.cleaning.00_general_cleaning
3. Explore notebooks inside /notebooks.
