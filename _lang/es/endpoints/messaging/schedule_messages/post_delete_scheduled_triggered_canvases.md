---
nav_title: "PUBLICAR: Borrar Lienzos programados desencadenados por la API"
article_title: "PUBLICAR: Eliminar Canvas programados desencadenados por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar Canvas programados desencadenados por API de Braze."

---
{% api %}
# Borrar Lienzos programados desencadenados por la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> El punto final para eliminar la programación te permite cancelar un mensaje que hayas programado antes a través de Canvas desencadenados por API antes de que se haya enviado.

Los mensajes programados o desencadenados que se borren muy cerca de la hora a la que debían enviarse, o durante la misma, se actualizarán con los mejores esfuerzos, por lo que los borrados de último segundo podrían aplicarse a todos, a algunos o a ninguno de tus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.trigger.schedule.delete`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| Obligatoria | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Obligatoria | Cadena | El `schedule_id` a borrar (obtenido de la respuesta a crear horario). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
