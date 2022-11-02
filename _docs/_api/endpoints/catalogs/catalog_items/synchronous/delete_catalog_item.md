---
nav_title: "DELETE: Delete Catalog Item"
article_title: "DELETE: Delete Catalog Item"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Delete Catalog Item Braze endpoint."

---
{% api %}
# Delete a catalog item
{% apimethod delete %}
/catalogs/:catalog_name/items/:item_id
{% endapimethod %}

Use this endpoint to delete an item in your catalog. 

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all of the synchronous catalog item endpoints.

## Request

### Route parameters
| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `catalog_name` | Required | String | Name of the catalog. Passed through the URL Route |
| `item_id`  | Required | String | The ID of the catalog item. Passed through the URL Route |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Request Body parameters
There is no request body for this endpoint.

### Example request

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

### Status Codes
| Code  |
|---|
| `200` |
| `400` |
| `404` | 
{: .reset-td-br-1}

### Example Successful Response

Status Code: `200`

Response Body

```json
{
  "message": "success"
}
```

### Example Failure Response

Status Code: `404`

Response Body

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
| `item-not-found`| Check that the item to be deleted exists in your catalog. |
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}