---
nav_title: Drag & Drop Editor Templates
permalink: "/dnd/email_template/"
hidden: true
---

# Create an Email Template using the Drag & Drop Editor

> Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. With this email editing experience, you can quickly design and template beautiful emails with ease.

## Step 1: Navigate to Templates and Select Editing Experience
Click on the __Templates & Media__ tab under __Engagement__ in the navigation bar. This will open to the __Email Template Gallery__.

Two editing options will now be shown:
- Selecting the 'Drag & Drop Editor' will allow you to select templates created using the drag & drop editor.
- Selecting the HTML Code Editor will allow you to use the existing editors and see your existing email templates.<br><br>

![dnd_editor_workflow][1]{: style="max-width:80%;"}

## Step 2: Create or Choose a Template

You can choose from the existing templates provided by Braze or any custom templates you have created using the drag & drop editor.

_Note: Your existing custom templates will need to be re-created using the drag & drop editor._

## Step 3: Customize Your Template

Once you have selected your template, you will be guided to the editor. A ‘Drag & Drop Editor’ badge will appear, indicating that you are about to use this editing experience for template creation (conversely, an HTML badge will appear if you are using the existing HTML or WYSIWYG editors).

![dnd_badge_icon][2]{: style="max-width:80%;"}

### Drag & Drop Editing Experience

The drag & drop editing experience is broken out into 3 sections: __Sending Settings__, __Content__, and __Preview & Test__.

{% tabs %}
{% tab Send Settings %}
#### __Sending Settings__
The Sending Settings section allows you to configure your from and reply-to address as well as set the subject line or pre-header. 

_Note: Advanced functionality will appear in the campaign or Canvas step composer. In advanced functionality, you can modify your inline CSS setting, set a BCC email address, and enter in a header or extra key-value pairs (if configured)._

{% endtab %}
{% tab Content %}

#### __Content__
The Content section contains the editor. There are 3 key components within this section.

- __Content__: This section includes a series of tiles that represent the different kinds of content you can use in your message. More will become available in the future. To use them, just drag one inside a column, it will auto-adjust to the column width. Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.<br><br> For more information see [Editor Block Properties]({{site.baseurl}}/dnd/editor_blocks/)<br><br>
- __Rows__: Rows are structural units that define the horizontal composition of a section of the message by using columns. Using more than one column allows you to put different content elements side by side. You can add all the structural elements you need to your message, regardless of the template you selected when you started.<br><br>
- __Settings__: General settings for the message. They are inherited by Rows and Content sections. For example, the font family set in the message settings is then used everywhere in your message, except where you use a custom setting.

This is very useful to build a coherent message very quickly.

{% endtab %}
{% tab Preview and Test %}

#### __Preview & Test__
The Preview & Test section allows you to preview your email based on different users.

- __Random User__: Braze will randomly select a user from the database and preview the email based on their attributes/event information.
Note: This user may or may not be part of your segmentation criteria. Segmentation is selected afterward, so Braze is unaware of your target audience at this point.<br><br>
- __Select User__: You can select a specific user based on their email address or `external_id`. The email will preview based on that user's attributes and event information<br><br>
- __Custom user__: You can customize a user. Braze will offer inputs for all available attributes and events. You can enter any information you would like to see in the preview email.
{% endtab %}
{% endtabs %}

_Note: Inbox Vision is currently unavailable during this testing phase and will be made available in the future_

## Step 4: Check for Email Errors
Email errors are presented on the ‘compose’ tab of the message workflow. Errors prevent you from progressing forward, while “Warnings”, indicate reminders to help you follow best practices. Depending on your business, you might choose to ignore them.

![dnd_compose_error][3]{: style="max-width:80%;"}

## Step 5: Save Your Template
Be sure to save your template by clicking the __Save Template__ button in the bottom right corner of the editor. You’re now ready to use this template in any campaign or Canvas step you choose.

_Note: Edits made to an existing template will not be reflected in campaigns that were created using previous versions of that template._

[1]: {% image_buster /assets/img/dnd_editor_workflow.png %}
[2]: {% image_buster /assets/img/dnd_badge_icon.png %}
[3]: {% image_buster /assets/img/dnd_compose_error.png %}
