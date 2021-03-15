---
nav_title: Link Templates
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 4
description: "Link Templates allow users to append parameters or pre-append URLs to all links in an Email message."
---
# Link Templates

> Link Templates allow users to append parameters or pre-append URLs to all links in an Email message.

This can be ideally used for the following use cases:

1. Appending Google Analytics query parameters to all links in a given Email message easily.
2. Pre-appending a URL to all links in a given Email message

## Creating a Link Template

On the Braze dashboard, Link Templates are found in the Templates & Media section. Dashboard users can create an unlimited number of Link Templates to support their various needs. Note that when using Link Templates and [Liquid][4], Liquid code must only be added within the body tag to ensure consistent rendering. 

There are two types of Link Templates a user can create.

#### Create a Link Template that inserts before a URL

Clients who want to pre-append a string or URL before a link in their Email message can create a new Link Template and choose the Template position to be "Before URL".  This will allow you to enter a string that will always get appended before a URL.  A preview section is provided to give you an example of the insertion process.

![pre-append][3]

#### Create a Link Template that appends after a URL

Clients who want to append query parameters after a URL in their Email message can create a new Link Template and choose the Template position to be "After URL".  This will allow you to enter query parameters (value=something) to the end of each URL.  You can have multiple parameters appended to the end of a URL.

![postappend][2]

### Selecting a Template

Once your templates are setup, you can select which template you would like to use from the Email Editor Composer.
Proceed to open the Email composer, click Content Library and select the Link Templating tab.  You will see all the links present in your Email and can add the template from there.

![messagecomposer][1]

### Managing Link Templates
You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) link templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
Archiving templates is not currently available for [Link Templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

### FAQ

*Q: Can I upload multiple templates to my Email?*

Yes, you can insert as many templates as you would like in your Email messages.  As a best practice, you should test your emails to ensure that the links are not exceeding 2000 characters as most browsers will shorten or cut the links.

*Q: How do I preview my links with all of the tags applied?*

Once you have applied the Link Template, you can send yourself a test email to view all the links.  Additionally, you can open the links from the preview pane in a new tab to view the links.  Lastly, you can hover over the links in the Preview Pane and see them at the bottom of your browser.

*Q: How does Link Templating work with Liquid?*

Link Templates are expanded and added to the each URL prior to any Liquid expansion happens.  As a best practice, if part of your URL is generated using a Liquid snippet, it is recommended that the URL base and "?" is hardcoded for Link Templates to be expanded correctly.  Refrain from adding the "?" to your Liquid as this will cause Link Templates to first add a "?" and then later the Liquid expansion process will add a second "?" 


[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
