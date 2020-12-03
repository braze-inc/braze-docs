---
nav_title: "GET: Canvas Data Series Analytics"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Canvas
description: "This article outlines details about the Canvas Data Series Analytics Endpoint."
---
{% api %}
# Canvas Data Series Analytics Endpoint
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

This endpoint allows you to export time series data for a Canvas.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Canvas%20export%20%20data%20series%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `canvas_id` | Yes | String | Canvas API Identifier |
| `ending_at` | Yes | DateTime (ISO 8601 string) | Date on which the data export should end - defaults to time of the request |
| `starting_at` | No | DateTime (ISO 8601 string) | Date on which the data export should begin (either length or starting_at are required) |
| `length` | No | String | Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) |
| `include_variant_breakdown` | No | Boolean | Whether or not to include variant stats (defaults to false) |
| `include_step_breakdown` | No | Boolean | Whether or not to include step stats (defaults to false) |
| `include_deleted_step_data` | No | Boolean | Whether or not to include step stats for deleted steps (defaults to false) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Canvas Identifier]({{site.baseurl}}/api/identifier_types/)

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&send_id=3456789&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "data": {
    "name": (string) Canvas name,
    "stats": [
      {
        "time": (string) date as ISO 8601 date,
        "total_stats": {
          "revenue": (float),
          "conversions": (int),
          "conversions_by_entry_time": (int),
          "entries": (int)
        },
        "variant_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {
            "name": (string) name of variant,
            "revenue": (int),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "entries": (int)
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (API identifier for step) {
            "name": (string) name of step,
            "revenue": (float),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "messages": {
              "email": [
                {
                  "sent": (int),
                  "opens": (int),
                  "unique_opens": (int),
                  "clicks": (int),
                  ... (more stats)
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
