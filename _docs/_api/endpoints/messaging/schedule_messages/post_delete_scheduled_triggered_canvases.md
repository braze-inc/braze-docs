---
nav_title: "POST: Delete scheduled API-triggered Canvases"
article_title: "POST: Delete Scheduled API-Triggered Canvases"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Delete scheduled API-triggered Canvases Braze endpoint."

---
{% api %}
# Delete scheduled API-triggered Canvases
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> The delete schedule endpoint allows you to cancel a message that you previously scheduled API-triggered Canvases before it has been sent.

Scheduled messages or triggers that are deleted close to or during the time they were supposed to be sent are updated with best efforts, so Braze may apply last-second deletions to all, some, or none of your targeted users.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.trigger.schedule.delete` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| Required | String | See [Canvas identifier]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Required | String | The `schedule_id` to delete (obtained from the response to create schedule). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
