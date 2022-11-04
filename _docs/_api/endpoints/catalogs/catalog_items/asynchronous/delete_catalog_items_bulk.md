---
nav_title: "DELETE: Delete Multiple Catalog Items"
article_title: "DELETE: Delete Multiple Catalog Items"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Delete Multiple Catalog Items Braze endpoint."

---
{% api %}
# Delete multiple catalog items
{% apimethod delete %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to delete multiple items in your catalog. Each request can support up to 50 items. This endpoint is asynchronous.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 100 requests per minute between all asynchronous catalog item endpoints.

## Request body

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "items": [ (max of 50 items)
        {"id": (required, item id)},
        {"id": (required, item id)},
    ]
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items`  | Required | Array | An array of item objects that include an `id` for the catalog items to be deleted. Maximum of 50 item objects per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example request

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## Response

### Example success responses

A status code `202` returns the following response.

```json
{
  "message": "success"
}
```

### Example error response 

A status code `400` or `404` returns the following response.

```json
{
    "errors": [
        {
            "id": "items-missing-ids",
            "message": "There are 1 item(s) that do not have ids",
            "parameters": [],
            "parameter_values": []
        }
    ],
    "message": "Invalid Request",
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `item-array-invalid` | `items` must be an array of objects. |
| `request-includes-too-many-items` | Your request has too many items. The maximum is 50. |
| `invalid-ids` | Item IDs can only include letters, numbers, hyphens, and underscores. |
| `ids-too-large` | Item IDs can't be more than 250 characters. |
| `ids-not-unique` | Item IDs must be unique in the request. |
| `ids-not-strings` | Item IDs must be of type string. |
| `items-missing-ids` | There are items that do not have item IDs. Check that each item has an item ID. |
| `items-too-large` | Item values can't exceed 5,000 characters. |
| `invalid-fields` | Confirm that the fields in the request exist in the catalog.                    |
| `fields-do-not-match` | Updated fields must match the fields in the catalog. |
| `unable-to-coerce-value` | Item types can't be converted. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}