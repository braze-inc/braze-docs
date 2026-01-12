---
nav_title: "PUT: Update translation in a campaign"
article_title: "PUT: Update Translation in a Campaign"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Update translation in a campaign endpoint."
---

{% api %}
# Update translation in a campaign
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> Use this endpoint to update multiple translations for a campaign. See [Locales in messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) for more information about translation features.

If you want to update translations after a campaign has been launched, you'll need to [save your message as a draft]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) first.

{% alert important %}
This endpoint is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `campaigns.translations.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Required | String | The ID of your campaign. |
| `message_variation_id` | Required | String | The ID of your message variation. |
| `locale_id`| Required | String | The ID (UUID) of the locale. |
| `translation_map` | Required | Object | Object containing the new translations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint's response.
{% endalert %}

## Example request

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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
