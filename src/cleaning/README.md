###📘 Español:

Este módulo contiene todas las funciones relacionadas con la limpieza de datos, desde procesamiento general hasta reglas específicas por hoja de Excel.
Aquí se estandarizan nombres de columnas, se imputan valores faltantes, se realiza lematización de texto, y más.

***Estructura:***

- general_clean.py: limpieza estándar que se aplica a todos los archivos.
- specific_clean.py: contiene reglas particulares por hoja.
- config_cleaning.py: configuración centralizada que define qué reglas aplicar por hoja.
- secondary_functions/: funciones auxiliares como lematización, detección de idioma, cálculo de edad, etc.

*Cómo usar:*
python -m src.cleaning.general_clean

**Dependencias clave:***

- pandas
- nltk
- spacy
- langdetect

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###📗 English:

This module contains all functions related to data cleaning, from general processing to sheet-specific rules.
It includes column standardization, missing value imputation, text lemmatization, and more.

***Structure:***

- general_clean.py: general cleaning applied to all files.
- specific_clean.py: contains tailored rules per Excel sheet.
- config_cleaning.py: centralized config for which rules apply to which sheet.
- secondary_functions/: helpers like lemmatization, language detection, age calculations, etc.

*How to use:*
python -m src.cleaning.general_clean

***Key dependencies:***

- pandas
- nltk
- spacy
- langdetect


