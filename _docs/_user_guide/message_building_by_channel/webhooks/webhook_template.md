---
nav_title: Creating a Webhook Template
platform: Message_Building_and_Personalization
subplatform: Webhooks
page_order: 2

tool:
  - Dashboard
  - Templates

channel:
  - webhooks

description: "This reference article covers how to create and customize Webhook templates for later use within the Braze platform."

---
# Creating a Webhook Template

### Step 1: Navigate to the Webhook Template Editor

You can access the Webhook Template by first clicking the **Campaigns** tab under **Engagement** on the navigation bar, which will reveal a drop-down menu with a 'Templates and Styles' tab.  Click on this tab to access the Webhook Template Editor.

![Webhook_template_campaign][1]

### Step 2: Create a New Template

You can now create a new template, edit an existing template or utilize one of the predesigned webhook templates that are offered.  The predesigned templates currently offered are for Twilio and Facebook messenger.

### Step 3: Customize Your Template

Webhook templates can be used for many different use cases.  You can start by entering a unique template name to be utilized.  You can also fill in the webhook URL, the Request Body, Request Headers, and select the HTTP Method to be used.

If you want to see how your webhook looks before sending it out to your users, you can send a test webhook through the Settings tab in the top right corner.

![Webhook_template_test][2]

### Step 4: Save Your Template

Be sure to save your template by clicking the "Save Template" button in the bottom right corner of the editor. You're now ready to use this template in any campaign you choose.

![Webhook_template_save][3]


> Edits made to an existing template will not be reflected in campaigns that were created using the previous versions of that template.

## Managing Webhook Templates

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) Webhook Templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

[1]: {% image_buster /assets/img_archive/webhook_template_campaign.png %}
[2]: {% image_buster /assets/img_archive/Webhook_template_test.png %}
[3]: {% image_buster /assets/img_archive/Webhook_template_save.png %}
