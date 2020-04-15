---
nav_title: "GET: List Available Email Templates"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the List Available Email Templates Braze endpoint."
---
{% api %}
# List Available Email Templates
{% apimethod get %}
/templates/email/list
{% endapimethod %}

Use this endpoint to get a list of available templates in your Braze account.

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Templates/ListEmailTemplates {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `modified_after`  | No | String in ISO 8601 | Retrieve only templates updated at or after the given time. |
| `modified_before`  |  No | String in ISO 8601 | Retrieve only templates updated at or before the given time. |
| `limit` | No | Positive Number | Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. |
| `offset` |  No | Positive Number | Number of templates to skip before returning rest of the templates that fit the search criteria. |

### Example URL
```
https://est.iad-01.braze.com/templates/email/list?modified_after=&modified_before&limit&offset
```

### Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=&modified_before&limit&offset' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Successful Response Properties

```json
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601),
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}
