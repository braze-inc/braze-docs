---
nav_title: "GET: Canvas Data Summary Analytics"
article_title: "GET: Canvas Data Summary Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Canvas Data Summary Analytics Endpoint."

---
{% api %}
# Canvas data summary endpoint
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas' results.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Required | String | See [Canvas API identifier]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Required | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data export should end. Defaults to time of the request. |
| `starting_at` | Optional* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data export should begin. <br><br>* Either `length` or `starting_at` is required. |
| `length` | Optional* | String | Max number of days before `ending_at` to include in the returned series. Must be between 1 and 14 (inclusive). <br><br>* Either `length` or `starting_at` is required. |
| `include_variant_breakdown` | Optional | Boolean | Whether or not to include variant stats (defaults to false).  |
| `include_step_breakdown`    | Optional | Boolean | Whether or not to include step stats (defaults to false). |
| `include_deleted_step_data` | Optional | Boolean | Whether or not to include step stats for deleted steps (defaults to false). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
