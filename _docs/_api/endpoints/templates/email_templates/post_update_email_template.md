---
nav_title: "POST: Update Email Template"
page_order: 4

layout: api_page2

page_type: reference
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Update Email Template Braze endpoint."
---

{% api %}

# Update Existing Email Templates

{% apimethod post %}
/templates/email/update
{% endapimethod %}

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

Use the endpoints below to update email templates on the Braze dashboard. You can access an email template's `email_template_id` by navigating to it on the Templates and Media page. The email template creation API endpoint will also return an `email_template_id` reference.

All fields other than the `api_key` and `email_template_id` are optional, but you must specify at least one field to update.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Templates/UpdateEmailTemplate {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#680315e8-32d4-4a3d-81b6-0085a91b9cdc {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
  "api_key": (required, string) your App Group REST API Key,
  "email_template_id": (required, string) your email template's API Identifier,
  "template_name": (optional, string) the name of your email template,
  "subject": (optional, string) the email template subject line,
  "body": (optional, string) the email template body that may include HTML,
  "plaintext_body": (optional, string) a plaintext version of the email template body,
  "preheader": (optional, string) the email preheader used to generate previews in some clients
}
```
{% endapi %}
