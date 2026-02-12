---
nav_title: Casos de uso del comercio electrónico
article_title: Casos de uso del comercio electrónico
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artículo de referencia cubre varias plantillas Braze prediseñadas, adaptadas específicamente para especialistas en marketing de comercio electrónico, que facilitan la aplicación de estrategias esenciales."
toc_headers: h2
---

# Cómo utilizar los eventos recomendados por eCommerce

> Esta página cubre cómo y dónde puedes utilizar los eventos recomendados de eCommerce en toda la plataforma, incluyendo cómo utilizar las plantillas Braze eCommerce Canvas.

{% alert important %}
[Los eventos recomendados por eCommerce]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. <br><br>Si utilizas el nuevo conector de Shopify, los eventos recomendados de comercio electrónico estarán disponibles automáticamente a través de la integración.
{% endalert %}

## Utilizar una plantilla Canvas

Para utilizar una plantilla Canvas:
1. Ve a **Mensajería** > **Canvas**.
2. Selecciona **Crear lienzo** > **Utilizar una plantilla de lienzo**.
3. Busca en la pestaña **Plantillas Braze** la plantilla que quieras utilizar. Puedes obtener una vista previa de una plantilla seleccionando su nombre.
4. Selecciona **Aplicar plantilla** para la plantilla que quieras utilizar.<br><br>![La página "Plantillas Canvas" se abre en la pestaña "Plantillas Braze" y muestra una lista de las plantillas utilizadas recientemente y de las plantillas Braze seleccionables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Plantillas Canvas para comercio electrónico

Braze ofrece cuatro plantillas Canvas de comercio electrónico.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalización de mensajes

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) es un potente lenguaje de plantillas utilizado por Braze que te permite crear contenido dinámico y personalizado para tus clientes. Al utilizar las etiquetas de Liquid, puedes personalizar los mensajes en función de los datos de clientes, la información sobre productos y otras variables, mejorando la experiencia de compra e impulsando la interacción.

### Características principales de Liquid

- **Contenido dinámico:** Inserta en tus mensajes información específica del cliente, como nombres, detalles del pedido y preferencias.
- **Lógica condicional:** Utiliza sentencias if/else para mostrar contenidos diferentes en función de condiciones específicas (como la ubicación del cliente y su historial de compras).
- **Bucles:** Iterar sobre colecciones de productos o datos de clientes para mostrar listas o cuadrículas de elementos.

### Primeros pasos con Liquid

Para empezar a personalizar tus mensajes utilizando etiquetas de Liquid, puedes consultar los siguientes recursos:

- Referencia de [datos de Shopify]({{site.baseurl}}/shopify_features/#shopify-data) con etiquetas de Liquid predefinidas
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentación

Utiliza los segmentos Braze para crear segmentos de clientes específicos basados en atributos y comportamientos concretos, y entregar mensajes y campañas personalizados. Con esta potente característica, puedes interactuar eficazmente con tus clientes llegando a la audiencia adecuada con el mensaje correcto en el momento adecuado.

Para más información sobre cómo empezar con los segmentos, consulta [Acerca de los segmentos Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Eventos recomendados

Los eventos de comercio electrónico se basan en [eventos recomendados]({{site.baseurl}}/recommended_events/).
Dado que los eventos recomendados son eventos personalizados con más opiniones, puedes buscar los nombres de eventos de comercio electrónico recomendados seleccionando cualquier [filtro de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtros de comercio electrónico

Segmenta a tus usuarios con filtros de comercio electrónico, como **Fuente de comercio electrónico** e **Ingresos totales**, yendo a la sección **de comercio electrónico** dentro del segmentador. 

Para ver una lista de filtros de comercio electrónico y sus definiciones, consulta [Filtros de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) y selecciona la categoría de búsqueda "Comercio electrónico".

![Desplegable de filtros de segmento con filtros "Comercio electrónico".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propiedades de eventos anidados

Para segmentar por propiedades de eventos anidados, puedes aprovechar [las Extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). Por ejemplo, puedes utilizar las extensiones de segmento para encontrar quién ha comprado el producto "SKU-123" en los últimos 90 días.

## Análisis

### Informe de eventos personalizado

Puedes hacer un seguimiento del volumen de eventos recomendados de comercio electrónico en el [informe Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Filtra por **Realizar evento personalizado** y, a continuación, especifica el [nombre]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) del [evento recomendado por eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) para ver su rendimiento a lo largo del tiempo.

![Gráfico de Eventos personalizados que muestra los resultados de seis eventos seleccionados.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Informe de conversiones 

### Informe de eventos personalizado

Para crear un [informe de Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) basado en quién ha realizado un evento admitido a través de la integración, puedes especificar el [nombre]({{site.baseurl}}/shopify_data_features/) concreto del [evento]({{site.baseurl}}/shopify_data_features/).

### Dashboards

#### Panel de conversiones

Para obtener información sobre las tendencias relacionadas con los pedidos realizados desde tus Lienzos lanzados, configura un [panel de Conversiones]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) y especifica tus Lienzos.

#### Panel de ingresos de comercio electrónico

Para obtener información sobre los ingresos atribuidos a la última campaña o Canvas con el que interactuó un usuario antes de hacer un pedido, utiliza el [panel de ingresos de comercio electrónico]({{site.baseurl}}/ecommerce_revenue_dashboard/) y selecciona una ventana de conversión.

### Generador de consultas

### Informe de ingresos 

Para analizar los datos de estos nuevos eventos, ve al [Generador de paneles]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) y visualiza el [panel**Ingresos de comercio electrónico - Atribución del último toque**]({{site.baseurl}}/ecommerce_revenue_dashboard/).
