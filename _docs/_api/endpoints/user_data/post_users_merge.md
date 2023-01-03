---
nav_title: "POST: Users Merge"
article_title: "POST: Users Merge"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Users Merge Braze endpoint."

---
{% api %}
# Users Merge
{% apimethod post %}
/users/merge
{% endapimethod %}

Use this endpoint to merge one user into another user. Up to 50 merges may be specified per request. This endpoint is asynchronous.


## Rate limit

{% multi_lang_include rate_limits.md endpoint='users merge' %}


## Request parameters

| Parameter | Required | Data Type | Description                                                                                                                                                                                                                                                   |
|---|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `merge_updates` | Required | Array | An object array. Each object should contain an `identifier_to_merge` object and an `identifier_to_keep` object, which should each reference a user either by `external_id` or `user_alias`. Both users being merged must be identified using the same method. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example Request

```
curl --location --request POST 'https://rest.iad-03.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

## Response

There are two status code responses for this endpoint: `202` and `400`.

### Example success response

The status code `202` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Troubleshooting

The following table lists possible error messages that may occur.

| Message |
| --- |
| 'merge_updates' must be an array of objects |
| a single request may not contain more than 50 merge updates |
| identifiers must be objects with an 'external_id' property that is a string, or 'user_alias' property that is an object |
| identifiers must be objects of the same type" |
| 'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep' |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
