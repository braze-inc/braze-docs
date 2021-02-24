---
nav_title: Drag and Drop editor Templates
alias: "/dnd/email_template"
hidden: true
---

# How to Create an Email Template using the Drag-and-Drop editor

> Email messages are great for delivering content to the user on their terms. They are also wonderful tools to re-engage users who may have even uninstalled your app. With the new email editing experience, you can quickly design and template beautiful emails with ease.


## Step 1: Navigate to the Email Templates
Click on the __Templates & Media__ tab under __Engagement__ in the navigation bar. This will open to the __Email Template Gallery__.

## Step 2: Choose the new editor
Two editing options will now be shown.  

![dnd_editor_workflow][1]

1. Selecting the HTML Code Editor will allow you to use the existing editors and see your existing email templates.
2. Selecting the 'Drag-and-Drop' editor will allow you to select templates created using the drag-and-drop editor.

## Step 3: Create or Choose a Template

You can choose from the existing templates provided by Braze or any custom templates you have created using the drag and drop editor.

_Note: Your existing custom templates will need to be re-created using the new editor._

## Step 4: Customize Your Template

Once you have selected your template, you will be guided to the editor.  A ‘drag and drop’ badge will appear, indicating that you are about to use the new editor for template creation (conversely, an HTML badge will appear if you are using the existing editor).

![dnd_badge_icon][2]

### New editing experience
The new editing experience is broken out into 3 sections.
1. Sending Settings
2. Content
3. Preview & Test

#### Sending Settings
This section allows you to configure your from and reply-to address as well as set the subject line or pre-header. 

_Note: Advanced functionality will appear in the campaign or canvas step composer.  In advanced functionality, you can modify your inline CSSsetting, set a BCC email address, and enter in a header or extra value pairs (if configured)._

#### Content
The content section contains the editor.  There are 3 key components within this section.

##### Content: 
This section includes a series of tiles that represent the different kinds of content you can use in your message. More will become available in the future.  To use them, just drag one inside a column, it will auto-adjust to the column width.

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.

##### Rows
Rows are structural units that define the horizontal composition of a section of the message by using columns.  Using more than one column allows you to put different content elements side by side.  You can add all the structural elements you need to your message, regardless of the template you selected when you started.


##### Settings: 
General settings for the message.  They are inherited by Rows and Content sections. 
For example, the font family set in the message settings is then used everywhere in your message, except where you use a custom setting.


This is very useful to build a coherent message very quickly.


#### Preview & Test

The Preview & Test section allows you to preview your email based on different users.

##### Random User
Braze will randomly select a user from the database and preview the email based on their attributes/event information.
Note: This user may or may not be part of your segmentation criteria.  Segmentation is selected afterward, so Braze is unaware of your target audience at this point.

##### Select User
You can select a specific user based on their email address or `external_id`.  The email will preview based on that users’ attributes and event information

##### Custom user
You can customize a user.  Braze will offer inputs for all available attributes and events.  You can enter any information you would like to see in the preview email.

_Note: Inbox Vision is currently unavailable in this editor view._


## Step 5: Check for Email Errors
Email errors are presented on the ‘compose’ tab of the message workflow.  Errors prevent you from progressing forward, while “Warnings”, indicate reminders to help you follow best practices.  Depending on your business, you might choose to ignore them.

![dnd_compose_error][3]


## Step 6: Save Your Template
Be sure to save your template by clicking the “Save Template” button in the bottom right corner of the editor. You’re now ready to use this template in any campaign or canvas step you choose.

Note: Edits made to an existing template will not be reflected in campaigns that were created using previous versions of that template.



[1]: {% image_buster /assets/img/dnd_editor_workflow.png %}
[2]: {% image_buster /assets/img/dnd_badge_icon.png %}
[3]: {% image_buster /assets/img/dnd_compose_error.png %}

