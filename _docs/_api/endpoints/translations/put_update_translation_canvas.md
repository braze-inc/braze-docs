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

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Required for translating a Canvas | String | The ID of your Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
	"step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac", // CANVAS ONLY
	"message_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
	"locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
	"translation_map": {
		"id_0": "Hola!",
		"id_1": "Me llamo Jacky",
		"id_2": "Donde estas la biblioteca?"
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