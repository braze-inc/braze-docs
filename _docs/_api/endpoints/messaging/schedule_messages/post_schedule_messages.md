---
nav_title: "POST: Create scheduled messages"
article_title: "POST: Create Scheduled Messages"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Create scheduled messages Braze endpoint."

---
{% api %}
# Create scheduled messages
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> Use this endpoint to schedule a campaign, Canvas, or other message to be sent at a designated time and provides you with an identifier to reference that message for updates.

If you're targeting a segment, a record of your request will be stored in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console/activitylog/) after all scheduled messages have been sent.

{% alert tip %}
If you're interested in sending messages immediately to designated users, use the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) instead.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `messages.schedule.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Optional | Boolean | You must set `broadcast` to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to `false`. <br><br> If `broadcast` is set to `true`, a recipients list cannot be included. However, use caution when setting `broadcast: true`, as unintentionally setting this flag may cause you to send your message to a larger-than-expected audience. |
| `external_user_ids` | Optional | Array of strings | See [external user identifier]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Optional | Array of user alias objects | See [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Optional | Connected audience object | See [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Optional | String | See [segment identifier]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Optional|String| See [campaign identifier]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Optional | String | See [send identifier]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Optional | Boolean | Ignore frequency capping for campaigns, defaults to false |
|`recipient_subscription_state`| Optional | String | Use this to send messages to only users who have opted in (`opted_in`), only users who have subscribed or are opted in (`subscribed`) or to all users, including unsubscribed users (`all`). <br><br>Using `all` users is useful for transactional email messaging. Defaults to `subscribed`. |
| `schedule` | Required | Schedule object | See [schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Optional | Messaging object | See [available messaging objects]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## Response

### Example success response

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}
