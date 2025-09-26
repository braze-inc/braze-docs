---
nav_title: "POST: Remove email addresses from spam list"
article_title: "POST: Remove Email Addresses from Spam List"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "This article outlines details about the Remove email addresses from the spam list Braze endpoint."

---
{% api %}
# Remove email addresses from spam list
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Use this endpoint to remove email addresses from your Braze spam list and spam list maintained by your email provider.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `email.spam.remove` permission.

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
| ----------|-----------| --------|------- |
| `email` | Required | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
