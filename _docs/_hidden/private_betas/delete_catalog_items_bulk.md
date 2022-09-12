---
nav_title: "DELETE: Delete Multiple Catalog Items"
permalink: /catalogs_bulk_delete/
hidden: true
layout: api_page

---
{% api %}
# Delete catalog items in bulk
{% apimethod patch %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to bulk delete items in your catalog. Each request can support up to 50 items.

{% alert important %}
Support for the this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Rate limit

This endpoint has a rate limit of 100 requests per minute.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

## Example error response 

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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


{% endapi %}