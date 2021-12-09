---
nav_title: "POST: Remove Hard Bounced Emails"
article_title: "POST: Remove Hard Bounced Emails"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about and using the Remove Hard Bounced Email Addresses Braze endpoint."
---

{% api %}
# Remove hard bounces
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

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

| Parameter | Required | Data Type       | Description                                                                        |
| --------- | -------- | --------------- | ---------------------------------------------------------------------------------- |
| `email`   | Required | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
