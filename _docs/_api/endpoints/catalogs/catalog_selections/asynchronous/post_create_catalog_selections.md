---
nav_title: "POST: Create catalog selection"
article_title: "POST: Create Catalog Selection"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the Create catalog selection Braze endpoint."

---
{% api %}
# Create catalog selection
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Use this endpoint to create a selection in your catalog.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.create_selection` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Path parameters

| Parameter      | Required | Data Type | Description          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Required | String    | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Request parameters

| Parameter   | Required | Data Type | Description                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Required | Object    | An object that contains selection criteria. The selection objects could contain `name`, `description`, `filters`, `results_limit`, `sort_field`, and `sort_order`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example Request

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ]
  }
}'
```

### Filter operators

| Field type | Supported operators                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Response

There are three status code responses for this endpoint: `202`, `400`, and `404`.

### Example success response

The status code `202` could return the following response body.

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

| Error                                | Troubleshooting                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Check that the catalog name is valid.                                                         |
| `company-size-limit-already-reached` | The catalog storage size limit is reached.                                                    |
| `selection-limit-reached`            | The catalog selections limit is reached.                                                      |
| `invalid-selection`                  | Check that the selection is valid.                                                            |
| `too-many-filters`                   | Check if the selection has too many filters.                                                  |
| `selection-name-already-exists`      | Check if the selection name already exists in the catalog.                                    |
| `selection-has-invalid-filter`       | Check if the selection filter is valid.                                                       |
| `selection-invalid-results-limit`    | Check if the selection results limit is valid.                                                |
| `invalid-sorting`                    | Check if the selection sorting is valid.                                                      |
| `invalid-sort-field`                 | Check if the selection sort field is valid.                                                   |
| `invalid-sort-order`                 | Check if the selection sort order is valid.                                                   |
| `selection-contains-too-many-arrays` | Check if the selection contains more than one field with `array` type. Only one is supported. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
