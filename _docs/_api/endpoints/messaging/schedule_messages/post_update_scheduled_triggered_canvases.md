---
nav_title: "POST: Update scheduled API-triggered Canvases"
article_title: "POST: Update Scheduled API-Triggered Canvases"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update scheduled API-triggered Canvases Braze endpoint."

---
{% api %}
# Update scheduled API-triggered Canvases
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Use this endpoint to update scheduled API-triggered Canvases that were created in the dashboard.

This allows you to decide what action should trigger the message to be sent. You can pass in `trigger_properties` that will be templated into the message itself.

Note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests.
  - For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time.
  - Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second changes could be applied to all, some, or none of your targeted users.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.trigger.schedule.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|String| See [Canvas identifier]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Optional | String | The `schedule_id` to update (obtained from the response to create schedule). |
|`schedule` | Required | Object | See [schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
