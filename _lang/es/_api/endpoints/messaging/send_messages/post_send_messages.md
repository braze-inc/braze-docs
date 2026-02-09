---
nav_title: "PUBLICAR: Envía mensajes inmediatamente utilizando sólo la API"
article_title: "PUBLICAR: Envía mensajes inmediatamente utilizando sólo la API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el punto final Enviar mensajes inmediatamente utilizando sólo la API de Braze."

---
{% api %}
# Envía mensajes inmediatamente utilizando sólo la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> Utiliza este punto final para enviar mensajes inmediatos a usuarios designados utilizando la API Braze.

Si te estás dirigiendo a un segmento específico, se almacenará un registro de tu solicitud en la [consola para desarrolladores](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% multi_lang_include api/payload_size_alert.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `messages.send`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Cuerpo de la solicitud

{% alert tip %}
Asegúrate de incluir [objetos de mensajería]({{site.baseurl}}/api/objects_filters/#messaging-objects) en tu cuerpo para completar tus peticiones.
{% endalert %}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Opcional | Booleano | Debes establecer `broadcast` en verdadero cuando envíes un mensaje a un segmento completo al que se dirige una campaña o Canvas. Este parámetro está predeterminado como falso (a 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
|`external_user_ids` | Opcional | Matriz de cadenas | Ver [ID de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Opcional | Matriz de objetos alias de usuario| Ver [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Opcional | Cadena | Ver [identificador de segmento]({{site.baseurl}}/api/identifier_types/#segment-identifier). |
|`audience`| Opcional | Objeto de audiencia conectado | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Opcional\*. | Cadena | Consulte [el identificador de campaña]({{site.baseurl}}/api/identifier_types/#campaign-identifier/) para obtener más información. <br><br>\*Requerido si deseas hacer un seguimiento de las métricas de la campaña (como _Envíos_, _Clics_ o _Rebotes_) en el panel de Braze. |
|`send_id`| Opcional | Cadena | Ver [identificador de envío]({{site.baseurl}}/api/identifier_types/#send-identifier). |
|`override_frequency_capping`| Opcional | Booleano | Ignore `frequency_capping` para las campañas, por defecto `false`. |
|`recipient_subscription_state`| Opcional | Cadena | Utiliza esta opción para enviar mensajes solo a los usuarios que se hayan adherido voluntariamente (`opted_in`), solo a los usuarios que se hayan suscrito o estén adheridos voluntariamente (`subscribed`) o a todos los usuarios, incluidos los que hayan cancelado la suscripción (`all`). <br><br>El uso de `all` usuarios es útil para la mensajería transaccional por correo electrónico. De forma predeterminada, `subscribed`. |
|`messages`| Opcional | Objetos de mensajería | Consulte [los objetos de mensajería disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## Detalles de la respuesta

Las respuestas de los puntos finales de envío de mensajes incluirán la dirección `dispatch_id` del mensaje como referencia para el envío del mensaje. `dispatch_id` es el ID del envío del mensaje, es decir, el ID único para cada "transmisión" enviada desde Braze. Para más información, consulta [Comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}
