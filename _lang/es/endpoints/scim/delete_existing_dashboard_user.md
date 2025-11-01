---
nav_title: "DELETE: Eliminar la cuenta de usuario del panel"
article_title: "DELETE: Eliminar cuenta de usuario del panel de control"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar una cuenta de usuario del panel de Braze."
---

{% api %}
# Eliminar la cuenta de usuario del panel
{% apimethod delete %}
/scim/v2/Usuarios/{id}
{% endapimethod %}

> Utiliza este punto final para eliminar de forma permanente un usuario existente del panel especificando el recurso `id` devuelto por el método SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) . 

Esto es similar a eliminar un usuario en la sección **Usuarios de la empresa** del panel de Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás un token SCIM. Utilizarás el origen de tu servicio como cabecera de `X-Request-Origin`. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning/).

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `id` | Obligatoria | Cadena | ID del recurso del usuario. Este parámetro es devuelto por los métodos `POST` `/scim/v2/Users/` o `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Cuerpo de la solicitud

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Ejemplo de solicitud
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Respuesta

### Ejemplo de respuesta de error

```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```

Si un desarrollador con este ID no existe en Braze, el punto final responderá con lo siguiente:
```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```
{% endapi %}
