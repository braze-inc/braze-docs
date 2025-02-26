---
nav_title: "GET: View Translation for a Canvas"
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
/canvas/translations/?locale_id={locale_id}
{% endapimethod %}

> Use this endpoint to view a translated message to see what this message looks like for a user.

{% alert important %}
Veiwing a translated message for a Canvas via API is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.translations.get` permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per hour.

## Path parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`step_id`| Required | String | The ID of your Canvas step. |
|`message_variation_id`| Required | String | The ID for your message variation. |
|`locale_id`| Required | String | The ID of the locale. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note all translation IDs are considered universal unique identifiers (UUIDs), which can be found in **Multi-Language Support** settings or in the request response.

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?locale_id={locale_id}' \
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
 				"name": "es-MX",
 				"country": "Mexico",
 				"language": "Spanish",
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

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
	"errors": [
		{
			"message": "Invalid locale ID"
		}
	]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error message                           | Troubleshooting                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirm the campaign ID matches the campaign you're translating.                   |
| `INVALID_LOCALE_ID`                     | Confirm your locale ID exists in your message translation.                         |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirm your message ID is correct.                                                |
| `MESSAGE_NOT_FOUND`                     | Check that the message to be translated.                                           |
| `LOCALE_NOT_FOUND`                      | Confirm the locale exists in your multi-language settings.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | Multi-language settings aren't turned on for your workspace.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Only email campaigns or Canvas messages with emails can be translated.             |
| `UNSUPPORTED_CHANNEL`                   | Only messages in email campaigns or Canvas messages with emails can be translated. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
