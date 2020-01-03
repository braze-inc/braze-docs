---
nav_title: "GET: Daily Active Users by Date"
page_order: 4

layout: api_page2

page_type: reference
platform: API
tool: Segments
description: "This article outlines details about the Daily Active Users endpoint."
---

{% api %}

# Daily Active Users by Date Endpoint

{% apimethod get %}
/kpi/dau/data_series
{% endapimethod %}

This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Kpi%20export%20%20dau%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986 {% endapiref %}

## Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `api_key`   | Yes      | String | App Group REST API Key |
| `length`    | Yes      | Integer | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at` | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request |
| `app_id`    | No       | String | App API Identifier; if excluded, results for all apps in app group will be returned |

### Example URL
`https://rest.iad-01.braze.com/kpi/dau/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&length=7&ending_at=2014-12-10T23:59:59-05:00`

## Response

`Content-Type: application/json`

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "dau" : (int)
        },
        ...
    ]
}
```

{% endapi %}
