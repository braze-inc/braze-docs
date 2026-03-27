---
nav_title: Link templates
article_title: Link Templates
page_order: 4
description: "This article covers how to create different types of link templates in your emails."
tool:
  - Templates
channel:
  - email

---

# Link templates

> With link templates, you can create dynamic and reusable links for your email campaigns by appending parameters or prepending URLs. This can create consistency in the URLs across your campaigns and messages. 

{% alert note %}
Link templates are an optional feature. If **Email Link Templates** is missing from the **Templates** section, contact your account manager to turn on the feature.
{% endalert %}

## How it works

Link templates are most often used in these following use cases:

- Appending Google Analytics query parameters to all links in a given email message
- Prepending a URL to all links in a given email message

Let's say you're running a promotional email campaign for a new product launch. You can use a link template that directs users to the product page and personalize the link to include your user's name or a specific promotional code. This can allow you to track how many users have clicked on the link and have made a purchase. This way, you can create consistency across your links and better track your analytics.

## Creating a link template

You can create an unlimited number of link templates to support your various needs. To create a link template, do the following:

1. Go to **Templates** > **Email Link Templates**. 
2. Select **Create email link template**.
3. Give your link template a name.
4. (Optional) Add a description, team, or tag to add details about the link template.
5. (Optional) Select the toggle to automatically add the link template to links in email campaigns and Canvases. This applies when adding a new link to any new or existing email.

There are two types of link templates you can create:

- [Link template that inserts before a URL](#prepend-link-template)
- [Link template that inserts after a URL](#append-link-template)

When using link templates and [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), Liquid must only be added within the body tag to ensure consistent rendering.

### Prepend: Create a link template that inserts before a URL {#prepend-link-template}

To add a string or URL before the links in your email message, do the following:

1. Create a new link template.
2. Set the **Template Position** to **Before URL**. 
3. Enter a string that will always get prepended to your URL. 

The **Template preview** is provided to give you an example of how the link template will be inserted before a URL.

![Template Position, Prepend URL, and Template Preview fields for the link template insertion process before a URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Append: Create a link template that inserts after a URL {#append-link-template}

If you want to add query parameters after a URL in your email message:

1. Create a new link template.
2. Set the **Template Position** to **After URL**. 
3. Enter the query parameters (`value=example`) to the end of each URL. You can have multiple parameters appended to the end of a URL.

![Template Position, Query Parameters, and Template Preview fields for the link template insertion process after a URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Using link templates in email campaigns

After your link templates are set up, you can select the template to use in your email.

1. Create an email campaign using the drag-and-drop editor or HTML editor.
2. In the **Content** section, select the **Link Management** tab.
3. Select **Add a Link Template**, then choose your link template.
4. Select **Add**.

{% alert important %}
To access the **Link Management** tab, you must have link aliasing turned on. To turn on link aliasing, contact your account manager.
{% endalert %}

![Link Management tab in the drag-and-drop editor with an example list of link templates.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Link templates aren't applied to plain text. This means Currents may show clicks that don't include the parameters from the link templates as those clicks may come from the plain text version of the email.
{% endalert %}

As you add link templates in the **Link Management** tab, scroll to the right to view the templates you've added. If existing links within an email already have a link template added, newly added links will also have the link template added by default.

## Managing link templates

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) link templates. Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
Archiving templates is not currently available for link templates.
{% endalert %}

{% alert tip %}
When including links in your message, be sure to start the URLs with `http://` or `https://`.
{% endalert %}

## Troubleshooting

### Missing UTM parameters

Link templating isn't applied to links in HTML comments. Check that your links aren't in HTML comments that are conditional statements.

### UTM parameters aren't displaying in each link, but are present when viewed in-browser

Check if the full path to the website was added. If not, the UTM parameter was not applied to clicked links in those cases. The user may still be redirected to the correct page from the website. For example, if the full website link is `https://www.somewebsite.com/women/designer/johnjane` and the link added to the email body is `https://www.somewebsite.com/designer/johnjane`, it's expected that the UTM parameters won't be added to the link.

### UTM parameters aren't appending for a link rendered from a Liquid tag

Before appending UTM parameters to a link, Braze checks if the resulting link is likely to fail. If so, Braze won't append the parameters.

### UTM values don't populate compared to the preview in a test send

When test sending link templates, `{{${user_id}}}` does not get rendered. Instead, duplicate the campaign and set it to target your internal users' email or `external_id` and launch the campaign to verify that all UTM parameters from the link template are populated.

## Frequently asked questions

For answers to frequently asked questions about link templates, check out our [Templates FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) page.

