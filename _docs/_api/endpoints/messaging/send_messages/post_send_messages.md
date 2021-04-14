---
nav_title: "POST: Send Messages Immediately via API Only"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Send Messages Immediately Braze endpoint."
---
{% api %}
# Sending Messages Immediately via API Only
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/messages/send
{% endapimethod %}

This endpoint allows you send your messages using our API. Be sure to include Messaging Objects in your body to complete your requests.

The send endpoint allows you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign states. see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "apple_push": (optional, apple push object),
     "android_push": (optional, android push object),
     "windows_phone8_push": (optional, windows phone 8 push object),
     "windows_universal_push": (optional, windows universal push object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "email": (optional, email object),
     "webhook": (optional, webhook object),
     "content_card": (optional, content card object),
     "sms": (optional, SMS object)
   }
 }
```

## Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`broadcast`|Optional|Boolean|See broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted|
|`external_user_ids` | Optional | Array of strings | See external identifier |
|`user_aliases`|Optional|Array of user alias objects| See user alias object|
|`segment_id `| Optional | String | See segment identifier |
|`audience`|Optional|Connected audience object|See connected audience|
|`campaign_id`|Optional*|String| *Required if you wish to track campaign stats (e.g. sends, clicks, bounces, etc) on the Braze dashboard. <br>See campaign identifier for more information|
|`send_id`| Optional | String | See send identifier |
|`override_frequency_capping`|Optional|Boolean|Ignore frequency_capping for campaigns, defaults to false |
|`recipient_subscription_state`|Optional|String|Use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed'|
|`messages`| Optional | Messaging objects | See available messaging objects|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Broadcast]({{site.baseurl}}/api/parameters/#broadcast)
- [User Alias Object]({{site.baseurl}}/api/objects_filters/user_alias_object/)
- [Segment Identifier]({{site.baseurl}}/api/identifier_types/)
- [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)
- [Campaign Identifier]({{site.baseurl}}/api/identifier_types/)
- [Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/)
- [API Parameters]({{site.baseurl}}/api/parameters)

### Available Messaging Objects

You can use these objects in the [request body](#request-body) above.

- [Android Objects]({{site.baseurl}}/api/objects_filters/android_objects/)
- [Apple Objects]({{site.baseurl}}/api/objects_filters/apple_objects/)
- [Content Cards Object]({{site.baseurl}}/api/objects_filters/content_cards_object/)
- [Email Object]({{site.baseurl}}/api/objects_filters/email_object/)
- [Kindle or FireOS Object]({{site.baseurl}}/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object]({{site.baseurl}}/api/objects_filters/sms_object/)
- [Web Objects]({{site.baseurl}}/api/objects_filters/web_objects/)
- [Webhook Object]({{site.baseurl}}/api/objects_filters/webhook_object/)
- [Windows Objects]({{site.baseurl}}/api/objects_filters/windows_objects/)

## Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)",
    "windows_phone8_push": "(optional, Windows Phone 8 Push Object)",
    "windows_universal_push": "(optional, Windows Universal Push Object)"
  }
}'\'''
```

## Response Details

Message sending endpoint responses will include the message’s `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each ‘transmission’ sent from the Braze platform). For more information on `dispatch_id` checkout out our [documentation]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}

