---
nav_title: "PUBLICAR: Eliminar direcciones de correo electrónico de la lista de correo no deseado"
article_title: "PUBLICAR: Eliminar direcciones de correo electrónico de la lista de correo no deseado"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto final Eliminar direcciones de correo electrónico de la lista de correo no deseado Braze."

---
{% api %}
# Eliminar direcciones de correo electrónico de la lista de correo no deseado
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Utiliza este punto final para eliminar direcciones de correo electrónico de tu lista de correo no deseado de Braze y de la lista de correo no deseado mantenida por tu proveedor de correo electrónico.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.spam.remove`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| ----------|-----------| --------|------- |
| `email` | Obligatoria | Cadena o matriz | Cadena de direcciones de correo electrónico a modificar, o una matriz de hasta 50 direcciones de correo electrónico a modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
