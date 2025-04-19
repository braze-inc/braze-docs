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

You can find the **Media Library** under **Templates**.

You can use the **Media Library** to:

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

{% alert tip %} For more help with the media library, check out our [Templates & Media FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Image details

Within the media library, you can see the asset type, size, dimensions, URL, the date it was added to the library, and other information. 

### Using the media library versus a CDN

Using the media library provides better caching and performance for in-app messages. All media library assets found in an in-app message will be pre-cached for faster display and will be available for offline display. Additionally, the media library is integrated with Braze composers, allowing marketers to select or tag images instead of copying and pasting image URLs.

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

##### More resources

- [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### Video

Videos that are uploaded to the media library can only be used in WhatsApp messages for now. For more information, refer to [Creating a Whatsapp Message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
Adding videos to WhatsApp messages is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Accessing the media library from a message composer

The media library acts as your dashboard's centralized location for assets, as all images are uploaded directly to it. This lets you reuse images across different messages.

![Two common ways of accessing the media library depending on the message composer. One shows the email Drag and Drop Editor with the title "Images and GIFs" and a button to "Add from Media Library". The other shows the standard editors, such as push and in-app messages, with the title "Media" and a button to "Add Image".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

## AI-generated images {#generate-ai}

{% multi_lang_include generative_ai/ai_images.md %}

{% alert important %}
Before using this feature, review [how your data is used and sent to OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_images#ai-policy).
{% endalert %}
