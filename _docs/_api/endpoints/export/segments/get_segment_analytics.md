---
nav_title: "GET: Segment Analytics"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Email Addresses from the Spam List Braze endpoint."
---
{% api %}
# Segment Analytics Endpoint
{% apimethod get %}
/segments/data_series
{% endapimethod %}

This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Segment%20export%20%20analytics%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## Parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `segment_id` | Yes | String | Segment API Identifier. |
| `length` | Yes | Integer | Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive. |
| `ending_at` | No | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

The `segment_id` for a given segment can be found in your Developer Console within your Braze account or you can use the [Segment List Endpoint]({{site.baseurl}}/api/endpoints/export/get_segment/).

## Example URL
`https://rest.iad-01.braze.com/segments/data_series?segment_id=segment identifier&length=14&ending_at=2018-06-27T23:59:59-5:00`

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id=segment%20identifier&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

`Content-Type: application/json`

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "size" : (int) size of the segment on that date
        },
        ...
    ]
}
```

{% endapi %}
