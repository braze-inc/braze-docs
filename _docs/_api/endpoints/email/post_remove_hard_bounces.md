---
nav_title: "POST: Remove hard bounced emails"
article_title: "POST: Remove Hard Bounced Emails"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "This article outlines details about the Remove hard bounced email addresses Braze endpoint."

---
{% api %}
# Remove hard bounced emails
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> Use this endpoint to remove email addresses from your Braze bounce list and bounce list maintained by your email provider.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `email.bounce.remove` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `email` | Required | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
