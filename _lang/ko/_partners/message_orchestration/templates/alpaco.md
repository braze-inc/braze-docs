---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "The Braze and Alpaco integration allows you to export on-brand, Liquid-compatible email templates and content blocks to Braze, ready for use in email and in-app messaging."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/) is an online creative management tool that offers a drag-and-drop editor for building reusable, brand-safe content for Braze. The Alpaco and Braze integration allows you to export Content Blocks, Email Templates, and In-App Message Templates.

_This integration is maintained by Alpaco._

{% alert note %}
Alpaco supports [full Liquid](https://shopify.github.io/liquid/) variables, and as such also fully supports any Liquid variables used in your Braze configurations.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Alpaco account | An Alpaco account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint. <br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use Cases

- Export fully designed **email templates** for use in Braze campaigns and transactional messaging.
- Create and manage **modular content blocks** (e.g., headers, footers, promotions) that can be reused across multiple channels.
- Design engaging **in-app messages** with the same creative flexibility as emails, making it easy to deliver consistent, on-brand experiences across channels.
- Enable **personalization** by including Braze-supported Liquid tags such as `{{first_name}}` or `{{custom_attribute}}`.
- Maintain **brand consistency** by centralizing creative design in Alpaco and pushing updates to Braze with a single export.

## Integration

Provide your Braze REST API key and cluster instance to the Alpaco customer success team. The team will then set up the initial integration for you.

{% alert note %}
This is a one-time setup and any exports in the future will automatically use this API key.
{% endalert %}

## Exporting Alpaco messages to Braze

### Step 1: Create a template in Alpaco

In Alpaco, create a template that expresses your brand identity. When you're ready, select **Save**.

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Step 2: Draft a message using the template

Next, go to the Alpaco lobby and use your template to create an email, in-app message, or content block. To double-check your message before exporting, select **Review**.

![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Step 3: Export your message to Braze

Select **Export**, then choose the Braze integration and specify whether you're exporting an email template or a content block.

If you make changes after export, you can re-export the content from Alpaco to update it in Braze.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Using Alpaco Templates and Blocks in Braze

Depending on the type of content you export, your template will appear in one of the following sections:

- **Templates & Media > Email Templates**
- **Templates & Media > Content Blocks**

Alpaco templates are ideal for organizations looking to centrally manage brand consistency. They also support Braze’s built-in tags for easy categorization and content management.
