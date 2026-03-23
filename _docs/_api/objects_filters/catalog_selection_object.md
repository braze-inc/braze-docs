---
nav_title: "Catalog selection object"
article_title: API Catalog Selection Object
page_order: 12
page_type: reference
description: "This reference article explains the different components of the catalog selection object."
tool: Catalogs

---

# Catalog selection object

> When creating a catalog selection, you can provide a selection object to define the filtering, sorting, and limiting criteria for items returned from your catalog.

The `selection` object allows you to specify which items from your catalog should be included in the selection based on filters, how they should be sorted, and how many results to return. Use this object when creating catalog selections through the API.

## Object body

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Object details

| Key | Required | Data Type | Description |
| --- | -------- | --------- | ----------- |
| `name` | Required | String | The name of the catalog selection. |
| `description` | Optional | String | A description of the catalog selection. |
| `external_id` | Required | String | A unique identifier for the selection. |
| `source` | Required | String | The source of the catalog data. For Shopify catalogs, set this to `"Shopify"`. For non-Shopify catalogs, use a descriptive string such as `"custom"` or the name of your integration. |
| `filters` | Optional | Array of objects | An array of filter objects to apply to the catalog items. You can specify up to four filters per request. If no filters are provided, all items from the catalog are included. |
| `results_limit` | Optional | Integer | The maximum number of results to return. Must be a number between 1 and 50. |
| `sort_field` | Optional | String | The field to sort results by. This must be paired with `sort_order`. If both `sort_field` and `sort_order` are not present, results are returned in random order. |
| `sort_order` | Optional | String | The order to sort results. Accepted values are `"asc"` (ascending) or `"desc"` (descending). This must be paired with `sort_field`. If both `sort_field` and `sort_order` are not present, results are returned in random order. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Filter object

Each filter object in the `filters` array contains the fields described in the following table.

| Key | Required | Data Type                                   | Description |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Required | String                                      | The catalog field to filter on. |
| `operator` | Required | String                                      | The comparison operator to use for filtering. Examples include `"includes value"` and `"does not include value"`. |
| `value`    | Required | Varies (string, number, boolean, time)     | The value to compare against. This must match the data type of the underlying catalog field (for example, string, number, boolean, time). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
The API supports a maximum of four filters per selection request. In the Braze dashboard, you can add up to 10 filters per selection. Filters are applied in the order they appear in the array.
{% endalert %}
