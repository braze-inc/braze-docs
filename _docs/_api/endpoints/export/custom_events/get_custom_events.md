---
nav_title: "GET: Custom Events List"
page_order: 4

layout: api_page

page_type: reference
platform: API
description: "This article outlines details about the Custom events List Endpoint."
---
{% api %}
# Get Custom Events List
{% apimethod get %}
/events/list
{% endapimethod %}

This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Request Parameter

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `page`    | No | Integer | The page of event names to return, defaults to 0 (returns the first set of up to 250) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A",
        "Event B",
        "Event C",
        ...
    ]
}
```

### Fatal Error Response Codes {#fatal-export}

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code       | Reason / Cause                                                   |
| ---------------- | ---------------------------------------------------------------- |
| 400 Bad Request  | Bad Syntax                                                       |
| 401 Unauthorized | Unknown or missing REST API Key                                  |
| 429 Rate Limited | Over rate limit                                                  |
| 5XX              | Internal server error, you should retry with exponential backoff |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}


{% endapi %}
