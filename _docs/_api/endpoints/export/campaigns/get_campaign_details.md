---
nav_title: "GET: Campaign Details"
page_order: 4

layout: api_page2

page_type: reference
platform: API
tool: Segments
description: "This article outlines details about and using the Segments List endpoint to export a list of available Segments."
---

{% api %}

# Segment List Endpoint

{% apimethod get %}
/segments/list
{% endapimethod %}

This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Segment%20export%20%20list%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `api_key` | Yes | String    | App Group REST API Key |
| `page` | No | Integer   | The page of segments to return, defaults to 0 (returns the first set of up to 100) |
| `sort_direction` | No | String | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest. |

### Example URL
`https://rest.iad-01.braze.com/segments/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1`

## Response

`Content-Type: application/json`

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) Segment API Identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) tag names associated with the segment
        },
        ...
    ]
}
```

{% endapi %}
