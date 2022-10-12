---
nav_title: "DELETE: Delete Multiple Catalog Items"
article_title: "DELETE: Delete Multiple Catalog Items"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the delete multiple catalog items Braze endpoint."

---
{% api %}
# Delete multiple catalog items
{% apimethod delete %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to delete multiple items in your catalog. Each request can support up to 50 items.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 100 requests per minute between all bulk endpoints.

## Request body

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "items": [
        {
            "id": "0"
        },
        {
            "id": "1"
        }
        // ... max of 50 items
    ]
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name`  | Required | String | Name of the imported catalog.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

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

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `invalid-ids` | Item IDs can only include letters, numbers, hyphens, and underscores. |
| `ids-too-large` | Item IDs can't be more than 250 characters. |
| `ids-not-unique` | Item IDs must be unique in the request. |
| `request-includes-too-many-items` | Your request has too many items. The maximum is 50.
| `fields-do-not-match` | Updated fields must match the fields in the catalog. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}