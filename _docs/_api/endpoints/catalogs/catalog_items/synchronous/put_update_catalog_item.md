---
nav_title: "PUT: Replace catalog item"
article_title: "PUT: Replace Catalog Item"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "This article outlines details about the Replace catalog item Braze endpoint."

---
{% api %}
# Replace catalog item
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Use this endpoint to replace an item in your catalog.

If the `item_id` isn't found, this endpoint will create the item in your catalog. This endpoint is synchronous.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.replace_item` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
| `item_id` | Required | String | The ID of the catalog item. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | An array that contains item objects. The item objects should contain fields that exist in the catalog except for the `id` field. Only one item object is allowed per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

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
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
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
| `arbitrary-error` | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Check that the catalog name is valid. |
| `filtered-set-field-too-long` | The field value is being used in a filtered set that exceeds the character limit for an item. |
| `id-in-body` | Remove any item IDs in the request body. |
| `ids-too-large` | Character limit for each item ID is 250 characters. |
| `invalid-ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores. |
| `invalid-fields` | Confirm that all fields you are sending in the API request already exist in the catalog. This is not related to the ID field mentioned in the error. |
| `invalid-keys-in-value-object` | Item object keys can't include `.` or `$`. |
| `item-already-exists` | The item already exists in the catalog. |
| `item-array-invalid` | `items` must be an array of objects. |
| `items-too-large` | Character limit for each item is 5,000 characters. |
| `request-includes-too-many-items` | You can only create one catalog item per request. |
| `too-deep-nesting-in-value-object` | Item objects can't have more than 50 levels of nesting. |
| `unable-to-coerce-value` | Item types can't be converted. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
