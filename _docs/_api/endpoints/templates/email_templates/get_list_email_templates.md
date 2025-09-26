---
nav_title: "GET: List available email templates"
article_title: "GET: List Available Email Templates"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the List available email templates Braze endpoint."

---
{% api %}
# List available email templates
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> Use this endpoint to get a list of available email templates in your Braze account.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Prerequisites
To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `templates.email.list` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `modified_after`  | Optional | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | Retrieve only templates updated at or after the given time. |
| `modified_before`  |  Optional | String in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | Retrieve only templates updated at or before the given time. |
| `limit` | Optional | Positive number | Maximum number of templates to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. |
| `offset`  |  Optional | Positive number | Number of templates to skip before returning rest of the templates that fit the search criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response 

{% alert important %}
Templates built using the drag-and-drop editor for email are not provided in this response.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}



