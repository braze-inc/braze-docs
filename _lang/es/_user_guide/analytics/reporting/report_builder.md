---
nav_title: Generador de informes
article_title: Generador de informes
alias: /report_builder/
page_type: reference
description: "Este artículo de referencia describe la característica del generador de informes."
tool:
    - Reports
page_order: 6.2
---

# Generador de informes

> Esta página explica cómo utilizar el generador de informes para crear y ver informes detallados utilizando datos de Braze, y cómo añadir informes a los paneles.

## Uso de una plantilla de informe

1. Ve a **Análisis** > **Generador de informes (Nuevo)**.
2. Selecciona la flecha **Más opciones** situada junto al botón **Crear informe nuevo** y, a continuación, selecciona **Usar una plantilla de informe**.<br><br>![Menú desplegable del botón «Crear informe nuevo» con opciones para crear un informe personalizado o utilizar una plantilla.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecciona una de las plantillas de informe de la biblioteca de plantillas de Braze.
    - Utiliza los **elementos de fila** y el menú desplegable **Etiquetas** para encontrar informes relevantes para tus casos de uso.<br><br>![Ventana «Plantillas de informes de Braze» con una lista de plantillas de Braze entre las que elegir.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Sigue los pasos 3 y siguientes de [Creación de un informe](#creating-a-report) para hacer el informe aún más personalizado y adaptarlo a tu caso de uso.

## Creación de un informe

1. Ve a **Análisis** > **Generador de informes (Nuevo)**.
2. Selecciona **Crear informe nuevo**.
3. En el menú desplegable **Filas**, selecciona lo que deseas incluir en el informe:
    - Campañas
    - Canvas
    - Campañas y Canvas
    - Canales
    - Etiquetas

    Ten en cuenta que la selección **de** **filas** afectará a [las métricas que puedes ver](#metrics-availability). Por ejemplo, puedes ver métricas multivariantes solo si informas sobre **lienzos** o **campañas** con un desglose **de variantes**. No puedes ver esas métricas al generar informes sobre **campañas y lienzos**, incluso si esas campañas y lienzos tienen pruebas multivariantes. 

![La sección «Filas y columnas» con campos para seleccionar las filas y agrupaciones de tu informe.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (Opcional) Selecciona **Añadir desglose** para desglosar tus datos en vistas más detalladas:
    \- Canales
    \- Fecha
        \- Utiliza esta opción para dividir los datos en intervalos de tiempo más pequeños. Por ejemplo, si te interesa conocer el rendimiento diario de tus campañas, selecciona la siguiente configuración:
            - **Filas**: Campañas
            - **Agrupación:** Fecha
            - **Intervalo:** Días
    \- Variantes
    \- Campañas y encuestas

{% alert tip %}
Prueba diferentes configuraciones de opciones de desglose para explorar las [múltiples formas en que puedes desglosar tus datos.](#metrics-availability)
{% endalert %}

{: start="5"}
5\. En la sección **Columnas**, selecciona **Personalizar métricas**.

![La sección «Personalizar métricas» con opciones para seleccionar varias métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. Explora las métricas por categoría y selecciona la casilla correspondiente para añadir una métrica a tu informe.
    \- Reordena las métricas y columnas arrastrando el icono punteado hacia arriba o hacia abajo.
7\. En **Contenido del informe**, configura el intervalo de fechas para el que deseas incluir datos en tu informe.
8\. A continuación, dependiendo de tus selecciones en el paso 3, elige añadir manual o automáticamente campañas, lienzos o ambos a tu informe.
    - **Añadir manualmente:** Selecciona cada campaña o Canvas que desees incluir en el informe utilizando los filtros de fechas **de** **último envío** y etiquetas o canales, o buscando el nombre de la campaña o Canvas.<br><br>![La sección «Añadir campañas y lienzos manualmente» con una lista de campañas para seleccionar.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Añadir automáticamente:** Establece reglas para determinar qué campañas o lienzos se incluirán en el informe. Solo tienes que seleccionar un campo en esta página.
        Ten en cuenta que, a medida que las campañas o lienzos adicionales cumplan las condiciones que establezcas en esta pantalla, se añadirán automáticamente a las futuras ejecuciones de tu informe.<br><br>![La sección «Añadir automáticamente campañas y lienzos» con campos para establecer reglas sobre qué campañas y lienzos deben añadirse al informe.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. Ejecuta el informe seleccionando **Guardar&  Ejecutar**.

{% alert note %}
El informe puede tardar unos minutos en generarse, dependiendo del intervalo de fechas y del número de campañas o lienzos que hayas seleccionado en la fase de configuración.
{% endalert %}

## Disponibilidad de métricas

Tu selección para **Filas** afecta a las métricas que puedes seleccionar.

{% alert tip %}
Si deseas informar sobre variantes en Canvas o pasos en Canvas, selecciona **Canvases** para las filas y deja el campo vacío o selecciona **Fecha** como desglose. Esto crea un menú desplegable **Vista de Canvas** para ver solo las métricas de Canvas, o agrupar las métricas por variante, paso o mensaje. 

![El menú desplegable «Vista de Canvas» abierto.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrica | Descripción |
| --- | --- |
| Métricas de conversión de conversión | Disponible para campañas, lienzos, campañas y lienzos. |
| Entradas | Disponible para campañas, lienzos, campañas y lienzos, etiquetas. |
| Fecha del último envío | Disponible para campañas, lienzos, campañas y lienzos. Solo se muestra para campañas programadas; no aparece para campañas basadas en acciones o activadas por API. |
| Envíos | Disponible para cada canal relevante. |
| Mensajes enviados | Disponible para campañas, lienzos, campañas y lienzos, etiquetas. |
| Línea de asunto | Disponible para campañas de envío por correo electrónico con desglose **de variantes**, lienzos y lienzos con desglose **de variantes**. |
| Ingresos totales | Disponible para campañas, lienzos, campañas y lienzos, etiquetas. No disponible con el desglose **de canales**. |
| Impresiones únicas | Disponible para campañas, lienzos, campañas y lienzos, etiquetas. |
| Destinatarios únicos | Disponible para campañas, lienzos, campañas y lienzos, etiquetas. No disponible con el desglose **de canales**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Variantes de mensajes eliminados

Las estadísticas de las variantes de mensajes eliminados no se muestran cuando desglosas tu informe por campañas o lienzos. Sin embargo, los totales a nivel de canal incluyen todas las estadísticas, independientemente de si la variante se ha eliminado. Por ejemplo, _los envíos_ por correo electrónico incluyen todos los envíos por correo electrónico, pero si desglosan esas estadísticas por campaña, las cifras pueden ser inferiores porque se filtran los envíos de variantes de mensajes eliminados.

## Ver un informe

Después de ejecutar el informe, podrás ver los resultados en formato de tabla en la página del informe. 

![Una tabla con los datos del informe para las métricas de cada campaña.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Creación de un gráfico de informe

En la parte inferior de la página, puedes crear un gráfico con tus datos seleccionando un **tipo de gráfico** y configurando las métricas del mismo. De forma predeterminada, verás la primera métrica.

![Un gráfico con los datos del informe y opciones para configurar el eje X, el eje Y, el tipo de gráfico y mucho más.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para crear un gráfico de líneas, selecciona **Fecha** como opción de desglose al configurar el informe. Esto mostrará las tendencias a lo largo del tiempo.
{% endalert %}

#### Descargar un gráfico de informe

Para descargar una imagen del gráfico del informe, selecciona el icono punteado y luego elige una opción de descarga.

![Un menú con opciones de descarga para diferentes formatos de archivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartir un informe

Puedes compartir un enlace al panel del informe seleccionando **Compartir** y una de estas opciones:
- **Compartir un enlace:** Copia y comparte el enlace.

![Menú desplegable «Compartir enlace» con un enlace al informe.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Enviar o programar un correo electrónico:** Envía un correo electrónico inmediatamente o a una hora determinada que contenga un enlace de descarga que caduque al cabo de una hora. Puedes seleccionar destinatarios de entre los usuarios de la empresa que aparecen en el menú desplegable **Destinatarios de correo electrónico** o introducir cualquier otra dirección de correo electrónico.

![Ventana «Programar un correo electrónico» con campos para elegir el formato del informe, quién debe recibirlo y cuándo debe enviarse.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Descargar CSV:** Descarga un archivo CSV del informe.

## Añadir un informe a un panel

1. Selecciona el icono punteado situado en la parte superior de la tabla del informe.
2. Selecciona **Añadir al panel**.
3. Selecciona si deseas crear un nuevo panel o añadirlo a uno ya existente.<br><br>![Ventana con opciones para seleccionar si deseas añadir el informe a un panel nuevo o existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Sigue los pasos indicados en [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) para obtener más información sobre cómo crear un panel.

