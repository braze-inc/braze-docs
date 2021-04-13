---
nav_title: "GET: Monthly Active Users for Last 30 Days"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Segments
description: "This article outlines details about the Monthly Active Users Endpoint."
---
{% api %}
# Monthly Active Users Endpoint
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Request Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `length`    | Yes | Integer | Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at` | No | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request |
| `app_id`    | No | String | App API identifier; if excluded, results for all apps in app group will be returned |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
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
            "time" : (string) date as ISO 8601 date,
            "mau" : (int)
        },
        ...
    ]
}
```
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
