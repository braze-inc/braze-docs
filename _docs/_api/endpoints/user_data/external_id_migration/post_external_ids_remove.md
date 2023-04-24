---
nav_title: "POST: Remove External ID"
article_title: "POST: Remove External ID"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the external IDs Remove endpoint."

---
{% api %}
# Remove external ID
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

Use this endpoint to remove your users' old deprecated external IDs. This endpoint completely removes the deprecated ID and cannot be undone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

{% alert warning %}
This endpoint completely removes the deprecated ID and cannot be undone. Using this endpoint to remove deprecated `external_ids` that are still associated with users in your system can permanently prevent you from finding those users' data.
{% endalert %}

You can send up to 50 external IDs per request.

You will need to create a new [API key]({{site.baseurl}}/api/api_key/) with permissions for this endpoint.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Required | Array of strings | External identifiers for the users to remove. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request example
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```
{% alert important %}
Only deprecated IDs can be removed; attempting to remove a primary external ID will result in an error.
{% endalert %}

## Response 
The response will confirm all successful removals, as well as unsuccessful removals with the associated errors. Error messages in the `removal_errors` field will reference the index in the array of the original request.

```
{
  "message" : (string) status message,
  "removed_ids" : (array) successful remove operations,
  "removal_errors": (array) <minor error message>
}
```

The `message` field will return `success` for any valid request. More specific errors are captured in the `removal_errors` array. The `message` field returns an error in the case of:
- Invalid API key
- Empty `external_ids` array
- `external_ids` array with more than 50 items
- Rate limit hit (>1,000 requests/minute)

{% endapi %}
