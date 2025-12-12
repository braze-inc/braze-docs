---
nav_title: "DELETE: Eliminar la clave de autenticación SDK"
article_title: "DELETE: Eliminar la clave de autenticación SDK"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles sobre el punto final Braze de la clave de autenticación del SDK."
---

{% api %}
# Borrar clave de autenticación SDK
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> Utiliza este punto final para eliminar una clave de autenticación SDK para tu aplicación.

{% alert important %}
La clave primaria no se puede borrar. Si intentas borrar la clave primaria, este punto final devolverá un error.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `sdk_authentication.delete`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatoria | Cadena | El identificador de la API de la aplicación. |
| `key_id` | Obligatoria | Cadena | El ID de la clave de autenticación SDK que hay que borrar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
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
    }
  ]
}
```

## Parámetros de respuesta

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `keys` | Matriz | Conjunto de objetos clave de autenticación SDK restantes. |
| `keys[].id` | Cadena | El ID de la clave de autenticación SDK. |
| `keys[].rsa_public_key` | Cadena | La cadena de clave pública RSA. |
| `keys[].description` | Cadena | Descripción de la clave de autenticación SDK. |
| `keys[].is_primary` | Booleano | Si esta clave es la clave principal de autenticación SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Reglas de validación

Este punto final tiene las siguientes reglas de validación:

- El `key_id` debe ser un ID de clave de autenticación SDK válido.
- El `app_id` debe ser un identificador de API de aplicación válido.
- La clave de autenticación SDK debe existir para la aplicación especificada.
- La clave de autenticación SDK primaria no se puede borrar.

{% endapi %}
