---
nav_title: "PUBLICAR: Añadir correos electrónicos a la lista de bloqueo"
article_title: "PUBLICAR: Añadir correos electrónicos a la lista de bloqueo"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "En este artículo se describen los detalles sobre el punto final Braze de correos electrónicos de la lista negra."

---
{% api %}
# Añadir correos electrónicos a la lista de bloqueo
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Braze ha lanzado el punto final [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/) con la misma funcionalidad que el punto final `/email/blacklist`. Te recomendamos que utilices el punto final `/email/blocklist`.
{% endalert %}

> Utiliza este punto final para dar de baja a un usuario del correo electrónico y marcarlo como rebote duro.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.blacklist`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| -----------|----------| --------|------- |
| `email` | Obligatoria | Cadena o matriz | Cadena de direcciones de correo electrónico a incluir en la lista negra, o una matriz de hasta 50 direcciones de correo electrónico a incluir en la lista negra. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}
