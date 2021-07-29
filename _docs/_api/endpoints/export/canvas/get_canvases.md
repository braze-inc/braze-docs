---
nav_title: "GET: Canvas List"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Canvas
description: "This article outlines details about the Canvas List endpoint ."
---
{% api %}
# Canvas List Endpoint
{% apimethod get %}
/canvas/list
{% endapimethod %}

This endpoint allows you to export a list of Canvases, including the name, Canvas API Identifier and associated Tags. The Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).

Archived Canvases will not be included in the API response unless the `include_archived` field is specified. Canvases that are stopped but not archived, however, will be returned by default.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer   | The page of Canvases to return, defaults to `0` (returns the first set of up to 100) |
| `include_archived` | Optional | Boolean | Whether or not to include archived Canvases, defaults to `false`. |
| `sort_direction` | Optional | String | - Sort creation time from newest to oldest: pass in the value `desc`.<br> - Sort creation time from oldest to newest: pass in the value `asc`. <br><br>If `sort_direction` is not included, the default order is oldest to newest. |
| `last_edit.time[gt]` | Optional | Time | Filters the results and only returns Canvases that were edited greater than the time provided till now. Format is `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Request
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) Canvas API Identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) Canvas name,
  		"tags" : (array) tag names associated with the Canvas,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
