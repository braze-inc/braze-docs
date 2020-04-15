---
nav_title: "POST: Create Email Template"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Create Email Templates Braze endpoint."
---
{% api %}
# Create Email Template
{% apimethod post %}
/templates/email/create
{% endapimethod %}

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database. All API requests are made over HTTPS.

Use the endpoints below to create email templates on the Braze dashboard. These templates will be available on the Templates and Media page. The response from this endpoint will include a field for `email_template_id`, which can be used to update the template in subsequent API calls.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Templates/CreateEmailTemplate {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Request Body

```json
{
   "template_name": (required, string) the name of your email template,
   "subject": (required, string) the email template subject line,
   "body": (required, string) the email template body that may include HTML,
   "plaintext_body": (optional, string) a plaintext version of the email template body,
   "preheader": (optional, string) the email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist.
 }
```

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create?template_name=Template%20Name&subject=Subject&body=Body&plaintext_body=Plaintext_Body&preheader=Header&tags=[%22Tag1%22,%20%22Tag2%22]' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

### Possible Errors
- `Template Name is required`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`
{% endapi %}
