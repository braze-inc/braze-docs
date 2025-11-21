---
nav_title: "POST: Update users subscription group status v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "This article outlines details about the Update user's subscription group status Braze V2 endpoint."

platform: API
channel:
  - Email
---

{% api %}
# Update user's subscription group status (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard.

You can access a subscription group's `subscription_group_id` by navigating to the **Subscriptions Group** page.

If you want to see examples or test this endpoint for **Email Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

If you want to see examples or test this endpoint for **SMS Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

If you want to see examples or test this endpoint for **WhatsApp Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `subscription.status.set` permission.

{% alert note %}
If you're interested in using this endpoint with [LINE subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/), contact your customer success manager.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

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
\* Note that you cannot include both `emails` and `phones` parameters. Also, `emails`, `phones`, and `external_ids` can all be sent individually.

{% alert tip %}
When creating new users using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.
{% endalert %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Required | String | The `id` of your subscription group. |
| `subscription_state` | Required | String | Available values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). |
| `external_ids` | Required* | Array of strings | The `external_id` of the user or users,  may include up to 50 `id`s. |
| `emails` | Required* | String or array of strings | The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). <br><br>If multiple users (`external_id`) in the same workspace share the same email address, all users that share the email address are updated with the subscription group changes. |
| `phones` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone numbers of the user, can be passed as an array of strings. Must include at least one phone number (up to 50). <br><br>If multiple users (`external_id`) in the same workspace share the same phone number, then all users that share the phone number are updated with the same subscription group changes.|
| `use_double_opt_in_logic` | Optional | Boolean | If this parameter is omitted or set to `false`, users won't be entered into the SMS double opt-in workflow. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Note that you cannot include both `emails` and `phones` parameters. Also, `emails`, `phones`, and `external_ids` can all be sent individually.
{% endalert %}

### Example requests

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

## Email

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
'
```

## SMS and WhatsApp

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
'
```

{% endapi %}
