---
nav_title: Diagnósticos
article_title: Informe de diagnósticos
page_order: 3
description: "Aprende a utilizar el informe de diagnósticos para monitorear el estado de los datos de entrada y salida en BrazeAI Decisioning Studio."
---

# Informe de diagnósticos

> El informe de diagnósticos contiene dos tipos de informe diferentes: **De salida** y **De entrada**.

{% tabs local %}
{% tab outbound %}
El informe de diagnósticos de salida muestra el volumen diario de recomendaciones generadas y activadas en tus audiencias. Úsalo para detectar problemas de entrega, rastrear picos o caídas en las activaciones y confirmar que los mensajes están llegando a los grupos correctos según lo esperado.

![Informe de diagnósticos de salida que muestra un gráfico de líneas con el seguimiento del volumen diario de recomendaciones generadas y activadas para diferentes grupos de audiencia. El gráfico muestra dos líneas etiquetadas como Generadas y Activadas, con el eje Y representando el número de recomendaciones y el eje X mostrando las fechas. Una leyenda identifica cada línea por color. La interfaz incluye filtros desplegables para el rango de fechas y la selección de audiencia sobre el gráfico.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

El informe de diagnósticos de entrada monitorea el estado de tus fuentes de datos en BrazeAI<sup>TM</sup>. Rastrea detalles como el recuento de archivos, tamaños y volúmenes de filas para cada activo, lo que te ayuda a confirmar que los datos están fluyendo según lo esperado y a solucionar problemas antes de que afecten a tus agentes o campañas.

Puedes usar el menú desplegable para seleccionar diferentes métricas del gráfico, como el tamaño promedio de archivo o el recuento de archivos.

![Informe de diagnósticos de entrada que muestra un gráfico de líneas con el seguimiento del recuento diario de archivos y el tamaño promedio de archivo para los activos de datos entregados a BrazeAI<sup>TM</sup>. El gráfico muestra dos líneas etiquetadas como Recuento de archivos y Tamaño promedio de archivo en MB, con el eje Y representando los valores y el eje X mostrando las fechas. Sobre el gráfico hay filtros desplegables para el rango de fechas y la selección de activos de datos.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Consulta la siguiente tabla para obtener más detalles sobre cada métrica en el informe de entrada:

| Campo | Descripción |
|-------|-------------|
| Activo de datos | El nombre del conjunto de datos o archivo entregado. |
| Fecha | La fecha en que se recibieron los datos. |
| Última hora de entrega | La hora más reciente en que se entregaron los datos. |
| Recuento de archivos | El número total de archivos recibidos. |
| Tamaño máximo de archivo (MB) | El tamaño del archivo más grande recibido, en megabytes. |
| Tamaño promedio de archivo (MB) | El tamaño promedio de todos los archivos recibidos, en megabytes. |
| Recuento de filas de archivo | El número total de filas contenidas en los archivos entregados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}