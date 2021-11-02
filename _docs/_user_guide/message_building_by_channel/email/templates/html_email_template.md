---
nav_title: Upload an Email Template
article_title: How to Upload an HTML Email Template
page_order: 2.1
description: "This reference article covers how to create, manage, and troubleshoot an HTML email template using the Braze dashboard."
tool:
  - Templates
channel:
  - email

---

# How to upload an HTML email template

> This article covers creating, managing, and troubleshooting HTML email templates in the Braze dashboard.

Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. The Braze dashboard has an email template editor that allows you to create custom-tailored, eye-catching emails and save them for later use in campaigns. You can also [create an Email Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/) using our editor.

## Prerequisites {#upload-requirements}

Before you begin, you need to create your HTML email template. This must be a single ZIP file containing the following:

* A single HTML file—the body of your email
* A folder of images that are referenced in the HTML file
* Less than 50 image files

This ZIP file should be under 5 MB.

## Uploading your template

### Step 1: Navigate to the email template editor

Go to the __Templates & Media__ page, under the __Engagement__ section. This opens the __Email Templates__ page.

### Step 2: Open the uploader

In the section **Start from a Basic HTML Template**, select **From File**.

### Step 3: Upload your template

Click **Upload From File** and select your template from your computer. Refer to the [Prerequisites](#upload-requirements) section to ensure your template meets the upload requirements.

#### Solve upload email template errors

There are several email error messages you may receive when uploading an HTML template file. If you receive an error, refer to the table below for common issues and their recommended fixes:

| Error | Fix |
|---|---|
|.zip over 5MB| Reduce your file size and try uploading again.|
|.zip corrupt| Inspect your file and try uploading again. |
|Missing HTML| Add HTML file to your ZIP file and try uploading again.|
|Multiple HTML| Remove one of the HTML files and try uploading again.|
|Images over 5MB| Reduce the number of images and try uploading again. |
|Extra Images| You may have additional images in your file that are not referenced in your HTML file. This will not cause a fail error, but the extra images will be discarded. If those images were supposed to be referenced in the HTML file, please check its contents, correct any errors, and try uploading again.
|Missing Images| If there are images referenced in your HTML file, but those images are not included in the image folder of the ZIP file, you will receive a file error. Inspect your file and correct any errors (like misspellings), or add the missing images to your ZIP file and try uploading again.|
{: .reset-td-br-1 .reset-td-br-2}

### Step 4: Finish and save your template

Be sure to save your template by clicking **Save Template** in the bottom right corner of the editor. You're now ready to use this template in any campaign or Canvas you choose.

{% alert note %}
If you make any edits to an existing template, those changes will not be reflected in campaigns that were created using previous versions of that template.
{% endalert %}

## Using your templates in API campaigns {#api_for_upload_email_templates}

To use your email for an API campaign, you need an `email_template_id`, which can be found at the bottom of any email template created in Braze.

![API Identifier section of an HTML email template][4]

## Managing email templates

You can [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) email templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## FAQs

For answers to frequently asked questions about email templates, check out our [email and link templates FAQs][10] page.


[4]: {% image_buster /assets/img_archive/email_template_id.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/