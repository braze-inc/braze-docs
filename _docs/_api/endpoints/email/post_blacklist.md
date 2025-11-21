---
nav_title: "POST: Blacklist emails"
article_title: "POST: Blacklist Emails"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "This article outlines the details about the Blacklist emails Braze endpoint."

---
{% api %}
# Blacklist emails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Braze has released the [`/email/blocklist` endpoint]({{site.baseurl}}/api/endpoints/email/post_blocklist/) with the same functionality as the `/email/blacklist` endpoint. We recommend you use the `/email/blocklist` endpoint instead.
{% endalert %}

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
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `email` | Required | String or array | String email address to blacklist, or an array of up to 50 email addresses to blacklist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}
