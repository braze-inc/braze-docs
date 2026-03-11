---
nav_title: Enviar mensajes SMS
article_title: Envío de mensajes SMS mediante la API REST
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo enviar mensajes SMS utilizando la API REST de Braze y una campaña API."
channel:
  - SMS
---

# Envío de mensajes SMS mediante la API REST

> Utiliza la API REST de Braze para enviar mensajes SMS transaccionales desde tu backend en tiempo real. Este enfoque te permite crear un servicio que envía mensajes SMS de forma programada, al tiempo que realiza el seguimiento de los análisis de entrega junto con tus otras campañas y lienzos en el panel de Braze.

Esto puede resultar especialmente útil para la mensajería transaccional de gran volumen cuyo contenido se define en tus sistemas backend. Por ejemplo, puedes notificar a los consumidores cuando reciban un mensaje de otro usuario, invitándolos a visitar tu sitio web y consultar su buzón de entrada.

Con este enfoque, tú puedes:

- Desencadena mensajes SMS desde tu backend en tiempo real.
- Realiza un seguimiento de análisis de todas tus campañas de marketing y lienzos.
- Amplía el caso de uso con características adicionales de Braze, como retrasos en los mensajes, reorientación de seguimiento y pruebas A/B.
- Si lo deseas, cambia a [la entrega activada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) para definir tus plantillas de mensajes en el panel de Braze sin dejar de desencadenar los envíos desde tu backend.

Para enviar un mensaje SMS a través de la API REST, debes configurar una campaña API en el panel de Braze y, a continuación, utilizar el[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)punto final para enviar el mensaje.

## Requisitos previos

Para completar esta guía, necesitas:

| Requisito | Descripción |
| --- | --- |
| Clave de API REST de Braze | Una clave con el`messages.send`permiso. Para crear una, ve a **Configuración** > **API e identificadores** > **Claves de API**. |
| Grupo de suscripción a SMS | Un grupo de suscripción SMS configurado en tu espacio de trabajo de Braze. |
| Servicio de backend | Un servicio backend o entorno de scripting capaz de realizar solicitudes HTTP POST a la API REST de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 1: Crear una campaña API

1. En el panel de Braze, ve a **Mensajería** > **Campañas**.
2. Selecciona **Crear campaña** y, a continuación, selecciona **Campañas API**.
3. Introduce un nombre y una descripción para tu campaña, como «Notificación por mensaje SMS».
4. Añade etiquetas relevantes para su identificación y seguimiento.
5. Selecciona **Añadir canal de mensajería** y, a continuación, selecciona **SMS**.
6. Anota el **ID de la campaña** y **el ID de la variación del mensaje** que se muestran en la página de la campaña. Necesitarás ambos valores al crear tu solicitud API.

## Paso 2: Enviar un mensaje SMS utilizando la API

Crea una solicitud POST al  punto[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)final. Incluye el ID de la campaña, el ID externo del destinatario y el contenido del SMS en la carga útil de la solicitud.

{% alert important %}
Cada destinatario mencionado en`external_user_ids`  debe existir ya en Braze. Los envíos solo por API no crean nuevos perfiles de usuario. Si necesitas crear usuarios como parte de un envío, utiliza[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)  primero o utiliza una [campaña activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Ejemplo de solicitud

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Reemplaza`YOUR_REST_ENDPOINT`  con la [URL del punto final REST]({{site.baseurl}}/api/basics/#endpoints) de tu espacio de trabajo.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Reemplaza los valores de marcador de posición con tus ID reales. El`body`campo admite [la personalización Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), por lo que puedes adaptar el contenido del mensaje a cada destinatario. Para obtener la lista completa de parámetros compatibles con el objeto de mensajería SMS, consulta [Objeto SMS]({{site.baseurl}}/api/objects_filters/messaging/sms_object/).

Después de crear la solicitud, envía la solicitud POST desde tu servicio backend a la API REST de Braze.

## Paso 3: Verifica tu integración

Una vez completada la configuración, verifica la integración:

1. Envía una solicitud API tal y como se describe en [el paso 2](#step-2-send-an-sms-message-using-the-api), utilizando tu propio ID de usuario como destinatario.
2. Confirma que el mensaje SMS se ha entregado a tu teléfono.
3. En el panel de Braze, ve a la página de resultados de la campaña y confirma que el envío se ha registrado.
4. Supervisa de cerca los resultados a medida que amplías tu campaña.

## Consideraciones

- Confirma que tus campañas SMS cumplen con las normativas pertinentes y los requisitos de los operadores. Incluye instrucciones para darse de baja (como «Envía STOP para darte de baja») en todos los mensajes. Para obtener más información, consulta [las leyes y normativas sobre SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) y [las palabras clave para la adhesión voluntaria y la baja]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/).
- Utiliza [las características de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze para adaptar el contenido de los SMS a los consumidores individuales, incluyendo contenido dinámico y datos específicos del usuario.
- La API REST de Braze ofrece [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/) adicionales para programar mensajes, activar campañas y mucho más.
