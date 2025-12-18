---
nav_title: "GET: Export send analytics"
article_title: "GET: Export Send Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export send analytics Braze endpoint."

---
{% api %}
# Export send analytics
{% apimethod get %}
/sends/data_series
{% endapimethod %}

> Use this endpoint to retrieve a daily series of various stats for a tracked `send_id` for API campaigns.

Braze stores send analytics for 14 days after the send. Campaign conversions will be attributed toward the most recent `send_id` that a given user has received from the campaign.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Prerequisites

This endpoint is for API campaigns only. To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `sends.data_series` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- |------------ |
| `campaign_id` | Required | String | See [campaign API identifier]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Required | String | See [Send API identifier]({{site.baseurl}}/api/identifier_types/). |
| `length` | Required | Integer | Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data series should end. Defaults to time of the request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time": (string) the date as ISO 8601 date,
            "messages": {
                "ios_push" : [
                    {
                      "variation_name": (string) variation name,
                      "sent": (int) the number of sends,
                      "delivered": (int) the number of messages successfully delivered,
                      "undelivered": (int) the number of undelivered,
                      "delivery_failed": (int) the number of rejected,
                      "direct_opens": (int) the number of direct opens,
                      "total_opens": (int) the number of total opens,
                      "bounces": (int) the number of bounces,
                      "body_clicks": (int) the number of body clicks,
                      "revenue": (float) the number of dollars of revenue (USD),
                      "unique_recipients": (int) the number of unique recipients at the campaign-level,
                      "conversions": (int) the number of conversions,
                      "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                      "conversions1": (optional, int) the number of conversions for the second conversion event,
                      "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                      "conversions2": (optional, int) the number of conversions for the third conversion event,
                      "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                      "conversions3_by_send_time": (optional, int) the number of conversions for the fourth, conversion event attributed to the date the campaign was sent
                      }
                  ]
            },
        "conversions_by_send_time": (optional, int),
        "conversions1_by_send_time": (optional, int),
        "conversions2_by_send_time": (optional, int),
        "conversions3_by_send_time": (optional, int),
        "conversions": (int),
        "conversions1": (optional, int),
        "conversions2": (optional, int),
        "conversions3": (optional, int),
        "unique_recipients": (int),
        "revenue": (optional, float)
      }
    ],
  "message": "success"
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
