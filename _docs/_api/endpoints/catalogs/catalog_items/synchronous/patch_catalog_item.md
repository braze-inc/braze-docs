---
nav_title: "PATCH: Edit Catalog Item"
article_title: "PATCH: Edit Catalog Item"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "This article outlines details about the Edit Catalog Item Braze endpoint."

---
{% api %}
# Edit catalog item
{% apimethod patch %}
/catalogs/catalog_name/items/item_id
{% endapimethod %}

Use this endpoint to edit an item in your catalog. 

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog item endpoints.

## Request body
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
    "items": [ (max of 50 items)
        {
            "id": (required, item id)
            "count": (required, item count)
        },
    ]
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name`  | Required | String | Name of the catalog. Passed through the URL path. |
| `item_id `  |  Required | String | Item ID for a catalog item. Passed through the URL path. |
| `items` | Required | Array | An array of item objects that include an `id` for the catalog items to be deleted. Maximum of 50 item objects per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example request

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
    "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Example responses

There are two status code responses: `200`, `400`, and `404`.

### Example success response

The status code `200` returns the following response.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` returns the following response.

```json
{
  "errors": [
    {
      "id": "ids-too-large",
      "message": "Item ids can not be larger than 250 characters",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `item-not-found` | Check that the item is in the catalog. |
| `item-array-invalid` | `items` must be an array of objects. |
| `request-includes-too-many-items` | You can only edit one catalog item per request. |
| `id-in-body` | An item ID already exists in the catalog. |
| `invalid-ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores.                 |
| `ids-too-large` | Character limit for each item ID is 250 characters. |
| `items-too-large` | Character limit for each item is 5,000 characters. |
| `invalid-fields` | Confirm that the fields in the request exist in the catalog. |
| `unable-to-coerce-value` | Item types can't be converted. |
| `filtered-set-field-too-long` | The field value is being used in a filtered set that exceeds the character limit for an item. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}