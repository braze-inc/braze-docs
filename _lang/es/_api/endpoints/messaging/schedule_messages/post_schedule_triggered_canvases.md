---
nav_title: "POST: Programar lienzos activados por la API"
article_title: "POST: Programar lienzos activados por la API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Programar Canvas desencadenados por API de Braze."

---
{% api %}
# Programar lienzos activados por la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/create
{% endapimethod %}

> Utilice este punto final para programar mensajes Canvas a través de la entrega activada por API, lo que le permite decidir qué acción debe activar el envío del mensaje.

Puedes pasar `canvas_entry_properties` que será templado en los mensajes enviados por los primeros pasos del Canvas.

Tenga en cuenta que para enviar mensajes con este punto final, debe tener un [ID de lienzo]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier), creado cuando construye un lienzo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.trigger.schedule.create`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the
  // Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Obligatoria|Cadena| Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Opcional | Matriz de objetos destinatarios | Ver [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Opcional | Objeto de audiencia conectado | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Opcional | Booleano | Debes establecer `broadcast` en verdadero cuando envíes un mensaje a un segmento completo al que se dirige una campaña o Canvas. Este parámetro está predeterminado como falso (a 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
| `canvas_entry_properties` | Opcional | Objeto | Pares clave-valor de personalización para todos los usuarios de este envío. Ver [objeto Propiedades de entrada de lienzo]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object). |
| `schedule` | Obligatoria | Objeto de programación | Ver [objeto de programación]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties": {}
    }
  ],
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
  "broadcast": false,
  "canvas_entry_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Respuesta

### Ejemplo de respuesta satisfactoria

```
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}
