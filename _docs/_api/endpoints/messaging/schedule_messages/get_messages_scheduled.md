---
nav_title: "GET: List upcoming scheduled campaigns and Canvases"
article_title: "GET: List Upcoming Scheduled Campaigns and Canvases"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "This article outlines details about the List upcoming scheduled campaigns and Canvases Braze endpoint."

---
{% api %}
# List upcoming scheduled campaigns and Canvases
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> Use this endpoint to return a JSON list of information about scheduled campaigns and entry Canvases between now and a designated `end_time` specified in the request.

Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint include campaigns and Canvases created and scheduled in the Braze dashboard.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `messages.schedule_broadcasts` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `end_time` | Required | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | End date of the range to retrieve upcoming scheduled campaigns and Canvases. This is treated as midnight in UTC time by the API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
