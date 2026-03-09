---
nav_title: "COLOCAR: Establecer la clave de autenticación SDK principal"
article_title: "COLOCAR: Establecer clave de autenticación SDK principal"
search_tag: Punto de conexión
page_order: 2
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto final SDK de Braze para establecer la clave de autenticación del SDK principal."
---

{% api %}
# Establecer la clave de autenticación del SDK principal
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> Utiliza este punto final SDK para establecer una clave de autenticación SDK como clave principal para tu aplicación.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `sdk_authentication.primary`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "key_id": "key id"
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatoria | Cadena | El identificador API de la aplicación. |
| `key_id` | Obligatoria | Cadena | El ID de la clave de autenticación del SDK que se va a marcar como principal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
```

## Respuesta
```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## Parámetros de respuesta

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `keys` | Matriz | Matriz de todos los objetos de clave de autenticación SDK. |
| `keys[].id` | Cadena | El ID de la clave de autenticación del SDK. |
| `keys[].rsa_public_key` | Cadena | La cadena de clave pública RSA. |
| `keys[].description` | Cadena | Descripción de la clave de autenticación del SDK. |
| `keys[].is_primary` | Booleano | Si esta clave es la clave de autenticación SDK principal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Reglas de validación

Este punto final tiene las siguientes reglas de validación:

- Debe`key_id` ser un ID de clave de autenticación SDK válido.
- Debe ser un identificador`app_id` API válido de la aplicación.
- La clave de autenticación SDK debe existir para la aplicación especificada.

{% endapi %}
