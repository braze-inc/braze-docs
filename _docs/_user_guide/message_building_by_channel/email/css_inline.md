---
nav_title: CSS Inlining
article_title: CSS Inlining
page_order: 5.1
description: "This reference article covers how to enable CSS inlining and some best practices."
channel:
  - email

---

# CSS inlining

> CSS inlining is a form of email preprocessing that moves styles in a CSS style sheet into the body of an HTML email. The term "inlining" refers to the fact that styles are applied "inline" to individual HTML elements.

For some email clients, CSS inlining can improve the way that emails render and help ensure that your emails look the way you expect.

## Using CSS inlining

You can control whether CSS inlining is turned on or off for any email message through a checkbox in the **Sending Info** tab of the HTML editor.

![Checkbox to manage CSS inlining in HTML composer.][2]{: style="max-width:80%;"} 

### Default inlining state

You can set a default on or off state globally from **Manage Settings** > **Email Settings** > **Inline CSS**. This setting ensures that all new email messages start with the desired default value. Note that changing this setting will not affect any of your existing email messages. You can also override this default at any time while composing email messages.

![Inline CSS on new emails by default option located in email settings.][1]

[1]:{% image_buster /assets/img_archive/css-inline1.png %}
[2]:{% image_buster /assets/img_archive/css-inline2.png %}
