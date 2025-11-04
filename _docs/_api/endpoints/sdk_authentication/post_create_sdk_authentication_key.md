---
nav_title: "POST: Create SDK authentication key"
article_title: "POST: Create SDK Authentication Key"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "This article outlines details about the Create SDK Authentication key Braze endpoint."
---

{% api %}
# Create SDK Authentication key
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> Use this endpoint to create a new SDK Authentication key for your app.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `sdk_authentication.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body
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

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Required | String | The app API identifier. |
| `rsa_public_key_str` | Required | String | The RSA public key string. Must be a valid RSA public key or it will return an error. |
| `description` | Required | String | Description for the SDK Authentication key. |
| `make_primary` | Optional | Boolean | If set to `true`, this key will be made the primary SDK Authentication key when it is created. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

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

## Response
```json
{
  "id": "key id"
}
```

## Response parameters

| Parameter | Data type | Description |
| --------- | --------- | ----------- |
| `id` | String | The ID of the newly created SDK Authentication key. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Validation rules

This endpoint has the following validation rules:

- You can have up to 3 SDK Authentication keys per app.
- The RSA public key string must be a valid RSA public key in the proper format.
- The `app_id` must be a valid app API identifier.
- The description cannot be empty.

{% endapi %}
