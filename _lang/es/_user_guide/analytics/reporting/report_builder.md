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
2. Selecciona la flecha **Más opciones** situada junto al botón **Crear informe nuevo** y, a continuación, selecciona **Utilizar una plantilla de informe**.<br><br><br><br>
3. Selecciona una de las plantillas de informe de la biblioteca de plantillas Braze.
    - Utiliza el desplegable **Elementos de fila** y **Etiquetas** para encontrar informes relevantes para tus casos de uso.<br><br><br><br>
4. Sigue el paso 3 y siguientes en [Crear un informe](#creating-a-report) para personalizar aún más el informe y adaptarlo a tu caso de uso.

## Crear un informe

1. Ve a **Análisis** > **Generador de informes (Nuevo)**.
2. Selecciona **Crear informe nuevo**.
3. En el desplegable **Filas**, selecciona una de las siguientes opciones para crear un informe:
    - Campañas
    - Canvas
    - Campañas y Canvas
    - Canales
    - Etiquetas



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

{% endalert %}

{: start="5"}
5\. En la sección **Columnas**, selecciona **Personalizar métricas**.



{: start="6"}
6\. Busca métricas por categoría y selecciona la casilla correspondiente para añadir una métrica a tu informe.
    \- Reordena las métricas y columnas arrastrando el icono de puntos hacia arriba o hacia abajo.
7\. En **Contenido del informe**, configura el intervalo de fechas para el que quieres incluir datos en tu informe.
8\. A continuación, en función de lo que hayas seleccionado en el paso 3, elige añadir manual o automáticamente campañas, lienzos o ambos a tu informe.
    - **Añade manualmente:** Elige cada campaña o Canvas que quieras incluir en el informe utilizando los filtros de fechas de **Último envío** y etiquetas o canales, o buscando el nombre de la campaña o Canvas.<br><br><br><br>
    - **Añade automáticamente:** Establece las reglas sobre qué campañas o Lienzos incluir en el informe. Sólo tienes que seleccionar un campo en esta página.
        \- Ten en cuenta que, a medida que las campañas o Lienzos adicionales cumplan las condiciones que establezcas en esta pantalla, se añadirán automáticamente a futuras ejecuciones de tu informe.<br><br><br><br>
9\. Ejecuta el informe seleccionando **Guardar y Ejecutar**.

{% alert note %}
El informe puede tardar unos minutos en ejecutarse, dependiendo del intervalo de fechas y del número de campañas o Lienzos que hayas seleccionado en la fase de configuración.
{% endalert %}

## 



|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |   |
|  |  |
|  |   |


## Ver un informe

Después de ejecutar tu informe, puedes ver los resultados en formato de tabla en la página del informe. 



### Crear un gráfico de informe

En la parte inferior de la página puedes crear un gráfico de tus datos seleccionando un **Tipo de gráfico** y configurando las métricas del gráfico. Por defecto, verás la primera métrica.



{% alert note %}
Para crear un gráfico de líneas, selecciona **Fecha** como opción de desglose al configurar el informe. Esto mostrará las tendencias a lo largo del tiempo.
{% endalert %}

#### Descargar un gráfico de informe

Para descargar una imagen del gráfico del informe, selecciona el icono de puntos y elige una opción de descarga.



## Añadir un informe a un panel de control

1. Selecciona el icono de puntos situado en la parte superior de la tabla de informes.
2. Selecciona **Añadir al panel**.
3. Selecciona si quieres crear un nuevo panel o añadirlo a uno ya existente.<br><br><br><br>
4. Sigue los pasos [del Generador de paneles]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) para saber más sobre cómo crear un panel.

