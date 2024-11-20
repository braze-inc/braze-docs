---
nav_title: "POST: Actualización de campañas programadas activadas por API"
article_title: "POST: Actualización de campañas programadas activadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "En este artículo se describen los detalles del punto final Actualizar campañas programadas desencadenadas por API de Braze."

---
{% api %}
# Actualización de campañas programadas activadas por API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Utilice este punto final para actualizar las campañas programadas activadas por API creadas en el panel de control, permitiéndole decidir qué acción debe activar el envío del mensaje.

Puede introducir `trigger_properties`, que se incluirá como plantilla en el propio mensaje.

Tenga en cuenta que para enviar mensajes con este punto final, debe tener un ID de campaña, creado al crear una [campaña activada por API]({{site.baseurl}}/api/api_campaigns/).

Cualquier horario sobrescribirá completamente el que haya proporcionado en la solicitud de creación de horario o en anteriores solicitudes de actualización de horario. Por ejemplo, si originalmente proporciona `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` y luego en su actualización proporciona `"schedule" : {"time" : "2015-02-20T14:14:47"}`, su mensaje ahora se enviará a la hora proporcionada en UTC, no en la hora local del usuario. Los desencadenantes programados que se actualicen muy cerca de la hora a la que debían enviarse, o durante la misma, se actualizarán con el máximo esfuerzo, por lo que los cambios de último segundo podrían aplicarse a todos, a algunos o a ninguno de sus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.trigger.schedule.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Obligatoria|Cadena| Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/)|
| `schedule_id` | Obligatoria | Cadena | El `schedule_id` a actualizar (obtenido de la respuesta para crear un horario). |
|`schedule` | Obligatoria | Objeto | Ver [objeto de programación]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
