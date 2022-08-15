---
nav_title: "POST: Catalog Items Bulk Patch"
permalink: /catalogs_items_patch/
hidden: true
layout: api_page

---
{% api %}
# Catalog items bulk patch
{% apimethod post %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to bulk edit items in your catalog.

{% alert important %}
Support for the this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
    "items": [
        {
            "id": "0",
            "count": 5
        },
        {
            "id": "1",
            "count": 10
        }
        // ... max of 50 items
    ]
}
```

{% endapi %}