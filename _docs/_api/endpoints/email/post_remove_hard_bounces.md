---
nav_title: "POST: Remove Hard Bounced Emails"
page_order: 3

layout: api_page

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Hard Bounced Email Addresses Braze endpoint."
---
{% api %}
# Remove Hard Bounces
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingHardBouncedEmailExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

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
| ----------|-----------| ---------|------ |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
