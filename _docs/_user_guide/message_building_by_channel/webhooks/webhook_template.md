---
nav_title: Create a webhook template
article_title: Create a Webhook Template
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "This reference article covers how to create and customize webhook templates for later use within the Braze platform."

---

# Create a webhook template

> As you build and customize your webhooks, you can create and leverage webhook templates for later use within the Braze platform. This way, you can consistently build a variety of webhooks across your different campaigns.

## Step 1: Go to the webhook template editor

In the Braze dashboard, go to **Templates** > **Webhook Templates**.

![The "Webhook Templates" page with predesigned and saved webhook templates.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Step 2: Choose your template

From here, you can choose to create a new template, use one of the predesigned webhook templates, or edit an existing template.

For example, if you're using [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) as a messaging channel, you can set up several webhooks using the predesigned templates for **LINE Carousel** or **LINE Image**.

## Step 3: Fill out template details

1. Give your webhook template a unique name.
2. (Optional) Add a template description to explain how this template is intended to be used.
3. Add [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed to help find and filter for your template.

## Step 4: Build your template

1. Enter the webhook URL.
2. Select the HTTP method.
3. Add a request body. This can be either **JSON Key/Value Pairs** or **Raw Text**.
4. (Optional) Add a request header. This may be required by your webhook destination.

![The "Compose" tab when creating a webhook template. Available fields are webhook URL, HTTP method, request body, and request headers. You can also add languages.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Step 5: Test your template

To see how your webhook looks before sending it to your users, you can send a test webhook using the **Test** tab. Here, you can select to preview the message as a random user, existing user, or custom user.

## Step 6: Save your template

Be sure to save your template by selecting **Save Template**. You're now ready to use this template in any campaign you choose.

{% alert note %}
Edits made to an existing template aren't reflected in campaigns that were created using previous versions of that template.
{% endalert %}

## Managing your templates

You can [duplicate and archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) webhook templates to help better organize and manage your list of templates.

Learn more about creating and managing templates and creative content in [Templates and Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

