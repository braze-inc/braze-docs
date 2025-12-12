---
nav_title: "GET: Lista centros de preferencia"
article_title: "GET: Lista Centros de Preferencia"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enumerar los centros de preferencias de Braze."

---
{% api %}
# Lista centros de preferencia
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

> Utiliza este punto final para listar tus centros de preferencia disponibles.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dd8f6667-5eba-4e19-a29e-ba74644c0b8e {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `preference_center.list`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 1000 solicitudes por minuto, por espacio de trabajo.

## Ruta y parámetros de la solicitud

No hay parámetros de ruta o solicitud para este punto final.

## Ejemplo de solicitud

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
{
  "preference_centers": [
    {
      "name": "My Preference Center 1",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-17T15:46:10Z",
      "updated_at": "2022-08-17T15:46:10Z"
    },
    {
      "name": "My Preference Center 2",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:13:06Z",
      "updated_at": "2022-08-19T11:13:06Z"
    },
    {
      "name": "My Preference Center 3",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:30:50Z",
      "updated_at": "2022-08-19T11:30:50Z"
    },
    {
      "name": "My Preference Center 4",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-09-13T20:41:34Z",
      "updated_at": "2022-09-13T20:41:34Z"
    }
  ]
}
```

{% endapi %}
