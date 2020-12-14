---
nav_title: "GET: Custom Events Analytics"
page_order: 4

layout: api_page

page_type: reference
platform: API
description: "This article outlines details about the Custom Events List Endpoint."
---
{% api %}
# Custom Events Analytics
{% apimethod get %}
/events/data_series
{% endapimethod %}

This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Custom%20events%20analytics%20export%20%20series%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `event`      | Yes      | String | The name of the custom event for which to return analytics                                                                   |
| `length`     | Yes      | Integer | Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `unit`       | No       | String | Unit of time between data points - can be "day" or "hour" (defaults to "day")  |
| `ending_at`  | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request |
| `app_id`     | No       | String | App API Identifier retrieved from the Developer Console to limit analytics to a specific app |
| `segment_id` | No       | String | Segment API Identifier indicating the analytics enabled segment for which event analytics should be returned |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Segment Identifier]({{site.baseurl}}/api/identifier_types/)

### Example URL
`https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&segment_id=123456789`

### Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&segment_id=123456789%20identifier' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
``` 

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
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

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
