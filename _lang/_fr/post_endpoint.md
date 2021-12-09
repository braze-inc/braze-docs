---
nav_title: "POST: [Endpoint Name]"
page_order:
layout: api_page
excerpt_separator: ""
page_type: reference
platform: API
channel:
  - Email
  - Push
tool:
  - Canvas
  - Campaigns
description: "This article outlines details about and using this POST [endpoint name] Braze endpoint."
noindex: true
---

{% api %}
# [Endpoint Name]

{% apimethod post %}
/email/spam/remove
{% endapimethod %}

This is the description of the endpoint. For example: "This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider."

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingSpamListEmailExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Request Body

This is where you can give more information about your endpoint request body, including an example of what one would look like.

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@123.com"
}
```

### Parameter Details

This is a place for you to describe additional details for the parameters above.

| Parameter | Required | Data Type       | Description                                                                        |
| --------- | -------- | --------------- | ---------------------------------------------------------------------------------- |
| `email`   | Yes      | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example Unsubscribe CURL

The following example CURL demonstrates how to unsubscribe a user from receiving email via the Braze APIs:

```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{"email":"EMAIL_TO_UNSUBSCRIBE","subscription_state":"unsubscribed"}' https://rest.iad-01.braze.com/email/status
```
{% endapi %}
