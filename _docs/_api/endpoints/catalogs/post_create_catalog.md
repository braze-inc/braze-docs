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
{% apimethod get %}
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

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

