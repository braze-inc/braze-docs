---
nav_title: Zendesk
article_title: Chat de Zendesk
description: "Aprende a integrar Zendesk Chat con Braze y a configurar una conversación bidireccional por SMS."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Chat de Zendesk

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) utiliza webhooks de cada plataforma para establecer una conversación bidireccional por SMS. Cuando un usuario solicita soporte, se crea un ticket en Zendesk. Las respuestas de los agentes se reenvían a Braze a través de una campaña de SMS desencadenada por la API, y las respuestas de los usuarios se devuelven a Zendesk.

## Requisitos previos


| Requisito previo | Descripción |
|---|---|
| Una cuenta de Zendesk | Se requiere una cuenta de Zendesk para aprovechar esta asociación.|
| Un token de autorización básica de Zendesk | Se utilizará un token de autorización básica de Zendesk para realizar una solicitud de webhook saliente de Braze a Zendesk.|
| Una clave de API REST Braze  | Una clave de API REST de Braze con permisos `campaigns.trigger.send`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**.|

## Ejemplos

Mejora la eficacia de la atención al cliente combinando las capacidades de Braze SMS con las respuestas en vivo de los agentes de Zendesk para atender las consultas de los usuarios con asistencia humana con prontitud.

## Integración de Zendesk Chat

### Paso 1: Crear un webhook en Zendesk

1. En la consola para desarrolladores de Zendesk, ve a webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. En **Crear webhook**, selecciona **Desencadenar o automatización**.
3. Para **la URL del punto** final, añade el punto final **/campaign/trigger/send**.
4. En **Autenticación**, selecciona **Token de portador** y añade la clave de API REST de Braze con permisos `campaigns.trigger.send`.

![Un ejemplo de webhook de Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### Paso 2: Crear una campaña de SMS salientes

A continuación, crearás una campaña de SMS que escuchará los webhooks de Zendesk y enviará una respuesta SMS personalizada a tus clientes.

#### Paso 2.1: Redacta tu mensaje

Cuando Zendesk envía el contenido de un mensaje a través de la API, éste tiene el siguiente formato:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Así que tenemos que extraer el detalle que queremos de esta cadena para mostrarlo en el mensaje, o de lo contrario un usuario verá todos los detalles.

![Un SMS de ejemplo sin formato.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

En el cuadro de texto **Mensaje**, añade el siguiente código Liquid y cualquier idioma de exclusión u otro contenido estático:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```
{% endraw %}

![Un SMS de ejemplo con formato.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Paso 2.2: Programar la entrega

Para el tipo de entrega, selecciona **Entrega desencadenada por API** y, a continuación, copia el ID de campaña que se utilizará en los pasos siguientes.

![Entrega desencadenada por la API]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Por último, en **Controles de entrega**, activa la reelegibilidad.

![Re-elegibilidad habilitada en "Controles de entrega".]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### Paso 3: Crea un desencadenador en Zendesk para reenviar las respuestas de los agentes a Braze

Ve a **Objetos y reglas** > **Reglas de negocio** > **Desencadenantes**.

1. Crea una nueva **categoría** (por ejemplo, **Desencadenar un mensaje**).
2. Crea un nuevo **desencadenante** (por ejemplo, **Responder vía SMS Braze**).
3. En **Condiciones**, selecciona:
- **Ticket>Comentario** está **Presente y el solicitante puede ver el comentario** para que el mensaje se desencadene cada vez que se incluya un nuevo comentario público en la actualización de un ticket
- **Billete>Actualizar** *no es un* **servicio Web (API)** para que cuando un usuario envíe un mensaje desde Braze, no se reenvíe a su teléfono móvil. Sólo se reenviarán los mensajes procedentes de Zendesk.

![Responde por SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

En **Acciones**, selecciona **Notificar por webhook** y elige el punto final que creaste en el paso 1. A continuación, especifica el cuerpo de la llamada a la API. Introduce el `campaign_id` del [paso 2.2](#step-22-schedule-the-delivery) en el cuerpo de la solicitud.

![Responde por SMS Braze JSON body.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Paso 4: Crear un desencadenador en Zendesk para actualizar a un usuario cuando se cierra un ticket

Si quieres notificar al usuario que el ticket se ha cerrado, crea una nueva campaña en Braze con el cuerpo de respuesta de la plantilla.

![Actualizar un usuario cuando se cierra un ticket.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Selecciona **Entrega desencadenada por API** y copia el ID de la campaña.

A continuación, configura un desencadenador para notificar a Braze cuando se cierre el ticket:
- Categoría: **Desencadenar un mensaje**
- En Condiciones, selecciona **Ticket>Estado del ticket** y cámbialo a **Resuelto**

![Resuelta la configuración de tickets en Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

En **Acciones**, selecciona **Notificar por webhook** y elige el segundo punto final que acabas de crear. A partir de ahí, tenemos que especificar el cuerpo de la llamada a la API:

![Cuerpo JSON de tickets resuelto.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Paso 5: Añadir un campo de usuario personalizado en Zendesk

En el Centro de Administración, selecciona **Personas** en la barra lateral y, a continuación, **Configuración** > **Campos de usuario**. Añade el campo de usuario personalizado `braze_external_id`.

### Paso 6: Configurar el reenvío de SMS entrantes

A continuación, crearás dos nuevas campañas webhook en Braze para poder reenviar los SMS entrantes de los clientes al buzón de entrada de Zendesk.

| Campaña           | Propósito                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Campaña webhook 1 | Crea un nuevo ticket en Zendesk.                                                     |
| Campaña webhook 2 | Reenvía todas las respuestas SMS conversacionales enviadas por el cliente a Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 }

#### Paso 6.1: Crear una categoría de palabras clave SMS

En el panel de Braze, ve a **Audiencia**, elige tu **grupo de suscripción a SMS** y, a continuación, selecciona **Añadir palabra clave personalizada**. Rellena los siguientes campos para crear una categoría de palabras clave SMS exclusiva para Zendesk.

| Campo            | Descripción                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Categoría de palabra clave | El nombre de tu categoría de palabras clave, como `ZendeskSMS1`.                                                                 |
| Palabras claves         | Tus palabras clave personalizadas, como `SUPPORT`.                                                                                  |
| Mensaje de respuesta    | El mensaje que se enviará cuando se detecte una palabra clave, como "Un representante del servicio de atención al cliente se pondrá en contacto contigo en breve". |
{: .reset-td-br-1 .reset-td-br-2 }

![Un ejemplo de categoría de palabras clave SMS en Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Paso 6.2: Crea tu primera campaña webhook

En el panel de Braze, crea tu primera campaña webhook. Este mensaje indicará a Zendesk que se está solicitando soporte.

En el compositor del webhook, rellena los siguientes campos:
- URL del webhook: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- Método HTTP: POST
- Encabezados de solicitud:
- Tipo de contenido: application/json
- Autorización:  Básica {{Token}}
- Cuerpo de la solicitud: 

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Un ejemplo de solicitud con las dos cabeceras requeridas.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Paso 6.3: Programar la primera entrega

Para **Programar entrega**, selecciona **Entrega basada en acciones** y, a continuación, elige **Enviar un mensaje SMS entrante** para tu tipo de desencadenante. Añade también el grupo de suscripción SMS y la categoría de palabras clave que configuraste anteriormente.

![La página "Programar entrega" de la primera campaña webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

En **Controles de entrega**, activa la reelegibilidad.

![Reelegibilidad seleccionada en "Controles de entrega" para la primera campaña webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Paso 6.4: Crea tu segunda campaña webhook

Configura una campaña webhook para reenviar los mensajes SMS restantes del usuario a Zendesk:

Como Zendesk envía el ID del ticket como una cadena, crea un bloque de contenido para convertir la cadena en un número entero y poder utilizarlo en el webhook de Zendesk.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

En el compositor de webhooks:
- URL del webhook: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Solicita: PUT
- KVP:
    - Tipo de contenido:application/JSON
    - Autorización: Básica {{Token}}

Cuerpo de muestra: 

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Paso 6.5: Completa la configuración de la segunda campaña webhook
- Configura un desencadenante basado en acciones para los usuarios que envían un mensaje entrante en la categoría "Otros".
- Configura los criterios de reeligibilidad.
- Añade las audiencias aplicables (en este caso, el atributo personalizado **zendesk_ticket_open** es **true**).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
