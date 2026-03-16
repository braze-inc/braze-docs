---
nav_title: Image specifications
article_title: Image specifications
page_order: 1

page_type: reference
description: "This reference article describes the recommended image sizes and specifications for each channel type."
tool:
  - Templates
  - Media

---

# Image specifications

> In general, smaller and high-quality images will load faster, so we recommend using the smallest asset possible to achieve your desired output. To maximize your image use in specific channels, refer to the details in this article.

You should always [preview and test your messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) on a variety of devices to confirm that the most important areas of your image and message appear as expected.

## Image behavior

{% multi_lang_include image_specs.md variable_name='image behavior' %}

## Video

Videos uploaded to the media library can only be used in WhatsApp messages. For more information, refer to [Creating a WhatsApp message]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#outbound-messages).

## GIFs

GIFs are supported in iOS push, in-app messages, email, Content Cards, and MMS or RCS messages. GIFs with very elongated shapes (for example, 3000 x 2 pixels) or 300 or more frames may fail to upload, even if the total file size is small.

## Channel guidance

### Content Cards

{% multi_lang_include image_specs.md variable_name='content cards' %}

### Email

{% multi_lang_include image_specs.md variable_name='email' %}

### In-app messages

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe-zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

For more information, refer to [In-app message creative details]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

#### Font Awesome

Braze supports using [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) for modal in-app message icons.

### Push notifications

{% multi_lang_include image_specs.md variable_name='payload size' %}

{% multi_lang_include image_specs.md variable_name='push notifications' %}

#### Recommended message lengths

For best results, refer to the following message length guidelines when crafting push messages. There may be some variance depending on the presence of an image, the notification state (iOS) and display setting of the user's device, as well as the size of the device.

| Message type | Recommended length (text only) | Recommended length (rich) |
| --- | --- | --- |
| iOS lock screen | 160 characters | 130 characters |
| iOS Notification Center | 160 characters | 130 characters |
| iOS banner alert | 80 characters | 65 characters |
| Android lock screen | 49 characters | N/A |
| Android notification drawer | 597 characters | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

For more information about iOS character counts, see [iOS character count guidelines]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count).

#### Web push

{% tabs %}
{% tab Images %}

| Browser | Recommended icon size |
| --- | --- |
| Chrome | 192 x 192 px or larger |
| Firefox | 192 x 192 px or larger |
| Safari | 192 x 192 px or larger (configurable per campaign with Safari 16 on macOS 13+) |
| Opera | 192 x 192 px or larger |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| Browser | Platform | Large image size |
| --- | --- | --- |
| Chrome | Android | 2:1 aspect ratio |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 aspect ratio |
| Edge | Windows | 2:1 aspect ratio |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 aspect ratio |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| Browser | Platform | Maximum title length | Maximum body length |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### Push notification examples

{% tabs %}
{% tab iOS %}

![iOS push notification with text that reads: "Hi! This is an iOS Push with an image" with an emoji. There is a small image beside the text.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS push notification on a hard push with the same text as the previous message with an expanded image preceding the text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Android push notification with a large image under the message text.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Large image notifications display best when using an image of at least 600 x 300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

For additional resources, see [Push image and text specifications]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/).

