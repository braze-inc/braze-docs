---
nav_title: "POST: Cancel exports by segment"
article_title: "POST: Cancel exports by segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about Cancel exports by segment Braze endpoint."

---
{% api %}
# Cancel exports by segment
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> Use this endpoint to cancel all ongoing exports with a specified segment ID.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `segments.list` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Required | String | The `segment_id` to cancel its ongoing exports. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}

