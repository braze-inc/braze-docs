---
nav_title: "PUBLICAR: Crear mensajes programados"
article_title: "PUBLICAR: Crear mensajes programados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear mensajes programados de Braze."

---
{% api %}
# Crear mensajes programados
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> Utiliza este punto final para programar el envío de una campaña, Canvas u otro mensaje a una hora determinada, y te proporciona un identificador para hacer referencia a ese mensaje en las actualizaciones.

Si te diriges a un segmento, se almacenará un registro de tu solicitud en la [Consola para desarrolladores](https://dashboard.braze.com/app_settings/developer_console/activitylog/) después de que se hayan enviado todos los mensajes programados.

{% alert tip %}
Si te interesa enviar mensajes inmediatamente a usuarios designados, utiliza en su lugar el [punto final`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `messages.schedule.create`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Opcional | Booleano | Debes establecer `broadcast` en verdadero cuando envíes un mensaje a un segmento completo al que se dirige una campaña o Canvas. Este parámetro está predeterminado en `false`. <br><br> Si `broadcast` está configurado como `true`, no se puede incluir una lista de destinatarios. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
| `external_user_ids` | Opcional | Matriz de cadenas | Ver [identificador de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Opcional | Matriz de objetos alias de usuario | Ver [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Opcional | Objeto de audiencia conectado | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Opcional | Cadena | Ver [identificador de segmento]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Opcional|Cadena| Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Opcional | Cadena | Ver [identificador de envío]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Opcional | Booleano | Ignora la limitación de frecuencia para las campañas, predeterminado a falso |
|`recipient_subscription_state`| Opcional | Cadena | Utiliza esta opción para enviar mensajes solo a los usuarios que se hayan adherido voluntariamente (`opted_in`), solo a los usuarios que se hayan suscrito o estén adheridos voluntariamente (`subscribed`) o a todos los usuarios, incluidos los que hayan cancelado la suscripción (`all`). <br><br>El uso de `all` usuarios es útil para la mensajería transaccional por correo electrónico. De forma predeterminada, `subscribed`. |
| `schedule` | Obligatoria | Objeto de programación | Ver [objeto de programación]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Opcional | Objeto de mensajería | Consulta [los objetos de mensajería disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## Respuesta

### Ejemplo de respuesta satisfactoria

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}
