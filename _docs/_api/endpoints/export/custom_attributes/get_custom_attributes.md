---
nav_title: "GET: Export custom attributes"
article_title: "GET: Export Custom Attributes"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export custom attributes Braze endpoint."

---
{% api %}
# Export custom attributes
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> Use this endpoint to export a list of custom attributes recorded for your app. The attributes are returned in groups of 50, sorted alphabetically.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `custom_attributes.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## Query parameters

Note that each call to this endpoint will return 50 attributes. For more than 50 attributes, use the `Link` header to retrieve the data on the next page as shown in the following example response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `cursor` | Optional | String | Determines the pagination of the custom attributes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example requests

### Without cursor

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### With cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### Fatal error response codes {#fatal-export}

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference [Fatal errors]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
