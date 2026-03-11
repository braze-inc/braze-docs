---
nav_title: WhatsApp y sistemas externos
article_title: Realiza la integración de Braze y WhatsApp con un sistema externo.
page_order: 2
description: "Este artículo de referencia proporciona una guía paso a paso para la integración de Braze y WhatsApp con un sistema externo de inteligencia artificial o comunicación."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Realiza la integración de Braze y WhatsApp con un sistema externo de inteligencia artificial o comunicación.

> Aprovecha el poder de los chatbots con IA y los traspasos a agentes en vivo en el canal de WhatsApp para optimizar tus operaciones de atención al cliente. Por la automatización de las consultas rutinarias y el paso fácil a los agentes humanos cuando sea necesario, puedes mejorar significativamente los tiempos de respuesta y la experiencia del cliente.

## Cómo funciona

La integración entre Braze y el sistema externo de inteligencia artificial o comunicación funciona como una vía de doble sentido, en la que Braze es el canal de comunicación y el sistema externo es la «inteligencia» que procesa los mensajes y formula las respuestas.

El flujo de trabajo de integración se puede dividir en dos flujos clave:
**Flujo entrante:** El mensaje de un usuario llega a Braze y, a continuación, se reenvía a tu sistema externo para su procesamiento.
**Flujo de salida:** Después de procesar el mensaje, tu sistema externo envía una respuesta a Braze, que a continuación entrega el mensaje al usuario final.

Para automatizar esta comunicación de manera eficiente, esta integración utiliza dos características clave de Braze: [campañas de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) y [campañas activadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

![Arquitectura de la integración entre el canal Braze WhatsApp y un sistema externo.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Arquitectura de la integración entre el canal Braze WhatsApp y un sistema externo.*</sup>

## Requisitos previos

| Requisito previo | Descripción |
| - | - |
| Sistema externo | Un sistema de inteligencia artificial o comunicación de terceros capaz de crear y administrar chatbots, sistemas automatizados de servicio al cliente mediante API, o ambos. |
| Integración entre Braze y WhatsApp | Un número de WhatsApp administrado por Braze. |
| Clave de API REST de Braze | Una clave de API REST con`campaigns.trigger.send`permisos. Esto se puede crear en el panel de Braze, en **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configurar la integración

### Paso 1: Crear una campaña de webhook para mensajes entrantes

En primer lugar, crea una campaña webhook para establecer una forma de enviar los mensajes de WhatsApp recibidos por Braze a tu sistema externo.

1. En Braze, crea una campaña de webhook.
2. En el compositor de webhooks, selecciona **Componer webhook**.
3. En el campo **URL de webhook**, introduce el punto final de la API (URL) del sistema externo que recibirá el mensaje.
4. Selecciona **Texto sin formato** para el cuerpo de la solicitud e introduce una carga útil con personalización que contenga el  y el número de`external_id` teléfono del usuario, el contenido del mensaje y otra información relevante, como:

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5\. En el paso **Programar entrega** del compositor de campañas, selecciona **Entrega basada en acciones** como tipo de entrega y **Enviar un mensaje entrante de WhatsApp** como activador de la campaña.

![Entrega basada en acciones con un desencadenante para enviar un mensaje entrante de WhatsApp.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Termina de redactar tu campaña, guárdala y lánzala. Después de lanzar la campaña, cada vez que se recibe un mensaje, Braze envía un webhook a tu sistema externo.

### Paso 2: Crea una campaña activada por API para mensajes salientes. {#step-2}

A continuación, crea una campaña activada por API para establecer una forma en que tu sistema externo envíe mensajes a los usuarios a través de WhatsApp.

1. En Braze, crea una campaña de WhatsApp. 
2. En el creador de mensajes, selecciona **«Mensaje de plantilla de WhatsApp**» o **«Mensaje de respuesta**» y, a continuación, selecciona la plantilla o el diseño del mensaje de respuesta. Puedes seleccionar cualquier diseño de mensaje de respuesta, ya que el mensaje entrante abrió la ventana de WhatsApp de 24 horas.

![Creador de mensajes con opciones para seleccionar el tipo y el diseño del mensaje.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Añade la propiedad de activación de la API al cuerpo del mensaje, por ejemplo {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Esto permite que tu sistema de IA rellene el mensaje que se enviará.

![Creador de mensajes con cuerpo del mensaje que contiene propiedades de activación.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. En el paso **Programar entrega** del compositor de campañas, selecciona **Entrega basada en acciones** como tipo de entrega.
5\. Guarda la campaña y toma nota del identificador único`campaign_id`que Braze genera para esta campaña. Necesitarás el ID para el siguiente paso.

### Paso 3: Conecta el sistema externo a la campaña que se desencadena mediante API.

Por último, configura tu sistema externo para que llame a Braze y envíe la respuesta.

1. En el código de tu sistema externo, después de procesar el mensaje recibido y generar la respuesta, realiza una solicitud POST al punto final `/messages/send`de Braze.
2. En el cuerpo`/messages/send` de la solicitud, incluye el`campaign_id`[paso 2](#step-2), el usuario `external_id`y el contenido de la respuesta del sistema externo.
3. Utiliza la propiedad de activación de la API del [paso 2](#step-2) para insertar la respuesta del sistema externo y no olvides incluir tu clave de API en el encabezado de solicitud para la autenticación, como en este ejemplo de cURL:

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"         
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

¡Ahora tienes una base sólida para crear un flujo de trabajo de chatbot con IA!

### Personalización de tu flujo de trabajo personalizado

Puedes ampliar tu lógica de integración para:
- Utiliza diferentes palabras clave para desencadear distintas campañas de webhooks.
- Crea flujos de conversación más complejos con campañas de varios pasos que se desencadenan a través de la API.
- Registra la información del chat en Braze como atributos personalizados para enriquecer el perfil de usuario y realizar la segmentación de futuras campañas.
