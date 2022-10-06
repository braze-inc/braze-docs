---
nav_title: "DELETE: Delete Catalog"
article_title: "DELETE: Delete Catalog"
search_tag: Endpoint
page_order: 12

layout: api_page
page_type: reference
description: "This article outlines details about the Delete Catalog Braze endpoint."

---
{% api %}
# Delete catalog
{% apimethod delete %}
/catalogs/catalog_name/
{% endapimethod %}

Use this endpoint to delete multiple items in your catalog. Each request can support up to 50 items.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of X requests per minute between all bulk endpoints.

{% endapi %}