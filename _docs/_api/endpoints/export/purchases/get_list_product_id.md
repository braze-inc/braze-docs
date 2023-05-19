---
nav_title: "GET: Export Product IDs"
article_title: "GET: Export Product IDs"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the Export product IDs Braze endpoint."

---
{% api %}
# Export product IDs
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> Use this endpoint to return a paginated lists of product IDs.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `page` | Optional | String | The page of your product list that you would like to view. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting](https://www.braze.com/docs/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}
