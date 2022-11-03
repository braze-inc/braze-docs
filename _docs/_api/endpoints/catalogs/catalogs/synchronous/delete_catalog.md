---
nav_title: "DELETE: Delete Catalog"
article_title: "DELETE: Delete Catalog"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Delete Catalog Braze endpoint."

---
{% api %}
# Delete catalog
{% apimethod delete %}
/catalogs/:catalog_name
{% endapimethod %}

Use this endpoint to delete a catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate Limit

This endpoint has a shared rate limit of 5 requests per minute between all of the synchronous catalog endpoints.

## Request
### Route Parameters

| Parameter      | Required | Data Type | Description                                       |
|----------------|----------|-----------|---------------------------------------------------|
| `catalog_name` | Required | String    | Name of the catalog. Passed through the URL Route |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Request Body Parameters
There is no request body for this endpoint.

### Example Request

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Response
### Status Codes

| Code  |
|-------|
| `200` |
| `404` | 
{: .reset-td-br-1}

### Example Successful Response
#### Status Code
`200`
#### Response Body

```json
{
  "message": "success"
}
```

### Example Failure Response
#### Status Code
`404`
#### Response Body

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error               | Troubleshooting                       |
|---------------------|---------------------------------------|
| `catalog-not-found` | Check that the catalog name is valid. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}