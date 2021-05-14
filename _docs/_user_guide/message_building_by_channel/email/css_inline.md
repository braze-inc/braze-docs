---
nav_title: CSS Inlining
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 3
description: "CSS inlining can improve the way emails render. This reference article covers how to enable CSS inlining and some best practices."

tool:
  - Dashboard

channel:
  - email

---
# CSS Inlining

## What is CSS inlining?

CSS Inlining is a form of email preprocessing that moves styles in a CSS style sheet into the body of an HTML email. The term "inlining" refers to the fact that styles are applied "inline" to individual HTML elements.

## Why use CSS inlining?

For some email clients, CSS inlining can improve the way that emails render and help ensure that your emails look the way you expect.

## How do I enable/disable CSS inlining?

You can control whether CSS Inlining is turned on or off for any email message through a checkbox in the Sending Info section of Braze's Email Composer.

![css-inline2][2]

Additionally, a default on or off state can be set globally from Manage App Group > Email Settings > Inline CSS. This setting ensures that all new email messages start with the desired default value. Note that changing this setting will not affect any of your existing email messages. You can also override this default at any time while composing email messages.

![css-inline1][1]

[1]:{% image_buster /assets/img_archive/css-inline1.png %}
[2]:{% image_buster /assets/img_archive/css-inline2.png %}
