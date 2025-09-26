---
nav_title: "POST: Update users subscription group status"
article_title: "POST: Update User's Subscription Group Status"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update user's subscription group status Braze endpoint."
---
{% api %}
# Update user's subscription group status
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/subscription/status/set
{% endapimethod %}

> Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard. 

You can access a subscription group's `subscription_group_id` by navigating to the **Subscription Group** page.

If you want to see examples or test this endpoint for **Email Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

If you want to see examples or test this endpoint for **SMS and RCS Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `subscription.status.set` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Request body

{% tabs %}
{% tab SMS and RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS and RCS subscription group - one of external_id or phone is required
 }
```
\* SMS and RCS subscription groups: Only `external_id` or `phone` is accepted.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* Email subscription groups: Either `email` or `external_id` is required.
{% endtab %}
{% endtabs %}

This property should not be used for updating a user's profile information. Use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) property instead.

{% alert tip %}
When creating new users using the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.
{% endalert %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Required | String | The `id` of your subscription group. |
| `subscription_state` | Required | String | Available values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). |
| `external_id` | Required* | Array of strings | The `external_id` of the user or users, may include up to 50 `id`s. |
| `email` | Required* | String or array of strings | The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). <br><br>If multiple users (`external_id`) in the same workspace share the same email address, then all users that share the email address are updated with the subscription group changes. |
| `phone` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone number of the user, can be passed as an array of strings. Must include at least one phone number (up to 50). <br><br>If multiple users (`external_id`) in the same workspace share the same phone number, then all users that share the phone number are updated with the same subscription group changes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example requests

### Email

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS and RCS

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

## Example success response

The status code `201` could return the following response body.

```json
{
    "message": "success"
}
```

{% alert important %}
The endpoint only accepts the `email` or `phone` value, not both. If given both, you will receive this response: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

