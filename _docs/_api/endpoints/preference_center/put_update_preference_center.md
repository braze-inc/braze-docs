---
nav_title: "PUT: Update Preference Center"
article_title: "PUT: Update Preference Center"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the Update a preference center Braze endpoint."

---
{% api %}
# Update a preference center
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalId}
{% endapimethod %}

Use this endpoint to update a preference center.

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