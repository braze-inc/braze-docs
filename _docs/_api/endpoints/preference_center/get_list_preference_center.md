---
nav_title: "GET: List Preference Centers"
article_title: "GET: List Preference Centers"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the List preference centers Braze endpoint."

---
{% api %}
# List preference centers
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

Use this endpoint to list your available preference centers.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Rate limit

This endpoint has a rate limit of 1,000 requests per minute, per app group.

## Example request

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response
```json
{
  "preference_centers":
    {
      "name": "Example",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "example_time_created",
      "updated_at": "example_time_updated"
    }
}
```

{% endapi %}