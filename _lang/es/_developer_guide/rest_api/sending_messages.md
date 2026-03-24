---
nav_title: Enviar mensajes
article_title: Envío de mensajes mediante la API REST
page_order: 1
page_type: reference
description: "Este artículo de referencia describe las dos formas de enviar mensajes mediante programación utilizando la API REST de Braze."
---

# Envío de mensajes mediante la API REST

> Puedes enviar mensajes desde tu backend en tiempo real utilizando dos puntos finales diferentes de Braze. Cada uno tiene una forma de solicitud diferente: uno requiere el contenido completo del mensaje en la solicitud; el otro requiere un ID de campaña y envía el contenido definido en el panel.

Este enfoque funciona con cualquier canal de mensajería compatible con la API (WhatsApp, correo electrónico, SMS, notificaciones push, tarjetas de contenido, webhooks y más).

## Dos formas de enviar

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **ID de campaña** | Opcional. Omítelo para enviar sin seguimiento de la campaña en el panel de control, o proporciona un ID de campaña API más`message_variation_id`  en cada mensaje para realizar el seguimiento en el panel de control. | Se requiere. |
| **Contenido del mensaje** | Debes incluir un`messages`objeto en la solicitud (por ejemplo, `messages.whats_app`, `messages.email`). | No aceptado. El contenido del mensaje se define en la campaña en el panel de Braze. |
| **Casos de uso** | Envía un mensaje con el contenido completamente especificado en la solicitud de la API. | Desencadena una campaña predefinida (contenido en el panel) para destinatarios específicos a través de la API. |

Para obtener información detallada sobre las solicitudes y respuestas, consulta las referencias [Enviar mensajes inmediatamente (solo API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) y [Enviar campañas mediante]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) el punto final [de entrega activado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

---

## Opción 1: Enviar con el contenido del mensaje en la solicitud (`/messages/send`)

Utiliza este punto final cuando desees especificar el contenido completo del mensaje en la solicitud de API. **Debes** incluir un`messages`objeto (por ejemplo, `messages.whats_app`, `messages.email`, o `messages.sms`). Puedes omitir`campaign_id`  para enviar sin seguimiento de la campaña, o incluir un ID de campaña API y`message_variation_id`  en cada mensaje para realizar un seguimiento de los envíos en el panel (consulta la [referencia del punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para obtener más detalles).

**Requisitos:** Clave de API con el`messages.send`permiso.

{% alert important %}
Cada destinatario debe `external_user_ids`existir ya en Braze. Para crear usuarios como parte de un envío, utiliza[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)primero  o, en su lugar, utiliza [la opción 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (campaña desencadenada por API).
{% endalert %}

### Ejemplo: Mensaje de plantilla de WhatsApp

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Para obtener la especificación completa del objeto WhatsApp, consulta [Objeto WhatsApp]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
El`/messages/send`punto final solo admite plantillas de WhatsApp con encabezados TEXT o IMAGE. Para DOCUMENT, VIDEO u otros tipos de encabezados multimedia, utiliza el [punto final de la campaña desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) o el panel de Braze.
{% endalert %}

### Ejemplo: Correo electrónico

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Para otros canales, consulta [Objetos de mensajería]({{site.baseurl}}/api/objects_filters/#messaging-objects).

---

## Opción 2: Desencadena una campaña con contenido en el panel (`/campaigns/trigger/send`)

Utiliza este punto final cuando el contenido del mensaje se cree en el panel de Braze (campaña activada por API). Envías un objeto **obligatorio**`campaign_id`  y los destinatarios; **no** envías un`messages`objeto .

**Requisitos:** Clave de API con el`campaigns.trigger.send`permiso.

### Paso 1: Crear una campaña desencadenada por API

1. En el panel de Braze, ve a **Mensajería** > **Campañas**.
2. Selecciona **Crear campaña** y, a continuación, **Campaña desencadenada por API** (no «Campaña API»).
3. Añade tu canal de mensajería (WhatsApp, correo electrónico, SMS, etc.) y crea el contenido del mensaje en el panel.
4. Anota el **ID de la campaña** (y **el ID de envío** si utilizas varias variantes de mensaje). Los utilizarás en la solicitud de API.

Para obtener más información sobre cómo crear campañas activadas por API, consulta [Entrega activada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

### Paso 2: Desencadena la campaña a través de la API.

Envía una solicitud POST a`/campaigns/trigger/send`  con`campaign_id`  y`recipients`  (o `broadcast`/`audience`). No incluyas un`messages`objeto: el contenido proviene de la campaña.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Para ver el cuerpo completo de la solicitud (incluidos `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), consulta la referencia del punto final [Enviar campañas mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body).

---

## Verifica tu integración

1. Envía una solicitud utilizando una de las opciones anteriores, con tu propio ID de usuario como destinatario.
2. Confirma que el mensaje se ha entregado.
3. Si utilizas la opción 2, comprueba la campaña en el panel de Braze para confirmar que el envío se ha registrado.

## Consideraciones

- Utiliza [las características de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze para adaptar el contenido cuando sea posible.
- Asegúrate de que tu mensajería cumpla con las normativas pertinentes e incluya las opciones de exclusión voluntaria y los avisos de privacidad necesarios.
- Para obtener más información sobre los puntos finales (programación, activadores de Canvas, etc.), consulta [Puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/).
