---
nav_title: "POST: Send Canvas Messages via API Triggered Delivery"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas

description: "This article outlines details about the Send Canvas Messages via API Triggered Delivery Braze endpoint."
---
{% api %}
# Sending Canvas Messages via API Triggered Delivery
{% apimethod post core_endpoint|https://www.braze.com/docs/sla %} 
/canvas/trigger/send
{% endapimethod %}

API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API.

This endpoint allows you to send Canvas messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/SendApiTriggeredDeliveryCanvasExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

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
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with canvas_entry_properties above)
      "send_to_existing_only": (optional, boolean) defaults to true,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    },
    ...
  ]
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|String|See Canvas Identifier|
|`canvas_entry_properties`|Optional|Object|Personalization key-value pairs that will apply to all users in this request|
|`broadcast`|Optional|Boolean|See Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted|
|`audience`|Optional|Connected Audience Object|See Connected Audience|
|`recipients`|Optional|Array|If not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Canvas Identifier]({{site.baseurl}}/api/identifier_types/)
- [Broadcast]({{site.baseurl}}/api/parameters/#broadcast)
- [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)
- [Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/)
- [Canvas Entry Properties]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [User Alias Object]({{site.baseurl}}/api/objects_filters/user_alias_object/)
- [User Attributes Object]({{site.baseurl}}/api/objects_filters/user_attributes_object/)
- [API Parameters]({{site.baseurl}}/api/parameters)
<br><br>
The `recipients` array may contain up to 50 objects, with each object containing a single `external_user_id` string and `canvas_entry_properties` object.
<br><br>
Either `external_user_id` or `user_alias` is required for this call. Requests must specify only one.
<br><br>
When `send_to_existing_only` is `true`, Braze will only send the message to existing users. When `send_to_existing_only` is `false` and a user with the given `id` does not exist, Braze will create a user with that id and attributes before sending the message.
<br><br>
Customers using the API for server-to-server calls may need to whitelist the appropriate API URL if they're behind a firewall.
<br><br>
If you include both specific users in your API call and a target segment in the dashboard, the message will send to specifically the user profiles that are in the API call *and* qualify for the segment filters.

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "canvas_id": "",
  "canva_entry_properties": "",
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
  "recipients": [{
    "user_alias": {
      "alias_name" : "",
      "alias_label" : ""
    },
    "external_user_id": "",
    "trigger_properties": {},
    "canvas_entry_properties": {},
    "send_to_existing_only": true,
    "attributes": {}
  }]
}'
```

## Response Details
Message sending endpoint responses will include the message’s `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each ‘transmission’ sent from the Braze platform). For more information on `dispatch_id` checkout out our [documentation]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

## Create Send Endpoint

__Using the Attributes Object in Canvas__

Braze has a Messaging Object called `Attributes` that allows you to add, create, or update attributes and values for a user before sending them an API Triggered Canvas using the `canvas/trigger/send` endpoint as this API call will process the User Attributes object before it processes and sends the Canvas. This helps minimize the risk of there being issues caused by [race conditions]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert important %}
Looking for Create Send Endpoint for Campaigns? Check out the documentation [here]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#create-send-endpoint).
{% endalert %}

{% endapi %}

[41]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
