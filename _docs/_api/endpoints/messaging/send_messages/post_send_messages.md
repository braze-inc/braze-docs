---
nav_title: "POST: Send messages immediately using the API only"
article_title: "POST: Send Messages Immediately Using the API Only"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Send messages immediately using API only Braze endpoint."

---
{% api %}
# Send messages immediately using the API only
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> Use this endpoint to send immediate messages to designated users using the Braze API.

If you are targeting a segment, a record of your request will be stored in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% multi_lang_include api/payload_size_alert.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `messages.send` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Request body

{% alert tip %}
Be sure to include [messaging objects]({{site.baseurl}}/api/objects_filters/#messaging-objects) in your body to complete your requests.
{% endalert %}

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
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Optional | Boolean | You must set `broadcast` to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). <br><br> If `broadcast` is set to true, a `recipients` list cannot be included. However, use caution when setting `broadcast: true`, as unintentionally setting this flag may cause you to send your message to a larger than expected audience. |
|`external_user_ids` | Optional | Array of strings | See [external user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Optional | Array of user alias objects| See [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Optional | String | See [segment identifier]({{site.baseurl}}/api/identifier_types/#segment-identifier). |
|`audience`| Optional | Connected audience object | See [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Optional* | String | See [campaign identifier]({{site.baseurl}}/api/identifier_types/) for more information. <br><br>*Required if you wish to track campaign stats (for example, sends, clicks, bounces, etc) on the Braze dashboard. |
|`send_id`| Optional | String | See [send identifier]({{site.baseurl}}/api/identifier_types/) |
|`override_frequency_capping`| Optional | Boolean | Ignore `frequency_capping` for campaigns, defaults to `false`. |
|`recipient_subscription_state`| Optional | String | Use this to send messages to only users who have opted in (`opted_in`), only users who have subscribed or are opted in (`subscribed`) or to all users, including unsubscribed users (`all`). <br><br>Using `all` users is useful for transactional email messaging. Defaults to `subscribed`. |
|`messages`| Optional | Messaging objects | See [available messaging objects]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
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
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## Response details

Message sending endpoint responses will include the message's `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the ID of the message dispatch, meaning the unique ID for each "transmission" sent from Braze. For more information, refer to [Dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}
