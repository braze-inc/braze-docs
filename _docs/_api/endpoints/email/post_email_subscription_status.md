---
nav_title: "POST: Change Email Subscription Status"
article_title: "POST: Change Email Subscription Status"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines the usage of and parameters for changing a User's Subscription Status with the Post Email Subscription Status Braze endpoint."

---
{% api %}
# Change user's email subscription status
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/email/status
{% endapimethod %}

This endpoint allows you to set the email subscription state for your users. Users can be `opted_in`, `unsubscribed`, or `subscribed` (not specifically opted in or out).

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `email` | Required | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
| `subscription_state` | Required | String | Either “subscribed”, “unsubscribed”, or “opted_in”. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
