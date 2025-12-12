---
nav_title: "GET: Ver detalles del centro de preferencias"
article_title: "GET: Ver detalles de Centro de Preferencia"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Ver detalles del centro de preferencias de Braze."

---
{% api %}
# Ver detalles del centro de preferencias
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Utiliza este punto final para ver los detalles de tus centros de preferencias, incluyendo cuándo se crearon y actualizaron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `preference_center.get`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 1000 solicitudes por minuto, por espacio de trabajo.

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Obligatoria | Cadena | El ID de su centro de preferencias. |
{: role="presentation" }

## Parámetros de la solicitud

No hay parámetros de solicitud para este punto final.

## Ejemplo de solicitud

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta
```json
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=2"
  },
  "state": "active"
}
```

{% endapi %}
