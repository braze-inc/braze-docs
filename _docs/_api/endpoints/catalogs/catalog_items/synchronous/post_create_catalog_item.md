---
nav_title: "POST: Create Catalog Item"
article_title: "POST: Create Catalog Item"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "This article outlines details about the Create Catalog Item Braze endpoint."

---
{% api %}
# Create a catalog item
{% apimethod post %}
/catalogs/catalog_name/items/item_id
{% endapimethod %}

Use this endpoint to create an item in your catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog item endpoints.

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_item`  | Required | String | Name of the imported catalog.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
	"items": [
        {
        	"count": 5
        }
        // will only accept 1 atom
    ]
}
```

## Example response

```json
{
	"items": [
		{
			"id": "0",
			"count": 5,
		}
	]
}
```

## Example error response

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog"
    },
    {
      "id": "item-already-exists",
      "message": "The item already exists"
    }
  ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `request-includes-too-many-items` | You can only create one catalog item per request. | 
| `id-in-body` | Remove any item IDs in the request body. |
| `invalid-ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores. |
| `ids-too-large` | Character limit for each item ID is 250 characters. |
| `items-too-large` | Character limit for each item is 5,000 characters. |
| `item-already-exists` | The item already exists in the catalog. |
| `invalid-fields` | Confirm that the fields in the request exist in the catalog. |
| `fields-do-not-match` | Fields must match the fields in the catalog. |
| `filtered-set-field-too-long` | The field value is being used in a filtered set that exceeds the character limit for an item. |
| `already-reached-catalog-item-limit` | Maximum number of catalogs reached. Contact your Braze account manager for more information. |
| `already-reached-company-item-limit` | Maximum number of catalog items reached. Contact your Braze account manager for more information. | 
| `unable-to-coerce-value` | Item types can't be converted. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}