---
nav_title: "GET: List Multiple Catalog Item Details"
article_title: "GET: List Multiple Catalog Item Details"
search_tag: Endpoint
page_order: 16

layout: api_page
page_type: reference
description: "This article outlines details about the List Multiple Catalog Item Details Braze endpoint."

---
{% api %}
# List multiple catalog item details
{% apimethod get %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to return multiple catalog items and their content.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a rate limit of 50 requests per minute.

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_item`  | Required | String | Name of the imported catalog.|
| `item_id `  |  Required | String | The item ID of the imported catalog item. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example response

```json
{
    "items": [
        {
            "id": "0",
            "count": 1,
        },
        {
            "id": "1",
            "count": 2,
        },
        {
            "id": "2",
            "count": 3,
        }
        // ... max of 50 items
    ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}