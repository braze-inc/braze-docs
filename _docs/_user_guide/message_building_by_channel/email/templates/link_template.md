---
nav_title: Link Templates
article_title: Link Templates
page_order: 4
description: "This article covers how to create different types of link templates in your emails."
tool:
  - Templates
channel:
  - email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/creating-link-templates){: style="float:right;width:120px;border:0;" class="noimgborder"}Link templates

> Link templates allow you to append parameters or prepend URLs to all links in an email message. This is most often used for the following use cases:

1. Appending Google Analytics query parameters to all links in a given email message
2. Prepending a URL to all links in a given email message

{% alert note %}
When using link templates and [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), Liquid code must only be added within the body tag to ensure consistent rendering.
{% endalert %}

## Creating a link template

![][11]{: style="float:right;max-width:20%;"}

To create a link template, navigate to the **Templates & Media** page, and select the **Link Templates** tab. You can create an unlimited number of link templates to support your various needs. Click **Create Link Template** to get started.

{% alert note %}
Link templates are an optional feature. If the **Link Templates** tab is missing from your **Templates & Media** page, reach out to your customer success manager or account manager to enable the feature flipper for link templates.
{% endalert %}

There are two types of link templates you can create:

- [Link template that inserts before a URL](#prepend-link-template)
- [Link template that inserts after a URL](#append-link-template)

### Prepend: Create a link template that inserts before a URL {#prepend-link-template}

If you want to add a string or URL before the links in your email message, create a new link template and set the **Template Position** to **Before URL**.  This will allow you to enter a string that will always get prepended to your URL. 

A preview section is provided to give you an example of the insertion process.

![Template Position, Prepend URL, and Template Preview fields for the link template insertion process before a URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Append: Create a link template that inserts after a URL {#append-link-template}

If you want to add query parameters after a URL in your email message, create a new link template and set the **Template Position** to **After URL**.  This will allow you to enter query parameters (`value=something`) to the end of each URL.  

You can have multiple parameters appended to the end of a URL.

![Template Position, Query Parameters, and Template Preview fields for the link template insertion process after a URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Using your templates in email campaigns

Once your templates are set up, you can select which template you would like to use in your email from the email editor.

- **HTML email editor:** Select your template from the **Link Management** tab. 
- **Drag & Drop Editor:** Select **Content** then **Link Management**. You will see all the links present in your email and can add the template from there. To access link templates in the Drag & Drop Editor, you must have [link aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) turned on. 

![Link Management tab in the Drag and Drop Editor with an example list of link templates.][1]

## Managing link templates

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) link templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
Archiving templates is not currently available for [link templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

## Frequently asked questions

For answers to frequently asked questions about link templates, check out our [Templates FAQ][10] page.

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
