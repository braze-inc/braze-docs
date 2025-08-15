---
nav_title: "POST: Schedule api-triggered Canvases"
article_title: "POST: Schedule API-Triggered Canvases"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Schedule API-triggered Canvases Braze endpoint."

---
{% api %}
# Schedule API-triggered Canvases
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/create
{% endapimethod %}

> Use this endpoint to schedule Canvas messages via API-triggered delivery, allowing you to decide what action should trigger the message to be sent.

You can pass in `canvas_entry_properties` that will be templated into the messages sent by the first steps of the Canvas.

Note that to send messages with this endpoint, you must have a [Canvas ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier), created when you build a Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.trigger.schedule.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the
  // Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see trigger properties,
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
|`canvas_id`|Required|String| See [Canvas identifier]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Optional | Array of recipients objects | See [recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Optional | Connected audience object | See [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Optional | Boolean | You must set `broadcast` to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). <br><br> If `broadcast` is set to true, a `recipients` list cannot be included. However, use caution when setting `broadcast: true`, as unintentionally setting this flag may cause you to send your message to a larger than expected audience. |
| `canvas_entry_properties` | Optional | Object | Personalization key-value pairs for all users in this send. See [Canvas entry properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object). |
| `schedule` | Required | Schedule object | See [schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties": {}
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
  "canvas_entry_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Response

### Example success response

```
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
