---
nav_title: "GET: Custom Events Analytics"
article_title: "GET: Custom Event Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Custom Events Analytics endpoint."

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
| `event`      | Required      | String | The name of the custom event for which to return analytics. |
| `length`     | Required      | Integer | Max number of units (days or hours) before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `unit`       | Optional       | String | Unit of time between data points. Can be `day` or `hour`, defaults to `day`.  |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data series should end. Defaults to time of the request. |
| `app_id`     | Optional       | String | App API identifier retrieved from the **Developer Console** to limit analytics to a specific app. |
| `segment_id` | Optional       | String | See [Segment API identifier]({{site.baseurl}}/api/identifier_types/). Segment ID indicating the analytics-enabled segment for which event analytics should be returned. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
