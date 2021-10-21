---
nav_title: "GET: List Available Content Blocks"
article_title: "GET: List Available Content Blocks"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the List Available Content Blocks Braze endpoint."

---
{% api %}
# List available content blocks
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

This endpoint will list you existing [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) information.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `modified_after`  | Optional | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | Retrieve only content blocks updated at or after the given time. |
| `modified_before`  |  Optional | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | Retrieve only content blocks updated at or before the given time. |
| `limit` | Optional | Positive Number | Maximum number of content blocks to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. |
| `offset`  |  Optional | Positive Number | Number of content blocks to skip before returning rest of the templates that fit the search criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": "string",
      "name": "string",
      "content_type": "html or text",
      "liquid_tag": "string",
      "inclusion_count" : "integer",
      "created_at": "time-in-iso",
      "last_edited": "time-in-iso",
      "tags" : "array of strings"
    }
  ]
}
```

### Possible errors
- `Modified after time is invalid.` - The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).

- `Modified before time is invalid.` - The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).

- `Modified after time must be earlier than or the same as modified before time.`

- `Content Block number limit is invalid.` - The `limit` parameter must be an integer (positive number) greater than 0.

- `Content Block number limit must be greater than 0.` - The `limit` parameter must be an integer (positive number) greater than 0.

- `Content Block number limit exceeds maximum of 1000.` - The `limit` parameter must be an integer (positive number) greater than 0.

- `Offset is invalid.` - The `offset` parameter must be an integer (positive number) greater than 0.

- `Offset must be greater than 0.` - The `offset` parameter must be an integer (positive number) greater than 0.

{% endapi %}
