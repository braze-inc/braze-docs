---
nav_title: "GET: List Catalogs"
article_title: "GET: List Catalogs"
search_tag: Endpoint
page_order: 11

layout: api_page
page_type: reference
description: "This article outlines details about the List Catalogs Braze endpoint."

---
{% api %}
# List catalogs in app group
{% apimethod get %}
/catalogs/
{% endapimethod %}

Use this endpoint to return a list of catalogs in an app group.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a rate limit of 50 requests per minute.

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "catalogs": [
        {
            "name": "catalog_1",
            "description": "this is catalog_1",
            "last_updated": "2022-04-06T14:36:55+0000",
            "num_items": 1000,
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
        {
            "name": "catalog_2",
            "description": "this is catalog_2",
            "last_updated": "2022-03-03T12:10:33+0000",
            "num_items": 200,
            "fields": [
                {
                    "name": "id",
                    "type": "string" 
                },
                {
                    "name": "is_restaurant"
                    "type": "boolean"
                }
            ]
        }
    ]
}
```

{% endapi %}