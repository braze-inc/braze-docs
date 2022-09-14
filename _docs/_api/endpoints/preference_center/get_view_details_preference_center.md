---
nav_title: "GET: View Details for Preference Centers"
article_title: "GET: View Details for Preference Centers"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the View details for preference centers Braze endpoint."

---
{% api %}
# List preference centers
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalId}
{% endapimethod %}

Use this endpoint to view the details for your preference centers.

{% alert important %}
Support for this endpoint is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Rate limit


## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string"
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`name`| Required | String | The name of the preference center. |
|`preference_center_page_html`| Optional | String | The HTML for the preference center page. |
|`confirmation_page_html`| Optional | String | The HTML for the confirmation page. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request example
{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example Preference Center",
  "preference_center_page_html": "HTML for preference center"
  "confirmation_page_html": "HTML here with a message to users."

```
{% endraw %}

{% endapi %}