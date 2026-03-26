---
nav_title: Casos de uso del comercio electrónico
article_title: Casos de uso del comercio electrónico
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artículo de referencia abarca varias plantillas prediseñadas de Braze adaptadas específicamente para los especialistas en marketing de comercio electrónico, lo que facilita la implementación de estrategias esenciales."
toc_headers: h2
---

# Cómo utilizar los eventos recomendados para el comercio electrónico

> Esta página explica cómo y dónde puedes utilizar los eventos recomendados para comercio electrónico en toda la plataforma, incluido cómo utilizar las plantillas de Braze eCommerce Canvas.

{% alert important %}
[Los eventos recomendados para el comercio electrónico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) se encuentran actualmente en fase de acceso anticipado. Si estás interesado en participar en este acceso anticipado, ponte en contacto con tu administrador del éxito del cliente de Braze. <br><br>Si utilizas el nuevo conector de Shopify, los eventos recomendados para el comercio electrónico estarán disponibles automáticamente a través de la integración.
{% endalert %}

## Uso de una plantilla de Canvas

Para utilizar una plantilla de Canvas:
1. Ve a **Mensajería** > **Canvas**.
2. Selecciona **Crear Canvas** > **Usar una plantilla de Canvas**.
3. Busca en la pestaña **Plantillas de Braze** la plantilla que deseas utilizar. Puedes obtener una vista previa de una plantilla seleccionando su nombre.
4. Selecciona **Aplicar plantilla** para la plantilla que deseas utilizar.<br><br>![La página «Plantillas de Canvas» se abre en la pestaña «Plantillas de Braze» y muestra una lista de las plantillas utilizadas recientemente y las plantillas de Braze seleccionables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Plantillas de Canvas para comercio electrónico

Braze ofrece cuatro plantillas de eCommerce Canvas.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalización de mensajes

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) es un potente lenguaje de plantillas utilizado por Braze que te permite crear contenido dinámico y personalizado para tus clientes. Mediante el uso de etiquetas de Liquid, puedes personalizar los mensajes en función de los datos de clientes, la información de los productos y otras variables, lo que mejora la experiencia de compra y fomenta la interacción.

### Características principales de Liquid

- **Contenido dinámico:** Inserta información personalizada del cliente, como nombres, detalles del pedido y preferencias, en tus mensajes.
- **Lógica condicional:** Utiliza sentencias if/else para mostrar contenido personalizado en función de condiciones específicas (como la ubicación del cliente y el historial de compras).
- **Bucles:** Repite las colecciones de productos o datos de clientes para mostrar listas o cuadrículas de artículos.

### Introducción a Liquid

Para empezar a personalizar tus mensajes utilizando etiquetas de Liquid, puedes consultar los siguientes recursos:

- Referencia [de datos de Shopify]({{site.baseurl}}/shopify_features/#shopify-data) con etiquetas de Liquid predefinidas
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentación

Utiliza los segmentos de Braze para crear segmentos de clientes específicos basados en atributos y comportamientos concretos, y entrega mensajes y campañas personalizados. Con esta potente característica, podrás atraer eficazmente a tus clientes llegando a la audiencia adecuada con el mensaje adecuado en el momento adecuado.

Para obtener más información sobre cómo empezar a utilizar los segmentos, consulta [Acerca de los segmentos de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Eventos recomendados

Los eventos de comercio electrónico se basan en [eventos recomendados]({{site.baseurl}}/recommended_events/).
Dado que los eventos recomendados son eventos personalizados más subjetivos, puedes buscar los nombres de los eventos de comercio electrónico recomendados seleccionando cualquier [filtro de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtros de comercio electrónico

Segmenta a tus usuarios con filtros de comercio electrónico, como **Fuente de comercio electrónico** e **Ingresos totales**, accediendo a la sección **Comercio electrónico** dentro del segmentador. 

Para obtener una lista de los filtros de comercio electrónico y sus definiciones, consulta [Filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) de [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) y selecciona la categoría de búsqueda «Comercio electrónico».

![Menú desplegable de filtros de segmento con filtros de «Comercio electrónico».]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propiedades de eventos anidados

Para segmentar por propiedades de eventos anidados, puedes aprovechar [las extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). Por ejemplo, puedes utilizar las extensiones de segmento para averiguar quién ha comprado el producto «SKU-123» en los últimos 90 días.

## Análisis

### Informe de eventos personalizados

Puedes realizar el seguimiento del volumen de eventos recomendados para el comercio electrónico en el [informe Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Filtra por **Realizar evento personalizado** y, a continuación, especifica el [nombre del evento recomendado por eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) para ver su rendimiento a lo largo del tiempo.

![Gráfico de eventos personalizados que muestra los resultados de seis eventos seleccionados.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Dashboards

#### Panel de conversiones

Después de lanzar una campaña o Canvas utilizando el evento de conversión «Realizar pedido», puedes crear un [informe de conversión]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#setting-up-your-report) correspondiente para realizar el seguimiento del rendimiento.

![Tabla de detalles de conversiones con campañas y lienzos, y las estadísticas de conversión asociadas.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### Panel de control de ingresos del comercio electrónico

Para obtener información sobre los ingresos atribuidos a la última campaña o Canvas con la que interactuó un usuario antes de realizar un pedido, utiliza el [panel de ingresos de comercio electrónico]({{site.baseurl}}/ecommerce_revenue_dashboard/) y selecciona una ventana de conversión.

### Informe de ingresos 

Para analizar los datos de estos nuevos eventos, ve al [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) y consulta el [panel de control **«Ingresos por comercio electrónico: atribución al último contacto**]({{site.baseurl}}/ecommerce_revenue_dashboard/)».
