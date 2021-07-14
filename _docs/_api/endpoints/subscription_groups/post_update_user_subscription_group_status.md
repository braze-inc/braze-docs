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

Use the endpoints below to batch update the subscription state of up to 50 users on the Braze dashboard. You can access a subscription groups `subscription_group_id` by navigating to it on the Subscription Group page.

If you want to see examples or test this endpoint for __Email Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Request Body

{% tabs %}
{% tab SMS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group),
   "external_id": (required*, array of strings) the external_id of the user or users, may include up to 50 ids,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Please note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* SMS subscription groups: Only `external_id` or `phone` is accepted.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group),
   "external_id": (required*, array of strings) the external_id of the user or users, may include up to 50 ids,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS subscription group - one of external_id or phone is required
 }
```
\* Email subscription groups: Either `email` or `external_id` is required.
{% endtab %}
{% endtabs %}

This property should not be used for updating a user's profile information. Please use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) property instead.

{% alert important %}
When creating new users via the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, you should leave a delay of around 2 minutes before adding users to the relevant Subscription Group to allow Braze time to fully create the user profile.
{% endalert %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `subscription_group_id` | Required | String | The `id` of your subscription group. |
| `subscription_state` | Required | String | Available values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). |
| `external_id` | Required* | Array of strings | The `external_id` of the user or users, may include up to 50 `id`s. |
| `email` | Required* | String | The email address of the user, can be passed as an array of strings. Must include at least one email address (with a max of 50). |
| `phone` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone number of the user, can be passed as an array of strings. Must include at least one phone number (with a max of 50). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Requests Email
```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "example-user",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

## Example Requests SMS
```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## Example Successful Response

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

