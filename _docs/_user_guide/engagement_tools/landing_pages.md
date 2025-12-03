---
nav_title: Landing pages
article_title: Landing Pages
page_order: 31
guide_top_header: "Landing Pages"
description: "This article contains resources on building and customizing Braze landing pages."
alias: /landing_pages/
---

# About landing pages

> Braze landing pages are standalone web pages that can drive your user acquisition and engagement strategy.

Use landing pages to grow your audience, capture user data, promote special offers, and support multichannel campaigns.

{% alert note %}
Landing page and custom domain availability depends on your Braze package. Contact your account manager or customer success manager to get started.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Prerequisites

Before you can access, create, and publish landing pages, you either need administrator [permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) or all the following permissions:

- Access Landing Pages
- Create Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Frequently asked questions

### What's the maximum size for landing pages?

The landing page body size can be up to 500 KB.

### Are there any technical requirements to publish a landing page?

No, there aren't any technical requirements.

### Is there an HTML editor for landing pages?

Yes. Use the **Custom Code** block in the drag-and-drop editor to add or edit HTML.

### Can I create a webhook inside a landing page?

No, this isn't currently supported.

### How can I add Google Analytics or Google Tag Manager to a landing page?

You can add Google Analytics or Google Tag Manager tracking to your landing pages by using the **Custom Code** block in the drag-and-drop editor. The location of the Custom Code block in your page determines where the tracking code is inserted in the HTML.

For Tag Manager web page installations, you must create a data layer. For more information, refer to Google's documentation on [the data layer and installation](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

To add tracking code:

1. When creating or editing a landing page, drag a **Custom Code** block to your page. For Google Analytics or Tag Manager scripts, place the block near the top of your page to ensure the tracking code loads early.
2. Paste your Google Analytics or Google Tag Manager tracking code into the block.
3. If using Google Tag Manager, make sure your code includes the data layer initialization (typically `dataLayer = []`) before the Tag Manager script.

The **Custom Code** block supports HTML, CSS, and JavaScript, allowing you to implement tracking pixels and other analytics tools.

