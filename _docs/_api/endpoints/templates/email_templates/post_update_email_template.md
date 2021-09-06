---
nav_title: "POST: Update Email Template"
article_title: "POST: Update Email Templates"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
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

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
  "should_inline_css": (optional, Boolean) One of 'true' or 'false' is expected
}
```

## Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Required |String|Your [email template's API identifier]({{site.baseurl}}/api/identifier_types/).|
|`template_name`|Optional|String|Name of your email template.|
|`subject`|Optional|String|Email template subject line.|
|`body`|Optional|String|Email template body that may include HTML.|
|`plaintext_body`|Optional|String|A plaintext version of the email template body.|
|`preheader`|Optional|String|Email preheader used to generate previews in some clients.|
|`tags`|Optional|String|[Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) must already exist.|
|`should_inline_css`|Optional|Boolean|Enables or disables the `inline_css` feature per template. If not provided, Braze will use the default setting for the AppGroup. One of `true` or `false` is expected.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request Example
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this Summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Possible Errors
- `Template Name is required`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`

- `"Invalid value for 'should_inline_css'.  One of 'true' or 'false' was expected"` - 'should_inline_css' accepts boolean characters only.  The error likely is being shown as the value is being sent as a 'string'.


{% endapi %}
