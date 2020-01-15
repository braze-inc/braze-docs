---
nav_title: "GET: Canvas Data Summary Analytics"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Canvas
description: "This article outlines details about the Canvas Data Summary Analytics Endpoint."
---
{% api %}
# Canvas Data Summary Endpoint
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas' results.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Canvas%20export%20%20data%20summary%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Request Parameter Details

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `api_key` | Yes | String | App Group REST API Key |
| `canvas_id` | Yes | String | Canvas API Identifier |
| `ending_at` | Yes | DateTime (ISO 8601 string) | Date on which the data export should end - defaults to time of the request |
| `starting_at` | No | DateTime (ISO 8601 string) | Date on which the data export should begin (either length or starting_at required) |
| `length` | No | String | Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) |
| `include_variant_breakdown` | No | Boolean | Whether or not to include variant stats (defaults to false)  |
| `include_step_breakdown`    | No | Boolean | Whether or not to include step stats (defaults to false) |
| `include_deleted_step_data` | No | Boolean | Whether or not to include step stats for deleted steps (defaults to false) |

## Response

`Content-Type: application/json`


```json
{
  "data": {
    "name": (string) Canvas name,
    "total_stats": {
      "revenue": (float),
      "conversions": (int),
      "conversions_by_entry_time": (int),
      "entries": (int)
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {
        "name": (string) name of variant,
        "revenue": (float),
        "conversions": (int),
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
          "android_push": (name of channel) [
            {
              "sent": (int),
              "opens": (int),
              "influenced_opens": (int),
              "bounces": (int)
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% endapi %}
