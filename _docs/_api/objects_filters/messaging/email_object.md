---
nav_title: "Email object"
article_title: Email Messaging Object
page_order: 5
page_type: reference
channel: email
description: "This reference article explains the different components of the Braze email object."

---

# Email object

> The `email` object allows you to modify or create emails through our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

## Email object

```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address gets added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) recommended length 50-100 characters,
  "email_template_id": (optional, string) if provided, Braze uses the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case Braze overrides the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this is passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [App identifier]({{site.baseurl}}/api/identifier_types/)
  - Any valid `app_id` from an app configured in your workspace works for all users in your workspace, regardless of whether the user has the specific app on their profile or not.
- For more information and best practices on preheaders, see our help article on [email body styling]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling).

{% alert warning %}
Braze recommends that you avoid using Google Drive links for your attachment's `url`, as this can block our servers' calls to get the file and result in the email message not sending.
{% endalert %}

Valid attachment types include: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf`, and `pkpass`.

An `email_template_id` can be retrieved from the bottom of any email template created with the HTML editor. The following shows an example of what this ID looks like:

![API Identifier section of an HTML email template.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"}

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

## Authentication for email file attachments

1. Navigate to **Settings** > **Connected Content** and click **Add Credential** to add your authentication credentials.
2. Enter a name, and add a username and password.
3. In email object of the `/messages/send` endpoint, include a `basic_auth_credential` property specifying the credential name in the attachment details. Refer to the following example with the credential name `company_basic_auth_credential_name`:

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basis auth attachment test",
      "from": "mail <mail@e.company.com>",
      "body": "my attachment test",
      "attachments":[
        { "file_name":"checkout_receipt.pdf",
        "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
        "basic_auth_credential": "company_basic_auth_credential_name" }
      ]
    }
  }
}
```

