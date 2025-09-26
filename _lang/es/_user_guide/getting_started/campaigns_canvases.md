---
nav_title: Campañas y Canvas
article_title: "Cómo empezar: Campañas y Canvas"
page_order: 3
page_type: reference
description: "Este artículo ofrece un resumen de las distintas formas en que puedes enviar mensajes con Braze."

---

# Cómo empezar: Campañas y Canvas

En Braze, puedes enviar mensajes a través de una [campaña](#campaigns) o de un [Canvas](#canvas-flow).

- Para enviar un único mensaje dirigido a un grupo de usuarios, elija una campaña. Una campaña es un paso de mensaje único para conectar con sus usuarios en varios canales de mensajería.
- Para enviar una serie de mensajes continuos en un recorrido global del cliente, elija Canvas Flow. Canvas Flow es nuestra herramienta de orquestación de recorridos. Mientras que las campañas son buenas para enviar mensajes sencillos y específicos, en los lienzos es donde puede llevar sus relaciones con los clientes al siguiente nivel.

## Campañas

Aunque las campañas pueden construirse de forma única dependiendo del canal, hay cuatro tipos principales de campañas en Braze que debe conocer:

| Tipo de campaña        | Descripción                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular              | Es el tipo de campaña más común. Puede dirigirse a uno o varios canales en función de sus objetivos de mensajería, y diseñar, personalizar y probar su contenido directamente en Braze con nuestros editores visuales. Aprende a [crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign). |
| Pruebas A/B          | En el caso de las campañas dirigidas a un único canal, puede enviar más de una versión de la misma campaña y ver cuál sale ganadora. Con una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) puede probar el texto, la personalización, etc. para un máximo de ocho versiones diferentes. |
| API                  | [Las campañas API]({{site.baseurl}}/api/api_campaigns/) te permiten enviar mensajes puntuales lo más rápidamente posible. A diferencia de otros tipos de campaña, en el panel Braze no se especifica el mensaje, los destinatarios ni el calendario. En su lugar, debe pasar estos identificadores a sus llamadas a la API. Suelen utilizarse para mensajes transaccionales en tiempo real o noticias de última hora.  |
| Correos electrónicos transaccionales | [Los correos electrónicos transaccionales]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) Braze están diseñados para enviar mensajes de correo electrónico automatizados y no promocionales con el fin de facilitar una transacción acordada entre usted y sus clientes. Envían notificaciones críticas para la empresa a un único usuario en las que la velocidad es lo más importante. *Disponible para determinados paquetes.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Las campañas regulares y de prueba A/B pueden programarse (como informar a una lista de usuarios sobre un próximo evento) o automatizarse para que se envíen en respuesta a una acción del usuario (como enviar un correo electrónico cuando alguien se suscribe a su boletín). Más información sobre [la programación de campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types).
{% endalert %}

Independientemente del tipo de campaña que cree, sus campañas pueden escuchar las necesidades de sus usuarios y ofrecer una respuesta pensada y personalizada. Una vez que haya enviado su campaña, utilice nuestras [herramientas de análisis integradas]({{site.baseurl}}/user_guide/analytics/reporting/) para ver cómo ha funcionado y cuántos usuarios se han convertido en función de sus [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Consulta estos recursos adicionales para saber más sobre las campañas en Braze:

- Braze Learning: [Configuración de la campaña](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [Ideas y estrategias]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## Canvas Flow

En lugar de enviar mensajes esporádicos a lo largo de varias campañas, Canvases crea una conversación fluida y continua con los usuarios. Esto se debe a que el recorrido de un usuario a través de un Canvas puede dividirse en diferentes caminos en función de sus acciones (o inacción) con su marca, lo que le permite hacer avanzar automáticamente a los usuarios a través de un flujo específico en tiempo real.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

De este modo, los lienzos son ideales para lanzar una red y captar a los usuarios que se quedan fuera del camino hacia la conversión y colocarlos en las iniciativas de difusión más eficaces.

Cuando se crea un Canvas, se siguen muchos de los mismos pasos que para configurar una campaña: especificar un público general, las condiciones de entrada y la configuración de envío. Tu Canvas comienza cuando alguien coincide con tu condición de activación. A continuación, se mueven a través de un camino en el lienzo hasta que cumplan sus condiciones de salida.

Tu lienzo puede tener cualquier combinación de [mensajes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), [retrasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), [experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/), etc. Puede enviar en cualquier canal de mensajería compatible, e incluso [integrarse con plataformas sociales y publicitarias]({{site.baseurl}}/partners/canvas_audience_sync/overview/) como Facebook, Google o TikTok.

Consulte estos recursos adicionales para obtener más información sobre Canvas Flow:

- Braze Learning: [Orquestación de recorridos con Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [Contornos de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## Canales de mensajería

Los canales de mensajería son los distintos canales de comunicación a través de los cuales puede interactuar con sus clientes y transmitir mensajes específicos. 

![]({% image_buster /assets/img/getting_started/channels.png %})

En la tabla siguiente se describen los canales que admitimos.

| Canal                                                                                              | Descripción                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | Envíe correos electrónicos personalizados a las bandejas de entrada de sus usuarios.                                                                                                       |
| [Notificaciones push móvil]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | Envíe mensajes directamente a los dispositivos móviles de los usuarios en forma de notificaciones.                                                                                   |
| [Web push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Envíe notificaciones a los navegadores de los usuarios, incluso cuando no estén activos en su sitio web.                                                         |
| [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | Muestre mensajes dentro de su aplicación móvil mientras los usuarios la utilizan activamente.                                                                             |
| [SMS, MMS y RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/).                   | Enviar mensajes de texto a los teléfonos móviles de los usuarios.                                                                                                            |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)              | Envía mensajes a través de la popular plataforma de mensajería, WhatsApp, para llegar a tus usuarios e interactuar con ellos.                                                   |
| [Pancartas]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)       | Incrusta mensajes directamente en tu aplicación o sitio web. |
| [Tarjetas de contenido*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)       | Proporcione una bandeja de entrada dentro de su aplicación o sitio web donde los usuarios puedan recibir mensajes e interactuar con ellos, o muestre los mensajes en un carrusel, como un banner, etc. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Interactúe con los usuarios en plataformas de televisión conectadas.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Habilite la comunicación en tiempo real y la integración con sistemas externos mediante retrollamadas HTTP personalizadas.                                                    |
| [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | Relaciónate con los usuarios de LINE, la aplicación de mensajería más popular de Japón.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponible como característica adicional\*.</sup>

{% alert tip %}
Para mensajes cortos y urgentes que pueden comunicarse a través de la mayoría de los canales (correo electrónico, SMS, push), aproveche el filtro de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) para enviar automáticamente el mensaje a través del mejor canal para cada usuario.
{% endalert %}

