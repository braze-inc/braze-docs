---
nav_title: "PATCH: Edit Catalog Item"
article_title: "PATCH: Edit Catalog Item"
search_tag: Endpoint
page_order: 7

layout: api_page
page_type: reference
description: "This article outlines details about the Edit Catalog Item Braze endpoint."

---
{% api %}
# Edit catalog item
{% apimethod patch %}
/catalogs/catalog_name/items/item_id
{% endapimethod %}

Use this endpoint to edit an item in your catalog. 

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of X requests per minute.

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
      "id": "item-not-found",
      "message": "Could not find item"
    }
  ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `request-includes-too-many-items` | You can only edit one item in your catalog per request. |
| `fields-do-not-match` | The item's fields must match with the fields in the catalog. |
| `items-too-large` | Character limit for each item is 5,000 characters. |
| `filtered-set-field-too-long` | The field value is being used in a filtered set that exceeds the character limit for an item. |
| `unable-to-coerce` | Item types can be converted. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}