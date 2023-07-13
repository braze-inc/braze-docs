---
nav_title: "GET: See Email Template Information"
article_title: "GET: See Email Template Information"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the See email template Braze endpoint."

---
{% api %}
# See email template information
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> Use this endpoint to get information on your email templates.

{% alert important %}
Templates built using the Drag-and-Drop Editor for email are not accepted.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

{% alert note %}
To use this endpoint, you'll need to generate an API key with the `templates.email.info` permission.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `email_template_id`  | Required | String | See [email template API identifier]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response 

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "email_template_id": (string) your email template's API Identifier,
  "template_name": (string) the name of your email template,
  "description": (string) the email template description,
  "subject": (string) the email template subject line,
  "preheader": (optional, string) the email preheader used to generate previews in some clients),
  "body": (optional, string) the email template body that may include HTML,
  "plaintext_body": (optional, string) a plaintext version of the email template body,
  "should_inline_css": (optional, boolean) whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
  "tags": (string) tag names,
  "created_at": (string) the time the email was created at in ISO 8601,
  "updated_at": (string) the time the email was updated in ISO 8601
}
```

Images in this response will show in the `body` variable as HTML.

{% endapi %}
