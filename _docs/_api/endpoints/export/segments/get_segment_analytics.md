---
nav_title: "GET: Export Segment Analytics"
article_title: "GET: Export Segment Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export segment analytics Braze endpoint."

---
{% api %}
# Export segment analytics
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> Use this endpoint to retrieve a daily series of the estimated size of a segment over time.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `segment_id` | Required | String | See [Segment API identifier]({{site.baseurl}}/api/identifier_types/).<br><br> The `segment_id` for a given segment can be found at **Developer Console** > **API Settings** within your Braze account or you can use the [Export segment list endpoint]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
| `length` | Required | Integer | Max number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data series should end. Defaults to time of the request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), **API Settings** is now **API Keys** and can be found at **Settings** > **Setup and Testing** > **API Keys**.
{% endalert %}

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
