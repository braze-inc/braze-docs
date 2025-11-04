---
nav_title: "GET: View translation for a campaign"
article_title: "GET: View Translation for a Campaign"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the View Translation for a campaign endpoint."
---

{% api %}
# View translation for a campaign
{% apimethod get %}
/campaigns/translations/?locale_id={locale_id}
{% endapimethod %}

> Use this endpoint to preview a translated message for a campaign.

{% alert important %}
This endpoint is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `campaigns.translations.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Query parameters

| Parameter              | Required | Data Type | Description                        |
|------------------------|----------|-----------|------------------------------------|
| `campaign_id`          | Required | String    | The ID of your campaign.           |
| `message_variation_id` | Required | String    | The ID for your message variation. |
| `locale_id`            | Required | String    | The ID of the locale.              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note all translation IDs are considered universal unique identifiers (UUIDs), which can be found in **Multi-Language Support** settings or in the request response.

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/?locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

### Example success response

The status code `200` could return the following response header and body.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Only email, push, and in-app-message campaigns or Canvas messages with emails can be translated.             |
| `UNSUPPORTED_CHANNEL`                   | Only email, push, or in-app-message campaigns or Canvas messages can be translated. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
