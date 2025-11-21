---
nav_title: "PUT: Set primary SDK authentication key"
article_title: "PUT: Set Primary SDK Authentication Key"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the Set primary SDK Authentication key Braze endpoint."
---

{% api %}
# Set primary SDK Authentication key
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> Use this endpoint to set an SDK Authentication key as the primary key for your app.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `sdk_authentication.primary` permission.

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
  "key_id": "key id"
}
```

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Required | String | The app API identifier. |
| `key_id` | Required | String | The ID of the SDK Authentication key to mark as primary. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
```

## Response
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

## Response parameters

| Parameter | Data type | Description |
| --------- | --------- | ----------- |
| `keys` | Array | Array of all SDK Authentication key objects. |
| `keys[].id` | String | The ID of the SDK Authentication key. |
| `keys[].rsa_public_key` | String | The RSA public key string. |
| `keys[].description` | String | Description of the SDK Authentication key. |
| `keys[].is_primary` | Boolean | Whether this key is the primary SDK Authentication key. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Validation rules

This endpoint has the following validation rules:

- The `key_id` must be a valid SDK Authentication key ID.
- The `app_id` must be a valid app API identifier.
- The SDK Authentication key must exist for the specified app.

{% endapi %}
