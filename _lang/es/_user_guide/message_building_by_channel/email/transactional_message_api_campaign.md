---
nav_title: Campañas de correo electrónico transaccionales
article_title: Campañas de correo electrónico transaccional
page_order: 10

description: "Este artículo de referencia explica cómo crear y configurar una nueva campaña de correo electrónico transaccional de Braze."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Campañas de correo electrónico transaccional

> Los correos electrónicos transaccionales de Braze se envían para facilitar una transacción acordada entre un remitente y el destinatario. Este artículo de referencia explica cómo crear una campaña de correo electrónico transaccional en el dashboard de Braze y generar un `campaign_id` para incluirlo en tus llamadas a la API para nuestro [punto de conexión `/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
El correo electrónico transaccional de Braze solo está disponible como parte de determinados paquetes de Braze. Ponte en contacto con tu administrador del éxito del cliente de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) para obtener más detalles.
{% endalert %}

El tipo de campaña de correo electrónico transaccional está diseñado específicamente para enviar mensajes de correo electrónico automatizados y no promocionales con el fin de facilitar una transacción acordada entre tú y tus clientes. Esto incluye información como:

- Confirmaciones de pedido
- Restablecimiento de contraseña
- Alertas de facturación
- Alertas de envío

En resumen, puedes utilizar los correos electrónicos transaccionales para enviar notificaciones críticas para la empresa originadas en tu servicio para un único usuario en las que la velocidad es de suma importancia. 

{% alert important %}
Los correos electrónicos transaccionales difieren de las campañas transaccionales, que pueden utilizarse para dirigirse a tus usuarios sin costes adicionales. Las campañas transaccionales, por ejemplo, pueden incluir mensajes enviados después de que un usuario añada un artículo a su cesta. Consulta las [opciones de segmentación de audiencia]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) para obtener más información.
{% endalert %}

{% alert note %}
Los envíos de la API de correo electrónico transaccional son compatibles con el archivado de mensajes. Si el archivado de mensajes está habilitado para correo electrónico en tu espacio de trabajo, Braze guarda una copia renderizada de cada envío de correo electrónico transaccional. Para más información, consulta [Archivado de mensajes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving/).
{% endalert %}

## Paso 1: Crear una nueva campaña

Para crear una nueva campaña de correo electrónico transaccional, crea una campaña y selecciona **Correo electrónico transaccional** como tu canal de mensajería.

![Desplegable Crear campaña con la opción resaltada para el correo electrónico transaccional.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ahora puedes pasar a configurar tu campaña de correo electrónico transaccional.

## Paso 2: Configura tu campaña

El flujo de creación de campañas de correo electrónico transaccional se simplifica en comparación con el de una [campaña de correo electrónico estándar]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) para garantizar que tu correo electrónico transaccional crítico para la empresa pueda llegar a todos los usuarios.

Como resultado, notarás que varios ajustes con los que puedes estar familiarizado de otros tipos de campaña de Braze no son necesarios al configurar este tipo de campaña:

- El paso **Entrega** se ha simplificado para eliminar las opciones de programación. Los correos electrónicos transaccionales siempre se desencadenarán a través de la API REST de Braze utilizando el ID de campaña que aparece en la página **Entrega**. También se han eliminado ajustes adicionales, como los controles de reelegibilidad y los ajustes de limitación de frecuencia, para confirmar que todos los usuarios están localizables para estas alertas transaccionales críticas cuando tu servicio desencadena una solicitud de envío.
- Se ha eliminado el paso **Audiencias objetivo**. Como los correos electrónicos transaccionales inscriben a toda tu base de usuarios como elegibles (incluidos los usuarios que cancelaron su suscripción), no es necesario especificar filtros o segmentos. Como resultado, si tienes alguna lógica que aplicar a quién debe recibir este mensaje, te recomendamos que apliques esa lógica antes de determinar si debes realizar la solicitud de API a Braze para desencadenar el mensaje a un usuario específico.
- Se ha eliminado el paso **Conversiones**. Por el momento, los correos electrónicos transaccionales no admiten el seguimiento de eventos de conversión.

![Flujo de trabajo de redactar, entrega y confirmar para crear una campaña de correo electrónico transaccional.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Para configurar tu campaña de correo electrónico transaccional, sigue estos pasos:

1. Añade un nombre descriptivo para que puedas encontrar los resultados en tu página de **Campañas** después de haber enviado tus mensajes.
2. Redacta tu correo electrónico o selecciona una plantilla.
3. Toma nota de tu `campaign_id`. Después de guardar tu campaña de API, debes incluir los campos `campaign_id` generados con tu solicitud de API donde se indica en el artículo [Punto de conexión de correo electrónico transaccional]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Haz clic en **Guardar campaña** y estarás listo para iniciar tu campaña de API.

{% alert note %}
La configuración de cancelación de suscripción con un solo clic para las campañas de correo electrónico transaccional se establece de forma predeterminada en **Usar predeterminado del espacio de trabajo**, de forma similar a otras campañas de correo electrónico. Dado que se trata de mensajería transaccional, Braze no añade la cancelación de suscripción con un solo clic. Para añadir una cancelación de suscripción con un solo clic a este tipo de campaña, [edita esta configuración]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) en **Información de envío**.
{% endalert %}

### Etiquetas no permitidas en los correos electrónicos transaccionales

Las etiquetas de Liquid `Connected Content` y `Promotion Code` no están disponibles en las campañas de correo electrónico transaccional.

El uso de la etiqueta `Connected Content` requiere que Braze realice una solicitud de API saliente durante nuestro proceso de envío, lo que puede ralentizar el proceso de envío de mensajes si el servicio externo al que se realiza la solicitud experimenta latencia. Del mismo modo, la etiqueta `Promotion Code` requiere que Braze realice un procesamiento adicional para evaluar la disponibilidad de una promoción antes de enviarla, lo que puede ralentizar el proceso de envío en caso de que no haya ninguna disponible.

En consecuencia, no admitimos la inclusión de etiquetas `Connected Content` o `Promotion Code` en ningún campo de tu campaña de correo electrónico transaccional.