---
nav_title: "DELETE: Delete Catalog Item"
article_title: "DELETE: Delete Catalog Item"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the Delete Catalog Item Braze endpoint."

---
{% api %}
# Delete a catalog item
{% apimethod delete %}
/catalogs/catalog_name/items/item_id
{% endapimethod %}

Use this endpoint to delete an item in your catalog. 

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of X requests per minute.

## Request body (need example)



### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name`  | Required | String | Name of the imported catalog.|
| `item_id` | Required | String | Item ID. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example error response 

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog"
    },
    {
      "id": "item-not-found",
      "message": "Could not find item"
    }
  ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `item-not-found`| Check that the item to be deleted exists in your catalog. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}