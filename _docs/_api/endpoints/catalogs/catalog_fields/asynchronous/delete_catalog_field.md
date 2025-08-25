---
nav_title: "DELETE: Delete catalog field"
article_title: "DELETE: Delete Catalog Field"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Delete catalog field Braze endpoint."

---
{% api %}
# Delete catalog field
{% apimethod delete %}
/catalogs/{catalog_name}/fields/{field_name}
{% endapimethod %}

> Use this endpoint to delete a catalog field.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.delete_fields` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Path parameters

| Parameter      | Required | Data Type | Description                |
| -------------- | -------- | --------- | -------------------------- |
| `catalog_name` | Required | String    | Name of the catalog.       |
| `field_name`   | Required | String    | Name of the catalog field. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example request

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/fields/ratings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Response

There are two status code responses for this endpoint: `202` and `404`.

### Example success response

The status code `202` could return the following response body:

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

| Error                           | Troubleshooting                                                  |
| ------------------------------- | ---------------------------------------------------------------- |
| `catalog-not-found`             | Check that the catalog name is valid.                            |
| `field-referenced-by-selection` | Check that the catalog field is currently in use by a selection. |
| `field-is-inventory`            | Check that the catalog field is used as an inventory field.      |
| `invalid-field-name`            | Check that the catalog field name is valid.                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
