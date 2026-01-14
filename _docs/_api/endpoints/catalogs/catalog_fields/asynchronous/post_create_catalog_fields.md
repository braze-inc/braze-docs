---
nav_title: "POST: Create catalog fields"
article_title: "POST: Create Catalog Fields"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the Create catalog fields Braze endpoint."

---
{% api %}
# Create catalog fields
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Use this endpoint to create multiple fields in your catalog.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.create_fields` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Path parameters

| Parameter      | Required | Data Type | Description          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Required | String    | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Request parameters

| Parameter | Required | Data Type | Description                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Required | Array     | An array that contains field objects. The fields objects should contain the name and type of the new fields. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example Request

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
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

| Error                                | Troubleshooting                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | An arbitrary error occurred. Please try again or contact [Support]({{site.baseurl}}/support_contact/). |
| `catalog-not-found`                  | Check that the catalog name is valid.                                                                  |
| `company-size-limit-already-reached` | The catalog storage size limit is reached.                                                             |
| `request-includes-too-many-fields`   | Each request can support up to 50 new fields.                                                          |
| `catalog-exceeds-fields-limit`       | Catalog cannot have more than 500 fields.                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
