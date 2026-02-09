---
nav_title: "DELETE: Delete catalog"
article_title: "DELETE: Delete Catalog"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Delete catalog Braze endpoint."

---
{% api %}
# Delete catalog
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> Use this endpoint to delete a catalog.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.delete` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example request

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Response

There are two status code responses for this endpoint: `200` and `404`.

### Example success response

The status code `200` could return the following response body:

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
