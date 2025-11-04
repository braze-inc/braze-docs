---
nav_title: "GET: Generar URL del centro de preferencias"
article_title: "GET: Generar URL del Centro de preferencias"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Generar URL del centro de preferencias de Braze."

---
{% api %}
# Generar URL del centro de preferencias
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Utilice este punto final para generar una URL para un centro de preferencias.

La URL de cada centro de preferencias es única para cada usuario.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `preference_center.user.get`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 1000 solicitudes por minuto, por espacio de trabajo.

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Obligatoria | Cadena | El ID de su centro de preferencias. |
|`userID`| Obligatoria | Cadena | El ID del usuario. |
{:  role="presentation" }

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| Obligatoria | Cadena | El ID de su centro de preferencias. |
|`external_id`| Obligatoria | Cadena | El ID externo de un usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
Este punto final sólo genera URL para el nuevo centro de preferencias (como los centros de preferencias creados mediante nuestra API o el editor de arrastrar y soltar).
{% endalert %}
