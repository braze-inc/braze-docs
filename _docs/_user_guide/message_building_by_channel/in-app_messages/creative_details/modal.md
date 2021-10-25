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

Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

![Modal Specs][1a]{: style="max-width: 801px; border: none;"}

## Image and copy behavior

Modal in-app messages are designed to fit the device at the best and most filling ratios possible, while staying true to the size and ratios of your chosen image or copy for your message.

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend that your images be 500KB.

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Layout | Asset Size | Notes |
|--- | --- | ------ |
| Image + Text | 29:10 aspect ratio<br>Hi-Res 1450 x 500px<br> Min. 725 x 250px | Tall or narrow images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
| Image Only | Nearly any aspect ratio<br>Hi-Res up to 1200 x 2000px<br> Min. 600 x 600px | The message will resize to fit images of most aspect ratios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

You should __always__ [preview and test your messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) on a variety of devices to ensure that the most important areas of your image and message appear as expected.

### Font Awesome

Braze supports using [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) for modal in-app message icons.

## Larger screens

On a tablet or desktop browser, a modal in-app message will still sit in the center of the app screen as shown below.

![Modal Viewport][1b]{: style="max-width: 800px; border: none;"}

[1a]: {% image_buster /assets/img/modal-spec.png %}
[1b]: {% image_buster /assets/img/modal-large-viewport.png %}


