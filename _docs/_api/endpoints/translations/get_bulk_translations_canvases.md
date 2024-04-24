---
nav_title: "GET: Translate Canvas"
article_title: "GET: Translate Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Translate Canvas endpoint."
---

{% api %}
# Translate Canvases
{% apimethod get %}
/{canvas_id}/translations
{% endapimethod %}

> Use this endpoint to view multiple translated Canvas messages and what these messages will look like for a user.

{% alert important %}
Translating campaign and Canvas messages via API is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.translations.get` permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per hour.

## Path parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Required for translating a Canvas | String | The ID of your Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/{canvas_id}/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

## Example success response

The status code `200` could return the following response header and body.

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

## Example error response

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