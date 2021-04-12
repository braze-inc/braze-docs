---
nav_title: "POST: Update Scheduled API Triggered Canvas Messages"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas

description: "This article outlines details about the Update Scheduled API Triggered Canvases Braze endpoint."
---
{% api %}
# Update Scheduled API Triggered Canvases
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/canvas/trigger/schedule/update
{% endapimethod %}

Use this endpoint to update scheduled API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

This endpoint allows you to update scheduled Canvas messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests. For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time. Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second changes could be applied to all, some, or none of your targeted users.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/UpdateScheduledApiTriggeredCanvasSendExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas Identifier,
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|String| See Canvas Identifier|
|`schedule_id`| Optional | String | The schedule_id to update (obtained from the response to create schedule) |
|`schedule` | Required | Object | See Schedule Object |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request Components
- [Canvas ID]({{site.baseurl}}/api/identifier_types/)
- [Schedule Object]({{site.baseurl}}/api/objects_filters/schedule_object/)

### Request Example
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas identifier",
  "schedule_id": "schedule identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
