---
nav_title: "PUBLICAR: Actualizar lienzos programados desencadenados por la API"
article_title: "PUBLICAR: Actualizar lienzos programados desencadenados por la API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar Canvas desencadenados por API programados de Braze."

---
{% api %}
# Actualizar lienzos programados desencadenados por la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Utiliza este punto final para actualizar los Lienzos programados desencadenados por la API que se crearon en el panel.

Esto te permite decidir qué acción debe desencadenar el envío del mensaje. Puedes introducir `trigger_properties`, que se incluirá como plantilla en el propio mensaje.

Ten en cuenta que para enviar mensajes con este punto final, debes tener un ID de Canvas, creado cuando construyes un [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Cualquier horario sobrescribirá completamente el que hayas proporcionado en la solicitud de crear horario o en anteriores solicitudes de actualizar horario.
  - Por ejemplo, si originalmente proporciona `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` y luego en su actualización proporciona `"schedule" : {"time" : "2015-02-20T14:14:47"}`, su mensaje ahora se enviará a la hora proporcionada en UTC, no en la hora local del usuario.
  - Los desencadenantes programados que se actualicen muy cerca de la hora a la que debían enviarse, o durante la misma, se actualizarán con el máximo esfuerzo, por lo que los cambios de último segundo podrían aplicarse a todos, a algunos o a ninguno de sus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.trigger.schedule.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Obligatoria|Cadena| Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Opcional | Cadena | El `schedule_id` para actualizar (obtenido de la respuesta para crear horario). |
|`schedule` | Obligatoria | Objeto | Ver [objeto de programación]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
