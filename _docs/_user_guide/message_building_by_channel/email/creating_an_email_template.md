---
nav_title: Create an Email Template
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 2
description: "Email messages are great for delivering content to the user on their terms. This reference article covers how to create, customize and manage email templates."
---
# How to Create an Email Template

> Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. The Braze dashboard has an email template editor that allows you to create custom-tailored, eye-catching emails and save them for later use in campaigns. You can also upload [your own HTML Email Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_email_template/).

## Step 1: Navigate to the Email Template Editor

Click on the __Templates & Media__ tab under __Engagement__ in the navigation bar. This will open to the __Email Template Gallery__.

## Step 2: Create or Choose a Template

Now, you can create a new template, or edit an existing template (plain or [mobile responsive][8]). If you'd like to create a new template, then you can choose from Braze's predesigned templates, or you can choose to create a new layout.

![New Template][2]

## Step 3: Customize Your Template

You can write your message within the rich-text editor or optionally flip over to our HTML editor to customize your content.

Braze will add a footer with an unsubscribe link at the bottom of your email by default. You can customize this footer in the **Email Settings** tab of the **Manage Settings** page. For more information, please read our [custom footer documentation][cf].

If you want to see how your email looks before sending it out to your users, you can send a test email to an address of your choosing through the Settings tab in the top right corner.

![Enter Email Template Editing][3]
<br>
<br>
![E-Mail Template Editor Guide][4]

Our editor supports **HTML Autocomplete** triggered by the 'Tab' key.  It should be used on naked HTML tags. For example, use of tab on `head` will result in:
{% raw %}
```
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <title>`substitute(Filename('', 'Page Title'), '^.', '\u&', '')`</title>

</head>
```
{% endraw %}

## Step 4: Check for Email Errors {#step-3a-check-for-email-errors}
The new E-Mail Editor will call out problems before you save. Here's a list of errors that are accounted for in our editor:

- Incorrect Liquid Syntax.
- [E-Mail bodies larger than 400kb; bodies are highly recommended to be less than 102kb.][7]
- Templates without an unsubscribe link.

## Step 5: Save Your Template {#step-4-save-your-template}

Be sure to save your template by clicking the "Save Template" button in the bottom right corner of the editor. You're now ready to use this template in any campaign you choose.

>  Edits made to an existing template will not be reflected in campaigns that were created using previous versions of that template.

## Using Your Templates in API Campaigns {#api_for_email_templates}
To use your email for an API campaign, you need an `email_template_id`, which can be found at the bottom of any Email Template created in Braze.

![Save Template][6]

## Managing Email Templates

You can [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) email templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).


[2]: {% image_buster /assets/img/email_templates/template2.jpg %}
[3]: {% image_buster /assets/img/email_templates/template3.jpg %}
[4]: {% image_buster /assets/img/email_templates/template4.jpg %}
[cf]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[6]: {% image_buster /assets/img/email_templates/template5.jpg %}
[7]: {{site.baseurl}}/help/best_practices/email/email_styling_tips/#email-size
[8]: {{site.baseurl}}/help/release_notes/2017/august/#mobile-responsive-email-templates
