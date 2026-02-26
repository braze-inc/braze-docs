---
nav_title: Media library
article_title: Media library
page_order: 0
page_type: reference
description: "This reference article covers the media library. Here, you can learn how to manage your assets in a single, centralized location, generate image using AI, access media in your message composer."
tool: Media

---

# Media library

> The media library allows you to manage your assets in a single, centralized location. 

## Media library vs. CDN

Using the media library instead of a Content Delivery Network (CDN) provides better caching and performance for in-app messages. All media library assets found in an in-app message will be pre-cached for faster display and will be available for offline display. Additionally, the media library is integrated with Braze composers, allowing marketers to select or tag images instead of copying and pasting image URLs.

## Accessing the media library

Within the media library, you can see the asset type, size, dimensions, URL, the date it was added to the library, and other information. To access your Braze media library, go to THIS > **Templates**. Here, you can:

* Upload multiple images at one time
* Upload Virtual Contact Files (.vcf)
* Upload video files for use in WhatsApp messages
* Upload a folder with your images (maximum 50 images)
* [Generate an image using AI](#generate-ai) and store it in the media library
* Crop an existing image to create the right ratio for your messages
* Add tags or teams to help further organize your images
* Search by tags or teams in the media library grid
* Drag and drop images or folders to be uploaded
* Delete images

![Media Library page that includes an "Upload To Library" section to drag and drop or upload files. There is also a list of uploaded content in the media library.]({% image_buster /assets/img_archive/media_library_main.png %})

Later when drafting a message in Braze, you can pull in your images from the media library.

![Two common ways of accessing the media library depending on the message composer. One shows the email Drag and Drop Editor with the title "Images and GIFs" and a button to "Add from Media Library". The other shows the standard editors, such as push and in-app messages, with the title "Media" and a button to "Add Image".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} For more help with the media library, check out our [Templates & Media FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Image specifications

All images uploaded to the media library must be less than 5&nbsp;MB. Supported file types are PNG, JPEG, GIF, SVG, and WebP. For specific image recommendations by messaging channel, refer to the following sections.

### Content Cards

{% multi_lang_include image_specs.md variable_name='content cards' %}

### Email

{% multi_lang_include image_specs.md variable_name="email"  %}

### In-app messages

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

For more information, refer to [In-app message creative details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

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

For more information about iOS character counts, see [iOS character count guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

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

### Video

Videos that are uploaded to the media library can only be used in WhatsApp messages for now. For more information, refer to [Creating a Whatsapp Message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Generating images with BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Before using this feature, review [how your data is used and sent to OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
