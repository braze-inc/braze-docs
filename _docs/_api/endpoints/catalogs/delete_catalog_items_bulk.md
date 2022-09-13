---
nav_title: "DELETE: Delete Multiple Catalog Items"
article_title: "DELETE: Delete Multiple Catalog Items"
search_tag: Endpoint
page_order: 1

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

## Rate limit

This endpoint has a rate limit of 100 requests per minute.

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

## Possible errors

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| catalog-not-found | Check that the catalog name is valid. |
| invalid-ids | Item IDs can only include letters, numbers, hyphens, and underscores. |
| ids-too-large | Item IDs can't be more than 250 characters. |
| items-too-large | Item values can't exceed 5,000 characters. |
| referenced-same-id-multiple-times | Item IDs must be unique in the request. |
| request-includes-too-many-items | Your request has too many items. The maximum is 50.
| fields-do-not-match | Updated fields must match the fields in the catalog. |
| unable-to-coerce | Item types can be converted. |
| arbitrary-error | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}