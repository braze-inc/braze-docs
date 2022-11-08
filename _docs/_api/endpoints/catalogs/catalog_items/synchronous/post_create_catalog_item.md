---
nav_title: "POST: Create Catalog Item"
article_title: "POST: Create Catalog Item"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "This article outlines details about the Create Catalog Item Braze endpoint."

---
{% api %}
# Create a catalog item
{% apimethod post %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

Use this endpoint to create an item in your catalog.

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

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | An array that contains item objects. The item objects should contain all of the fields in the catalog except for the `id` field. Only one item object is allowed per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example Request

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    }
  ]
}'
```

## Response

There are three status code responses for this endpoint: `201`, `400`, and `404`.

### Example success response

The status code `201` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

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
| `item-array-invalid` | `items` must be an array of objects. |
| `request-includes-too-many-items` | You can only create one catalog item per request. | 
| `id-in-body` | Remove any item IDs in the request body. |
| `invalid-ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores. |
| `ids-too-large` | Character limit for each item ID is 250 characters. |
| `items-too-large` | Character limit for each item is 5,000 characters. |
| `item-already-exists` | The item already exists in the catalog. |
| `invalid-fields` | Confirm that the fields in the request exist in the catalog. |
| `fields-do-not-match` | Fields must match the fields in the catalog. |
| `filtered-set-field-too-long` | The field value is being used in a filtered set that exceeds the character limit for an item. |
| `already-reached-catalog-item-limit` | Maximum number of catalogs reached. Contact your Braze account manager for more information. |
| `already-reached-company-item-limit` | Maximum number of catalog items reached. Contact your Braze account manager for more information. | 
| `unable-to-coerce-value` | Item types can't be converted. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}