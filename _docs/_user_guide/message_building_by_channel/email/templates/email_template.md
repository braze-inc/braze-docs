---
nav_title: Create an Email Template
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 2
description: "Email messages are great for delivering content to the user on their terms. This reference article covers how to create, customize, and manage email templates."

tool:
  - Dashboard
  - Templates

channel:
  - email

---
# How to Create an Email Template

> This article covers how to create, customize, and manage email templates.

Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. The Braze dashboard has an email template editor that allows you to create custom-tailored, eye-catching emails and save them for later use in campaigns. You can also upload your own [HTML Email Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_email_template/).

## Creating Your Template

### Step 1: Navigate to the Email Template Editor

In the left navigation, click __Templates & Media__, under the __Engagement__ section. This will open up the __Email Template Gallery__.

### Step 2: Create or Choose a Template

Now, you can create a new template or edit an existing template (plain or [mobile responsive][8]). 

If you'd like to create a new template, you can choose to edit one of Braze's predesigned templates, or you can select **Blank Template** to create a new layout. If you have your own email template you'd like to upload, click **From File** to upload your [HTML Email Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_email_template/).

![New Template][2]

### Step 3: Customize Your Template

Give your new template a name and optional description. You can also assign [tags][20] to keep track of your templates for engagement use.  

Click **Edit Email Body** to enter the email editor and start crafting your template. You can write your message within the classic (rich-text) editor or optionally flip over to the HTML editor to customize your content.

![Enter Email Template Editing][3]

Our editor supports **HTML Autocomplete** triggered by the `Tab` key.  This feature should be used on naked HTML tags. For example, using `Tab` on a `<head>` tag will result in:
{% raw %}
```
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <title>`substitute(Filename('', 'Page Title'), '^.', '\u&', '')`</title>

</head>
```
{% endraw %}

![E-Mail Template Editor Guide][4]

Braze will add a footer with an unsubscribe link at the bottom of your email by default. You can customize this footer in the **Email Settings** tab of the **Manage Settings** page. For more information, please read our article on [custom footers][cf].

#### Step 3a: Preview and Test Your Message

After you finish composing your template, you can test it before sending it out.

From the bottom of the overview screen, click **Preview and Test**. Here you can preview how your email will appear in a customer's inbox. With **Preview as User** selected, you can preview your email as a random user, select a specific user, or create a custom user. This allows you to test that your Connected Content and personalization calls are working as they should.

You can also switch between desktop, mobile, and plaintext views to get a sense of how your message will appear in different contexts.

When you're ready for a final check, select **Test Send** and send a test message to yourself or a group of content testers to ensure that your email displays properly on a variety of devices and email clients.

![newemailtest][15]

If you see any issues with your template, or want to make any changes, click **Edit Email** to return to the editor.

#### Step 3b: Check for Email Errors
The new Email Editor will call out problems before you save. Here's a list of errors that are accounted for in our editor:

- Liquid syntax problems.
- [Email bodies larger than 400kb; bodies are highly recommended to be less than 102kb.][7]
- Templates without an unsubscribe link.
- Emails with a blank **Body** or **Subject**.
- Emails with no unsubscribe link.

### Step 4: Save Your Template

Be sure to save your template by clicking **Save Template** in the bottom right corner of the editor. You're now ready to use this template in any campaign you choose.

{% alert note %}
If you make any edits to an existing template, those changes will not be reflected in campaigns that were created using previous versions of that template.
{% endalert %}

## Using Your Templates in API Campaigns
To use your email for an API campaign, you need an `email_template_id`, which can be found at the bottom of any email template created in Braze.

![Save Template][6]

## Managing Email Templates

You can [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) email templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## FAQs

For answers to frequently asked questions about email templates, check out our [Email and Link Templates FAQs][9] page.


[2]: {% image_buster /assets/img/email_templates/template2.jpg %}
[3]: {% image_buster /assets/img/email_templates/template3.jpg %}
[4]: {% image_buster /assets/img/email_templates/template4.jpg %}
[cf]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[6]: {% image_buster /assets/img/email_templates/template5.jpg %}
[7]: {{site.baseurl}}/help/best_practices/email/email_styling_tips/#email-size
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/

