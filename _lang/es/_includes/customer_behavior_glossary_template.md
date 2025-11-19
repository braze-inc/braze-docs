---
nav_title: Comportamiento del cliente y eventos del usuario
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los distintos Eventos de comportamiento del cliente y del usuario que Braze puede rastrear y enviar a los Almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 7
---

Póngase en contacto con su representante de Braze o abra un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesita acceder a derechos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta nuestra [Biblioteca de Eventos de Interacción con Mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) o nuestros [ejemplos de datos de muestra Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación del comportamiento del cliente y de la estructura de eventos del usuario y valores de la plataforma %}

### Estructura del evento

Este desglose del comportamiento del cliente y de los eventos del usuario muestra qué tipo de información se incluye generalmente en un comportamiento del cliente o en un evento del usuario. Con una sólida comprensión de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos Currents entrantes para elaborar informes y gráficos basados en datos, y aprovechar otras valiosas métricas de datos.

![Desglose de un evento de usuario que muestra un evento de compra con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades específicas del comportamiento y propiedades específicas del dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

El comportamiento del cliente y los eventos del usuario se componen de propiedades **específicas del usuario**, propiedades **específicas del comportamiento** y propiedades **específicas del dispositivo**.

### Valores de la plataforma

Algunos eventos devuelven un valor `platform` que especifica la plataforma del dispositivo del usuario.
<br>La siguiente tabla detalla los posibles valores devueltos:

| Dispositivo de usuario | Valor de la plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de datos (como Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Algunas combinaciones de eventos y destinos que figuran en esta lista aún no están disponibles de forma general. Para saber qué actos cuentan con el apoyo de distintos socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y consulta sus respectivas páginas.<br><br>Además, ten en cuenta que Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900 KB.
{% endalert %}