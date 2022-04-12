---
nav_title: "Email Object"
article_title: Email Messaging Object
page_order: 5
page_type: reference
channel: email
description: "This article explains the different components of Braze's Email Object."

---

# Email object specification

The `email` object allows you to modify or create emails via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

## Body
```json
{
  "app_id": (required, string), see App Identifier below,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your app group's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your app group's email settings) If provided and the BCC feature is enabled for your account, this address will get added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the App Group,
  "attachments": (optional, array), array of JSON objects that define the files you need attached, defined by "file_name" and "url" below,
    "file_name": (required, string) the name of the file you would like to attach to your email, excluding the extension (e.g., ".pdf"). You can attach any number of files up to 2MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you would like to attach to your email. The file name's extension will be detected automatically from the URL defined below, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [App Identifier]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)
- For more information and best practices on pre-headers, see our help article on [email body styling][46].

{% alert warning %}
Braze recommends that you avoid using Google Drive links for your attachment's `url`, as this can block our servers' calls to get the file and result in the email message not sending.
{% endalert %}

An `email_template_id` can be retrieved from the bottom of any email template created with the HTML editor. Below is an example of what this ID looks like:

![API Identifier section of an HTML email template][31]

## Example email object with attachment

```json
{
  "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
  "messages":{
     "email":{
        "app_id":"YOUR_APP_ID",
        "attachments":[{
            "file_name":"YourFileName",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

[31]: {% image_buster /assets/img_archive/email_template_id.png %}
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling
