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
|`step_id`| Required | String | The ID of your Canvas step. |
|`message_variation_id`| Required | String | The ID of your message variation. |
|`locale_name`| Required | String | The name of the locale. |
|`workflow_id` | Required | String | The ID of the Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Note all translation IDs are considered universal unique identifiers (UUIDs), which can be found in **Multi-Language Support** settings or in the request response.
{% endalert %}

## Example request

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad", // CANVAS ONLY
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac", // CANVAS ONLY
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

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error message  | Troubleshooting |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Occurs when the third-party translator provides translations with exceptions that generate Liquid errors. Contact Braze Support for further assistance. |
| `The provided translations are missing 'id_1', 'id_2'` | Translation IDs are mismatched or translated text exceeds limits. For example, this could mean the payload shape is missing fields in the translation object. Every message (when enabled for multi-language) should have a specific number of "translation blocks" with an ID associated with it. If the payload provided is missing any of the IDs, then this would be considered an incomplete object and result in an error. |
| `The provided locale code does not exist.` | The third-party translator's payload contains a locale code that doesn't exist in Braze. |
| `The provided translations have exceeded the maximum of 20MB.` | The provided payload exceeds the size limit. |
| `You have exceeded the maximum number of requests. Please try again later.` | All Braze APIs have built-in rate limiting, and this error will automatically returned when the rate has exceeded the allotted amount for this authentication token. |
| `This message does not support multi-language.` | This can occur when a message ID doesn't support multi-language messages yet. Only messages in the following channels can be translated: push, in-app messages, and email. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
