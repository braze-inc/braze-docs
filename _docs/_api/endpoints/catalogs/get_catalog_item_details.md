---
nav_title: "GET: List Catalog Item Details"
article_title: "GET: List Catalog Item Details"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the list catalog item details Braze endpoint."

---
{% api %}
# List catalog item details
{% apimethod get %}
/catalogs/catalog_name/items/item_id
{% endapimethod %}

Use this endpoint to return a catalog item and its content.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Rate limit

This endpoint has a rate limit of 100 requests per minute.

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_item`  | Required | String | Name of the catalog.|
| `item_id `  |  Required | String | The item ID of the catalog item. |
{: .reset-td-br-1 .reset-td-br-2}

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
"items": [
    {
        "id": "0",
        "count": 5,
    }
]
```

## Possible errors

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| catalog-not-found | Check that the catalog name is valid. |
| item-not-found | Check that the item is in the catalog. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}