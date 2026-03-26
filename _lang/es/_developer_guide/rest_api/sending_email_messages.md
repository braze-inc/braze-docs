---
nav_title: Enviar mensajes de correo electrónico
article_title: Enviar mensajes de correo electrónico usando la API REST
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo enviar mensajes de correo electrónico usando la API REST de Braze y una campaña de API."
channel:
  - email
---

# Enviar mensajes de correo electrónico usando la API REST

> Usa la API REST de Braze para enviar correos electrónicos transaccionales desde tu backend en tiempo real. Este enfoque te permite crear un servicio que envía correos electrónicos de forma programática mientras realizas el seguimiento de los análisis de entrega junto con tus otras campañas y Canvas en el dashboard de Braze.

Esto puede ser especialmente útil para la mensajería transaccional en la que el contenido se define en tus sistemas de backend. Por ejemplo, puedes notificar a los consumidores cuando reciben un mensaje de otro usuario, invitándolos a visitar tu sitio web y revisar su buzón de entrada.

Con este enfoque, puedes:

- Desencadenar correos electrónicos desde tu backend en tiempo real.
- Realizar el seguimiento de los análisis junto con todas tus campañas y Canvas gestionados por marketing, incluyendo aperturas, clics y rebotes.
- Usar los datos de interacción con los mensajes para desencadenar mensajes posteriores, como seguimientos de reorientación.
- Ampliar el caso de uso con características adicionales de Braze, como retrasos en los mensajes y pruebas A/B.
- Opcionalmente, cambiar a la [entrega desencadenada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) para definir tus plantillas de correo electrónico en el dashboard de Braze y seguir desencadenando los envíos desde tu backend.

Para enviar un correo electrónico a través de la API REST, necesitas configurar una campaña de API en el dashboard de Braze y luego usar el punto de conexión [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para enviar el mensaje.

## Requisitos previos

Para completar esta guía, necesitas:

| Requisito | Descripción |
| --- | --- |
| Clave de API REST de Braze | Una clave con el permiso `messages.send`. Para crear una, ve a **Configuración** > **APIs e identificadores** > **Claves de API**. |
| ID de aplicación de Braze | El identificador de tu aplicación dentro de tu espacio de trabajo. Para encontrarlo, ve a **Configuración** > **APIs e identificadores** y consulta la sección **Identificadores de aplicación**. Este valor es obligatorio en el campo `app_id` del objeto de mensajería de correo electrónico. Para más información, consulta [Identificador de aplicación]({{site.baseurl}}/api/identifier_types/). |
| Contenido HTML del correo electrónico | El cuerpo HTML de tu mensaje de correo electrónico, preparado con antelación. |
| Servicio de backend | Un servicio de backend o entorno de scripting capaz de realizar solicitudes HTTP POST a la API REST de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 1: Crear una campaña de API

1. En el dashboard de Braze, ve a **Mensajería** > **Campañas**.
2. Selecciona **Crear campaña** y luego selecciona **Campaña de API**.
3. Introduce un nombre y una descripción para tu campaña, como "Notificación de mensaje por correo electrónico".
4. Añade etiquetas relevantes para la identificación y el seguimiento.
5. Selecciona **Añadir canal de mensajería** y luego selecciona **Correo electrónico**.
6. Anota el **ID de campaña** que se muestra en la página de la campaña. Necesitarás este valor al construir tu solicitud de API. Opcionalmente, anota también el **ID de variación de mensaje**: inclúyelo en tu solicitud si quieres atribuir las estadísticas de envío a una variación de mensaje específica.

## Paso 2: Enviar un correo electrónico usando la API

Construye una solicitud POST al punto de conexión [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Incluye el ID de campaña, el ID de usuario externo del destinatario y el contenido del correo electrónico en la carga útil de la solicitud.

{% alert important %}
Cada destinatario referenciado en `external_user_ids` debe existir previamente en Braze. Los envíos exclusivos por API no crean nuevos perfiles de usuario. Si necesitas crear usuarios como parte de un envío, usa primero [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), o usa una [campaña desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) en su lugar.
{% endalert %}

### Ejemplo de solicitud

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Reemplaza `YOUR_REST_ENDPOINT` con la [URL del punto de conexión REST]({{site.baseurl}}/api/basics/#endpoints) de tu espacio de trabajo.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

Reemplaza los valores de marcador de posición con tus ID reales. El campo `from` debe usar el formato `"Nombre para mostrar <email@address.com>"`. El campo `body` acepta HTML válido y admite [personalización con Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), por lo que puedes adaptar el contenido del correo electrónico a cada destinatario. Para ver la lista completa de parámetros admitidos por el objeto de mensajería de correo electrónico, consulta [Objeto de correo electrónico]({{site.baseurl}}/api/objects_filters/messaging/email_object/).

Después de construir la solicitud, envía la solicitud POST desde tu servicio de backend a la API REST de Braze.

## Paso 3: Verificar tu integración

Después de completar la configuración, verifica tu integración:

1. Envía una solicitud de API como se describe en el [Paso 2](#step-2-send-an-email-using-the-api), usando tu propio ID de usuario como destinatario.
2. Confirma que el correo electrónico se entrega en tu buzón de entrada.
3. En el dashboard de Braze, ve a la página de resultados de la campaña y confirma que el envío se ha registrado.
4. Monitorea los resultados de cerca a medida que escales tu campaña.

## Consideraciones

- Confirma que tus campañas de correo electrónico cumplen con las regulaciones pertinentes, como el RGPD y CAN-SPAM, incluyendo las opciones de cancelación de suscripción y los avisos de privacidad necesarios. Para más información, consulta [Gestión de suscripciones de usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) y [Mejores prácticas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/).
- Usa las [características de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze para adaptar el contenido del correo electrónico a consumidores individuales, incluyendo contenido dinámico y datos específicos del usuario.
- La API REST de Braze ofrece [puntos de conexión de mensajería]({{site.baseurl}}/api/endpoints/messaging/) adicionales para programar mensajes, desencadenar campañas y más.