---
nav_title: "GET: Export News Feed Card Analytics"
article_title: "GET: Export News Feed Card Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export News Feed card analytics Braze endpoint."

---
{% api %}
# Export News Feed card analytics
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> Use this endpoint to retrieve a daily series of engagement stats for a card over time.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `feed.data_series` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter   | Required | Data Type | Description |
| ----------- | -------- | --------- | ----------- |
| `card_id` | Required | String | See [Card API identifier]({{site.baseurl}}/api/identifier_types/). <br><br> The `card_id` for a given card can be found on the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page and on the card details page within your dashboard, or you can use the [Export News Feed cards list endpoint]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
| `length` | Required | Integer | Maximum number of units (days or hours) before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `unit` | Optional | String | Unit of time between data points. Can be `day` or `hour`, defaults to `day`.  |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data series should end. Defaults to time of the request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
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
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
