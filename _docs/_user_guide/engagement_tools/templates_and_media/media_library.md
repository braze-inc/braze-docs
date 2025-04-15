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

![Media Library page that includes an "Upload To Library" section to drag and drop or upload files. There is also a list of uploaded content in the media library.][1]

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

![Two common ways of accessing the media library depending on the message composer. One shows the email Drag and Drop Editor with the title "Images and GIFs" and a button to "Add from Media Library". The other shows the standard editors, such as push and in-app messages, with the title "Media" and a button to "Add Image".][1.5]{: style="border:none"}

## Generate an image using AI {#generate-ai}

You can generate images for your media library using [DALL·E 3](https://openai.com/index/dall-e-3/), an AI system from OpenAI, a Braze third-party provider. This system can create realistic images and art from a description in natural language. Each request generates four variations of your prompt, and your company can generate images 10 times per day. This total applies to all users in your company.

1. From the media library, select <i class="fas fa-wand-magic-sparkles"></i> **AI Image Generator**.
2. Enter a description of the image you want to generate, up to 300 characters. The more detailed the description, the better your result. This feature only supports text input—uploading an image as a reference isn’t available.
3. Select **Generate Images**. It can take about a minute for images to generate.
4. Select <i class="fas fa-download" title="Add image to Media Library"></i> on the images you would like to add to your media library.

![AI image generator modal in the media library.][6]{: style="max-width:75%"}

Between you and Braze, any images generated using DALL·E 3 are your intellectual property. Braze will not assert any claims of copyright ownership on such images and makes no warranty of any kind with respect to any AI-generated content or images.

To generate images, Braze will send your query to OpenAI's API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the input you provide. As detailed in [OpenAI’s API Platform Commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, which may include its [Usage Policy](https://openai.com/policies/usage-policies) and its [Sharing & Publication Policy](https://openai.com/policies/sharing-publication-policy). Braze makes no warranty of any kind with respect to any AI-generated content. 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
