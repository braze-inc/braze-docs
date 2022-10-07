---
nav_title: "POST: Create Catalog"
article_title: "POST: Create Catalog"
search_tag: Endpoint
page_order: 10

layout: api_page
page_type: reference
description: "This article outlines details about the Create Catalog Braze endpoint."

---
{% api %}
# Create catalog
{% apimethod post %}
/catalogs/
{% endapimethod %}

Use this endpoint to create a catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of X requests per minute between all bulk endpoints.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
	"catalogs": [
		{
			"name": "catalog_1",
            "description": "this is catalog_1",
            "fields": [
                {
                    "name": "id",
                    "type": "string" 
                },
                {
                    "name": "count"
                    "type": "number"
                }
            ]
        }
        // will only accept 1 atom
    ]
}
```

## Request parameters


## Example response

```json
{
    "catalogs": [
        {
            "name": "catalog_1",
            "description": "this is catalog_1",
            "last_updated": "2022-04-06T14:36:55+0000",
            "num_items": 1000,
            "size_in_mb": 25,
            "fields": [
            	{
            		"name": "id",
                    "type": "string" 
                },
                {
                	"name": "count"
                    "type": "number"
                }
            ]
        },
    ]
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `invalid_catalog_name` | Catalog name can only include letters, numbers, hyphens, and underscores. |
| `catalog-name-too-large` | Character limit for a catalog name is 250. |
| `catalog-name-already-exists` | Catalog with that name already exists. |
| `invalid-fields` | Field are not formatted correctly. |
| `too-many-fields` | Number of fields limit is 30. |
| `invalid-field-names` | Fields can only include letters, numbers, hyphens, and underscores. |
| `field-names-too-large` | Character limit for a field name is 250. |
| `field-names-not-unique` | Item types can be converted. |
| `reached-company-catalogs-limit` | Maximum number of catalogs reached. Contact your Braze account manager for more information. |
| `description-too-long` | Character limit for description is 250. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}