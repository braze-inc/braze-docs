---
nav_title: "GET: View default source values for Canvas translation tags"
article_title: "GET: View default source values for Canvas translation tags"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the Canvas translation source endpoint."
---

{% api %}
# View default source values for a canvas's translation tags
{% apimethod get %}
/canvas/translations/source
{% endapimethod %}

> Use this endpoint to view all the default translation sources for a canvas's translation tags. These are the values with the {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. See [Locales in messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) for more information about translation features.

{% alert important %}
This endpoint is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.translations.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Query parameters

| Parameter              | Required | Data Type | Description                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | Required | String    | The ID of the Canvas.              |
| `step_id`              | Required | String    | The ID of your Canvas step.        |
|`message_variation_id`| Required | String | The ID of your message variation. |
| `locale_id`            | Optional | String    | The ID (UUID) of the locale.              |
| `post_launch_draft_version`| Optional | Boolean | When `true` returns the latest draft version instead of the latest live published version. Defaults to `false` returning the latest live version.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint's response.
{% endalert %}

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

### Example success response

The status code `200` could return the following response header and body.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}
