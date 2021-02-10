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

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `segment_id` | Yes | String | Segment API Identifier. |
| `length` | Yes | Integer | Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive. |
| `ending_at` | No | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Segment Identifier]({{site.baseurl}}/api/identifier_types/)
<br><br>
The `segment_id` for a given segment can be found in your Developer Console within your Braze account or you can use the [Segment List Endpoint]({{site.baseurl}}/api/endpoints/export/get_segment/).

## Example URL
`https://rest.iad-01.braze.com/segments/data_series?segment_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&length=14&ending_at=2018-06-27T23:59:59-5:00`

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
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
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
