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
/catalogs/{catalog_name}
{% endapimethod %}

Use this endpoint to delete a catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 5 requests per minute between all synchronous catalog endpoints.

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request parameters

There is no request body for this endpoint.

## Example request

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Response

There are two status code responses for this endpoint: `200` and `404`.

### Example success response

The status code `200` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `404` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

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

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}