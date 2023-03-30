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

{% endapi %}