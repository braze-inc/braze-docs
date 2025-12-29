---
nav_title: Campañas y Lonas
article_title: "Cómo empezar: Campañas y Lonas"
page_order: 3
page_type: reference
description: "Este artículo ofrece un resumen de las distintas formas en que puedes enviar mensajes con Braze."

---

# Cómo empezar: Campañas y Lonas

En Braze, puedes enviar mensajes a través de una [campaña](#campaigns) o de un [Canvas](#canvas).

- Para enviar un único mensaje dirigido a un grupo de usuarios, elige una campaña. Una campaña es un paso de mensaje único para conectar con tus usuarios en varios canales de mensajería.
- Para enviar una serie de mensajes continuos en un recorrido del cliente global, elige Canvas, nuestra herramienta de orquestación de recorridos. Mientras que las campañas son buenas para enviar mensajes sencillos y específicos, en los Lienzos es donde llevas tus relaciones con los clientes al siguiente nivel.

## Campañas

Aunque las campañas pueden construirse de forma única dependiendo del canal, hay cuatro tipos principales de campañas en Braze que debes conocer:

| Tipo de campaña        | Descripción                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular              | Es el tipo de campaña más habitual. Puedes dirigirte a uno o varios canales en función de tus objetivos de mensajería, y diseñar, personalizar y probar tu contenido directamente en Braze con nuestros editores visuales. Aprende a [crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign). |
| Pruebas A/B          | Para las campañas dirigidas a un solo canal, puedes enviar más de una versión de la misma campaña y ver cuál sale ganadora. Con una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) puedes probar el texto, la personalización y mucho más para hasta ocho versiones diferentes. |
| API                  | [Las campañas API]({{site.baseurl}}/api/api_campaigns/) te permiten enviar mensajes puntuales lo más rápidamente posible. A diferencia de otros tipos de campaña, en el panel Braze no se especifica el mensaje, los destinatarios ni la programación. En su lugar, pasa estos identificadores a tus llamadas a la API. Suelen utilizarse para mensajería transaccional en tiempo real o noticias de última hora.  |
| Correos electrónicos transaccionales | [Los correos electrónicos transaccionales]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) Braze están diseñados para enviar mensajes de correo electrónico automatizados y no promocionales que faciliten una transacción acordada entre tú y tus clientes. Envían notificaciones críticas para la empresa a un único usuario, donde la rapidez es de suma importancia. *Disponible para paquetes seleccionados.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Las campañas regulares y de pruebas A/B pueden programarse (como informar a una lista de usuarios sobre un próximo evento) o automatizarse para que se envíen en respuesta a la acción de un usuario (como enviar un correo electrónico cuando alguien se suscribe a tu boletín). Más información sobre [la programación de campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types).
{% endalert %}

Independientemente del tipo de campaña que crees, tus campañas pueden escuchar las necesidades de tus usuarios y entregar una respuesta atenta y personalizada. Después de enviar tu campaña, utiliza nuestras [herramientas de análisis integradas]({{site.baseurl}}/user_guide/analytics/reporting/) para ver su rendimiento y el número de usuarios que han convertido en función de tus [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Consulta estos recursos adicionales para saber más sobre las campañas en Braze:

- Braze Learning: [Configuración de la campaña](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Crea una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [Ideas y estrategias]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## Canvas

En lugar de enviar mensajes esporádicos a lo largo de varias campañas, los Lienzos crean una conversación fluida y continua con los usuarios. Esto se debe a que el recorrido de un usuario a través de un Canvas puede dividirse en diferentes rutas en función de sus acciones (o inacción) con tu marca, lo que te permite hacer avanzar automáticamente a los usuarios a través de un flujo específico en tiempo real.

\![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

De este modo, los Lienzos son estupendos para lanzar una red y captar a los usuarios que se salen del camino hacia la conversión y colocarlos en las iniciativas de divulgación más eficaces.

Cuando creas un Canvas, sigues muchos de los mismos pasos que cuando configuras una campaña: especificar una audiencia general, las condiciones de entrada y la configuración de envío. Tu Canvas se inicia cuando alguien coincide con tu condición desencadenante. Luego se mueven por un camino en el Canvas hasta que cumplen tus condiciones de salida.

Tu Canvas puede tener cualquier combinación de [mensajes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), [retrasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), [experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) y mucho más. Puedes enviar a través de cualquier canal de mensajería compatible, e incluso [integrarlo con plataformas sociales y publicitarias]({{site.baseurl}}/partners/canvas_audience_sync/overview/) como Facebook, Google o TikTok.

Consulta estos recursos adicionales para saber más sobre Canvas:

- Braze Learning: [Orquestación de viajes con Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Crea un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [Contornos de lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## Canales de mensajería

Los canales de mensajería son los distintos canales de comunicación a través de los cuales puedes interactuar con tus clientes y entregar mensajes específicos. 

\![]({% image_buster /assets/img/getting_started/channels.png %})

En la tabla siguiente se describen los canales que admitimos.

| Canal                                                                                              | Descripción                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | Envía correos electrónicos personalizados a los buzones de entrada de tus usuarios.                                                                                                       |
| [Push móvil]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | Entrega mensajes directamente a los dispositivos móviles de los usuarios como notificaciones.                                                                                   |
| [Web push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Entrega notificaciones a los navegadores web de los usuarios, incluso cuando no estén activamente en tu sitio web.                                                         |
| [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | Muestra mensajes dentro de tu aplicación móvil mientras los usuarios la utilizan activamente.                                                                             |
| [SMS, MMS y RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/).                   | Envía mensajes de texto a los teléfonos móviles de los usuarios.                                                                                                            |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)              | Envía mensajes a través de la popular plataforma de mensajería, WhatsApp, para llegar a tus usuarios e interactuar con ellos.                                                   |
| [Pancartas]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)       | Incrusta mensajes directamente en tu aplicación o sitio web. |
| [Tarjetas de contenido*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)       | Proporciona un buzón de entrada dentro de tu aplicación o sitio web donde los usuarios puedan recibir mensajes e interactuar con ellos, o muestra mensajes en un carrusel, como un banner, etc. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Interactúa con los usuarios en plataformas de televisión conectadas.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Habilita la comunicación en tiempo real y la integración con sistemas externos mediante devoluciones de llamada HTTP personalizadas.                                                    |
| [LÍNEA]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | Relaciónate con los usuarios de LINE, la aplicación de mensajería más popular de Japón.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponible como característica adicional\*.</sup>

{% alert tip %}
Para mensajes cortos y urgentes que pueden comunicarse a través de la mayoría de canales (correo electrónico, SMS, push), aprovecha el filtro de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) para enviar automáticamente el mensaje a través del mejor canal para cada usuario.
{% endalert %}

