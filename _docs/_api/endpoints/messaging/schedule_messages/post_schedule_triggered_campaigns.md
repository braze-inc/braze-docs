---
nav_title: "POST: Schedule API-Triggered Campaigns"
article_title: "POST: Schedule API-Triggered Campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Schedule API-triggered campaigns Braze endpoint."

---
{% api %}
# Schedule API-triggered campaigns
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/create
{% endapimethod %}

> Use this endpoint to send dashboard created campaign messages via API-triggered delivery, allowing you to decide what action should trigger the message to be sent.

You can pass in `trigger_properties` that will be templated into the message itself.

Note that to send messages with this endpoint, you must have a [campaign ID]({{site.baseurl}}/api/identifier_types/), created when you build an [API-triggered campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `campaigns.trigger.schedule.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String| See [campaign identifier]({{site.baseurl}}/api/identifier_types/)|
| `send_id` | Optional | String | See [send identifier]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Optional | Array of recipients objects | See [recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Optional | Connected audience object | See [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Optional | Boolean | You must set `broadcast` to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). <br><br> If `broadcast` is set to true, a `recipients` list cannot be included. However, use caution when setting `broadcast: true`, as unintentionally setting this flag may cause you to send your message to a larger than expected audience. |
| `trigger_properties` | Optional | Object | Personalization key-value pairs for all users in this send. See [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). |
| `schedule` | Required | Schedule object | See [schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
    }
  ],
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
  "broadcast": false,
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Response

### Example success response

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}
