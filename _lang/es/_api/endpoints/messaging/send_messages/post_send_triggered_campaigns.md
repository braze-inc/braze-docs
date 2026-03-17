---
nav_title: "PUBLICAR: Enviar campañas utilizando la entrega desencadenada por API"
article_title: "PUBLICAR: Enviar campañas mediante entrega desencadenada por API"
search_tag: Punto de conexión
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el punto final Braze de envío de campañas mediante entrega desencadenada por API."

---
{% api %}
# Envía mensajes de campaña utilizando la entrega desencadenada por API
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints  %}
/campaigns/trigger/send
{% endapimethod %}

> Utiliza este punto final para enviar mensajes inmediatos y puntuales a usuarios designados utilizando la entrega desencadenada por la API.

La entrega desencadenada por API te permite alojar el contenido de los mensajes dentro del panel Braze, al tiempo que dictas cuándo se envía un mensaje y a quién mediante tu API.

Si te diriges a un segmento, se almacena un registro de tu solicitud en la [consola para desarrolladores](https://dashboard.braze.com/app_settings/developer_console/activitylog/). Para enviar mensajes con este punto final, debes tener un [ID de campaña](https://www.braze.com/docs/api/identifier_types/) creado al crear una [campaña desencadenada por la API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `campaigns.trigger.send`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Obligatoria|Cadena|Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Opcional | Cadena | Ver [identificador de envío]({{site.baseurl}}/api/identifier_types/). |
|`trigger_properties`| Opcional | Objeto | Ver [propiedades del desencadenante]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Los pares clave-valor de personalización se aplican a todos los usuarios de esta solicitud. |
|`broadcast`| Opcional | Booleano | Debes establecer`broadcast`  en verdadero cuando envíes un mensaje a todo el segmento configurado como audiencia objetivo de la campaña en el panel de Braze. Este parámetro está predeterminado como falso (a 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
|`audience`| Opcional | Objeto de audiencia conectado| Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). Cuando incluyes `audience`, el mensaje solo se envía a los usuarios que coinciden con los filtros definidos, como los atributos personalizados y los estados de suscripción. |
|`recipients`| Opcional | Matriz | Ver [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/).<br><br>Si `send_to_existing_only` es `false`, debe incluirse un objeto de atributo.<br><br>Si no`recipients` se proporciona y`broadcast`se establece en verdadero, el mensaje se envía a todo el segmento configurado como audiencia objetivo de la campaña en el panel de Braze. <br><br> Si`email`  es el identificador, debes incluir[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email)  en el objeto destinatarios. |
|`attachments`| Opcional | Matriz | Si `broadcast` está configurado como verdadero, no se puede incluir la lista `attachments`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- La matriz de destinatarios puede contener hasta 50 objetos, cada uno de ellos con una única cadena `external_user_id` y un objeto `trigger_properties`.
- Cuando`send_to_existing_only`  es`true`  (el valor predeterminado), Braze envía el mensaje solo a los usuarios existentes. Si el`external_user_id`  no coincide con ningún usuario existente, la API sigue devolviendo una respuesta`201` de éxito, pero el envío se cancela internamente con un resultado de`Unknown External User ID`  y no se genera ningún evento Currents. Cuando se configura en`false`  y se proporciona un objeto de atributos, Braze crea un nuevo usuario si no existe ninguno. Ten en cuenta que la configuración`send_to_existing_only`  a  no`false` es compatible con los alias de usuario; no se pueden crear nuevos usuarios solo con alias a través de este punto final. Para enviar a un usuario que solo tiene un alias de usuario, este debe existir ya en Braze.

El estado del grupo de suscripción de un usuario puede actualizarse mediante la inclusión de un parámetro `subscription_groups` dentro del objeto `attributes`. Para más detalles, consulta [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object).

{% alert note %}
El`segment_id`parámetro no es compatible con este punto final. Para dirigirte a un segmento, configúralo en la configuración de audiencia objetivo de la campaña en el panel de Braze y utiliza `"broadcast": true`, o bien utiliza el`audience`parámetro  con los filtros [de audiencia de Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/).
{% endalert %}

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## Detalles de la respuesta

Las respuestas de los puntos finales de envío de mensajes incluyen el mensaje`dispatch_id`para poder hacer referencia al envío del mensaje. El `dispatch_id` es el ID del envío del mensaje, un ID único para cada transmisión enviada desde Braze. Al utilizar este punto final, recibes un único `dispatch_id` para todo un conjunto de usuarios por lotes. Para más información sobre `dispatch_id`, consulta nuestra documentación sobre [el comportamiento de Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

Si tu solicitud encuentra un error fatal, consulta [Errores y respuestas]({{site.baseurl}}/api/errors/#fatal-errors) para ver el código de error y la descripción.

## Objeto de atribución para campañas

Braze tiene un objeto de mensajería llamado`attributes`  que te permite añadir, crear o actualizar atributos y valores para un usuario antes de enviarle una campaña activada por API. Utiliza el`campaign/trigger/send`  punto final, ya que esta llamada a la API procesa el objeto de atributos de usuario antes de procesar y enviar la campaña. Esto ayuda a minimizar el riesgo de que se produzcan problemas causados por [condiciones de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/).

{% alert tip %}
¿Buscas la versión Canvas de este punto final? Echa un vistazo a [Enviar mensajes Canvas utilizando la entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint).
{% endalert %}

{% endapi %}
