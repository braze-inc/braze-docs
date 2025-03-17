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
/canvas/translations
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
|`step_id`| Required | String | The ID of your Canvas step. |
|`message_variation_id`| Required | String | The ID of your message. |
|`locale_id`| Required | String | The ID of the locale. |
|`workflow_id` | Required | String | The ID of the Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note all translation IDs are considered universal unique identifiers (UUIDs), which can be found in **Multi-Language Support** settings or in the GET request response.

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
|`INVALID_CAMPAIGN_ID`|Confirm the campaign ID matches the campaign you're translating.|
|`INVALID_LOCALE_ID`|Confirm your locale ID exists in your message translation.|
|`INVALID_MESSAGE_VARIATION_ID`|Confirm your message ID is correct.|
|`INVALID_TRANSLATION_OBJECT`|Translation IDs are mismatched or translated text exceeds limits.|
|`MESSAGE_NOT_FOUND`|Check that the message to be translated.|
|`LOCALE_NOT_FOUND`| Confirm the locale exists in your multi-language settings. |
|`MISSING_TRANSLATIONS`|Translation IDs must match to the message.|
|`MULTI_LANGUAGE_NOT_ENABLED`|Multi-language settings aren't turned on for your workspace.|
|`MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE`|Only email campaigns or Canvas messages with emails can be translated.|
|`UNSUPPORTED_CHANNEL`| Only messages in email campaigns or Canvas messages with emails can be translated.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


          INVALID_CAMPAIGN_ID = "Invalid campaign or step ID"
          INVALID_LOCALE_ID = "Invalid locale ID"
          INVALID_MESSAGE_VARIATION_ID = "Invalid message ID"
          INVALID_TRANSLATION_OBJECT = "Invalid translation object"
          MESSAGE_NOT_FOUND = "Message not found"
          LOCALE_NOT_FOUND = "Locale not found"
          MISSING_TRANSLATIONS = "Missing translations from the request body"
          MULTI_LANGUAGE_NOT_ENABLED = "Multi-language feature is not enabled on this company"
          MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE = "This message does not have multi-language setup"
          UNSUPPORTED_CHANNEL = "This message type does not support multi-language"

{% endapi %}
