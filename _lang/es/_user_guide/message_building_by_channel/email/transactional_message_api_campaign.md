---
nav_title: Campañas de correo electrónico transaccional
article_title: Campañas de correo electrónico transaccional
page_order: 10

description: "Este artículo de referencia explica cómo crear y configurar una nueva campaña de correo electrónico transaccional Braze."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Campañas transaccionales por correo electrónico

> Los correos electrónicos transaccionales Braze se envían para facilitar una transacción acordada entre el remitente y el destinatario. Este artículo de referencia explica cómo crear una campaña de correo electrónico transaccional en el panel de control de Braze y generar un `campaign_id` para incluirlo en sus llamadas a la API para nuestro [punto final`/transactional/v1/campaigns/{campaign_id}/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
El correo electrónico transaccional Braze solo está disponible como parte de determinados paquetes Braze. Póngase en contacto con su gestor de éxito de clientes de Braze o abra un [ticket de soporte]({{site.baseurl}}/braze_support/) para obtener más información.
{% endalert %}

El tipo de campaña de correo electrónico transaccional está diseñado para enviar mensajes de correo electrónico automatizados y no promocionales con el fin de facilitar una transacción acordada entre usted y sus clientes. Esto incluye información como:

- Confirmaciones de pedido
- Restablecer contraseña
- Alertas de facturación
- Alertas de envío

En resumen, puede utilizar los correos electrónicos transaccionales para enviar notificaciones críticas para la empresa originadas en su servicio para un único usuario en las que la velocidad es de suma importancia. 

{% alert important %}
Los correos electrónicos transaccionales difieren de las campañas transaccionales, que pueden utilizarse para dirigirse a sus usuarios sin costes adicionales. Las campañas transaccionales, por ejemplo, pueden incluir mensajes enviados después de que un usuario añada un artículo a su cesta. Consulte [las opciones de segmentación del público]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) para obtener más información.
{% endalert %}

## Paso 1: Crear una nueva campaña

Para crear una nueva campaña de correo electrónico transaccional, cree una campaña y seleccione **Correo electrónico transaccional** como canal de mensajería.

![Crea el desplegable Campaña con la opción resaltada para el correo electrónico transaccional.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ahora, puede pasar a configurar su campaña de correo electrónico transaccional.

## Paso 2: Configura tu campaña

El flujo de creación de campañas de correo electrónico transaccional se simplifica en comparación con el de una [campaña de correo electrónico estándar]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) para garantizar que el correo electrónico transaccional crítico para su empresa pueda llegar a todos los usuarios.

Como resultado, observará que varios ajustes con los que puede estar familiarizado de otros tipos de campaña Braze no son necesarios al configurar este tipo de campaña:

- El paso **Entrega** se ha simplificado para eliminar las opciones de programación. Los correos electrónicos transaccionales siempre se activarán a través de la API REST de Braze utilizando el ID de campaña que aparece en la página **Entrega**. También se han eliminado ajustes adicionales, como los controles de reelegibilidad y los ajustes de limitación de frecuencia, para confirmar que todos los usuarios están localizables para estas alertas transaccionales críticas cuando su servicio activa una solicitud de envío.
- Se ha eliminado el paso **Audiencias objetivo**. Como los correos electrónicos transaccionales inscriben a toda su base de usuarios como elegibles (incluidos los usuarios dados de baja), no es necesario especificar filtros o segmentos. Como resultado, si tiene alguna lógica que aplicar a quién debe recibir este mensaje, le recomendamos que aplique esa lógica antes de determinar si debe realizar la solicitud de API a Braze para activar el mensaje a un usuario específico.
- Se ha eliminado el paso **Conversiones**. Por el momento, los correos electrónicos transaccionales no admiten el seguimiento de eventos de conversión.

![Flujo de trabajo de composición, entrega y confirmación para crear una campaña de correo electrónico transaccional.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Para configurar su campaña de correo electrónico transaccional, siga estos pasos:

1. Añade un nombre descriptivo para que puedas encontrar los resultados en tu página de **Campañas** después de haber enviado tus mensajes.
2. Redacte su correo electrónico o seleccione una plantilla.
3. Toma nota de tu `campaign_id`. Después de guardar su campaña de API, debe incluir los campos `campaign_id` generados con su solicitud de API donde se indica en el artículo [Punto final de correo electrónico transaccional]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Haga clic en **Guardar campaña** y estará listo para iniciar su campaña API.

{% alert note %}
La configuración de cancelación de suscripción con un solo clic para las campañas de correo electrónico transaccionales se establece por defecto en **Utilizar espacio de trabajo predeterminado**, de forma similar a otras campañas de correo electrónico. Dado que se trata de mensajes transaccionales, Braze no permite darse de baja con un solo clic. Para añadir una cancelación de suscripción con un solo clic a este tipo de campaña, [edite esta configuración]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) en **Información de envío**.
{% endalert %}

### Etiquetas no permitidas en los correos electrónicos transaccionales

Las etiquetas `Connected Content` y `Promotion Code` Liquid no están disponibles en las campañas de correo electrónico transaccionales.

El uso de la etiqueta `Connected Content` requiere que Braze realice una solicitud de API saliente durante nuestro proceso de envío, lo que puede ralentizar el proceso de envío de mensajes si el servicio externo que solicitamos experimenta latencia. Del mismo modo, la etiqueta `Promotion Code` requiere que Braze realice un procesamiento adicional para evaluar la disponibilidad de una promoción antes de enviarla, lo que puede ralentizar el proceso de envío en caso de que no haya ninguna disponible.

En consecuencia, no admitimos la inclusión de etiquetas `Connected Content` o `Promotion Code` en ningún campo de su campaña de correo electrónico transaccional.


