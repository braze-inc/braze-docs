---
nav_title: "PUT: Update translation in a Content Block"
article_title: "PUT: Update Translation in a Content Block"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the Update translation in a Content Block endpoint."
---

{% api %}
# Update translation in a Content Block
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Use this endpoint to update multiple translations for a [Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/). See [Locales in messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) for more information about translation features.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `content_blocks.translations.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Required | String | The ID of your Content Block. |
| `locale_id`| Required | String | The ID (UUID) of the locale. |
| `translation_map` | Required | Object | Object containing the new translations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint's response.
{% endalert %}

## Example request

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
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
