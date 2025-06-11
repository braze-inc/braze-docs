---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "The Braze and Alpaco integration allows you to export on-brand, Liquid-compatible email templates and content blocks to Braze, ready for use in email and in-app messaging."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) is an online creative management tool that offers a drag-and-drop editor for building reusable, brand-safe content for Braze. The Alpaco and Braze integration allows you to export:  
>
> - **Email Templates**  
> - **Content Blocks**  
> - **In-App Message Templates**

_This integration is maintained by Alpaco._

{% alert note %}
Alpaco supports [full Liquid](https://shopify.github.io/liquid/) variables, and as such also fully supports any Liquid variables used in your Braze configurations.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Alpaco account | An Alpaco account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint. <br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`.  |
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

## Exporting Alpaco emails to Braze

### Step 1: Create a template or Content Block in Alpaco

In the Alpaco platform, use the different settings and options to create a template that expresses your brand identity. Select **Save** when you're happy with your template.

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Step 2: Create an email or message

After the template is created, navigate to the lobby and use it to create an email, content block or In-app Message. Select **Review** to make sure everything looks right.

![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Step 3: Review and export to Braze

Select **Export**, choose the Braze integration, and specify whether you're exporting an Email Template or a Content Block.

If you make changes after export, simply re-export the content from Alpaco to update it in Braze.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Using Alpaco templates and blocks in Braze

Depending on the type of content you export, your template will appear in one of the following sections:

- **Templates & Media > Email Templates**
- **Templates & Media > Content Blocks**

Alpaco templates are ideal for organizations looking to centrally manage brand consistency. They also supports Braze’s built-in tags for easy categorization and content management.
