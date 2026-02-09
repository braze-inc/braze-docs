---
nav_title: Generador de informes
article_title: Generador de informes
alias: /report_builder/
page_type: reference
description: "Este artículo de referencia describe la característica Generador de informes."
tool:
    - Reports
page_order: 6.2
---

# Generador de informes

> Esta página explica cómo utilizar el Generador de informes para crear y ver informes granulares utilizando datos de Braze, y cómo añadir informes a los paneles.

## Utilizar una plantilla de informe

1. Ve a **Análisis** > **Generador de informes (Nuevo)**.
2. Selecciona la flecha **Más opciones** situada junto al botón **Crear informe nuevo** y, a continuación, selecciona **Utilizar una plantilla de informe**.<br><br>![Botón desplegable "Crear informe nuevo" con opciones para crear un informe personalizado o utilizar una plantilla.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecciona una de las plantillas de informe de la biblioteca de plantillas Braze.
    - Utiliza el desplegable **Elementos de fila** y **Etiquetas** para encontrar informes relevantes para tus casos de uso.<br><br>![Ventana "Plantillas de informes Braze" con una lista de plantillas Braze para seleccionar.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Sigue el paso 3 y siguientes de [Crear un informe](#creating-a-report) para personalizarlo aún más y adaptarlo a tu caso de uso.

## Crear un informe

1. Ve a **Análisis** > **Generador de informes (Nuevo)**.
2. Selecciona **Crear informe nuevo**.
3. En el desplegable **Filas**, selecciona sobre qué quieres informar:
    - Campañas
    - Canvas
    - Campañas y Canvas
    - Canales
    - Etiquetas

    Ten en cuenta que tu selección de **Filas** afectará a [las métricas que puedes ver](#metrics-availability). Por ejemplo, sólo puedes ver métricas multivariantes si informas sobre **Lienzos** o **Campañas** con un desglose de **Variantes**. No puedes ver esas métricas al informar sobre **campañas y lienzos**, aunque esas campañas y lienzos tengan pruebas multivariantes. 

![La sección "Filas y columnas" con campos para seleccionar las filas y agrupaciones de tu informe.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (Opcional) Selecciona **Añadir desglose** para desglosar tus datos en vistas más granulares:
    \- Canales
    \- Fecha
        \- Utilízalo para dividir tus datos en intervalos de tiempo más pequeños. Por ejemplo, si te interesa conocer el rendimiento de tus campañas por días, selecciona la siguiente configuración:
            - **Filas**: Campañas
            - **Agrupación:** Fecha
            - **Intervalo:** Días
    \- Variantes
    \- Campañas y Lonas

{% alert tip %}
Prueba distintas configuraciones de opciones de desglose para explorar las [muchas formas en que puedes desglosar tus datos](#metrics-availability).
{% endalert %}

{: start="5"}
5\. En la sección **Columnas**, selecciona **Personalizar métricas**.

![La sección "Personalizar métricas" con opciones para seleccionar múltiples métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. Busca métricas por categoría y selecciona la casilla correspondiente para añadir una métrica a tu informe.
    \- Reordena las métricas y columnas arrastrando el icono de puntos hacia arriba o hacia abajo.
7\. En **Contenido del informe**, configura el intervalo de fechas para el que quieres incluir datos en tu informe.
8\. A continuación, en función de lo que hayas seleccionado en el paso 3, elige añadir manual o automáticamente campañas, lienzos o ambos a tu informe.
    - **Añade manualmente:** Elige cada campaña o Canvas que quieras incluir en el informe utilizando los filtros de fechas de **Último envío** y etiquetas o canales, o buscando el nombre de la campaña o Canvas.<br><br>![La sección "Añadir manualmente campañas y lienzos" con una lista de campañas para seleccionar.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Añade automáticamente:** Establece las reglas sobre qué campañas o Lienzos incluir en el informe. Sólo tienes que seleccionar un campo en esta página.
        \- Ten en cuenta que, a medida que las campañas o Lienzos adicionales cumplan las condiciones que establezcas en esta pantalla, se añadirán automáticamente a futuras ejecuciones de tu informe.<br><br>![La sección "Añadir automáticamente campañas y lienzos" con campos para establecer reglas sobre qué campañas y lienzos deben añadirse al informe.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. Ejecuta el informe seleccionando **Guardar & Ejecutar**.

{% alert note %}
El informe puede tardar unos minutos en ejecutarse, dependiendo del intervalo de fechas y del número de campañas o Lienzos que hayas seleccionado en la fase de configuración.
{% endalert %}

## Disponibilidad métrica

Tu selección de **Filas** afecta a las métricas que puedes seleccionar.

{% alert tip %}
Si quieres informar sobre variantes o pasos en Canvas, selecciona **Lienzos** para las filas y deja el campo vacío o selecciona **Fecha** como desglose. Esto crea un desplegable de **la Vista del Canvas** para ver las métricas sólo del Canvas, o agrupar las métricas por variante, paso o mensaje. 

![El desplegable abierto "Vista del Canvas".]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrica | Descripción |
| --- | --- |
| Métricas de conversión | Disponible para Campañas, Lonas, Campañas y Lonas. |
| Entradas | Disponible para Campañas, Lienzos, Campañas y Lienzos, Etiquetas. |
| Última fecha de envío | Disponible para Campañas, Lonas, Campañas y Lonas. Sólo se muestra para campañas programadas; no se rellena para campañas basadas en acciones o desencadenadas por API. |
| Envíos | Disponible para cada canal relevante. |
| Mensajes enviados | Disponible para Campañas, Lienzos, Campañas y Lienzos, Etiquetas. |
| Línea del asunto | Disponible para Campañas por correo electrónico con desglose de **variantes**, Lienzos y Lienzos con desglose de **variantes**. |
| Ingresos totales | Disponible para Campañas, Lienzos, Campañas y Lienzos, Etiquetas. No disponible con el desglose **Canales**. |
| Impresiones únicas | Disponible para Campañas, Lienzos, Campañas y Lienzos, Etiquetas. |
| Destinatarios únicos | Disponible para Campañas, Lienzos, Campañas y Lienzos, Etiquetas. No disponible con el desglose **Canales**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Variantes de mensajes eliminados

Las estadísticas de las variantes de mensajes eliminados no se muestran cuando desglosas tu informe por campañas o Lienzos. Sin embargo, los totales a nivel de canal incluyen todas las estadísticas, independientemente de si se ha eliminado la variante. Por ejemplo, _los Envíos_ por correo electrónico incluyen todos los envíos por correo electrónico, pero si desglosas esas estadísticas por campañas, las cifras pueden ser inferiores porque se filtran los envíos de las variantes de mensajes eliminados.

## Ver un informe

Después de ejecutar tu informe, puedes ver los resultados en formato de tabla en la página del informe. 

![Una tabla con los datos del informe de las métricas de cada campaña.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Crear un gráfico de informe

En la parte inferior de la página puedes crear un gráfico de tus datos seleccionando un **Tipo de gráfico** y configurando las métricas del gráfico. Por defecto, verás la primera métrica.

![Un gráfico de los datos del informe con opciones para configurar el eje x del gráfico, el eje y, el tipo de gráfico, etc.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para crear un gráfico de líneas, selecciona **Fecha** como opción de desglose al configurar el informe. Esto mostrará las tendencias a lo largo del tiempo.
{% endalert %}

#### Descargar un gráfico de informe

Para descargar una imagen del gráfico del informe, selecciona el icono de puntos y elige una opción de descarga.

![Un menú con opciones de descarga para diferentes formatos de archivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartir un informe

Puedes compartir un enlace del panel al informe seleccionando **Compartir** y una de estas opciones:
- **Comparte un enlace:** Copia y comparte el enlace.

![desplegable "Compartir un enlace" con un enlace al informe.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Envía o programa un correo electrónico:** Envía un correo electrónico inmediatamente o a una hora determinada que contenga un enlace de descarga que caduque al cabo de una hora. Puedes seleccionar destinatarios de entre los usuarios del panel que aparecen en el desplegable **Destinatarios de correo electrónico** o introducir cualquier otra dirección de correo electrónico.

![Ventana "Programar un correo electrónico" con campos para elegir el formato del informe, quién debe recibirlo y cuándo debe enviarse.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Descargar CSV:** Descarga un CSV del informe.

## Añadir un informe a un panel de control

1. Selecciona el icono de puntos situado en la parte superior de la tabla de informes.
2. Selecciona **Añadir al panel**.
3. Selecciona si quieres crear un nuevo panel o añadirlo a uno ya existente.<br><br>![Ventana con opciones para seleccionar si quieres añadir el informe a un panel nuevo o existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Sigue los pasos [del Generador de paneles]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) para saber más sobre cómo crear un panel.

