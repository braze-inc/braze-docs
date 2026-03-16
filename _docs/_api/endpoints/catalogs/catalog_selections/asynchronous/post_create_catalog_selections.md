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
| `selection` | Required | Object    | An object that contains selection criteria. See [catalog selection object]({{site.baseurl}}/api/objects_filters/catalog_selection_object/) for a full breakdown of the object and its fields. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Selection object parameters

| Parameter        | Required | Data Type | Description                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | Required | String    | The name of the catalog selection. |
| `description`    | Optional | String    | A description of the catalog selection. |
| `external_id`    | Required | String    | A unique identifier for the selection. |
| `source`         | Required | String    | The source of the catalog data. For Shopify catalogs, use `"Shopify"`. For custom catalogs, use `"custom"`. |
| `filters`        | Optional | Array    | An array of filter objects to apply to the catalog items. You can specify up to four filters per request. If no filters are provided, all items from the catalog are included. |
| `results_limit`  | Optional | Integer   | The maximum number of results to return. Must be a number between 1 and 50. |
| `sort_field`     | Optional | String    | The field to sort results by. This must be paired with `sort_order`. If both `sort_field` and `sort_order` are not present, the results are randomized. |
| `sort_order`     | Optional | String    | The order to sort results. Accepted values are `"asc"` (ascending) or `"desc"` (descending). This must be paired with `sort_field`. If both `sort_field` and `sort_order` are not present, the results are randomized. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
The `sort_field` and `sort_order` parameters must be used together. If you provide one without the other, or if you omit both parameters, the selection results are returned in a randomized order.
{% endalert %}

## Example Request

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "custom",
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
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
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

{% alert note %}
The API supports a maximum of four filters per selection request. In the Braze dashboard, you can add up to 10 filters per selection. Filters are applied in the order they appear in the array.
{% endalert %}

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
