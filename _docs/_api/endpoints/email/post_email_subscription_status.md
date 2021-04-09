---
nav_title: "POST: Change Email Subscription Status"
page_order: 2

layout: api_page

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines the usage of and parameters for changing a User's Subscription Status with the Post Email Subscription Status Braze endpoint."
---
{% api %}
# Change User's Email Subscription Status
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/email/status
{% endapimethod %}

This endpoint allows you to set the email subscription state for your users. Users can be `opted_in`, `unsubscribed`, or `subscribed` (not specifically opted in or out).

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/ChangingEmailSubscriptionStatusExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `email` | Yes | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
| `subscription_state` | Yes | String | Either “subscribed”, “unsubscribed”, or “opted_in”. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Example Request
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
