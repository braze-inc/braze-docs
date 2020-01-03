---
nav_title: "POST: Schedule API Triggered Canvas Messages"
page_order: 4

layout: api_page2

page_type: reference
platform: API
tool:
  - Canvas

description: "This article outlines details about the Update Scheduled Canvases Braze endpoint."
---

{% api %}

# Schedule API Triggered Canvases

{% apimethod post %}
/canvas/trigger/schedule/create
{% endapimethod %}

Use this endpoint to trigger API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in `canvas_entry_properties` that will be templated into the messages sent by the first steps of the Canvas.

This endpoint allows you to schedule Canvas messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas]({{ site.baseurl }}/api/identifier_types/#canvas-api-identifier).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateScheduledApiTriggeredCanvasExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2806cc2f-1ddf-4b84-a4c2-34aa9a53986c {% endapiref %}


## Request Body

```
Content-Type: application/json
```

```json
{
  "api_key": (required, string) see App Group REST API Key,
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
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see Trigger Properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

This endpoint uses the [Schedule Object]({{ site.baseurl }}/api/objects_filters/schedule_object/).

{% endapi %}
