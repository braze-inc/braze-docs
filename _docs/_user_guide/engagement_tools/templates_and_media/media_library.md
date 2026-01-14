---
nav_title: Media Library
article_title: Media Library
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

All images uploaded to the media library must be less than 5&nbsp;MB. Supported file types are PNG, JPEG, GIF, and SVG. For specific image recommendations by messaging channel, refer to the following sections.

### Content Cards

{% multi_lang_include image_specs.md variable_name='content cards' %}

### Email

{% multi_lang_include image_specs.md variable_name="email"  %}

### In-app messages

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

For more information, refer to [In-app message creative details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
For additional resources, see [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Video

Videos that are uploaded to the media library can only be used in WhatsApp messages for now. For more information, refer to [Creating a Whatsapp Message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Generating images with BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Before using this feature, review [how your data is used and sent to OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
