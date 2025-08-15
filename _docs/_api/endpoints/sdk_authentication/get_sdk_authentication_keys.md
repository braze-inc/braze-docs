---
nav_title: "GET: List SDK authentication keys"
article_title: "GET: List SDK Authentication Keys"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the List SDK Authentication keys Braze endpoint."
---

{% api %}
# List SDK Authentication keys
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> Use this endpoint to retrieve all SDK Authentication keys for your app.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `sdk_authentication.keys` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Required | String | The app API identifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```json
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
| `keys` | Array | Array of SDK Authentication key objects. |
| `keys[].id` | String | The ID of the SDK Authentication key. |
| `keys[].rsa_public_key` | String | The RSA public key string. |
| `keys[].description` | String | Description of the SDK Authentication key. |
| `keys[].is_primary` | Boolean | Whether this key is the primary SDK Authentication key. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Validation rules

This endpoint has the following validation rules:

- The `app_id` parameter must be a valid app API identifier.
- The app must exist in your workspace.

{% endapi %}
