---
nav_title: "POST: Create Catalog"
article_title: "POST: Create Catalog"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the Create Catalog Braze endpoint."

---
{% api %}
# Create catalog
{% apimethod post %}
/catalogs
{% endapimethod %}

Use this endpoint to create a catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 5 requests per minute between all synchronous catalog endpoints.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
	"catalogs": [
		{
			"name": "required, string",
            "description": "required, string",
            "fields": [
                {
                    "name": "required, string",
                    "type": "required, string" 
                },
                {
                    "name": "required, string",
                    "type": "required, string"
                }
            ]
        }
        // will only accept 1 item
    ]
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `name`  | Required | String | Name of the imported catalog.|
| `description` | Required | String | Description for the catalog. |
| `fields` | Required | Array of strings | Catalog items to create. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Example request

```json
curl --location --request POST 'https://rest.iad-01.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
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
|  `too-many-catalog-atoms` | Only 1 catalog is allowed per request. |
| `invalid_catalog_name` | Catalog name can only include letters, numbers, hyphens, and underscores. |
| `catalog-name-too-large` | Character limit for a catalog name is 250. |
| `catalog-name-already-exists` | Catalog with that name already exists. |
| `id-not-first-column` | The ID must be the first field in the array. Check that the type is a string. |
| `invalid-fields` | Field are not formatted correctly. |
| `too-many-fields` | Number of fields limit is 30. |
| `invalid-field-names` | Fields can only include letters, numbers, hyphens, and underscores. |
| `field-names-too-large` | Character limit for a field name is 250. |
| `field-names-not-unique` | Item types can't be converted. |
| `reached-company-catalogs-limit` | Maximum number of catalogs reached. Contact your Braze account manager for more information. |
| `description-too-long` | Character limit for description is 250. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}