---
nav_title: "Mark SDK Authentication Key as Primary"
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the Mark SDK Authentication Key as Primary Braze endpoint."
platform: API
---

# Mark SDK Authentication Key as Primary

{% apimethod put %}
/app_group/sdk_auth_key/primary
{% endapimethod %}

Mark an SDK Authentication key as the primary key.

## Request Body

```json
{
  "app_id": "App API key",
  "key_id": "key id"
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `app_id` | Required | String | The App API Identifier. |
| `key_id` | Required | String | The ID of the SDK Authentication key to mark as primary. |

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
| `keys` | Array | Array of all SDK Authentication key objects. |
| `keys[].id` | String | The ID of the SDK Authentication key. |
| `keys[].rsa_public_key` | String | The RSA public key string. |
| `keys[].description` | String | Description of the SDK Authentication key. |