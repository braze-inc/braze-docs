---
nav_title: "PUT: Update Catalog Item"
article_title: "PUT: Update Catalog Item"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "This article outlines details about the Update catalog item Braze endpoint."

---
{% api %}
# Update catalog item
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Use this endpoint to update an item in your catalog. 

If the `item_id` isn't found, this endpoint will create the item. This endpoint is synchronous.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

{% alert note %}
To use this endpoint, you'll need to generate an API key with the `catalogs.replace_item` permission.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
| `item_id` | Required | String | The ID of the catalog item. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | An array that contains item objects. The item objects should contain fields that exist in the catalog except for the `id` field. Only one item object is allowed per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example request

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Response

There are three status code responses for this endpoint: `200`, `400`, and `404`.

### Example success response

The status code `200` could return the following response body.

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
| `already_reached_catalog_item_limit` | Maximum number of catalogs reached. Contact your Braze account manager for more information. |
| `already_reached_company_item_limit` | Maximum number of items reached. Contact your Braze account manager for more information. |
| `arbitrary_error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
| `catalog_not_found` | Check that the catalog name is valid. |
| `filtered-set-field-too-long` | The field value is being used in a filtered set that exceeds the character limit for an item. |
| `id_in_body` | Remove any item IDs in the request body. |
| `ids_too_large` | Character limit for each item ID is 250 characters. |
| `invalid_ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores. |
| `invalid_fields` | Confirm that the fields in the request exist in the catalog. |
| `invalid_keys_in_value_object` | Item object keys can't include `.` or `$`. |
| `item_already_exists` | The item already exists in the catalog. |
| `item_array_invalid` | `items` must be an array of objects. |
| `items_too_large` | Item values can't exceed 5,000 characters. |
| `request_includes_too_many_items` | Your request has too many items. The item limit per request is 50. |
| `too_deep_nesting_in_value_object` | Item objects can't have more than 50 levels of nesting. |
| `unable_to_coerce_value` | Item types can't be converted. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}