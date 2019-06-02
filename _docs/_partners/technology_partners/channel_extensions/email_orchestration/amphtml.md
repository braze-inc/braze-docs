---
nav_title: AMP for Email
alias: /partners/amphtml
---

# AMP for Email

With [AMP for Email](https://amp.dev/about/email), you can add interactive elements to your emails elevate your communications with your customers to a whole new level.


## Requirements

Requirement   | Description
--------------| -----
Braze API Key | The API key must have the *Template's* permission enabled before use.

Must have plaintext_body and HTML body as backups. Gmail Supports.

## Writing Your AMP Email


### Elements

{% tabs %}
  {% tabs Essentials %}

  {% endtab %}

  {% tabs Dynamic %}

  {% endtab %}

  {% tabs Creative %}

  {% endtab %}
{% endtab %}
## API Usage

When you use any of [our Messaging Endpoints]({{ site.baseurl }}/api/endpoints/messaging/) to send an email, add `amp_body` as an object specification, as shown below.

### Email Object Specification

```json
{
  "app_id": (required, string) see App Identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your app group's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMPHTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html".
  "body": (required unless email_template_id is given, valid HTML),
  "preheader"*: (optional, string) Recommended length 50-100 characters.
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline css on the body. If not provided, falls back to the default css inlining value for the App Group,
  "attachments": (optional, array), array of json objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```
