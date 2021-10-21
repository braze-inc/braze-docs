---
nav_title: Create an Email Template
article_title: Creating an Email Template
page_order: 2
description: "Email messages are great for delivering content to the user on their terms. This reference article covers how to create, customize, and manage email templates."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"

---

# How to create an email template

> This article covers how to create, customize, and manage email templates.

Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. The Braze dashboard has an email template editor that allows you to create custom-tailored, eye-catching emails and save them for later use in campaigns. You can also upload your own [HTML Email Template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Creating your template

### Step 1: navigate to the email template editor

In the left navigation, click __Templates & Media__, under the __Engagement__ section. This will open up the __Email Template Gallery__.

### Step 2: create or choose a template

Now, you can create a new template or edit an existing template (plain or [mobile responsive][8]) using either the drag & drop editing experience or standard HTML experience. If you'd like to create a new template, then you can choose from Braze's predesigned templates, or you can choose to create a new layout.

![New Template][2]

_Note: Any existing custom HTML templates will need to be re-created using the Drag & Drop Editor._

### Step 3: customize your template

You can write your message within the rich-text editor or optionally flip over to our HTML editor or Drag & Drop Editor to customize your content. Once selected, you will be guided to the editor experience you chose. An 'HTML Editor' or 'Drag & Drop Editor' badge will appear, indicating that you are about to use this editing experience for template creation.

{% alert important %}
When composing your email template copy, do not switch back and forth between different editor types (HTML/Block/Classic) as that may shift the previously created HTML leading to rendering issues. 
{% endalert %}

![dnd_badge_icon]({% image_buster /assets/img/dnd_badge_icon.png %})

{% tabs %}
{% tab HTML Editor %}

Braze will add a footer with an unsubscribe link at the bottom of your HTML emails by default. You can customize this footer in the **Email Settings** tab of the **Manage Settings** page. For more information, please read our [custom footer documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer).

![Enter Email Template Editing]({%image_buster/assets/img/email_templates/template3.jpg %})
<br>
<br>
![E-Mail Template Editor Guide]({%image_buster/assets/img/email_templates/template4.jpg %})

Our editor supports **HTML Autocomplete** triggered by the `Tab` key.  This feature should be used on naked HTML tags. For example, using `Tab` on a `<head>` tag will result in:
{% raw %}
```
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <title>`substitute(Filename('', 'Page Title'), '^.', '\u&', '')`</title>

</head>
```
{% endraw %}
{% endtab %}
{% tab Drag & Drop Editor %}

The drag & drop editing experience is broken out into 3 sections: __Sending Settings__, __Content__, and __Preview & Test__.

{% subtabs %}
{% subtab Send Settings %}
#### __Sending settings__
The Sending Settings section allows you to configure your from and reply-to address as well as set the subject line or pre-header. 

_Note: Advanced functionality will appear in the campaign or Canvas step composer. In advanced functionality, you can modify your inline CSS setting, set a BCC email address, and enter in a header or extra key-value pairs (if configured)._

{% endsubtab %}
{% subtab Content %}
#### __Content__
the content section contains the editor. there are three key components within this section.

- __Content__: This section includes a series of tiles that represent the different kinds of content you can use in your message. More will become available in the future. To use them, just drag one inside an existing row segment; it will auto-adjust to the column width. Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.<br><br> For more information see [Editor Block Properties]({{site.baseurl}}/dnd/editor_blocks/)<br><br>
- __Rows__: Rows are structural units that define the horizontal composition of a section of the message by using columns. Using more than one column allows you to put different content elements side by side. You can add all the structural elements you need to your message, regardless of the template you selected when you started.<br><br>
- __Settings__: General settings for the message. They are inherited by Rows and Content sections. For example, the font family set in the message settings will be used everywhere in your message, except where you use a custom setting.

This is very useful to build a coherent message very quickly.
{% endsubtab %}
{% subtab Preview and Test %}
#### __Preview & test__
The Preview & Test section allows you to preview your email based on different users.

- __Random User__: Braze will randomly select a user from the database and preview the email based on their attributes/event information.
Note: This user may or may not be part of your segmentation criteria. Segmentation is selected afterward, so Braze is unaware of your target audience at this point.<br><br>
- __Select User__: You can select a specific user based on their email address or `external_id`. The email will preview based on that user's attributes and event information<br><br>
- __Custom user__: You can customize a user. Braze will offer inputs for all available attributes and events. You can enter any information you would like to see in the preview email.
{% endsubtab %}
{% endsubtabs %}

_Note: Inbox Vision is currently unavailable during this testing phase and will be made available in the future_

{% alert tip %}
To read more about the different components of the drag & drop editing experience, visit our drag & drop documentation articles [here]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/). 
{% endalert %}

{% endtab %}
{% endtabs %}

Braze will add a footer with an unsubscribe link at the bottom of your email by default. You can customize this footer in the **Email Settings** tab of the **Manage Settings** page. For more information, please read our article on [custom footers][cf].

#### Step 4a: check for email errors
Email errors are presented on the 'compose' tab of the message workflow. Errors prevent you from progressing forward, while "Warnings" indicate reminders to help you follow best practices. Depending on your business, you might choose to ignore them.

![dnd_compose_error][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Here's a list of errors that are accounted for in our editor:

- Incorrect Liquid Syntax
- [Email bodies larger than 400kb; bodies are highly recommended to be less than 102kb][7]
- Templates without an unsubscribe link
- Emails with a blank **Body** or **Subject**.
- Emails with no unsubscribe link.

#### Step 4b: preview and test your message

After you finish composing your template, you can test it before sending it out.

From the bottom of the overview screen, click **Preview and Test**. Here you can preview how your email will appear in a customer's inbox. With **Preview as User** selected, you can preview your email as a random user, select a specific user, or create a custom user. This allows you to test that your Connected Content and personalization calls are working as they should.

You can also switch between desktop, mobile, and plaintext views to get a sense of how your message will appear in different contexts.

When you're ready for a final check, select **Test Send** and send a test message to yourself or a group of content testers to ensure that your email displays properly on a variety of devices and email clients.

![New Email Preview][15]

If you see any issues with your template or want to make any changes, click **Edit Email** to return to the editor.

### Step 5: save your template

Be sure to save your template by clicking **Save Template** in the bottom right corner of the editor. You're now ready to use this template in any campaign or Canvas step you choose.

{% alert note %}
If you make any edits to an existing template, those changes will not be reflected in campaigns created using previous versions of that template.
{% endalert %}

## Using your templates in api campaigns
To use your email for an API campaign, you need an `email_template_id`, which can be found at the bottom of any email template created in Braze.

![Save Template][6]

## Managing email templates

You can [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) email templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## FAQs

for answers to frequently asked questions about email templates, check out our [email and link templates faqs][9] page.


[2]: {% image_buster /assets/img/email_templates/template2.png %}
[1]: {% image_buster /assets/img/dnd_compose_error.png %}
[3]: {% image_buster /assets/img/email_templates/template3.jpg %}
[4]: {% image_buster /assets/img/email_templates/template4.jpg %}
[cf]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[6]: {% image_buster /assets/img/email_templates/template5.jpg %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
