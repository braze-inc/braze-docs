---
nav_title: "POST: Create Email Template"
article_title: "POST: Create Email Templates"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Create Email Templates Braze endpoint."
---
{% api %}
# Create email template
{% apimethod post %}
/templates/email/create
{% endapimethod %}

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database. All API requests are made over HTTPS.

Use these endpoints to create email templates on the Braze dashboard. These templates will be available on the **Templates & Media** page. The response from this endpoint will include a field for `email_template_id`, which can be used to update the template in subsequent API calls.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "template_name": (required, string) the name of your email template,
   "subject": (required, string) the email template subject line,
   "body": (required, string) the email template body that may include HTML,
   "plaintext_body": (optional, string) a plaintext version of the email template body,
   "preheader": (optional, string) the email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) One of 'true' or 'false' is expected
 }
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`template_name`|Required|String|Name of your email template.|
|`subject`|Required|String|Email template subject line.|
|`body`|Required|String|Email template body that may include HTML.|
|`plaintext_body`|Optional|String|A plaintext version of the email template body.|
|`preheader`|Optional|String|Email preheader used to generate previews in some clients.|
|`tags`|Optional|String|[Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) must already exist.|
|`should_inline_css`|Optional|Boolean|Enables or disables the `inline_css` feature per template. If not provided, Braze will use the default setting for the AppGroup. One of `true` or `false` is expected.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Possible errors

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

| Error | Troubleshooting |
| --- | --- |
| Template name is required |
| Tags must be an array | Tags must be formatted as an array of strings, for example `["marketing", "promotional", "transactional"]`. |
| All tags must be strings | Make sure your tags are encapsulated in quotes (`""`). |
| Some tags could not be found | To add a tag when creating an email template, the tag must already exist in Braze. |
| Email must have valid Content Block names | The email might contain Content Blocks that don't exist in this environment. |
| Invalid value for `should_inline_css`. One of `true` or `false` was expected | This parameter only accepts boolean values (true or false). Make sure the value for `should_inline_css` is not encapsulated in quotes (`""`), which causes the value to be sent as a string instead. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
