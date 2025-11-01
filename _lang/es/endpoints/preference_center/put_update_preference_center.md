---
nav_title: "COLOCAR: Actualizar el centro de preferencias"
article_title: "COLOCAR: Actualizar el Centro de Preferencias"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar un centro de preferencias de Braze."

---
{% api %}
# Actualizar el centro de preferencias
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Utiliza este punto final para actualizar un centro de preferencias.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `preference_center.update`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 10 solicitudes por minuto, por espacio de trabajo.

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Obligatoria | Cadena | El ID de su centro de preferencias. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "unknown macro": {links-tags}
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
    "links-tags": [
      {
        "rel": "string", (required) One of: "icon", "shortcut icon", or "apple-touch-icon",
        "type": "string", (optional) Valid values: "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
        "sizes": "string", (optional),
        "color": "string", (optional) Use when type="mask-icon",
        "href": "string", (required)
      }
    ]
  }
} 
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| Obligatoria | Cadena | El HTML de la página del centro de preferencias. |
|`preference_center_title`| Opcional | Cadena | El título para el centro de preferencias y las páginas de confirmación. Si no se especifica un título, el título de las páginas será predeterminado "Centro de preferencias". |
|`confirmation_page_html`| Obligatoria | Cadena | El HTML de la página de confirmación. |
|`state` | Opcional | Cadena | Elige `active` o `draft`.|
|`options` | Opcional | Objeto | Atributos: <br>`meta-viewport-content`: Cuando esté presente, se añadirá una metaetiqueta `viewport` a la página con `content= <value of attribute>`.<br><br> `link-tags`: Establece un favicon para la página. Cuando se establece, se añade a la página una etiqueta `<link>` con un atributo rel.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
```
{% endraw %}

## Ejemplo de respuesta
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
