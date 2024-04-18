---
nav_title: "GET: Translate Campaign or Canvas messages"
article_title: "GET: Translate Campaign or Canvas messages"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Translate campaign or Canvas messages endpoint."
---

{% api %}
# Translate messages for campaign or Canvas
{% apimethod get %}
/{campaigns}/translations
{% endapimethod %}

{% apimethod get %}
/{canvas}/translations
{% endapimethod %}

> Use this endpoint to view multiple translated messages and what these messages will look like for a user.

{% alert important %}
Translating campaign and Canvas messages via API is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with `campaigns.translations.get` and `canvas.translations.get` permissions for campaigns and Canvases respectively.

## Rate limit

This endpoint has a rate limit of 250,000 requests per hour.

## Path parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaigns`| Required for translating a campaign | String | The ID of your campaign. |
|`canvas`| Required for translating a Canvas | String | The ID of your Canvas. |

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/{campaigns}/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "zh-HK",
 				"country": "Hong Kong",
 				"language": "Chinese (Traditional)",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
			}
		}
	]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error message | Troubleshooting |
| --- | --- |
| Translation IDs are mismatched or translated text exceeds limits. | 
| Invalid locale ID. | Confirm your locale ID exists in your message translation. |
| Translation IDs are mismatched or translated text exceeds limits. | Translation IDs must match to the message. |
| This message does not support multi-language. | Only email campaigns or Canvas messages with emails can be translated. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}