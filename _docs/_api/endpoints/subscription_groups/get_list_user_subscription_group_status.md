---
nav_title: "GET: List Users' Subscription Group Status"
page_order: 4

layout: api_page

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

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/GetUsersSubscriptionStatus {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `subscription_group_id`  | Yes | String | The `id` of your subscription group. |
| `external_id`  |  Yes* | String | The `external_id` of the user (must include at least one and at most 50 `external_ids`). Do not submit external_id and email/phone, as only the external_id will be accepted. |
| `email` | Yes* | String | The email address of the user. It can be passed as an array of string with a max of 50. Do not submit external_id and email, as only the external_id will be accepted. |
| `phone` | No* | String | The phone number of the user. You must include _at least one_ phone number (if email is not included) and _at most 50 phone numbers_. The recommendation is to provide this in the `E.164 format`. Do not submit external_id and phone, as only the external_id will be accepted.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


One of `external_id` or `email` or `phone` is required.
For SMS subscription groups, either `external_id` or `phone` is required.
For EMAIL subscription groups, either `external_id` or `email` is required.

### Example Request
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id=1f3-33203-3dd3-d323d3&external_id=12345&email=example.email@braze.com&phone=+11112223333
```

### Example Request for multiple users
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id=1f3-33203-3dd3-d323d3&external_id[]=1&external_id[]=2
```

### Example Request for SMS
```
curl --location --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id=1f3-33203-3dd3-d323d3&external_id=12345&email=example.email@braze.com&phone=+11112223333' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

### Example Request for Email
```
curl --location --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id=1f3-33203-3dd3-d323d3&external_id=1234&email=example.email@braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

All successful responses will return `subscribed`, `unsubscribed`, or `unknown` depending on status and user history with the subscription group.

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
