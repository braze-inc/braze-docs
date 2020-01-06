---
nav_title: "GET: List Users' Subscription Group Status"
page_order: 4

layout: api_page2

page_type: reference
platform: API
channel:
  - SMS
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the List Users' Subscription Group Status Braze endpoint."
---

{% api %}

# Get Users' Subscription Group Status

{% apimethod get %}
/subscription/status/get
{% endapimethod %}

Use the endpoints below to get the subscription state of a user in a subscription group. These groups will be available on the __Subscription Group__ page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call.  This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

If you want to see examples or test this endpoint for __Email Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/GetUsersSubscriptionStatus {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

<br>

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/GetUsersSubscriptionStatus {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `subscription_group_id`  | Yes | String | The `id` of your subscription group. |
| `external_id`  |  Yes* | String | The `external_id` of the user (must include at least one and at most 50 `external_ids`). |
| `email` | Yes* | String | The email address of the user. It can be passed as an array of string with a max of 50. |
| `phone` | No* | String | The phone number of the user. You must include _at least one_ phone number (if email is not included) and _at most 50 phone numbers_. The recommendation is to provide this in the `E.164 format`.|

/* Generally, either `external_id` or `email` is required.

For SMS subscription groups, either `external_id` or `phone` is required.

Your request must include `phone` or `email` value, _but not both_.

### Example Request

```
https://rest.iad-03.braze.com/subscription/user/status?api_key=23abc-def5-3729-owod-23f9f3j30&email=example%2B1%40braze.com
```
### Response

All successful responses will return `subscribed`, `unsubscribed`, or `unknown` depending on status and user history with the subscription group.

{% endapi %}
