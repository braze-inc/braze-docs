---
nav_title: "POST: Send Canvas Messages via API Triggered Delivery"
page_order: 4

layout: api_page2

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Email Addresses from the Spam List Braze endpoint."
---

{% api %}

# Sending Canvas Messages via API Triggered Delivery

API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API. Please see this section of [Braze Academy for further details][39].

This endpoint allows you to send Canvas messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas]({{ site.baseurl }}/api/identifier_types/#canvas-api-identifier).

{% apimethod post %}
/canvas/trigger/send
{% endapimethod %}


{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/SendMessageImmediatelyExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74fc3f0d-11f1-40f6-93f4-2eacb0ed459a {% endapiref %}

```
Content-Type: application/json
```

## Request Body

```json
{
  "api_key": (required, string) see App Group REST API Key,
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
    },
    ...
  ]
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

The `recipients` array may contain up to 50 objects, with each object containing a single `external_user_id` string and `canvas_entry_properties` object.

Customers using the API for server-to-server calls may need to whitelist the appropriate API URL if they're behind a firewall.

If you include both specific users in your API call and a target segment in the dashboard, the message will send to specifically the user profiles that are in the API call *and* qualify for the segment filters.

Message sending endpoint responses will include the message's `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each 'transmission' sent from the Braze platform).


{% endapi %}


[41]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
