---
nav_title: "GET: View Details for Preference Center"
article_title: "GET: View Details for Preference Center"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the View details for preference center Braze endpoint."

---
{% api %}
# View details for preference center
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalId}
{% endapimethod %}

Use this endpoint to view the details for your preference centers, including when it was created and updated.

## Rate limit

This endpoint has a rate limit of 1,000 requests per minute, per app group.

## Example request

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response 
```json 
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null
}
```

{% endapi %}
