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
/catalogs/:catalog_name/items
{% endapimethod %}

Use this endpoint to delete multiple items in your catalog. Each request can support up to 50 items. This endpoint is asynchronous. 

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate Limit

This endpoint has a shared rate limit of 100 requests per minute between all of the asynchronous catalog item endpoints.

## Request
### Path Parameters

| Parameter      | Required | Data Type | Description                                      |
|----------------|----------|-----------|--------------------------------------------------|
| `catalog_name` | Required | String    | Name of the catalog. Passed through the URL Path |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Request Body Parameters

| Parameter | Required | Data Type | Description                                                                                                                                                              |
|-----------|----------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `items`   | Required | Array     | An array that contains Item Objects. The item objects should contain an `"id"` referencing the items Braze should delete. Up to 50 item objects are allowed per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Example Request

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
### Status Codes

| Code  |
|-------|
| `202` |
| `400` |
| `404` | 
{: .reset-td-br-1}

### Example Successful Response
#### Status Code 
`202`
#### Response Body

```json
{
  "message": "success"
}
```

### Example Failure Response
#### Status Code
`400`
#### Response Body

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

The following table lists possible returned errors and their associated troubleshooting steps.

| Error                             | Troubleshooting                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------|
| `catalog-not-found`               | Check that the catalog name is valid.                                           |
| `request-includes-too-many-items` | Your request has too many items. The item limit per request is 50.              |
| `invalid-ids`                     | Item IDs can only include letters, numbers, hyphens, and underscores.           |
| `ids-too-large`                   | Item IDs can't be more than 250 characters.                                     |
| `ids-not-unique`                  | Check that the item IDs are unique in the request.                              |
| `ids-not-strings`                 | Item IDs must be of type string.                                                |
| `items-missing-ids`               | There are items that do not have item IDs. Check that each item has an item ID. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}