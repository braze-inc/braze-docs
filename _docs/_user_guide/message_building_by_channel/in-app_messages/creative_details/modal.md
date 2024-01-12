---
nav_title: Modal
article_title: Modal In-App Messages
page_order: 1
channel:
  - in-app messages
tool:
  - Media
description: "This reference article covers the message and design requirements of modal in-app messages."

---

# Modal in-app messages

> Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

![Two modal in-app messages side-by-side, detailing the image and text recommendations. See following sections for details.][1a]{: style="max-width: 801px; border: none;"}

## Image sizes and specifications

Modal in-app messages are designed to fit the device at the best and most filling ratios possible, while staying true to the size and ratios of your chosen image or copy for your message.

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

You should always [preview and test your messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) on a variety of devices to ensure that the most important areas of your image and message appear as expected.

{% multi_lang_include image_specs.md variable_name='payload size' %}

### In-app messages

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

#### Font Awesome

Braze supports using [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) for modal in-app message icons.

### Push notifications

{% multi_lang_include image_specs.md variable_name='push notifications' %}

### Email

{% multi_lang_include image_specs.md variable_name='email' %}

## Image behavior

| Layout | Behavior |
| --- | --- |
| Image and text | Tall or narrow images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
| Image only | The message will resize to fit images of most aspect ratios. |
{: .reset-td-br-1 .reset-td-br-2}

### Larger screens

On a tablet or desktop browser, a modal in-app message will still sit in the center of the app screen as shown in the following screenshot.

![Modal in-app message as it would appear on a large screen. Similarly to phone screens, the message sits in the center of the screen.][1b]{: style="max-width: 800px; border: none;"}

[1a]: {% image_buster /assets/img/modal-spec.png %}
[1b]: {% image_buster /assets/img/modal-large-viewport.png %}


