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

## Adding Google Analytics or Google Tag Manager to a landing page

To add Google Analytics or Google Tag Manager tracking to your landing pages, you must create a data layer before implementing the tracking code, such as in the following snippet.

```json
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

For more information about installation, refer to [Google's documentation](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Frequently asked questions

### What's the maximum size for landing pages?

The landing page body size can be up to 500 KB.

### Are there any technical requirements to publish a landing page?

No, there aren't any technical requirements.

### Is there an HTML editor for landing pages?

Yes. Use the **Custom Code** block in the drag-and-drop editor to add or edit HTML.

### Can I create a webhook inside a landing page?

No, this isn't currently supported.