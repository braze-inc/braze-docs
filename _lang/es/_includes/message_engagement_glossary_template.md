---
nav_title: Eventos de participación en mensajes
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los distintos eventos de compromiso de mensajes que Braze puede rastrear y enviar a los almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 6
---

Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de almacén de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Para los esquemas que se aplican a los demás socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y comprueba sus respectivas páginas.

Póngase en contacto con su gestor de cuenta o abra un [ticket de asistencia]({{site.baseurl}}/braze_support/) si necesita acceder a derechos de eventos adicionales. Si no encuentra lo que necesita en este artículo, consulte nuestra [Biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) o nuestros [ejemplos de datos de muestra Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación de la estructura de los eventos de compromiso de mensajes y de los valores de la plataforma %}

### Estructura del evento

Este desglose de eventos muestra qué tipo de información se incluye generalmente en un evento de compromiso de mensajes. Con una sólida comprensión de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos Currents entrantes para elaborar informes y gráficos basados en datos, y aprovechar otras valiosas métricas de datos.

![Desglose de un evento de compromiso de mensaje que muestra un evento de cancelación de suscripción de correo electrónico con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades de seguimiento de campaña o Canvas y propiedades específicas del evento]({% image_buster /assets/img/message_engagement_event.png %})

Los eventos de participación en mensajes se componen de propiedades **específicas de usuario**, propiedades de **seguimiento de campaña/tela** y propiedades **específicas de evento**.

### Esquema de ID de usuario

Nota las convenciones de nomenclatura para los ID de usuario.

| Esquema Braze | Esquema Currents | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que asigna automáticamente Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario configurado por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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
Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900 KB.
{% endalert %}

{% alert note %}
Los objetos relacionados con el Flujo del Canvas tienen ID que pueden utilizarse para agruparlos y traducirse a nombres legibles por humanos mediante el [punto final Exportar detalles del Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Algunos campos pueden tardar más en mostrar su estado más reciente después de actualizar una campaña o Canvas. Estos campos son:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Si se requiere una coherencia total, te recomendamos que esperes una hora desde la última actualización de estos campos antes de enviar la mensajería a tus usuarios.
{% endalert %}