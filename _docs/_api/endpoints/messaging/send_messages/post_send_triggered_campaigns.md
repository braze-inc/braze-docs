---
nav_title: "POST: Send campaigns using API-triggered delivery"
article_title: "POST: Send Campaigns Using API-Triggered Delivery"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Send campaigns using API-triggered delivery Braze endpoint."

---
{% api %}
# Send campaign messages using API-triggered delivery
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Use this endpoint to send immediate, one-off messages to designated users using API-triggered delivery.

API-triggered delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom using your API.

If you're targeting a segment, a record of your request is stored in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console/activitylog/). To send messages with this endpoint, you must have a [campaign ID](https://www.braze.com/docs/api/identifier_types/) created when you build an [API-triggered campaign]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `campaigns.trigger.send` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String|See [campaign identifier]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Optional | String | See [send identifier]({{site.baseurl}}/api/identifier_types/). |
|`trigger_properties`| Optional | Object | See [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Personalization key-value pairs apply to all users in this request. |
|`broadcast`| Optional | Boolean | You must set `broadcast` to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). <br><br> If `broadcast` is set to true, a `recipients` list cannot be included. However, use caution when setting `broadcast: true`, as unintentionally setting this flag may cause you to send your message to a larger-than-expected audience. |
|`audience`| Optional | Connected audience object| See [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Optional | Array | See [recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/).<br><br>If `send_to_existing_only` is `false`, an attribute object must be included.<br><br>If `recipients` is not provided and `broadcast` is set to true, the message is sent to the entire segment targeted by the campaign. <br><br> If `email` is the identifier, you must include [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) in the recipients object. |
|`attachments`| Optional | Array | If `broadcast` is set to true, then the `attachments` list cannot be included. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- The recipients array may contain up to 50 objects, with each object containing a single `external_user_id` string and a `trigger_properties` object.
- When `send_to_existing_only` is `true` (the default), Braze sends the message only to existing users. When set to `false` and an attributes object is provided, Braze creates a new user if one doesn't exist. Note that setting `send_to_existing_only` to `false` is not supported for user aliases&#8212;new alias-only users cannot be created through this endpoint. To send to an alias-only user, the user must already exist in Braze

A user's subscription group status can be updated using the inclusion of a `subscription_groups` parameter within the `attributes` object. For more details, refer to [User attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## Response details

Message-sending endpoint responses include the message's `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the ID of the message dispatch, a unique ID for each transmission sent from Braze. When using this endpoint, you receive a single `dispatch_id` for an entire batched set of users. For more information on `dispatch_id` check out our documentation on [Dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

If your request encounters a fatal error, refer to [Errors and responses]({{site.baseurl}}/api/errors/#fatal-errors) for the error code and description.

## Attributes object for campaigns

Braze has a messaging object called `attributes` that let you add, create, or update attributes and values for a user before you send them an API-triggered campaign. Using the `campaign/trigger/send` endpoint as this API call processes the user attributes object before it processes and sends the campaign. This helps minimize the risk of there being issues caused by [race conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/).

{% alert tip %}
Looking for the Canvas version of this endpoint? Check out [Sending Canvas messages using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint).
{% endalert %}

{% endapi %}
