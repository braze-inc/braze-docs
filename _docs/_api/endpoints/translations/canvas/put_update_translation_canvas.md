---
nav_title: "PUT: Update translation in a Canvas"
article_title: "PUT: Update Translation in a Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Update translation in a Canvas endpoint."
---

{% api %}
# Update translation in a Canvas
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Use this endpoint to update multiple translations for a Canvas.

If you want to update translations after a Canvas has been launched, you'll need to [save your message as a draft]({{site.baseurl}}/post-launch_edits/) first.

{% alert important %}
This endpoint is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.translations.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Required | String | The ID of the Canvas. |
|`step_id`| Required | String | The ID of your Canvas step. |
|`message_variation_id`| Required | String | The ID of your message variation. |
|`locale_id`| Required | String | The ID (UUID) of the locale. |
|`translation_map` | Required | Object | Object containing the new translations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint's response.
{% endalert %}

## Example request

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

### Example success response

```json
{
	"message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
	"errors": [
		{
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}
