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

You can access a subscription group's `subscription_group_id` by navigating to the **Subscription Group** page.

To see examples or test this endpoint for **Email Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

To see examples or test this endpoint for **SMS Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

To see examples or test this endpoint for **WhatsApp Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `subscription.status.set` permission.

{% alert note %}
If you're interested in using this endpoint with [LINE subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/), contact your customer success manager.
{% endalert %}

## Differences from V1

The V2 endpoint differs from the [V1 endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) in the following ways:

- **Multiple subscription groups**: V2 lets you update multiple subscription groups in a single API request, while V1 supports only one subscription group per request.
- **Update both email and SMS in one call**: When using `external_ids`, you can update both email and SMS subscription groups for the same users in a single API call. With V1, you must make separate API calls for email and SMS subscription groups.
- **Using email or phone identifiers**: If you use `emails` or `phones` instead of `external_ids`, you cannot update both email and SMS subscription groups in the same request. You must make separate API calls—one for email subscription groups and one for SMS subscription groups.

{% alert important %}
**Phone number format**: Phone numbers must be in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, `+12223334444`). Phone numbers that are not in E.164 format are rejected.
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
| `phones` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | You can pass user phone numbers as an array of strings. Must include at least one phone number (up to 50). Phone numbers must be in E.164 format (for example, `+12223334444`). <br><br>If multiple users (`external_id`) in the same workspace share the same phone number, then all users that share the phone number are updated with the same subscription group changes.|
| `use_double_opt_in_logic` | Optional | Boolean | If this parameter is omitted or set to `false`, users are not entered into the SMS double opt-in workflow. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
**Identifier selection**: 
- To update both email and SMS subscription groups in a single API call, use `external_ids`. You cannot include both `emails` and `phones` in the same request.
- If you use `emails` or `phones` instead of `external_ids`, make separate API calls—one for email subscription groups and one for SMS subscription groups.
- You can send `emails`, `phones`, or `external_ids` individually.
{% endalert %}

### Example requests

The following example uses `external_ids` to update both email and SMS subscription groups in a single API call. This is only possible when using `external_ids`—you cannot update both email and SMS subscription groups in one call when using `emails` or `phones`.

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
