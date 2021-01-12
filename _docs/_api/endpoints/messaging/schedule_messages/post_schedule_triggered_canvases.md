---
nav_title: "POST: Schedule API Triggered Canvas Messages"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas

description: "This article outlines details about the Update Scheduled Canvases Braze endpoint."
---
{% api %}
# Schedule API Triggered Canvases
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/canvas/trigger/schedule/create
{% endapimethod %}

Use this endpoint to trigger API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in `canvas_entry_properties` that will be templated into the messages sent by the first steps of the Canvas.

This endpoint allows you to schedule Canvas messages (up to 90 days in advance) via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateScheduledApiTriggeredCanvasExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2806cc2f-1ddf-4b84-a4c2-34aa9a53986c {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "canvas_id": (required, string) see Canvas Identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, Array of Recipient Object),
  // for any keys that conflict between these trigger properties and those in a Recipient Object, the value from the
  // Recipient Object will be used
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key value pairs for the first step for all users in this send; see Trigger Properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message (up to 90 days in the future),
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|String| See Canvas Identifier|
|`recipients` | Optional | Array of Recipient Objects | See Recipients Object |
|`audience` | Optional | Connected Audience Object | See Connected Audience | 
|`broadcast` | Optional | Boolean | See Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted |
| `canvas_entry_properties` | Optional | Object | Personalization key value pairs for all users in this send; see Trigger Properties |
| `schedule` | Required | Schedule Object | See Schedule Object |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request Components
- [Canvas Identifier]({{site.baseurl}}/api/identifier_types/)
- [Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/)
- [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)
- [Broadcast]({{site.baseurl}}/api/parameters/#broadcast)
- [Trigger Properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)
- [Schedule Object]({{site.baseurl}}/api/objects_filters/schedule_object/)

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "canvas_id": "",
  "recipients": [{
    "user_alias": "",
    "external_user_id": "",
    "trigger_properties": "",
    "canvas_entry_properties": {}
  }],
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
}
'
```

{% endapi %}
