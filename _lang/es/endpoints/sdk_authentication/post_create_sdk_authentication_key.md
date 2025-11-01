---
nav_title: "PUBLICAR: Crear clave de autenticación SDK"
article_title: "PUBLICAR: Crear clave de autenticación SDK"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto final Braze Crear clave de autenticación SDK."
---

{% api %}
# Crear clave de autenticación SDK
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> Utiliza este punto final para crear una nueva clave de autenticación SDK para tu aplicación.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `sdk_authentication.create`.

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
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatoria | Cadena | El identificador de la API de la aplicación. |
| `rsa_public_key_str` | Obligatoria | Cadena | La cadena de clave pública RSA. Debe ser una clave pública RSA válida o devolverá un error. |
| `description` | Obligatoria | Cadena | Descripción de la clave de autenticación SDK. |
| `make_primary` | Opcional | Booleano | Si se establece en `true`, esta clave se convertirá en la clave principal de autenticación SDK cuando se cree. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```json
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----", 
  "description": "SDK Authentication Key for iOS App", 
  "make_primary": false
}'
```

## Respuesta
```json
{
  "id": "key id"
}
```

## Parámetros de respuesta

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `id` | Cadena | El ID de la clave de autenticación SDK recién creada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Reglas de validación

Este punto final tiene las siguientes reglas de validación:

- Puedes tener hasta 3 claves de autenticación SDK por aplicación.
- La cadena de clave pública RSA debe ser una clave pública RSA válida en el formato adecuado.
- El `app_id` debe ser un identificador de API de aplicación válido.
- La descripción no puede estar vacía.

{% endapi %}
