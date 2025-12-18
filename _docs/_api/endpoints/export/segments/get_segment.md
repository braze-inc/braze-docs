---
nav_title: "GET: Export segment list"
article_title: "GET: Export Segment List"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about Export the segments list Braze endpoint."

---
{% api %}
# Export segment list
{% apimethod get %}
/segments/list
{% endapimethod %}

> Use this endpoint to export a list of segments, each of which will include its name, Segment API identifier, and whether it has analytics tracking enabled.

The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `segments.list` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | The page of segments to return, defaults to 0 (returns the first set of up to 100). |
| `sort_direction` | Optional | String | - Sort creation time from newest to oldest: pass in the value `desc`.<br> - Sort creation time from oldest to newest: pass in the value `asc`. <br><br>If `sort_direction` is not included, the default order is oldest to newest. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
