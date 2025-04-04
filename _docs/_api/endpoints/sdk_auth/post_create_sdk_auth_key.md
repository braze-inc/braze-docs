---
nav_title: "Create SDK Authentication Key"
page_order: 0
layout: api_page
page_type: reference
description: "This article outlines details about the Create SDK Authentication Key Braze endpoint."
platform: API
---

# Create SDK Authentication Key

{% apimethod post %}
/app_group/sdk_auth_key/create
{% endapimethod %}

Create a new SDK Authentication key for your app.

This endpoint will return an error if you have more than 3 keys or try to create a duplicate key.

## Request Body

```json
{
  "app_id": "App API key",
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `app_id` | Required | String | The App API Identifier. |
| `rsa_public_key_str` | Required | String | The RSA public key string. Must be a valid RSA public key or it will return an error. |
| `description` | Required | String | Description for the SDK Authentication key. |
| `make_primary` | Optional | Boolean | If set to true, this key will be made the primary SDK Authentication key when it is created. |

## Response

```json
{
  "id": "key id"
}
```

### Response Parameters

| Parameter | Data Type | Description |
| --- | --- | --- |
| `id` | String | The ID of the newly created SDK Authentication key. |