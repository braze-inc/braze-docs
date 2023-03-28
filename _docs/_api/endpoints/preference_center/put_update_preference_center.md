---
nav_title: "PUT: Update Preference Center"
article_title: "PUT: Update Preference Center"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the Update a preference center Braze endpoint."

---
{% api %}
# Update a preference center
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Use this endpoint to update a preference center.

## Rate limit

This endpoint has a rate limit of 10 requests per minute, per workspace.

## Path parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Required | String | The ID for your preference center. |

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| Required | String | The HTML for the preference center page. |
|`preference_center_title`| Optional | String | The title for the preference center and confirmation pages. If a title is not specified, the title of the pages will default to "Preference Center". |
|`confirmation_page_html`| Required | String | The HTML for the confirmation page. |
|`state` | Optional | String | Choose `active` or `draft`.|
|`options` | Optional | Object | Attributes: `meta-viewport-content`. When present, a `viewport` meta tag will be added to the page with `content= <value of attribute>`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
```
{% endraw %}

## Example response
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
