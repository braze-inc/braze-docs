---
nav_title: "GET: List available content blocks"
article_title: "GET: List Available Content Blocks"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the List available Content Blocks Braze endpoint."

---
{% api %}
# List available Content Blocks
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> Use this endpoint to list your existing [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) information.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Prerequisites
To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `content_blocks.list` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `modified_after`  | Optional | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | Retrieve only Content Blocks updated at or after the given time. |
| `modified_before`  |  Optional | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | Retrieve only Content Blocks updated at or before the given time. |
| `limit` | Optional | Positive Number | Maximum number of Content Blocks to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. |
| `offset`  |  Optional | Positive Number | Number of Content Blocks to skip before returning rest of the templates that fit the search criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

```json
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `Modified after time is invalid` | The provided date is not a valid or parsable date. Reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | The provided date is not a valid or parsable date. Reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | Change the `modified_after` value to a time that is earlier than the `modified_before` time. |
| `Content Block number limit is invalid` | The `limit` parameter must be an integer (positive number) greater than 0. |
| `Content Block number limit must be greater than 0` | Change the `limit` parameter to an integer greater than 0. |
| `Content Block number limit exceeds maximum of 1000` | Change the `limit` parameter to an integer less than 1000. |
| `Offset is invalid` | The `offset` parameter must be an integer greater than 0. |
| Offset must be greater than 0 | Change the `offset` parameter to an integer greater than 0. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
