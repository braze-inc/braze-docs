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

# Link templates

> Link templates allow you to append parameters or prepend URLs to all links in an email message.

Link templates are most often used in these following use cases:

1. Appending Google Analytics query parameters to all links in a given email message
2. Prepending a URL to all links in a given email message

{% alert note %}
Link templates are an optional feature. If **Email Link Templates** is missing from the **Templates** section, reach out to your account manager to turn on the feature.
{% endalert %}

## Creating a link template

![][11]{: style="float:right;max-width:20%;"}

You can create an unlimited number of link templates to support your various needs. To create a link template:

1. Go to **Templates** > **Email Link Templates**. 
2. Click **Create Link Template**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is located at **Engagement** > **Templates & Media** > **Link Templates**.
{% endalert %}

There are two types of link templates you can create:

- [Link template that inserts before a URL](#prepend-link-template)
- [Link template that inserts after a URL](#append-link-template)

When using link templates and [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), Liquid must only be added within the body tag to ensure consistent rendering.

### Prepend: Create a link template that inserts before a URL {#prepend-link-template}

If you want to add a string or URL before the links in your email message, create a new link template and set the **Template Position** to **Before URL**. Next, enter a string that will always get prepended to your URL. 

A preview section is provided to give you an example of the insertion process.

![Template Position, Prepend URL, and Template Preview fields for the link template insertion process before a URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Append: Create a link template that inserts after a URL {#append-link-template}

If you want to add query parameters after a URL in your email message, create a new link template and set the **Template Position** to **After URL**. Next, enter query parameters (`value=something`) to the end of each URL.

You can have multiple parameters appended to the end of a URL.

![Template Position, Query Parameters, and Template Preview fields for the link template insertion process after a URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Using link templates in email campaigns

After your link templates are set up, you can select the template to use in your email.

- **HTML editor:** Go to the **Link Management** tab under the **Content** section. Select **Add a Link Template**, choose your link template, and select **Add**.

{% alert important %}
To access the **Link Management** tab in the updated HTML email editor, you must have link aliasing turned on. To turn on link aliasing, contact your account manager.
{% endalert %}

- **Drag-and-drop editor:** Select **Content** > **Link Management** tab. Then, select **Add a Link Template**. To access link templates in the drag-and-drop editor, you must have [link aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) turned on.

![Link Management tab in the drag-and-drop editor with an example list of link templates.][1]

{% alert note %}
Link templates aren't applied to plain text. This means Currents may show clicks that don't include the parameters from the link templates as those clicks may come from the plain text version of the email.
{% endalert %}

As you add link templates in the **Link Management** tab, scroll to the right to view the templates you've added.

## Managing link templates

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) link templates. Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
Archiving templates is not currently available for link templates.
{% endalert %}

## Frequently asked questions

For answers to frequently asked questions about link templates, check out our [Templates FAQ][10] page.

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
