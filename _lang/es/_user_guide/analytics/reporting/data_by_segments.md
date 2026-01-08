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

> Utiliza las plantillas de informes [del Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para desglosar las métricas de rendimiento de las campañas, Canvas, variantes y pasos por segmentos.

[El seguimiento de análisis]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) debe estar activado para los segmentos de los que quieras acceder a las métricas.

Para ejecutar estos informes, haz lo siguiente:
1. En **el Generador de consultas**, elige crear un informe nuevo SQL con una plantilla. 
2. Selecciona Desgloses de **segmento** para la métrica, que filtra las plantillas para aquellas en las que la métrica incluye desgloses de segmento, que son:
- Métricas de rendimiento del correo electrónico por segmento
- Métricas de interacción por correo electrónico para variantes o pasos, por segmento.
- Compras e ingresos por segmento
- Compras e ingresos por variantes o etapas, por segmento
- Rendimiento push por segmento

La página Desglose de segmentos contiene un editor SQL, un panel lateral con pestañas para Variables, Tablas de datos disponibles, Historial de consultas y el Generador de consultas AI, y una sección de resultados.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Plantillas de informes

{% tabs %}
{% tab Email engagement metrics by segment %}

### Ver métricas de campañas o Lienzos {#campaign-canvas-email}

Para ver las métricas de rendimiento del correo electrónico desglosadas por segmento a nivel de campaña o Canvas, utiliza la pestaña [Variables](#variables) para especificar las campañas o Canvases y un marco temporal para extraer los datos. Si no se especifican campañas o Canvases, el informe incluirá correos electrónicos de todas las campañas y Canvases del periodo de tiempo especificado. También puedes optar por ver todas las campañas y Lienzos con determinadas etiquetas.

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Envía
- Entregas
- Quejas
- Unique Opens
- Abre una máquina única
- Unique abre sin máquina
- Clics únicos
- Cancelar suscripción
- Rebotes
- Rebotes blandos
- Aplazado

#### Resultados

Tus resultados mostrarán las métricas de interacción del correo electrónico por segmento para las campañas o Canvases que hayas seleccionado. Si no seleccionaste campañas o Canvases específicos, tu informe mostrará las métricas de correo electrónico de cada segmento en todas las campañas de correo electrónico y Canvases dentro del periodo de tiempo de tu informe. 

- **Filas:** Segmentos
- **Columnas:** Métricas de interacción del correo electrónico

### Visualización de métricas de variantes o pasos

Para ver el rendimiento del correo electrónico desglosado por segmentos a nivel de variante de campaña, de variante en Canvas o de paso en Canvas, elige primero un informe a nivel de variante o de paso (son los informes que tienen "para variantes o pasos" en el título) y, a continuación, utiliza la pestaña **Variables** para especificar lo siguiente:

- Campaña o Canvas específico (necesario si se utiliza un informe de variantes o de pasos) 
- Variantes (obligatorio si utilizas un informe de variantes o de pasos)
- Paso en Canvas (opcional)

Las métricas son las mismas que las ofrecidas para la plantilla [a nivel de campaña o Canvas](#campaign-canvas-email). Si eliges varias variantes, tus resultados se agruparán por variantes.

#### Resultados

Tus resultados mostrarán las métricas de interacción del correo electrónico por segmento para las variantes o pasos que hayas seleccionado. 

- **Filas:** Segmentos
- **Columnas:** Métricas de interacción del correo electrónico

{% endtab %}

{% tab Purchases and revenue by segment %}
### Ver métricas de campañas o Lienzos

Para ver las métricas de compras e ingresos desglosadas por segmentos para una campaña o Canvas concretos, utiliza la pestaña [Variables](#variables) para especificar lo siguiente:

- Ventana de conversión (el número de días tras la recepción del correo electrónico o el clic al que Braze debe atribuir las compras o los ingresos)
- Producto específico (opcional) 

Además, utiliza la pestaña **Variables** para especificar si deseas ejecutar el informe para una o varias campañas o Lienzos, o para una o varias etiquetas. Si no se eligen campañas, Canvases o etiquetas, el informe se ejecutará para todos los correos electrónicos de campañas o Canvases durante el periodo de tiempo que hayas elegido.

Actualmente, este informe extrae métricas sólo del canal de correo electrónico. Los datos de ingresos o compras procedentes de canales distintos del correo electrónico no se reflejarán en el informe. 

Las siguientes métricas están disponibles para los correos electrónicos:

- Compras únicas al recibirlas
- Ingresos al cobro
- Compras únicas al hacer clic
- Ingresos por clic
- Destinatarios únicos
- Clics únicos en el correo electrónico

Todas las métricas de tasa utilizan destinatarios únicos de correo electrónico como denominador.

#### Definiciones

- "Tras la recepción" se refiere a eventos de compra o ingresos que se produjeron dentro de tu ventana de conversión especificada, después de que los usuarios recibieran las campañas o Lienzos especificados. 
- "Al hacer clic" se refiere a los eventos de compra o ingresos que se produjeron después de los eventos de compra, dentro de tu ventana de conversión especificada, después de que los usuarios hicieran clic en las campañas o Lienzos especificados.

Por ejemplo, supongamos que un segmento contiene 10 usuarios y cinco de ellos realizaron una compra tras recibir tu correo electrónico. Si uno de esos cinco hiciera una compra después de hacer clic en tu correo electrónico, tu "Tasa de compras únicas al recibirlo" sería del 50% y tu "Tasa de compras únicas al hacer clic" sería del 10%.

El informe muestra métricas de correo electrónico que incluyen compras únicas al recibir, ingresos al recibir, compras únicas al hacer clic, ingresos al hacer clic, destinatarios únicos y clics únicos en el correo electrónico.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Resultados

Tus resultados mostrarán métricas de compra por segmento para tus campañas o Lienzos seleccionados. Si no seleccionaste campañas o Canvases específicos, tu informe mostrará las métricas de compra de cada segmento en todas las campañas de correo electrónico o Canvases dentro del periodo de tiempo de tu informe. 

- **Filas:** Segmentos
- **Columnas:** Métricas de compra


### Visualización de métricas de variantes o pasos

Para ver las métricas de compras e ingresos desglosadas por segmentos para una variante de campaña, una variante en Canvas o un paso en Canvas concretos, utiliza la pestaña [Variables](#variables) para especificar lo siguiente:

- Campaña específica o Canvas
- Variantes 
- Paso en Canvas (opcional) 
- Rango temporal
- Producto específico (opcional) 

#### Resultados

Tus resultados mostrarán métricas de compra por segmento para las variantes o pasos que hayas seleccionado.

- **Filas:** Segmentos
- **Columnas:** Métricas de compra

{% endtab %}
{% tab Top or bottom messaging for email engagement %}

### Visualización de las métricas de los mejores o peores rendimientos

Este informe de la pestaña [Variables](#variables) muestra las campañas, los Canvases o los pasos en Canvas que obtuvieron el mayor o el menor rendimiento para una métrica de interacción por correo electrónico especificada. 

Los casos de uso incluyen: 
- 10 campañas con las tasas de apertura de correo electrónico únicas más altas
- 25 Lienzos con más cancelaciones de suscripción por correo electrónico
- 50 pasos en Canvas con los clics únicos más altos

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Envía
- Entregas
- Quejas
- Unique Opens
- Abre una máquina única
- Unique abre sin máquina
- Clics únicos
- Cancelar suscripción
- Rebotes
- Rebotes blandos
- Quejas

Para ver este informe, debes especificar las siguientes variables en la pestaña **Variables**:
- **Métrica:** Selecciona una de las métricas para clasificar tus resultados
- **Número de informes:** Selecciona los resultados superiores o inferiores y el número de resultados, como los 10 primeros o los 15 últimos
- **Tipo de mensaje:** Especifica si tus resultados son campañas, Lienzos o pasos en Canvas

#### Resultados

Tus resultados mostrarán las campañas, Lienzos o pasos en Canvas superiores (o inferiores) que hayas seleccionado. Por ejemplo, si seleccionaste las 10 mejores campañas por tasa de clics, tus resultados mostrarán las 10 mejores campañas ordenadas de mayor a menor tasa de clics. Tus columnas mostrarán todas las métricas de interacción por correo electrónico de cada fila (campañas, lienzos o pasos de mensajes).

{% endtab %}
{% tab Top or bottom messaging for purchases %}

### Visualización de las métricas de los mejores o peores rendimientos

Este informe, en la pestaña [Variables](#variables), muestra las campañas, los lienzos o los pasos en Canvas con mayor o menor rendimiento para una determinada métrica de compras o ingresos.

Los casos de uso incluyen:
- 20 campañas con las tasas de compra más altas para un producto específico
- 25 Lienzos con más ingresos generados
- 10 pasos en Canvas con la tasa más baja de compra de productos

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Compras únicas al recibirlas
- Ingresos al cobro
- Compras únicas al hacer clic
- Ingresos por clic
- Destinatarios únicos
- Clics únicos en el correo electrónico

Para ver este informe, debes especificar las siguientes variables en la pestaña **Variables**:
- **Métrica:** Selecciona una de las métricas para clasificar tus resultados
- **Número de informes:** Selecciona los resultados superiores o inferiores y el número de resultados, como los 10 primeros o los 15 últimos
- **Tipo de mensaje:** Especifica si tus resultados son campañas, Lienzos o pasos en Canvas
- **Ventana de conversión:** El número de días tras la recepción del correo electrónico o el clic al que Braze atribuirá las compras o los ingresos 

#### Definiciones

- "Tras la recepción" se refiere a eventos de compra o ingresos que se produjeron dentro de tu ventana de conversión especificada, después de que los usuarios recibieran las campañas o Lienzos especificados. 
- "Al hacer clic" se refiere a los eventos de compra o ingresos que se produjeron después de los eventos de compra, dentro de tu ventana de conversión especificada, después de que los usuarios hicieran clic en las campañas o Lienzos especificados.

Por ejemplo, supongamos que un segmento contiene 10 usuarios y cinco de ellos realizaron una compra tras recibir tu correo electrónico. Si uno de esos cinco hiciera una compra después de hacer clic en tu correo electrónico, tu tasa de "compras únicas al recibirlo" sería del 50% y tu tasa de "compras únicas al hacer clic" sería del 10%.

#### Resultados

Tus resultados mostrarán las campañas, Lienzos o pasos en Canvas superiores (o inferiores) que hayas seleccionado. Por ejemplo, si seleccionaste las 10 mejores campañas para "ingresos por clic", tus resultados mostrarán las 10 mejores campañas ordenadas de mayor a menor "ingresos por clic". Tus columnas mostrarán todas las métricas de compra de cada fila (campañas, lienzos o pasos de mensajes).

{% endtab %}
{% tab Push performance by segment %}

### Visualización de métricas push para segmentos

Este informe de la pestaña [Variables](#variables) muestra las métricas push desglosadas por segmentos. 

En la pestaña **Variables**, especifica las campañas o Lienzos para los que quieres ver las métricas y un intervalo de tiempo para extraer los datos. Si no seleccionas ninguna campaña o Canvases, el informe mostrará los push de todas las campañas y Canvases en el periodo de tiempo que hayas especificado. También puedes ver todas las campañas y Lienzos con determinadas etiquetas.

Las siguientes métricas push están disponibles en este informe:

- Envía
- Rebotes
- Entregas
- Direct Opens

#### Resultados

Tu informe mostrará los siguientes resultados:

- **Filas:** Segmentos
- **Columnas:** Métricas push
{% endtab %}
{% endtabs %}