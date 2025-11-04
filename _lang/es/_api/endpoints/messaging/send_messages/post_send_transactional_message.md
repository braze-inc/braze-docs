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

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

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

{% multi_lang_include http_event_postback.md %}

{% endapi %}
