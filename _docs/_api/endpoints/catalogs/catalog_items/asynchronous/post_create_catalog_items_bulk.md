---
nav_title: "POST: Create Multiple Catalog Items"
article_title: "POST: Create Multiple Catalog Items"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the Create Multiple Catalog Items Braze endpoint."

---
{% api %}
# Create multiple catalog items
{% apimethod post %}
/catalogs/catalog_name/items
{% endapimethod %}

Use this endpoint to create multiple items in your catalog. Each request can support up to 50 items. This endpoint is asynchronous.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 100 requests per minute between all asynchronous catalog item endpoints.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
    "items": [ (max of 50 items)
        {
            "id": (required, item id),
            "count": (required, item count),
        },
        {
            "id": (required, item id),
            "count": (required, item count),
        },
        {
            "id": (required, item id),
            "count": (required, item count),
        }
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
curl --location --request POST 'https://rest.iad-01.braze.com/catalogs/catalog_name/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Response

There are three status code responses: `202`, `400`, and `404`.

### Example success responses

The status code `202` returns the following response.

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
            "id": "fields-do-not-match",
            "message": "Fields do not match with fields on the catalog",
            "parameters": [
                "id"
            ],
            "parameter_values": [
                "restaurant2"
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
| `invalid-ids` | Item IDs can only include letters, numbers, hyphens, and underscores. |
| `ids-too-large` | Item IDs can't be more than 250 characters. |
| `ids-not-unique` | Item IDs must be unique in the request. |
| `items-missing-ids` | There are items that do not have item IDs. Check that each item has an item ID. |
| `items-too-large` | Item values can't exceed 5,000 characters. |
| `request-includes-too-many-items` | Your request has too many items. The maximum is 50. |
| `invalid-fields` | Confirm that the fields in the request exist in the catalog. |
| `fields-do-not-match` | Updated fields must match the fields in the catalog. |
| `unable-to-coerce-value` | Item types can't be converted. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}