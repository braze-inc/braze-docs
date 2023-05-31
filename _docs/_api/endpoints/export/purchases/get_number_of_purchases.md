---
nav_title: "GET: Export Number of Purchases"
article_title: "GET: Export Number of Purchases"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the Export number of purchases Braze endpoint."

---
{% api %}
# Export number of purchases
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Use this endpoint to return the number of purchases made within a specific time.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `ending_at` | Optional | Datetime (ISO-8601 string) | Date on which the data export should end. Defaults to time of the request. |
| `length` | Required | Integer | Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `unit` | Optional | String | Unit of time between data points. Can be day or hour, defaults to day. |
| `app_id` | Optional | String | App API identifier retrieved from the **API Keys** page. If excluded, results for all apps in a workspace will be returned. |
| `product` | Optional | String | Name of product to filter response by. If excluded, results for all apps will be returned. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  “data”: [{
        "time": "2023-04-03",
        "purchase_quantity": 118
      },
      {
        "time": "2023-04-04",
        "purchase_quantity": 127
      }],
  “message”: “success”
}
```

{% endapi %}

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting](https://www.braze.com/docs/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}
