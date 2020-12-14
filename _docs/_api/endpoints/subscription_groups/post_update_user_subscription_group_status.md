---
nav_title: "POST: Update User's Subscription Group Status"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel:
  - Email
  - SMS
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Update User's Subscription Group Status Braze endpoint."
---
{% api %}
# Update Users' Subscription Group Status
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/subscription/status/set
{% endapimethod %}

Use the endpoints below to update the subscription state of a user on the Braze dashboard. You can access a subscription groups `subscription_group_id` by navigating to it on the Subscription Group page.

If you want to see examples or test this endpoint for __Email Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/SetUsersSubscriptionStatus {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/SetUsersSubscriptionStatus {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

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
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group),
   "external_id": (required*, string) the external_id of the user,
   "email": (required*, string) the email address of the user
   //one of external_id or email is required
   //can be passed as an array of string with a max of 50
   //endpoint only accepts email or phone value, not both
   "phone": (required*, string in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers).
   //one of external_id or phone is required
 }
```
\* SMS subscription groups: Only `external_id` or `phone` is accepted.<br>
\* Email subscription groups: Either `email` or `external_id` is required. 

### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `subscription_group_id` | Yes | String | The id of your subscription group, |
| `subscription_state` | Yes | String | Available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group) |
| `external_id` | Yes* | String | The external_id of the user |
| `email` | Yes* | String | The email address of the user |
| `phone` | Yes* | String in E.164 format | Tags must already exist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Using Email
```json
{
  "subscription_group_id": "pto81fff-734f-80e5-b7b2-b880562888ww",
  "subscription_state": "unsubscribed",
  "email": "your.user@email.com"
}

```

This property should not be used for updating a user's profile information. Please use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) property instead.

#### Using Phone Number
```json
{
  "subscription_group_id": "pto81fff-734f-80e5-b7b2-b880562888ww",
  "subscription_state": "unsubscribed",
  "phone": "+12223334444"
}

```

This property should not be used for updating a user's profile information. Please use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) property instead.

### Example Requests Email
```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "subscription_group_id": "pto81fff-734f-80e5-b7b2-b880562888ww",
  "subscription_state": "unsubscribed",
  "external_id": "user123",
  "email": "your.user@email.com"
}
'
```

### Example Requests SMS
```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "subscription_group_id": "pto81fff-734f-80e5-b7b2-b880562888ww",
  "subscription_state": "unsubscribed",
  "external_id": "user123",
  "phone": "+12223334444"
}
'
```

### Example Successful Response

Response: (status 201)

```json
{
    "message": "success"
}
```

{% alert important %}
The endpoint only accepts the `email` or `phone` value, not both. If given both, you will receive this response: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

[support]: {{site.baseurl}}/support_contact/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/