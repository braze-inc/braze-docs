---
nav_title: "PUBLICAR: Borrar campañas programadas desencadenadas por la API"
article_title: "PUBLICAR: Eliminar campañas programadas desencadenadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar campañas programadas desencadenadas por API de Braze."

---
{% api %}
# Borrar campañas programadas desencadenadas por la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> Utiliza este punto final para cancelar un mensaje Canvas que hayas programado previamente a través de la API antes de que se haya enviado.

Los mensajes programados o desencadenados que se borren muy cerca de la hora a la que debían enviarse, o durante la misma, se actualizarán con los mejores esfuerzos, por lo que los borrados de último segundo podrían aplicarse a todos, a algunos o a ninguno de tus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.trigger.schedule.delete`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id`| Obligatoria | Cadena | Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Obligatoria | Cadena | El `schedule_id` a borrar (obtenido de la respuesta a crear horario). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
