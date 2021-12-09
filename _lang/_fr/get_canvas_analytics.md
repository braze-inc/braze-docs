---
nav_title: "GET: Canvas Data Series Analytics"
article_title: "GET: Canvas Data Series Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Canvas Data Series Analytics Endpoint."
---

{% api %}
# Canvas data series analytics endpoint
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

This endpoint allows you to export time series data for a Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## Request parameters

| Parameter                   | Required  | Data Type                                                                      | Description                                                                                                                                                                        |
| --------------------------- | --------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `canvas_id`                 | Required  | String                                                                         | See [Canvas API identifier]({{site.baseurl}}/api/identifier_types/).                                                                                                               |
| `ending_at`                 | Required  | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data export should end. Defaults to time of the request.                                                                                                         |
| `starting_at`               | Optional* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data export should begin. <br><br>* Either `length` or `starting_at` is required.                                                                    |
| `length`                    | Optional* | String                                                                         | Max number of days before `ending_at` to include in the returned series. Must be between 1 and 14 (inclusive). <br><br>* Either `length` or `starting_at` is required. |
| `include_variant_breakdown` | Optional  | Boolean                                                                        | Whether or not to include variant stats (defaults to false).                                                                                                                       |
| `include_step_breakdown`    | Optional  | Boolean                                                                        | Whether or not to include step stats (defaults to false).                                                                                                                          |
| `include_deleted_step_data` | Optional  | Boolean                                                                        | Whether or not to include step stats for deleted steps (defaults to false).                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
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
