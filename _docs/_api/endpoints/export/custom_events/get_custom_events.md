---
nav_title: "GET: Custom Events List"
page_order: 4

layout: api_page

page_type: reference
platform: API
description: "This article outlines details about the Custom Events List Endpoint."
---
{% api %}
# Get Custom Events List
{% apimethod get %}
/events/list
{% endapimethod %}

This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Custom%20events%20analytics%20export%20%20list%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `api_key` | Yes | String | App Group REST API Key |
| `page`    | No | Integer | The page of event names to return, defaults to 0 (returns the first set of up to 250) |

### Example URL
`https://rest.iad-01.braze.com/events/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1`

## Response

`Content-Type: application/json`

```json
Content-Type: application/json
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

{% endapi %}
