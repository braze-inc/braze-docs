---
nav_title: "POST: Create Catalog"
article_title: "POST: Create Catalog"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the Create Catalog Braze endpoint."

---
{% api %}
# Create catalog
{% apimethod post %}
/catalogs
{% endapimethod %}

Use this endpoint to create a catalog.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

If you'd like to share your feedback on this endpoint or make a request, contact the Braze Catalogs team at [catalogs-product@braze.com](mailto:catalogs-product@braze.com)

## Rate limit

This endpoint has a shared rate limit of 5 requests per minute between all synchronous catalog endpoints.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
	"catalogs": [ (max of 1 item)
		{
			"name": (required, string),
            "description": (required, string),
            "fields": [
                {
                    "name": (required, string),
                    "type": (required, string) 
                },
                {
                    "name": (required, string),
                    "type": (required, string)
                }
            ]
        }
    ]
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalogs` | Required | Array | An array that contains catalog objects. Only one catalog is allowed per request. Refer to the catalog object parameters in the following section. | 

#### Catalog object parameters 
| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `name`  | Required | String | Name of the catalog.|
| `description` | Required | String | Description for the catalog. |
| `fields` | Required | Array | An array that contains objects, which contains keys `"name"` and `"type"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Example request

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## Responses

There are two status code responses: `201` and `400`.

### Example success response

The status code `201` returns the following response.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### Example error response

The status code `400` returns the following response.

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
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
| `catalog-array-invalid` | `catalogs` must be an array of objects |
| `too-many-catalog-atoms` | You can only create one catalog per request. |
| `invalid_catalog_name` | Catalog name can only include letters, numbers, hyphens, and underscores. |
| `catalog-name-too-large` | Character limit for a catalog name is 250. |
| `catalog-name-already-exists` | Catalog with that name already exists. |
| `id-not-first-column` | The `id` must be the first field in the array. Check that the type is a string. |
| `invalid-fields` | `fields` is not formatted correctly. |
| `too-many-fields` | Number of fields limit is 30. |
| `invalid-field-names` | Fields can only include letters, numbers, hyphens, and underscores. |
| `invalid-field-types` | Make sure the field types are valid. |
| `field-names-too-large` | Character limit for a field name is 250. |
| `field-names-not-unique` | The same field name is referenced twice. |
| `reached-company-catalogs-limit` | Maximum number of catalogs reached. Contact your Braze account manager for more information. |
| `description-too-long` | Character limit for description is 250. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}