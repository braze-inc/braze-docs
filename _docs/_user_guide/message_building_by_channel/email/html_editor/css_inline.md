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

For some email clients, CSS inlining can improve the way that emails render and help confirm that your emails look the way you expect.

## Using CSS inlining

You can control whether CSS inlining is turned on or off for any email message through a checkbox in the **Sending Info** tab of the HTML editor.

![Checkbox to manage CSS inlining in HTML composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:80%;"}

### Default inlining state

You can set a default on or off state globally from **Settings** > **Email Preferences**. Locate the setting for **CSS Inlining**. This setting determines the desired default value that all new email messages start with. Note that changing this setting will not affect any of your existing email messages. You can also override this default at any time while composing email messages.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is located at **Manage Settings** > **Email Settings**.
{% endalert %}

![Inline CSS on new emails by default option located in email settings.]({% image_buster /assets/img_archive/css-inline1.png %})

[1]:{% image_buster /assets/img_archive/css-inline1.png %}
[2]:{% image_buster /assets/img_archive/css-inline2.png %}
