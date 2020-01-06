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
{% apimethod post %}
/email/status
{% endapimethod %}

This endpoint allows you to set the email subscription state for your users. Users can be `opted_in`, `unsubscribed`, or `subscribed` (not specifically opted in or out).

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/ChangingEmailSubscriptionStatusExample {% endapiref %}
{% apiref postman %}https://brazeapis.postman.co/collections/4689407-29829c45-e619-4c12-910f-564ec8ccfda9?version=latest&workspace=e6986601-aa60-4cf9-8366-b2238ee9edd6#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Request Body

`Content-Type: application/json`

```json
{
  "api_key": "{{api_key}}",
  "email": "example@123.com",
  "subscription_state": "subscribed"
}
```

### Parameters

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | See App Group REST API Key in Parameter Definitions. |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
| `subscription_state` | Yes | String | Either “subscribed”, “unsubscribed”, or “opted_in”. |

{% endapi %}
