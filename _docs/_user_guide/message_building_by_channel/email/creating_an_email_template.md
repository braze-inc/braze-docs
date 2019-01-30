---
nav_title: Email Templates
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 2
---
# Email Templates

## Creating an Email Template

Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. The Braze dashboard has an email template editor that allows you to create custom-tailored, eye-catching emails and save them for later use in campaigns.

### Step 1: Navigate to the Email Template Editor

Click on the __Templates & Media__ tab under __Engagement__ in the navigation bar. This will open to the __Email Template Gallery__.

![Email Templates][1]

### Step 2: Create or Choose a Template

Now, you can create a new template, or edit an existing template (plain or [mobile responsive][8]). If you'd like to create a new template, then you can choose from Braze's predesigned templates, or you can choose to create a new layout.

![New Template][2]

### Step 3: Customize Your Template

You can write your message within the rich-text editor or optionally flip over to our HTML editor to customize your content.

Braze will add a footer with an unsubscribe link at the bottom of your email by default. You can customize this footer in the Email Settings tab of the Manage App Group page. For more information, please read our [custom footer documentation][cf].

If you want to see how your email looks before sending it out to your users, you can send a test email to an address of your choosing through the Settings tab in the top right corner.

![Enter Email Template Editing][3]
![E-Mail Template Editor Guide][6]

Our Editor supports **HTML Autocomplete** triggered by the 'Tab' key.  It should be used on naked HTML tags. for example, use of tab on `head` will result in:
{% raw %}
```
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <title>`substitute(Filename('', 'Page Title'), '^.', '\u&', '')`</title>

</head>
```
{% endraw %}

### Step 4: Check for Email Errors {#step-3a-check-for-email-errors}
The new E-Mail Editor will call out problems before you save. Here's a list of errors that are accounted for in our editor:

- Incorrect Liquid Syntax.
- [E-Mail bodies larger than 400kb; bodies are highly recommended to be less than 102kb.][7]
- Templates without an unsubscribe link.

### Step 5: Save Your Template {#step-4-save-your-template}

Be sure to save your template by clicking the "Save Template" button in the bottom right corner of the editor. You're now ready to use this template in any campaign you choose.

>  Edits made to an existing template will not be reflected in campaigns that were created using previous versions of that template.

### Using Your Templates in API Campaigns {#api_for_email_templates}
To use your email for an API campaign, you need an `email_template_id`, which can be found at the bottom of any Email Template created in Braze.

![Save Template][4]

## Upload an HTML Email Template

### Step 1: Navigate to the Email Template Editor
Click on the __Templates & Media__ tab under __Engagement__ in the navigation bar. This will open to the __Email Template Gallery__.

### Step 2: Open the Uploader
Click on the _Upload_ option in the __Basic Email Templates__ box.

### Step 3: Upload your Template
Navigate to and upload your template from your computer.

![HTML Uploader][9]

#### Upload Requirements:

##### Within a single .zip file…
- A single HTML file (the body of your email)
- A folder of images that are referenced in the HTML file
- Less than 50 image files

##### Uploaded file must be…
- Under 5MB
- Zipped in a single file

##### Solve Upload Email Template Errors
There are a number of email error messages you can receive when uploading an HTML file for Email. You will receive specific error message describing each of these. Here are a few samples with their recommended fixes:

| Error | Fix |
|---|---|
|.zip over 5MB| Reduce your file size and try uploading again.|
|.zip corrupt| Inspect your file and try uploading again. |
|Missing HTML| Add HTML file to your .zip file and try uploading again.|
|Multiple HTML| Remove one of the HTML files and try uploading again.|
|Images over 5MB| Reduce the number of images and try uploading again. |
|Extra Images| You may have extra images in your file that are not referenced in your HTML file. This will not cause a fail error, but those extra images will be discarded. If those images were supposed to be referenced in the HTML file, please check its contents and correct any errors, then try uploading again.
|Missing Images| If there are images referenced in your HTML file but those images are not included in the image folder of the .zip file, you will receive a file error. Inspect your file and correct any errors (like misspellings), or add the missing images to your .zip file and try uploading again.|


### Step 4: Finish and Save Your Template
Click “Save Template” in the bottom right corner of the editor. You can now use this template in any campaign you choose!

> Edits made to an existing template will not be reflected in campaigns created using previous versions of that template.

#### Using Your Templates in API Campaigns {#api_for_upload_email_templates}
To use your email for an API campaign, you need an `email_template_id`, which can be found at the bottom of any Email Template created in Braze.

![Save Template][4]



[1]: {% image_buster /assets/img_archive/email_templates1_new.png %}
[2]: {% image_buster /assets/img_archive/email_templates2_new.png %}
[3]: {% image_buster /assets/img_archive/email_templates3a_new.png %}
[4]: {% image_buster /assets/img_archive/email_templates4-new.png %}
[cf]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[5]: {{ site.baseurl }}/assets/img_archive/email_temlplates5.png
[6]: {% image_buster /assets/img_archive/email_templates3b_new.png %}
[7]: {{ site.baseurl }}/help/best_practices/email/email_styling_tips/#email-size
[8]: {{ site.baseurl }}/help/release_notes/2017/august/#mobile-responsive-email-templates
[9]: {% image_buster /assets/img_archive/step1and2htmluploader.gif %}
