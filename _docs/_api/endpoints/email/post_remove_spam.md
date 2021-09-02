---
nav_title: "POST: Remove Email Addresses from Spam List"
article_title: "POST: Remove Email Addresses from Spam List"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about and using the Remove Email Addresses from the Spam List Braze endpoint."

---
{% api %}
# Remove Email Addresses from Spam List
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Request Body
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Request Parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| --------|------- |
| `email` | Required | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
