---
nav_title: "POST: Blocklist emails"
article_title: "POST: Blocklist Emails"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "This article outlines the details about the Blocklist emails Braze endpoint."

---
{% api %}
# Blocklist emails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> Use this endpoint to unsubscribe a user from email and mark them as hard bounced.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `email.blacklist` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `email` | Required | String or array | String email address to blocklist, or an array of up to 50 email addresses to blocklist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
