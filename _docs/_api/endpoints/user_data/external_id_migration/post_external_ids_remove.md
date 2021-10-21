---
nav_title: "POST: External ID Remove"
article_title: "POST: External ID Remove"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the external IDs Remove endpoint."

---
{% api %}
# External id remove
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

{% alert note %}
For security purposes, this feature is disabled by default. To enable this feature, please reach out to your Success Manager.
{% endalert %}

Use this endpoint to remove your users' old deprecated external IDs. This endpoint completely removes the deprecated ID and cannot be undone.

You can send up to 50 external IDs per request.

You will need to create a new [API key]({{site.baseurl}}/api/api_key/) with permissions for this endpoint.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

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
  "external_ids" : 
    [
      "existing_deprecated_external_id_string",
      ...
    ]
}'
```
{% alert important %}
Only deprecated IDs can be removed; attempting to remove a primary external ID will result in an error.
{% endalert %}

## Response 
the response will confirm all successful removals, as well as unsuccessful removals with the associated errors. error messages in the `removal_errors` field will reference the index in the array of the original request.

```
{

  "message" : (string) status message,
  "removed_ids" : (array of successful Remove Operations),
  "removal_errors": (array of any <minor error message>)

}
```

The `message` field will return `success` for any valid request. More specific errors are captured in the `removal_errors` array. The `message` field returns an error in the case of:
- Invalid API key
- Empty `external_ids` array
- `external_ids` array with more than 50 items
- Rate limit hit (>1,000 requests/minute)

{% endapi %}
