---
nav_title: "GET: Export custom events list"
article_title: "GET: Export Custom Events List"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export custom events list Braze endpoint."

---
{% api %}
# Export custom events list
{% apimethod get %}
/events/list
{% endapimethod %}

> Use this endpoint to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `events.list` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='events list' %}

## Request parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | The page of event names to return, defaults to 0 (returns the first set of up to 250). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
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
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### Fatal error response codes {#fatal-export}

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference [Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
