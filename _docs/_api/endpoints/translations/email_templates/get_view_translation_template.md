---
nav_title: "GET: View all translations and locales for email template"
article_title: "GET: View All Translations and Locales for Email Template"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the View all translations and locales for Email Template endpoint."
---

{% api %}
# View all translations and locales for an email template
{% apimethod get %}
/templates/email/translations/
{% endapimethod %}

> Use this endpoint to view all translations and locales for an [email template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates).

{% alert important %}
This endpoint is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `templates.translations.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Query parameters

| Parameter     | Required | Data Type | Description                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Required | String    | The ID for your email template. |
| `locale_id`   | Required | String    | The ID of the locale.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note all translation IDs are considered universal unique identifiers (UUIDs), which can be found in **Multi-Language Support** settings or in the request response.

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/' \
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
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        },
        {
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            },
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
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
| `INVALID_LOCALE_ID`                     | Confirm your locale ID exists in your message translation.                         |
| `LOCALE_NOT_FOUND`                      | Confirm the locale exists in your multi-language settings.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | Multi-language settings aren't turned on for your workspace.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Only email templates and email, push, and in-app-message campaigns or Canvas messages with emails can be translated.             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
