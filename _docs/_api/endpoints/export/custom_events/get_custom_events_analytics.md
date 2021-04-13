---
nav_title: "GET: Custom Events Analytics"
page_order: 4

layout: api_page

page_type: reference
platform: API
description: "This article outlines details about the Custom events List Endpoint."
---
{% api %}
# Custom Events Analytics
{% apimethod get %}
/events/data_series
{% endapimethod %}

This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Request Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `event`      | Yes      | String | The name of the custom event for which to return analytics                                                                   |
| `length`     | Yes      | Integer | Max number of units (days or hours) before `ending_at` to include in the returned series - must be between 1 and 100 inclusive |
| `unit`       | No       | String | Unit of time between data points - can be "day" or "hour" (defaults to "day")  |
| `ending_at`  | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request |
| `app_id`     | No       | String | App API identifier retrieved from the Developer Console to limit analytics to a specific app |
| `segment_id` | No       | String | Segment API identifier indicating the analytics enabled segment for which event analytics should be returned |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Segment Identifier]({{site.baseurl}}/api/identifier_types/)

## Example Request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %} 

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int)
        },
        ...
    ]
}
```

### Fatal Error Response Codes {#fatal-export}

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code       | Reason / Cause                                                   |
| ---------------- | ---------------------------------------------------------------- |
| 400 Bad Request  | Bad Syntax                                                       |
| 401 Unauthorized | Unknown or missing REST API Key                                  |
| 429 Rate Limited | Over rate limit                                                  |
| 5XX              | Internal server error, you should retry with exponential backoff |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
