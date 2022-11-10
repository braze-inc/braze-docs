---
nav_title: "POST: Update User's Subscription Group Status V2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "This article outlines details about the Update User's Subscription Group Status Braze V2 endpoint."

platform: API
channel:
  - Email
---

{% api %}
# Update user's subscription group status
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard. You can access a subscription group's `subscription_group_id` by navigating to the **Subscriptions Group** page.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

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

{% alert important %}
When creating new users via the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, you should leave a delay of around 2 minutes before adding users to the relevant Subscription Group to allow Braze time to fully create the user profile.
{% endalert %}


## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `subscription_group_id` | Required | String | The `id` of your subscription group. |
| `subscription_state` | Required | String | Available values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). |
| `external_ids` | Required* | Array of strings | The `external_id` of the user or users,  may include up to 50 `id`s. |
| `emails` | Required* | String or array of strings | The email address of the user, can be passed as an array of strings. Must include at least one email address (with a max of 50). <br><br>If multiple users (`external_id`) in the same app group share the same email address, all users that share the email address are updated with the subscription group changes. |
| `phones` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone numbers of the user, can be passed as an array of strings. Must include at least one phone number (with a max of 50). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
Note that you cannot send `emails` and `phones` in the same subscription group section of the call. Instead, send either `emails` or `phones` along with the `external_ids`. As another option, you can send `emails`, `phones`, or `external_ids` individually.
{% endalert %}

## Example request for email and SMS

The following example uses `external_id` to make one API call for email and SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Example request email

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
```

## Example request SMS

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
```

{% endapi %}
