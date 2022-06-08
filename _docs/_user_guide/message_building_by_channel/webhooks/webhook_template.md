---
nav_title: Creating a Webhook Template
article_title: Creating a Webhook Template
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "This reference article covers how to create and customize webhook templates for later use within the Braze platform."

---

# Creating a webhook template

## Step 1: Navigate to the webhook template editor

You can access the Webhook Template Editor by first clicking the **Campaigns** tab under **Engagement** on the navigation bar, which will reveal a drop-down menu with a Templates and Styles tab.  Click this tab to access the Webhook Template Editor.

![Webhook Templates tab under the Templates and Media page on the Braze dashboard.][1]

## Step 2: Create a new template

You can now create a new template, edit an existing template, or utilize one of the predesigned webhook templates that are offered.

## Step 3: Customize your template

Webhook templates can be used for many different use cases.  You can start by entering a unique template name to be utilized.  You can also fill in the webhook URL, the Request Body, Request Headers, and select the HTTP Method to be used.

![Compose tab when creating a webhook template. Available fields are language, webhook URL, and request body.][2]{: style="max-width:80%"}

If you want to see how your webhook looks before sending it out to your users, you can send a test webhook through the **Settings** tab.

## Step 4: Save your template

Be sure to save your template by clicking the **Save Template** button. You're now ready to use this template in any campaign you choose.

![Webhook Template Save][3]{: style="max-width:50%"}

{% alert note %}
Edits made to an existing template will not be reflected in campaigns that were created using the previous versions of that template.
{% endalert %}

## Managing webhook templates

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) Webhook Templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

[1]: {% image_buster /assets/img_archive/webhook_template_campaign.png %}
[2]: {% image_buster /assets/img_archive/Webhook_template_test.png %}
[3]: {% image_buster /assets/img_archive/Webhook_template_save.png %}
