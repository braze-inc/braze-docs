---
nav_title: "Get SDK Authentication Keys"
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the Get SDK Authentication Keys Braze endpoint."
platform: API
---

# Get SDK Authentication Keys

{% apimethod get %}
/app_group/sdk_auth_keys?app_id=App_API_Key
{% endapimethod %}

Get all SDK Authentication keys for your app.

## Request Parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `app_id` | Required | String | The App API Identifier. |

## Response

```json
{
  "keys": [
    {
      "id": "key id",
      "rsa_public_key": "RSA public key string",
      "description": "description"
    },
    ...
  ]
}
```

### Response Parameters

| Parameter | Data Type | Description |
| --- | --- | --- |
| `keys` | Array | Array of SDK Authentication key objects. |
| `keys[].id` | String | The ID of the SDK Authentication key. |
| `keys[].rsa_public_key` | String | The RSA public key string. |
| `keys[].description` | String | Description of the SDK Authentication key. |