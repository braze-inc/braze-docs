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
# Export product IDs
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Use this endpoint to return a time series of purchases made.

## Rate limit

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `ending_at` | Optional | Datetime (ISO-8601 string) | Date on which the data export should end. Defaults to time of the request. |
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
