---
nav_title: "PUT: Update Translation in a Canvas"
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
/{canvas_id}/translations
{% endapimethod %}

> Use this endpoint to update multiple translations for a Canvas.

{% alert important %}
Updating a translation for Canvas messages via API is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.translations.update` permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per hour.

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`locale_name`| Required | String | The name of the locale. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "canvas_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## Example success response

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
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
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