---
nav_title: "POST: Update email template"
article_title: "POST: Update Email Templates"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update email template Braze endpoint."

---
{% api %}
# Update existing email templates
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> Use this endpoint to update email templates on the Braze dashboard.

You can access an email template's `email_template_id` by navigating to it on the **Templates & Media** page. The [Create email template endpoint]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) will also return an `email_template_id` reference.

All fields other than the `email_template_id` are optional, but you must specify at least one field to update.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Prerequisites
To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `templates.email.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Required |String|Your [email template's API identifier]({{site.baseurl}}/api/identifier_types/).|
|`template_name`|Optional|String|Name of your email template.|
|`subject`|Optional|String|Email template subject line.|
|`body`|Optional|String|Email template body that may include HTML.|
|`plaintext_body`|Optional|String|A plaintext version of the email template body.|
|`preheader`|Optional|String|Email preheader used to generate previews in some clients.|
|`tags`|Optional|String|[Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) must already exist.|
|`should_inline_css`|Optional|Boolean|Enables or disables the `inline_css` feature per template. If not provided, Braze will use the default setting for the AppGroup. One of `true` or `false` is expected.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| Template name is required | Enter a template name. |
| Tags must be an array | Tags must be formatted as an array of strings, for example `["marketing", "promotional", "transactional"]`. |
| All tags must be strings | Make sure your tags are encapsulated in quotes (`""`). |
| Some tags could not be found | To add a tag when creating an email template, the tag must already exist in Braze. |
| Invalid value for `should_inline_css`. One of `true` or `false` was expected | This parameter only accepts boolean values (true or false). Make sure the value for `should_inline_css` is not encapsulated in quotes (`""`), which causes the value to be sent as a string instead. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
