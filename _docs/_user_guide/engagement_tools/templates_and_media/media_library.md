---
nav_title: Media Library
article_title: Media Library
page_order: 0
page_type: reference
description: "This reference article covers the Media Library. Here, you can learn how to manage your assets in a single, centralized location, generate image using AI, access media in your message composer."
tool: Media

---

# Media library

> The Media Library allows you to manage your assets in a single, centralized location. To access this feature go into the **Media Library** tab in the [Templates & Media][4] section of your dashboard.

You can use the **Media Library** to:

* Upload multiple images at one time
* Upload Virtual Contact Files (.vcf)
* Upload a folder with your images (max 50 images)
* [Generate an image using AI](#generate-ai) and store it in the Media Library
* Crop an existing image to create the right ratio for your messages
* Add tags or teams to help further organize your images
* Search by tags or teams in the Media Library grid
* Drag and drop images or folders to be uploaded
* Delete images

![Media Library page that includes an "Upload To Library" section to drag and drop or upload files. There is also a list of uploaded content in the Media Library.][1]

{% alert tip %} For more help with the Media Library, check out our [Templates & Media FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Image details

Within the Media Library, you can see the image type, size, dimensions, URL, and date it was added to the library.

## Image specifications

All images uploaded to the Media Library must be less than 5MB. Supported file types are PNG, JPEG, and GIF. For specific image recommendations by messaging channel, refer to the following sections.

### Content Cards

| Card type | Aspect ratio     | Image quality       |
| --------- | ---------------- | ------------------- |
| Classic   | 1:1 aspect ratio | 60 x 60 px        |
| Captioned | 4:3 aspect ratio | 600 px minimum width |
| Banner    | Any aspect ratio | 600 px minimum width |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For more information, refer to [Content Card creative details]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

### Email

| Image type   | Aspect ratio     | Image quality       |
| ------------ | ---------------- | ------------------- |
| Header image | Any aspect ratio | 600 px maximum width |
| Body image   | Any aspect ratio | 480 px maximum width |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Smaller, high quality images will load faster, so we recommend that you use the smallest asset possible to achieve your desired output.

### In-app messages

{% tabs local %}
{% tab Full screen %}

| Layout | Aspect ratio | Image quality | Notes |
| ----- | ----- | ----- | ----- |
| Image and text | 6:5 aspect ratio | High resolution 1200 x 1000 px<br><br>Minimum resolution 600 x 500 px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport. |
| Image only | 3:5 aspect ratio | High resolution 1200 x 2000 px<br><br>Minimum resolution 600 x 1000 px | Cropping can occur on the left and right edges on taller devices. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Modal %}

| Layout | Aspect ratio | Image quality | Notes |
| ----- | ----- | ----- | ----- |
| Image and text | 29:10 aspect ratio | High resolution 1450 x 500 px<br><br>Minimum resolution 600 x 205 px | Tall images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
| Image only | Nearly any aspect ratio | High resolution 1200 x 2000 px<br><br>Minimum resolution 600 x 600 px | The message will resize to fit images of most aspect ratios.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Slideup %}

| Layout | Aspect ratio | Image quality | Notes |
| ----- | ----- | ----- | ----- |
| Image and text | 1:1 aspect ratio | High resolution 150 x 150 px<br><br>Minimum resolution 50 x 50 px | Images of various aspect ratios will fit into a square image container, without cropping.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% endtabs %}

For more information, refer to [In-app message creative details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% tabs local %}
{% tab iOS %}

| Aspect ratio | Image quality | Notes |
| ---- | ---- | ---- |
| 2:1 aspect ratio (recommended) | 1038 x 1038 px maximum | As of January 2020, iOS rich push notifications can handle images 1038 x 1038 px as long as they are under 10MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### More resources

- [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS rich notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)

{% endtab %}
{% tab Android %}

Android rich notifications do not support GIFs.

| Image type | Aspect ratio | Image quality |
| ---- | ----- | ---- |
| Push icon | 1:1 aspect ratio | N/A |
| Expanded notification | 2:1 aspect ratio | Small: 512 x 256 px<br>Medium: 1024 x 512 px<br>Large: 2048 x 1024 px |
| Inline image | 3:2 aspect ratio | N/A |

##### More resources

- [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Android rich notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)
- [Android inline image push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/)

{% endtab %}
{% endtabs %}

## Accessing the Media Library from a message composer

The Media Library acts as your dashboard's centralized location for assets, as all images are uploaded directly to it. This lets you re-use images across different messages.

![Two common ways of accessing the Media Library depending on the message composer. One shows the email Drag and Drop Editor with the title "Images and GIFs" and a button to "Add from Media Library". The other shows the standard editors, such as push and in-app messages, with the title "Media" and a button to "Add Image".][1.5]{: style="border:none"}

## Generate an image using AI {#generate-ai}

You can generate images for your Media Library using [DALL·E 2](https://openai.com/dall-e-2/), an AI system from OpenAI that can create realistic images and art from a description in natural language. Each request generates four variations of your prompt, and your company can generate images 10 times per day. This total applies to all users in your company.

1. From the Media Library, click <i class="fas fa-wand-magic-sparkles"></i> **AI Image Generator**.
2. Enter a description of the image you want to generate, up to 300 characters. The more detailed the description, the better your result.
3. Click **Generate Images**. It can take about a minute for images to generate.
4. Click <i class="fas fa-download" title="Add image to Media Library"></i> on the images you like to add them to your Media Library.

![AI image generator modal in the Media Library.][6]{: style="max-width:75%"}

Between you and Braze, any images generated using DALL·E 2 is your intellectual property. Braze will not assert any claims of copyright ownership on such images and makes no warranty of any kind with respect to any AI-generated content or images.

[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
