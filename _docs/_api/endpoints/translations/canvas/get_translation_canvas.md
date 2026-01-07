---
nav_title: "GET: View translation for a Canvas"
article_title: "GET: View Translation for a Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the View translation for a Canvas endpoint."
---

{% api %}
# View translation for a Canvas
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> Use this endpoint to preview a translated message for a Canvas. See [Locales in messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) for more information about translation features.

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
| `locale_id`            | Optional | String    | The ID (UUID) of the locale.       |
| `post_launch_draft_version`| Optional | Boolean | When `true` returns the latest draft version instead of the latest live published version. Defaults to `false` returning the latest live version.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint's response.
{% endalert %}

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

### Example success response

The status code `200` could return the following response header and body.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        }
    ]
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
