---
nav_title: "POST: Schedule Messages"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Schedule Messages Braze endpoint."
---
{% api %}
# Create Scheduled Messages
{% apimethod post %}
/messages/schedule/create
{% endapimethod %}

The create schedule endpoint allows you to schedule a Campaign, Canvas, or other message to be sent at a designated time and provides you with an identifier to reference that message for updates. If you are targeting a segment, a record of your request will be stored in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console/activitylog/) after all scheduled messages have been sent.

Use this endpoint to send messages directly from the API.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateScheduledMessageExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8f813eee-7db3-4a99-b2ec-e972235d55b9 {% endapiref %}


## Request Body

```
Content-Type: application/json
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see External User ID,
  "user_aliases": (optional, array of User Alias Object) see User Alias,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  "segment_id": (optional, string) see Segment Identifier,
  "campaign_id": (optional, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "override_messaging_limits": (optional, bool) ignore global rate limits for campaigns, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "windows_push": (optional, Windows Phone 8 Push Object),
    "windows8_push": (optional, Windows Universal Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object),
    "webhook": (optional, Webhook object),
    "content_card": (optional, Content Card Object),
    "sms": (optional, SMS Object)
  }
}
```

### Request Components
- [Broadcast]({{site.baseurl}}/api/parameters/#broadcast)
- [User Alias Object]({{site.baseurl}}/api/objects_filters/user_alias_object/)
- [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)
- [Segment Identifier]({{site.baseurl}}/api/identifier_types/)
- [Campaign Identifier]({{site.baseurl}}/api/identifier_types/)
- [Schedule Object]({{site.baseurl}}/api/objects_filters/schedule_object/)
- [API Parameters]({{site.baseurl}}/api/parameters)

For more information on the "broadcast" flag, check out [Broadcast]({{site.baseurl}}/api/parameters/#broadcast) within our [API Parameters]({{site.baseurl}}/api/parameters) documentation.

### Available Messaging Objects

You can use these objects in the [request body](#request-body) above.
- [Android Objects]({{site.baseurl}}/api/objects_filters/android_objects/)
- [Apple Objects]({{site.baseurl}}/api/objects_filters/apple_objects/)
- [Content Cards Object]({{site.baseurl}}/api/objects_filters/content_cards_object/)
- [Email Object]({{site.baseurl}}/api/objects_filters/email_object/)
- [Kindle or FireOS Object]({{site.baseurl}}/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object]({{site.baseurl}}/api/objects_filters/sms_object/)
- [Web Objects]({{site.baseurl}}/api/objects_filters/web_objects/)
- [Webhook Object]({{site.baseurl}}/api/objects_filters/webhook_objects/)
- [Windows Objects]({{site.baseurl}}/api/objects_filters/windows_objects/)

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create?broadcast&external_user_ids&user_aliases&audience&segment_id&campaign_id&send_id&override_messaging_limits&recipient_subscription_state&schedule&messages' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
    "broadcast": "",
    "external_user_ids": "",
    "user_aliases": {
      "alias_name" : "",
      "alias_label" : ""
    },
    "segment_id": "",
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
    "campaign_id": "",
    "send_id": "",
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
    "windows_push": (optional, Windows Phone 8 Push Object),
    "windows8_push": (optional, Windows Universal Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```


{% endapi %}

[41]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
