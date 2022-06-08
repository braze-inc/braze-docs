---
nav_title: "GET: List Product IDs"
article_title: "GET: List Product IDs"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the List Product IDs Braze endpoint."

---
{% api %}
# List product IDs endpoint
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

This endpoint returns paginated lists of product IDs.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='purchases product list' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `page`  | Optional | String | The page of your product list that you would like to view. |
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
    "5499334426779",
    "5499334819995",
    "5499335442587",
    "5499335835803",
    "Calendula Face Mask Peel",
    "Dior Lip Gloss",
    "Rice Bowl",
    "product_name"
  ],
  "message": "success"
}
```

{% endapi %}
