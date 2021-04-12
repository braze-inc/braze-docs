---
nav_title: "GET: See Email Template Information"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the See Email Template Braze endpoint."
---
{% api %}
# See Email Template Information
{% apimethod get %}
/templates/email/info
{% endapimethod %}

Use to get information on your email templates.

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

{% alert important %}
Templates built using the Drag & drop editor are not accepted
{% endalert %}

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Templates/SeeEmailTemplateInformation {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `email_template_id`  | Yes | String | Your email template’s API Identifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Template Identifier]({{site.baseurl}}/api/identifier_types/)

### Example URL
`https://rest.iad-01.braze.com/templates/email/info?email_template_id=759c2ad9-eefc-4af1-bde4-602630644935`

### Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id=759c2ad9-eefc-4af1-bde4-602630644935' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Successful Response Properties

```json
GET https://YOUR_REST_API_URL/templates/email/info
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "email_template_id": (string) your email template's API Identifier,
  "template_name": (string) the name of your email template,
  "description": (string) email template description,
  "subject": (string) the email template subject line,
  "preheader": (optional, string) the email preheader used to generate previews in some clients),
  "body": (optional, string) the email template body that may include HTML,
  "plaintext_body": (optional, string) a plaintext version of the email template body,
  "should_inline_css": (optional, boolean) whether there is inline CSS in the body of the template - defaults to the css inlining value for the App Group,
  "tags": (string) tag names,
  "created_at": (string, in ISO 8601),
  "updated_at": (string, in ISO 8601)
}
```

Images in this response will show in the `body` variable as HTML.

{% endapi %}
