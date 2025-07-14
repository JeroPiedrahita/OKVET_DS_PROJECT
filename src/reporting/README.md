###📘 Español:

Este módulo permite la generación automática de reportes a partir de los datos limpios y analizados.
Los reportes pueden ser PDF, Excel o imágenes, listos para compartir con clientes o stakeholders.

***Contenido esperado:***

- Plantillas de reporte (resumen, análisis por ciudad, especie, etc.).
- Exportación a PDF o HTML.
- Composición de gráficos con texto interpretativo.

*Cómo usar:*

from src.reporting.report_generator import generate_pdf_report
generate_pdf_report(dataframe, output_path="reporte_mascotas.pdf")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###📗 English:

This module handles the automatic generation of reports from cleaned and analyzed data.
Reports can be exported to PDF, Excel, or images, ready to be shared with clients or stakeholders.

***Expected contents:***

- Report templates (summary, city-based analysis, species-based trends, etc.).
- Export to PDF or HTML.
- Integration of charts and descriptive text.

*How to use:*

from src.reporting.report_generator import generate_pdf_report
generate_pdf_report(dataframe, output_path="pet_report.pdf")
