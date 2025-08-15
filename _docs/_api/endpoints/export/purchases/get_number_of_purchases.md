---
nav_title: "GET: Export number of purchases"
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

> Use this endpoint to return the total number of purchases in your app over a time range.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `purchases.quantity_series` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `ending_at` | Optional | Datetime ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data export should end. Defaults to time of the request. |
| `length` | Required | Integer | Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `unit` | Optional | String | Unit of time between data points. Can be day or hour, defaults to day. |
| `app_id` | Optional | String | App API identifier retrieved from the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page. If excluded, results for all apps in a workspace will be returned. |
| `product` | Optional | String | Name of product to filter response by. If excluded, results for all apps will be returned. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}
