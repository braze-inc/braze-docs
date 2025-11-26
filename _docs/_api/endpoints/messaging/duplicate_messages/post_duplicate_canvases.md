---
nav_title: "POST: Duplicate Canvases"
article_title: "POST: Duplicate Canvases"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the Duplicate Canvases endpoint."
---

{% api %}
# Duplicate Canvases using the API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Use this endpoint to duplicate Canvases. This API endpoint is similar to [duplicating Canvases in the Braze dashboard][1].

{% alert important %}
This endpoint is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `canvas.duplicate` permission.

## Rate limit

This endpoint is limited to 100 API calls per minute.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Required | String | See [Canvas identifier](https://www.braze.com/docs/api/identifier_types/). |
|`name`| Required | String | The name of the resulting Canvas. |
|`description`| Optional | String | The description field for the resulting Canvas. |
|`tag_names` | Optional | String | The tags for the resulting Canvas. These must be existing tags. If you add new tags in the request, they will overwrite any tags that were on the original Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Response

This endpoint will return a `202` status code, and the Canvas creation will occur asynchronously. You can use the [Security event download][2] to see records of when Canvases were duplicated and by which API key.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}
