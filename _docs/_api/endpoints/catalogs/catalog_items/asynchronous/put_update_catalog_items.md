---
nav_title: "PUT: Update Multiple Catalog Items"
article_title: "PUT: Update Multiple Catalog Items"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "This article outlines details about the Update multiple catalog items Braze endpoint."

---
{% api %}
# Update catalog items
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use this endpoint to update multiple items in your catalog. 

Each request can support up to 50 catalog items. This endpoint is asynchronous.

{% alert note %}
To use this endpoint, you'll need to generate an API key with the `catalogs.replace_items` permission.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | An array that contains item objects. Each object must have an ID. The item objects should contain fields that exist in the catalog. Up to 50 item objects are allowed per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example request

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2
    }
  ]
}'
```

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
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `request_includes_too_many_items` | Your request has too many items. The item limit per request is 50. |
| `ids_not_unique` | Check that each item ID is unique. |
| `ids_too_large` | Character limit for each item ID is 250 characters. |
| `ids_not_string` | Confirm that each item ID is a string. |
| `invalid_ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores. |
| `items_missing_ids` | Confirm that each item has an ID. |
| `items_too_large` | Item values can't exceed 5,000 characters. |
| `invalid_fields` | Confirm that the fields in the request exist in the catalog. |
| `unable_to_coerce_value` | Item types can't be converted. |
| `invalid_keys_in_value_object` | Item object keys can't include `.` or `$`. |
| `too_deep_nesting_in_value_object` | Item objects can't have more than 50 levels of nesting. |
| `item_array_invalid` | `items` must be an array of objects. |
| `catalog_not_found` | Check that the catalog name is valid. | 
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
