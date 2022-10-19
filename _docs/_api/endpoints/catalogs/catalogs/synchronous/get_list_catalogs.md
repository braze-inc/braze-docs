---
nav_title: "GET: List Catalogs"
article_title: "GET: List Catalogs"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the List Catalogs Braze endpoint."

---
{% api %}
# List catalogs in app group
{% apimethod get %}
/catalogs
{% endapimethod %}

Use this endpoint to return a list of catalogs in an app group.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 5 requests per minute between all synchronous catalog endpoints.

## Example request

```
https://rest.iad-03.braze.com/catalogs
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "catalogs": [
        {
            "description": "this is catalog 1",
            "fields": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "rating",
                    "type": "number"
                }
            ],
            "name": "catalog_1",
            "num_items": 5,
            "updated_at": "2022-09-27T15:49:18.818+00:00"
        },
        {
            "description": "this is catalog_2",
            "fields": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "column_1",
                    "type": "string"
                },
                {
                    "name": "column_2",
                    "type": "number"
                },
                {
                    "name": "column_3",
                    "type": "boolean"
                },
                {
                    "name": "column_4",
                    "type": "time"
                },
            ],
            "name": "catalog_2",
            "num_items": 10,
            "updated_at": "2022-08-31T20:22:56.127+00:00"
        }
    ]
}
```

{% endapi %}