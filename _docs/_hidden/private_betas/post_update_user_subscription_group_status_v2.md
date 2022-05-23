---
nav_title: "POST: Update User's Subscription Group Status V2"
permalink: /post_update_user_subscription_group_status_v2/
hidden: true
layout: api_page
page_type: reference
description: "This article outlines details about the Update User's Subscription Group Status Braze V2 endpoint."

platform: API
channel:
  - Email
---

{% api %}
# Update users' subscription group status
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

Use this endpoint to update the subscription state of up to 50 users on the Braze dashboard. You can access a subscription group's `subscription_group_id` by navigating to the **Subscription Group** page.

## Rate limit

{% alert note %}
A rate limit is applied to requests made to this endpoint for customers who onboarded with Braze on or after September 16, 2021. For more information, see [API Limits]({{site.baseurl}}/api/basics/#api-limits).
{% endalert %}

## Request body

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```

## Request parameters
| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `subscription_group_id` | Required | String | The `id` of your subscription group. |
| `subscription_state` | Required | String | Available values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). |
| `external_id` | Required* | Array of strings | The `external_id` of the user or users, may include up to 50 `id`s. |
| `email` | Required* | String or array of strings | The email address of the user, can be passed as an array of strings. Must include at least one email address (with a max of 50). <br><br>If multiple users (`external_id`) in the same app group share the same email address, then all users that share the email address are updated with the subscription group changes. |
| `phone` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone numbers of the user, can be passed as an array of strings. Must include at least one phone number (with a max of 50). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request for email and SMS

The following example uses `external_id` to make one API call.

```
{
   "subscription_groups":[
    {
      "subscription_group_id":"39ab6c08-d141-44ee-a39f-fb3e22c3592a",
      "subscription_state":"subscribed",
      "external_ids":[
        "einfra-187","example1@email.com"
      ]
    },
    {
      "subscription_group_id":"dbad58f7-5be8-4c62-8797-56fefec099b7",
      "subscription_state":"subscribed",
      "external_ids":[
        "einfra-187","example1@email.com"
      ]
    }
  ]
 }
```

## Example request email

```
{
 "subscription_groups":[
  {
     "subscription_group_id":"bcc803d1-45df-4548-8f02-c4e9e87a1f8f",
     "subscription_state":"subscribed",
     "emails":[
      "example1@email.com","example2@email.com"
    ]
   }
 ]
}
```

## Example request SMS

```
{
 "subscription_groups":[
   {
     "subscription_group_id":"4af7ba9b-13ef-4c21-b3f1-d4bfaf3dd5d8",
     "subscription_state":"subscribed",
     "phones":[
       "+12223334444","+15556667777”
     ]
   }
 ]
}
```

{% endapi %}