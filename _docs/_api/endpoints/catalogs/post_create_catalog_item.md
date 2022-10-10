---
nav_title: "POST: Create Catalog Item"
article_title: "POST: Create Catalog Item"
search_tag: Endpoint
page_order: 11

layout: api_page
page_type: reference
description: "This article outlines details about the Create Catalog Item Braze endpoint."

---
{% api %}
# Create a catalog item
{% apimethod post %}
/catalogs/catalog_name/items/item_id/
{% endapimethod %}

Use this endpoint to create an item in your catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

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
| `request-includes-too-many-items` | You can only create one catalog item per request. | 
| `id-in-body` | Remove any item IDs in the request body. |
| `catalog-not-found` | Check that the catalog name is valid. |
| `item-already-exists` | The catalog item already exists. |
| `items-too-large` | Item values can't exceed 5,000 characters. |
| `ids-not-unique` | Item IDs must be unique in the request. |
| `request-includes-too-many-items` | Your request has too many items. The maximum is 50. |
| `fields-do-not-match` | Fields must match the fields in the catalog. |
| `unable-to-coerce` | Item types can't be converted. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}