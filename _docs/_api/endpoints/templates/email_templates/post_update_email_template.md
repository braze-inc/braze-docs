---
nav_title: "POST: Update Email Template"
page_order: 4

layout: api_page

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

All fields other than the `email_template_id` are optional, but you must specify at least one field to update.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Templates/UpdateEmailTemplate {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#680315e8-32d4-4a3d-81b6-0085a91b9cdc {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
  "email_template_id": (required, string) your email template's API Identifier,
  "template_name": (optional, string) the name of your email template,
  "subject": (optional, string) the email template subject line,
  "body": (optional, string) the email template body that may include HTML,
  "plaintext_body": (optional, string) a plaintext version of the email template body,
  "preheader": (optional, string) the email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist
}
```

### Request Example
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update?email_template_id=ab1cde55-fg47-4h3i-8297-158jk3l2466m&template_name=Weekly%20Newsletter&subject=This%20Week%27s%20Styles&body=Check%20out%20this%20week%27s%20digital%20lookbook%20to%20inspire%20your%20outfits.%20Take%20a%20look%20at%20https://www.braze.com/&plaintext_body=This%20is%20the%20updated%20text%20within%20my%20email%20body%20and%20here%20is%20a%20link%20to%20https://www.braze.com/.&preheader=We%20want%20you%20to%20have%20the%20best%20looks%20this%20Summer&tags=[%22Tag1%22,%20%22Tag2%22]' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email_template_id": "ab1cde55-fg47-4h3i-8297-158jk3l2466m",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this Summer",
  "tags": ["Tag1", "Tag2"]
}'
```

### Possible Errors
- `Template Name is required`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`

{% endapi %}
