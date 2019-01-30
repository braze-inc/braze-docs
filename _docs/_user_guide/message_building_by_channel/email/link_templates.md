---
nav_title: Link Templates
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 4
---
# Link Templates

Link Templates, allow users to append parameters or pre-append URI's to all links in an Email message.  This can be ideally used for the following use cases:

1. Appending Google Analytics query parameters to all links in a given Email message easily.
2. Pre-appending a URI to all links in a given Email message

## Creating a Link Template

On the Braze dashboard, Link Templates are found in the Templates & Media section. Dashboard users can create an unlimited number of Link Templates to support their various needs.

There are two types of Link Templates a user can create.

#### Create a Link Template that inserts before a URI

Clients who want to pre-append a string or URI before a link in their Email message can create a new Link Template and choose the Template position to be "Before URI".  This will allow you to enter a string that will always get appended before a URI.  A preview section is provided to give you an example of the insertion process.

![pre-append][3]

#### Create a Link Template that appends after a URI

Clients who want to append query parameters after a URI in their Email message can create a new Link Template and choose the Template position to be "After URI".  This will allow you to enter query parameters (value=something) to end of each URI.  You can have multiple parameters appended to the end of a URI.

![postappend][2]

### Selecting a Template

Once your templates are setup, you can select which template you would like to use from the Email Editor Composer.
Proceed to open the Email composer, click Content Library and select Link Templating tab.  You will see all the links present in your Email and can add the template from there.

![messagecomposer][1]

### FAQ

*Q: Can I upload multiple templates to my Email?*

Yes, you can insert as many templates as you would like in your Email messages.  As best practice, you should test your emails to ensure that the links are not exceeding 2000 characters as most browsers will shorten or cut the links.

*Q: How do I preview my links with all of the tags applied?*

Once you have applied the Link Template, you can send yourself a test email to view all the links.  Additionally you can open the links from the preview pane in a new tab to view the links.  Lastly you can hover over the links in the Preview Pane and see them at the bottom of your browser.


[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
