---
nav_title: WhatsApp y sistema externo
article_title: Integración de Braze y WhatsApp con un sistema externo
page_order: 2
description: "Este artículo de referencia proporciona una guía paso a paso para integrar la integración de Braze y WhatsApp con una IA externa o un sistema de comunicación."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integración de Braze y WhatsApp con una IA externa o un sistema de comunicación

> Aprovecha el poder de los chatbots de IA y las entregas de agentes en vivo en el canal WhatsApp para agilizar tus operaciones de atención al cliente. Automatizando las consultas rutinarias y pasando fácilmente a agentes humanos cuando sea necesario, puedes mejorar significativamente los tiempos de respuesta y mejorar la experiencia general del cliente.

## Cómo funciona

La integración entre Braze y la IA externa o el sistema de comunicación funciona como una vía de doble sentido, en la que Braze es el canal de mensajería y el sistema externo es la "inteligencia" que procesa los mensajes y formula las respuestas.

El flujo de trabajo de integración puede dividirse en dos flujos clave:
**Flujo entrante:** El mensaje de un usuario llega a Braze y se reenvía a tu sistema externo para que lo procese.
**Flujo de salida:** Tras procesar el mensaje, tu sistema externo envía una respuesta a Braze, que a su vez entrega el mensaje al usuario final.

Para automatizar eficazmente esta comunicación, esta integración utiliza dos características clave de Braze: [las campañas webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) y [las campañas desencadenadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

\![Arquitectura de la integración entre el canal de WhatsApp de Braze y un sistema externo.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Arquitectura de la integración entre el canal de WhatsApp de Braze y un sistema externo.*</sup>

## Requisitos previos

| Prerrequisito | Descripción |
| - | - |
| Sistema externo | Un sistema de IA o comunicación de terceros capaz de crear y administrar chatbots, sistemas automatizados de servicio al cliente mediante API, o ambos. |
| Integración de Braze y WhatsApp | Un número de WhatsApp administrado por Braze | Un número de WhatsApp administrado por Braze | Un número de WhatsApp administrado por Braze | Un número de WhatsApp administrado por Braze | Un número de WhatsApp administrado por Braze | Un número de WhatsApp administrado por Braze
| Clave de API REST de Braze | Una clave de API REST con permisos `campaigns.trigger.send`. Se puede crear en el panel de Braze yendo a **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configurar la integración

### Paso 1: Crea una campaña webhook para mensajes entrantes

En primer lugar, crea una campaña de webhook para establecer una forma de enviar los mensajes de WhatsApp recibidos por Braze a tu sistema externo.

1. En Braze, crea una campaña webhook.
2. En el compositor de webhooks, selecciona **Componer webhook**.
3. En el campo **URL del webhook**, introduce el punto final de la API (URL) del sistema externo que recibirá el mensaje.
4. Selecciona **Texto sin formato** para el cuerpo de la solicitud e introduce una carga útil con personalización que contenga la dirección `external_id` y el número de teléfono del usuario, el contenido del mensaje y otra información relevante, como por ejemplo

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
5\. En el paso **Programar entrega** del compositor de tu campaña, selecciona **Basado en acciones** para el tipo de entrega y **Enviar un mensaje entrante de WhatsApp** para el desencadenante de la campaña.

Entrega basada en acciones con un desencadenante de envío de un mensaje entrante de WhatsApp.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Termina de componer tu campaña, luego guárdala y lánzala. Ahora, cada vez que se reciba un mensaje, Braze enviará un webhook a tu sistema externo.

### Paso 2: Crea una campaña desencadenada por API para mensajes salientes {#step-2}

A continuación, crea una campaña desencadenada por la API para establecer una forma de que tu sistema externo envíe mensajes a los usuarios a través de WhatsApp.

1. En Braze, crea una campaña de WhatsApp. 
2. En el creador de mensajes, selecciona **la plantilla de mensaje de WhatsApp** o el **mensaje de respuesta** y, a continuación, selecciona la plantilla o el diseño del mensaje de respuesta. Puedes seleccionar cualquier diseño de mensaje de respuesta porque el mensaje entrante abrió la ventana de WhatsApp 24 horas.

\![Creador de mensajes con opciones para seleccionar el tipo de mensaje y el diseño del mensaje.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Añade la propiedad desencadenante de la API al cuerpo del mensaje, como {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Esto permite a tu sistema de IA rellenar el mensaje que se enviará.

\![Creador de mensajes con cuerpo de mensaje que contiene propiedades desencadenantes.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. En el paso **Programar entrega** del compositor de tu campaña, selecciona **Basada en acciones** para el tipo de entrega.
5\. Guarda la campaña y toma nota del `campaign_id` único que Braze genera para esta campaña. Necesitarás el ID para el siguiente paso.

### Paso 3: Conecta el sistema externo a la campaña desencadenada por la API

Por último, configura tu sistema externo para que llame a Braze y envíe la respuesta.

1. En el código de tu sistema externo, tras procesar el mensaje recibido y generar la respuesta, haz una petición POST al punto final Braze `/messages/send`.
2. En el cuerpo de la solicitud `/messages/send`, incluye el `campaign_id` del [Paso 2](#step-2), el `external_id` del usuario y el contenido de la respuesta del sistema externo.
3. Utiliza la propiedad desencadenar API del [paso 2](#step-2) para insertar la respuesta del sistema externo, y no olvides incluir tu clave de API en el encabezado de solicitud para la autenticación, como en este ejemplo de cURL:

{% raw %}
```json
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

¡Ahora tienes una base sólida para construir un flujo de trabajo de chatbot de IA!

### Personaliza tu flujo de trabajo

Puedes ampliar tu lógica de integración para:
- Utiliza palabras clave diferentes para desencadenar campañas webhook distintas.
- Crea flujos de conversación más complejos con campañas desencadenadas por API de varios pasos.
- Registra la información del chat en Braze como atributos personalizados para enriquecer el perfil de usuario y segmentar futuras campañas.
