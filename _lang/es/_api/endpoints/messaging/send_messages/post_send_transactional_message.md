---
nav_title: "POST: Envía correos electrónicos transaccionales utilizando la entrega desencadenada por la API"
article_title: "POST: Envía correos electrónicos transaccionales utilizando la entrega desencadenada por la API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el punto final Braze de Envío de mensajes de correo electrónico transaccional mediante entrega desencadenada por API."

---

{% api %}
# Envía correos electrónicos transaccionales utilizando la entrega desencadenada por la API
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Utiliza este punto final para enviar mensajes transaccionales inmediatos y puntuales a un usuario designado.

Este punto final se utiliza junto con la creación de una [campaña de correo electrónico transaccional]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) Braze y el ID de campaña correspondiente.

{% alert important %}
El correo electrónico transaccional está disponible actualmente como parte de determinados paquetes Braze. Ponte en contacto con tu administrador del éxito del cliente de Braze para obtener más información.
{% endalert %}

Similar al [punto final Enviar campaña desencadenada]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), este tipo de campaña te permite alojar contenido de mensajes dentro del panel de Braze, al tiempo que dicta cuándo y a quién se envía un mensaje a través de tu API. A diferencia del punto final Enviar campaña desencadenada, que acepta una audiencia o segmento al que enviar mensajes, una solicitud a este punto final debe especificar un único usuario, ya sea mediante `external_user_id` o `user_alias`, ya que este tipo de campaña está diseñada para la mensajería 1:1 de alertas como confirmaciones de pedidos o restablecimiento de contraseñas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `transactional.send`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='correo electrónico transaccional' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `campaign_id` | Obligatoria | Cadena | ID de la campaña |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Opcional | Cadena |  Una cadena compatible con Base64. Validado con la siguiente regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Este campo opcional te permite pasar un identificador interno para este envío concreto, que se incluirá en los eventos enviados desde el postback de eventos HTTP transaccionales. Cuando se introduce, este identificador también se utilizará como clave de deduplicación, que Braze almacenará durante 24 horas. <br><br>Pasar el mismo identificador en otra solicitud no dará lugar a una nueva instancia de un envío de Braze durante 24 horas.|
|`trigger_properties`|Opcional|Objeto|Ver [propiedades del desencadenante]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Pares clave-valor de personalización que se aplicarán al usuario en esta solicitud. |
|`recipient`|Obligatoria|Objeto| El usuario al que diriges este mensaje. Puede contener `attributes` y un único `external_user_id` o `user_alias`.<br><br>Ten en cuenta que si proporcionas un ID de usuario externo que aún no existe en Braze, al pasar cualquier campo al objeto `attributes` se creará este perfil de usuario en Braze y se enviará este mensaje al usuario recién creado. <br><br>Si envías varias solicitudes al mismo usuario con datos diferentes en el objeto `attributes`, los atributos `first_name`, `last_name` y `email` se actualizarán de forma sincrónica y se incluirán como plantilla en tu mensaje. Los atributos personalizados no tienen esta misma protección, así que procede con cautela cuando actualices a un usuario a través de esta API y pases diferentes valores de atributos personalizados en rápida sucesión.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Respuesta

El punto final Enviar correo electrónico transaccional responderá con el `dispatch_id` del mensaje que representa la instancia de este envío de mensaje. Este identificador puede utilizarse junto con los eventos del postback de eventos HTTP transaccionales para rastrear el estado de un correo electrónico individual enviado a un único usuario.

### Ejemplos de respuestas

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Solución de problemas

El punto final también puede devolver un código de error y un mensaje legible por humanos en algunos casos, la mayoría de los cuales son errores de validación. Estos son algunos errores comunes que puedes obtener al realizar solicitudes no válidas.

| Error | Solución de problemas |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | El ID de campaña proporcionado no corresponde a una campaña transaccional. |
| `The external reference has been queued.  Please retry to obtain send_id.` | El external_send_id se ha creado recientemente, prueba con un nuevo external_send_id si vas a enviar un mensaje nuevo. |
| `Campaign does not exist` | El ID de campaña proporcionado no corresponde a una campaña existente. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | El ID de campaña proporcionado corresponde a una campaña archivada. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | El ID de campaña proporcionado corresponde a una campaña en pausa. |
| `campaign_id must be a string of the campaign api identifier` | El ID de campaña proporcionado no tiene un formato válido. |
| `Error authenticating credentials` | La clave de API proporcionada no es válida |
| `Invalid whitelisted IPs `| La dirección IP que envía la solicitud no está en la lista blanca de IP (si se está utilizando). |
| `You do not have permission to access this resource` | La clave de API utilizada no tiene permiso para realizar esta acción |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La mayoría de los puntos finales en Braze tienen una implementación de límite de velocidad que devolverá un código de respuesta 429 si has hecho demasiadas peticiones. El punto final de envío transaccional funciona de forma diferente: si superas el límite de tasa asignado, nuestro sistema seguirá ingiriendo las llamadas a la API, devolviendo códigos de éxito y enviando los mensajes; sin embargo, es posible que esos mensajes no estén sujetos al SLA contractual de la característica. Ponte en contacto con nosotros si necesitas más información sobre esta funcionalidad.

## Postback de eventos HTTP transaccionales

Todos los correos electrónicos transaccionales se complementan con devoluciones del estado del evento enviadas como una petición HTTP de vuelta a tu URL especificada. Eso te permitirá evaluar el estado del mensaje en tiempo real y tomar medidas para llegar al usuario en otro canal si el mensaje no se acaba entregando, o usar un sistema interno alternativo en caso de que Braze esté experimentando latencia.

Para asociar los eventos entrantes a una instancia concreta de envío, puedes elegir entre capturar y almacenar el `dispatch_id` de Braze devuelto en la [respuesta de la API](#example-response), o pasar tu propio identificador al campo `external_send_id`. Un ejemplo de un valor que puedes elegir pasar a ese campo puede ser un ID de pedido, en el que después de completar el pedido 1234, se desencadena un mensaje de confirmación de pedido al usuario a través de Braze, y se incluye `external_send_id : 1234` en la solicitud. Todos los postbacks de eventos siguientes, como `Sent` y `Delivered`, incluirán `external_send_id : 1234` en la carga útil, lo que te permitirá confirmar que el usuario ha recibido correctamente su correo electrónico de confirmación del pedido.

Para empezar a utilizar el **Postback de eventos** HTTP **transaccionales**, ve a **Configuración** > **Preferencias de correo electrónico** en tu panel de Braze y localiza la sección **Postback de estado de eventos transaccionales**. Introduce la URL deseada para recibir devoluciones.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), esta página se encuentra en **Administrar configuración** > Configuración de correo electrónico.
{% endalert %}

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### Cuerpo de la devolución

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### Estado del mensaje

|  Estado | Descripción |
| ------------ | ----------- |
| `sent` | Mensaje enviado correctamente a un socio de envío de correo electrónico Braze |
| `processed` | El socio de envío de correo electrónico ha recibido y preparado correctamente el mensaje para enviarlo al proveedor de buzón de entrada del usuario |
| `aborted` | Braze no pudo enviar correctamente el mensaje debido a que el usuario no tenía una dirección de correo electrónico, o se llamó a la lógica de cancelación de Liquid en el cuerpo del mensaje. Todos los eventos abortados incluyen un campo `reason` dentro del objeto de metadatos que indica por qué se ha abortado el mensaje |
|`delivered`| El mensaje fue aceptado por el proveedor de buzón de entrada de correo electrónico del usuario |
|`bounced`| El mensaje fue rechazado por el proveedor de buzón de entrada de correo electrónico del usuario. Todos los eventos rebotados incluyen un campo `reason` dentro del objeto de metadatos que refleja el código de error de rebote proporcionado por el proveedor del buzón de entrada |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ejemplo de devolución
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```


{% endapi %}
