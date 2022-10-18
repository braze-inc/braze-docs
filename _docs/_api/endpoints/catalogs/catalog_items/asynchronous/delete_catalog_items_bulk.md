---
nav_title: "DELETE: Delete Multiple Catalog Items"
article_title: "DELETE: Delete Multiple Catalog Items"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the delete multiple catalog items Braze endpoint."

---
{% api %}
# Delete multiple catalog items
{% apimethod delete %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to delete multiple items in your catalog. Each request can support up to 50 items.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 100 requests per minute between all asynchronous catalog item endpoints.

## Request body

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "items": [ (max of 50 items)
        {
            "id": (required, item id)
        },
        {
            "id": (required, item id)
        },
    ]
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name`  | Required | String | Name of the imported catalog.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example request

```
https://rest.iad-03.braze.com/catalogs/catalog_name/items
```

## Example error response 

```json
{
  "errors": [
    {
        "id": "invalid-ids",
        "message": "Item ids can only include letters, numbers, hyphens, and underscores",
        "parameters": ["id"],
        "parameter_values": ["item_id"]
    },
    {
        "id": "items-missing-ids",
        "message": "There are 5 items that do not have ids",
        "parameters": [],
        "parameter_values": []
    }
    ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `invalid-ids` | Item IDs can only include letters, numbers, hyphens, and underscores. |
| `ids-too-large` | Item IDs can't be more than 250 characters. |
| `ids-not-unique` | Check that the item IDs are unique in the request. |
| `items-missing-ids` | There are items that do not have item IDs. Check that each item has an item ID. | 
| `request-includes-too-many-items` | Your request has too many items. The item limit per request is 50. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}