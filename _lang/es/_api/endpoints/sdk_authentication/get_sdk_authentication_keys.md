---
nav_title: "GET: Lista de claves de autenticación SDK"
article_title: "GET: Lista de claves de autenticación SDK"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto final Braze de las claves de autenticación del SDK de listas."
---

{% api %}
# Lista de claves de autenticación SDK
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> Utiliza este punto final para recuperar todas las claves de autenticación SDK de tu aplicación.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `sdk_authentication.keys`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatoria | Cadena | El identificador de la API de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```json
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
| `keys` | Matriz | Matriz de objetos clave de autenticación SDK. |
| `keys[].id` | Cadena | El ID de la clave de autenticación SDK. |
| `keys[].rsa_public_key` | Cadena | La cadena de clave pública RSA. |
| `keys[].description` | Cadena | Descripción de la clave de autenticación SDK. |
| `keys[].is_primary` | Booleano | Si esta clave es la clave principal de autenticación SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Reglas de validación

Este punto final tiene las siguientes reglas de validación:

- El parámetro `app_id` debe ser un identificador de API de aplicación válido.
- La aplicación debe existir en tu espacio de trabajo.

{% endapi %}
