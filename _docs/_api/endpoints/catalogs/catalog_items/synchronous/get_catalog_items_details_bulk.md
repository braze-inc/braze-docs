---
nav_title: "GET: List multiple catalog item details"
article_title: "GET: List Multiple Catalog Item Details"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the List multiple catalog item details Braze endpoint."

---
{% api %}
# List multiple catalog item details
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use this endpoint to return multiple catalog items and their content.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.get_items` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Query parameters

Note that each call to this endpoint will return 50 items. For a catalog with more than 50 items, use the `Link` header to retrieve the data on the next page as shown in the following example response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `cursor` | Optional | String | Determines the pagination of the catalog items. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Request parameters

There is no request body for this endpoint.

## Example requests

### Without cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### With cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

There are three status code responses for this endpoint: `200`, `400`, and `404`.

### Example success response

The status code `200` could return the following response header and body.

{% alert note %}
The `Link` header won't exist if the catalog has less than or equal to 50 items. For calls without a cursor, `prev` will not show. When looking at the last page of items, `next` will not show.
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
  "errors": [
    {
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
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
| `invalid-cursor` | Check that your `cursor` is valid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
