---
nav_title: "Delete SDK Authentication Key"
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the Delete SDK Authentication Key Braze endpoint."
platform: API
---

# Delete SDK Authentication Key

{% apimethod delete %}
/app_group/sdk_auth_key/delete
{% endapimethod %}

Delete an SDK Authentication key.

{% alert warning %}
You cannot delete the primary key. If you attempt to delete the primary key, this endpoint will return an error.
{% endalert %}

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
| `key_id` | Required | String | The ID of the SDK Authentication key to delete. |

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
| `keys` | Array | Array of remaining SDK Authentication key objects. |
| `keys[].id` | String | The ID of the SDK Authentication key. |
| `keys[].rsa_public_key` | String | The RSA public key string. |
| `keys[].description` | String | Description of the SDK Authentication key. |