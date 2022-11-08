---
nav_title: "GET: List Catalog Item Details"
article_title: "GET: List Catalog Item Details"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the List Catalog Item Details Braze endpoint."

---
{% api %}
# List catalog item details
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

Use this endpoint to return a catalog item and its content.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog item endpoints.

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
| `item_id` | Required | String | The ID of the catalog item. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request parameters

There is no request body for this endpoint.

## Example request

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are two status code responses for this endpoint: `200` and `404`.

### Example success response

The status code `200` could return the following response body.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Example error response

The status code `404` could return the following response. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `item-not-found` | Check that the item is in the catalog. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}