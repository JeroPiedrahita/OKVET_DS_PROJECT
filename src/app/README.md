### 📘 Español:
Este módulo contiene el frontend del proyecto, es decir, la interfaz gráfica con la que los usuarios podrán interactuar.
Aquí se mostrarán los gráficos, tablas y reportes generados con opciones de filtrado, navegación e interacción.

Puede estar construido con tecnologías como Streamlit, Dash o integraciones con FastAPI y frontend en JavaScript.

Estructura:

- main.py: archivo principal que lanza la aplicación.
- components/: elementos visuales reutilizables (filtros, cards, gráficas).
- pages/: vistas separadas por funcionalidades (ej. consumo, vacunas, reportes).
- assets/: imágenes, íconos y archivos estáticos de estilo.
- config/: parámetros generales como rutas, nombres, colores, etc.

*Cómo ejecutar la app (ejemplo con Streamlit):*

streamlit run app/main.py

***Dependencias clave:***

- streamlit o dash
- pandas
- plotly / matplotlib / seaborn
- (opcional) fastapi, jinja2, requests

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📗 English:
This module contains the frontend of the project, meaning the graphical interface that users will interact with.
It will display generated charts, tables, and reports, with filtering, navigation, and interactive options.

It can be built using technologies like Streamlit, Dash, or even FastAPI + a JavaScript frontend.

***Structure:***

- main.py: main file that launches the application.
- components/: reusable UI elements (filters, cards, charts).
- pages/: separated views by functionality (e.g., consumption, vaccines, reports).
- assets/: images, icons, and static style files.
- config/: general settings like paths, names, colors, etc.

***How to run the app (example using Streamlit):***

streamlit run app/main.py


***Key dependencies:***

- streamlit or dash
- pandas
- plotly / matplotlib / seaborn
- (optional) fastapi, jinja2, requests
