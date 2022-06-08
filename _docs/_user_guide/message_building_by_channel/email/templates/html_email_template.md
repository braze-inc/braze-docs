---
nav_title: Uploading an Email Template
article_title: Uploading an HTML Email Template
page_order: 2.1
description: "This reference article covers how to create, manage, and troubleshoot an HTML email template using the Braze dashboard."
tool:
  - Templates
channel:
  - email

---

# Uploading an HTML email template

> This article covers creating, managing, and troubleshooting HTML email templates in the Braze dashboard.

The Braze dashboard allows you to upload your very own HTML email templates and save them for later use in campaigns. You can also [create an email template]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/) using our editor.

## Prerequisites {#upload-requirements}

Before you begin, you need to create your HTML email template. This must be a single ZIP file containing the following:

* A single HTML file—the body of your email
* A folder of images that are referenced in the HTML file
* Less than 50 image files

This ZIP file should be under 5 MB.

## Uploading your template

### Step 1: Navigate to the email template editor

Go to the **Templates & Media** page in the **Engagement** section. This opens the **Email Templates** page.

### Step 2: Open the uploader

Under the **Template Type** section, select **HTML Editor**. Then scroll down to the section **Start from a Basic HTML Template** and select **From File**.

### Step 3: Upload your template

Click **Upload From File** and select your template from your computer. Refer to the [Prerequisites](#upload-requirements) section to ensure your template meets the upload requirements.

#### Troubleshoot uploading template errors

There are several email error messages you may receive when uploading an HTML template file. If you receive an error, refer to the following table for common issues and their recommended fixes:

| Error | Fix |
|------|---|
|.zip over 5MB| Reduce your file size and try uploading again.|
|.zip corrupt| Inspect your file and try uploading again. |
|Missing HTML| Add the HTML file to your ZIP file and try uploading again.|
|Multiple HTML| Remove one of the HTML files and try uploading again.|
|Images over 5MB| Reduce the number of images and try uploading again. |
|Extra Images| You may have additional images in your file that are not referenced in your HTML file. This will not cause a fail error, but the extra images will be discarded. If those images were supposed to be referenced in the HTML file, then check the content, correct any errors, and try uploading again.
|Missing Images| If there are images referenced in your HTML file, but those images are not included in the image folder of the ZIP file, you will receive a file error. Inspect your file and correct any errors (like misspellings), or add the missing images to your ZIP file and try uploading again.|
{: .reset-td-br-1 .reset-td-br-2}

### Step 4: Finish and save your template

Be sure to save your template by clicking **Save Template**. You're now ready to use this template in any campaign or Canvas you choose!

{% alert note %}
If you make any edits to an existing template, those changes will not be reflected in campaigns that were created using previous versions of that template.
{% endalert %}

## Using your templates in API campaigns {#api_for_upload_email_templates}

To use your email for an API campaign, you need the `email_template_id`, which can be found at the bottom of any email template created in Braze.

![API Identifier section of an HTML email template.][4]

## Managing email templates

You can [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) email templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## FAQs

For answers to frequently asked questions about email templates, check out our [email and link templates FAQs][10] page.


[4]: {% image_buster /assets/img_archive/email_template_id.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/