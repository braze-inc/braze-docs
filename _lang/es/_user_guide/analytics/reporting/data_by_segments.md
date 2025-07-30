---
nav_title: Métricas por segmentos
article_title: Métricas por segmentos
page_order: 2.5
page_type: reference
description: "Esta página describe cómo puedes utilizar las plantillas de informes del Generador de consultas para desglosar las métricas de rendimiento de campañas, Canvas, variantes y pasos por segmentos."
tool: 
  - Segments
  - Reports
  
---

# Métricas por segmentos

> Utilice las plantillas de informes [del Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para desglosar las métricas de rendimiento de las campañas, Canvas, variantes y pasos por segmentos.

[El seguimiento de Analytics]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) debe estar activado para los segmentos para los que desea acceder a las métricas.

Para ejecutar estos informes, haga lo siguiente:
1. En **el Generador de consultas**, elige crear un informe nuevo SQL con una plantilla. 
2. Selecciona Desgloses de **segmento** para la métrica, que filtra las plantillas para aquellas en las que la métrica incluye desgloses de segmento, que son:
- Métricas de rendimiento del correo electrónico por segmento
- Métricas de compromiso del correo electrónico para variantes o pasos, por segmento
- Compras e ingresos por segmento
- Compras e ingresos por variantes o pasos, por segmento
- Rendimiento de notificaciones push por segmento

![La página de desglose de segmentos contiene un editor SQL, un panel lateral con pestañas para Variables, Tablas de datos disponibles, Historial de consultas y el Generador de consultas AI, y una sección de resultados.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Plantillas de informes

{% tabs %}
{% tab Métricas de compromiso del correo electrónico por segmento %}

### Visualización de las métricas de las campañas o los lienzos {#campaign-canvas-email}

Para ver las métricas de rendimiento del correo electrónico desglosadas por segmento a nivel de campaña o de lienzo, utilice la pestaña [Variables](#variables) para especificar las campañas o los lienzos y un intervalo de tiempo para extraer los datos. Si no se especifica ninguna campaña o lienzo, el informe incluirá los correos electrónicos de todas las campañas y lienzos del periodo especificado. También puede optar por ver todas las campañas y lienzos con determinadas etiquetas.

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Envíos
- Entregas
- Quejas
- Unique Opens
- Machine Opens de máquina
- Machine Opens no de máquina
- Clics únicos
- Cancelaciones de suscripción
- Rebotes
- Rebotes suaves
- Aplazado

#### Resultados

Los resultados mostrarán las métricas de interacción por correo electrónico por segmento para las campañas o lienzos que haya seleccionado. Si no seleccionó campañas o Canvases específicos, su informe mostrará las métricas de correo electrónico para cada segmento a través de todas las campañas de correo electrónico y Canvases dentro del marco de tiempo de su informe. 

- **Filas:** Segmentos
- **Columnas:** Métricas de participación por correo electrónico

### Visualización de métricas para variantes o pasos

Para ver el rendimiento del correo electrónico desglosado por segmento a nivel de variante de campaña, variante de Canvas o paso de Canvas, elija primero un informe a nivel de variante o paso (son informes que tienen "para variantes o pasos" en el título) y, a continuación, utilice la pestaña **Variables** para especificar lo siguiente:

- Campaña específica o Canvas (necesario si se utiliza un informe a nivel de variante o paso) 
- Variantes (obligatorio si se utiliza un informe a nivel de variante o de paso)
- Paso del lienzo (opcional)

Las métricas son las mismas que las ofrecidas para la plantilla [a nivel de campaña o Canvas](#campaign-canvas-email). Si elige varias variantes, los resultados se agruparán por variante.

#### Resultados

Los resultados mostrarán las métricas de participación del correo electrónico por segmento para las variantes o pasos seleccionados. 

- **Filas:** Segmentos
- **Columnas:** Métricas de participación por correo electrónico

{% endtab %}

{% tab Compras e ingresos por segmento %}
### Visualización de las métricas de las campañas o los lienzos

Para ver las métricas de compra e ingresos desglosadas por segmento para una campaña o Canvas específicos, utilice la pestaña [Variables](#variables) para especificar lo siguiente:

- Ventana de conversión (el número de días tras la recepción del correo electrónico o el clic al que Braze debe atribuir las compras o los ingresos)
- Producto específico (opcional) 

Además, utilice la pestaña **Variables** para especificar si desea ejecutar el informe para una o varias campañas o lienzos, o una o varias etiquetas. Si no se seleccionan campañas, lienzos o etiquetas, el informe se ejecutará para todos los correos electrónicos de campañas o lienzos durante el periodo de tiempo seleccionado.

Actualmente, este informe extrae métricas únicamente del canal de correo electrónico. Los datos de ingresos o compras procedentes de canales distintos del correo electrónico no se reflejarán en el informe. 

Las siguientes métricas están disponibles para los correos electrónicos:

- Compras únicas en el momento de la recepción
- Ingresos en el momento de la recepción
- Compras únicas al hacer clic
- Ingresos al hacer clic
- Destinatarios únicos
- Clics únicos por correo electrónico

Todas las métricas de tasa utilizan destinatarios únicos de correo electrónico como denominador.

#### Definiciones

- "Tras la recepción" se refiere a los eventos de compra o ingresos que se produjeron dentro de la ventana de conversión especificada, después de que los usuarios recibieran las campañas o los lienzos especificados. 
- "Al hacer clic" se refiere a los eventos de compra o ingresos que se produjeron después de los eventos de compra, dentro de su ventana de conversión especificada, después de que los usuarios hicieran clic en las campañas o lienzos especificados.

Por ejemplo, supongamos que un segmento contiene 10 usuarios y cinco de ellos realizaron una compra después de recibir su correo electrónico. Si uno de esos cinco hiciera una compra después de hacer clic en tu correo electrónico, tu "Tasa de compras únicas al recibirlo" sería del 50% y tu "Tasa de compras únicas al hacer clic" sería del 10%.

![El informe muestra las métricas de correo electrónico, incluidas las compras únicas al recibir, los ingresos al recibir, las compras únicas al hacer clic, los ingresos al hacer clic, los destinatarios únicos y los clics únicos en el correo electrónico.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Resultados

Sus resultados mostrarán las métricas de compra por segmento para sus campañas o Lienzos seleccionados. Si no ha seleccionado campañas o lienzos específicos, el informe mostrará las métricas de compra de cada segmento en todas las campañas de correo electrónico o lienzos dentro del periodo de tiempo del informe. 

- **Filas:** Segmentos
- **Columnas:** Métricas de compra


### Visualización de métricas para variantes o pasos

Para ver las métricas de compra e ingresos desglosadas por segmento para una variante de campaña, variante de Canvas o paso de Canvas específicos, utilice la pestaña [Variables](#variables) para especificar lo siguiente:

- Campaña específica o lienzo
- Variantes 
- Paso del lienzo (opcional) 
- Intervalo de fechas
- Producto específico (opcional) 

#### Resultados

Sus resultados mostrarán las métricas de compra por segmento para las variantes o pasos que haya seleccionado.

- **Filas:** Segmentos
- **Columnas:** Métricas de compra

{% endtab %}
{% tab Mensajería superior o inferior para la interacción por correo electrónico %}

### Visualización de las métricas de los mejores o peores resultados

Este informe de la pestaña [Variables](#variables) muestra las campañas, los lienzos o los pasos del lienzo que han obtenido los mejores o peores resultados en una métrica específica de interacción por correo electrónico. 

Los casos de uso incluyen: 
- 10 campañas con las tasas de apertura de correo electrónico únicas más altas
- 25 Canvas con más cancelaciones de suscripción por correo electrónico
- 50 Pasos del lienzo con más clics únicos

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Envíos
- Entregas
- Quejas
- Unique Opens
- Machine Opens de máquina
- Machine Opens no de máquina
- Clics únicos
- Cancelaciones de suscripción
- Rebotes
- Rebotes suaves
- Quejas

Para ver este informe, debe especificar las siguientes variables en la pestaña **Variables**:
- **Métricas:** Seleccione una de las métricas para clasificar sus resultados
- **Número de informes:** Seleccione los resultados superiores o inferiores y el número de resultados, como los 10 primeros o los 15 últimos
- **Tipo de mensaje:** Especifique si sus resultados son campañas, lienzos o pasos de lienzo

#### Resultados

Los resultados mostrarán las campañas, los lienzos o los pasos del lienzo que haya seleccionado. Por ejemplo, si ha seleccionado las 10 mejores campañas por porcentaje de clics, los resultados mostrarán las 10 mejores campañas ordenadas de mayor a menor porcentaje de clics. Sus columnas mostrarán todas las métricas de participación de correo electrónico para cada fila (campañas, lienzos o pasos de mensajes).

{% endtab %}
{% tab Mensajería superior o inferior para las compras %}

### Visualización de las métricas de los mejores o peores resultados

Este informe de la pestaña [Variables](#variables) muestra las campañas, los lienzos o los pasos de lienzo con mayor o menor rendimiento para una métrica específica de compra o ingresos.

Los casos de uso incluyen:
- 20 campañas con los mayores índices de compra de un producto específico
- 25 Lonas con más ingresos generados
- 10 Pasos del lienzo con el menor índice de compra de productos

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Compras únicas en el momento de la recepción
- Ingresos en el momento de la recepción
- Compras únicas al hacer clic
- Ingresos al hacer clic
- Destinatarios únicos
- Clics únicos por correo electrónico

Para ver este informe, debe especificar las siguientes variables en la pestaña **Variables**:
- **Métricas:** Seleccione una de las métricas para clasificar sus resultados
- **Número de informes:** Seleccione los resultados superiores o inferiores y el número de resultados, como los 10 primeros o los 15 últimos
- **Tipo de mensaje:** Especifique si sus resultados son campañas, lienzos o pasos de lienzo
- **Ventana de conversión:** El número de días tras la recepción del correo electrónico o el clic al que Braze atribuirá compras o ingresos 

#### Definiciones

- "Tras la recepción" se refiere a los eventos de compra o ingresos que se produjeron dentro de la ventana de conversión especificada, después de que los usuarios recibieran las campañas o los lienzos especificados. 
- "Al hacer clic" se refiere a los eventos de compra o ingresos que se produjeron después de los eventos de compra, dentro de su ventana de conversión especificada, después de que los usuarios hicieran clic en las campañas o lienzos especificados.

Por ejemplo, supongamos que un segmento contiene 10 usuarios y cinco de ellos realizaron una compra después de recibir su correo electrónico. Si uno de esos cinco hace una compra después de hacer clic en su correo electrónico, su tasa de "compras únicas al recibirlo" sería del 50% y su tasa de "compras únicas al hacer clic" sería del 10%.

#### Resultados

Los resultados mostrarán las campañas, los lienzos o los pasos del lienzo que haya seleccionado. Por ejemplo, si ha seleccionado las 10 campañas principales para "ingresos por clic", los resultados mostrarán las 10 campañas principales ordenadas de mayor a menor "ingresos por clic". Sus columnas mostrarán todas las métricas de compra para cada fila (campañas, Canvases o pasos de Mensaje).

{% endtab %}
{% tab Rendimiento push por segmento %}

### Visualización de las métricas push de los segmentos

Este informe de la pestaña [Variables](#variables) muestra las métricas push desglosadas por segmentos. 

En la pestaña **Variables**, especifique las campañas o lienzos para los que desea ver las métricas y un periodo de tiempo para extraer los datos. Si no selecciona ninguna campaña o lienzo, el informe mostrará los envíos de todas las campañas y lienzos en el periodo especificado. También puede ver todas las campañas y lienzos con determinadas etiquetas.

Las siguientes métricas push están disponibles en este informe:

- Envíos
- Rebotes
- Entregas
- Apertura directa

#### Resultados

Su informe mostrará los siguientes resultados:

- **Filas:** Segmentos
- **Columnas:** Métricas push
{% endtab %}
{% endtabs %}