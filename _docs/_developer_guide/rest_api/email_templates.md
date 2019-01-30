---
nav_title: Email Templates
page_order: 3.1
search_rank: 5
---

# Email Templates

Use the Email Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

## Creating Email Templates

Use the endpoints below to create email templates on the Braze dashboard. These templates will be available on the Templates and Media page. The response from this endpoint will include a field for `email_template_id`, which can be used to update the template in subsequent API calls.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/create`
US-02 | `https://rest.iad-02.braze.com/templates/email/create`
US-03 | `https://rest.iad-03.braze.com/templates/email/create`
US-04 | `https://rest.iad-04.braze.com/templates/email/create`
US-06 | `https://rest.iad-06.braze.com/templates/email/create`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/create`

```json
POST https://YOUR_REST_API_URL/templates/email/create
Content-Type: application/json
{
   "api_key": (required, string) your App Group REST API Key,
   "template_name": (required, string) the name of your email template,
   "subject": (required, string) the email template subject line,
   "body": (required, string) the email template body that may include HTML,
   "plaintext_body": (optional, string) a plaintext version of the email template body,
   "preheader": (optional, string) the email preheader used to generate previews in some clients
 }
```

## Updating Email Templates

Use the endpoints below to update email templates on the Braze dashboard. You can access an email template's `email_template_id` by navigating to it on the Templates and Media page. The email template creation API endpoint will also return an `email_template_id` reference.

All fields other than the `api_key` and `email_template_id` are optional, but you must specify at least one field to update.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/update`
US-02 | `https://rest.iad-02.braze.com/templates/email/update`
US-03 | `https://rest.iad-03.braze.com/templates/email/update`
US-04 | `https://rest.iad-04.braze.com/templates/email/update`
US-06 | `https://rest.iad-06.braze.com/templates/email/update`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/update`

```json
POST https://YOUR_REST_API_URL/templates/email/update
Content-Type: application/json
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

## List Email Templates Available

Use the endpoints below to get a list of available templates.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/list`
US-02 | `https://rest.iad-02.braze.com/templates/email/list`
US-03 | `https://rest.iad-03.braze.com/templates/email/list`
US-04 | `https://rest.iad-04.braze.com/templates/email/list`
US-06 | `https://rest.iad-06.braze.com/templates/email/list`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/list`

### Request Parameters

```json
{
  “api_key”: (required, string) your App Group REST API Key
  “modified_after”: (optional, string in ISO 8601), retrieve only templates updated at or after the given time
  “modified_before”: (optional, string in ISO 8601), retrieve only templates updated at or before the given time
  “limit”: (optional, positive number), maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000
  “offset”: (optional, positive number), number of templates to skip before returning rest of the templates that fit the search criteria
}
```

### Successful Response Properties

```json
GET https://YOUR_REST_API_URL/templates/email/list

{
  “count”: number of templates returned
  “templates”: [template with the following properties]:
    “email_template_id”: (string) your email template's API Identifier,
    “template_name”: (string) the name of your email template,
    “created_at”: (string, in ISO 8601),
    “updated_at”: (string, in ISO 8601)
}
```

## See Email Template Information

Use the endpoints below to get information on your email templates.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/info`
US-02 | `https://rest.iad-02.braze.com/templates/email/info`
US-03 | `https://rest.iad-03.braze.com/templates/email/info`
US-04 | `https://rest.iad-04.braze.com/templates/email/info`
US-06 | `https://rest.iad-06.braze.com/templates/email/info`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/info`

### Request Parameters

```json
{
  “api_key”: (required, string) your App Group REST API Key
  “email_template_id”: (required, string) your email template’s API Identifier
}
```

### Successful Response Properties

```json
GET https://YOUR_REST_API_URL/templates/email/info
{
  “email_template_id”: (string) your email template's API Identifier,
  “template_name”: (string) the name of your email template,
  “subject”: (string) the email template subject line,
  “preheader”: (optional, string) the email preheader used to generate previews in some clients),
  “body”: (optional, string) the email template body that may include HTML,
  “plaintext_body”: (optional, string) a plaintext version of the email template body,
  “should_inline_css”
  “tags”: (string) tag names,
  “created_at”: (string, in ISO 8601),
  “updated_at”: (string, in ISO 8601)
}
```

Images in this response will show in the "body" variable as HTML.
