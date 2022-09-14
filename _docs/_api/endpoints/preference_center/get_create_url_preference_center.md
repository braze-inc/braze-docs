---
nav_title: "GET: Generate Preference Center URL"
article_title: "GET: Generate Preference Center URL"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Generate preference center URL Braze endpoint."

---
{% api %}
# Generate preference center URL
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalId}/url/{userId}
{% endapimethod %}

Use this endpoint to list preference centers.

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