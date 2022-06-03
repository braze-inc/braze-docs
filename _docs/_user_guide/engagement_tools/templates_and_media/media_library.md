---
nav_title: Media Library
article_title: Media Library
page_order: 0
page_type: reference
description: "This reference article describes how to use the Media Library to manage your assets in a single, centralized location."
tool: Media

---

# Media library

> The Media Library allows you to manage your assets in a single, centralized location. To access this feature go into the **Media Library** tab in the [Templates & Media][4] section of your dashboard.

You can use the **Media Library** to:

* Upload multiple images at one time
* Upload Virtual Contact Files (.vcf)
* Upload a folder with your images (max: 50 images)
* Crop an existing image to create the right ratio for your messages
* Add tags or teams to help further organize your images
* Search by tags or teams in the new Media Library grid
* Drag and drop images or folders to be uploaded
* Delete images

![Media Library page that includes an "Upload To Library" section to drag and drop or upload files. There is also a list of uploaded content in the Media Library.][1]

## Stats available

Within the Media Library, you can see the image dimensions, URL, type as well as the date it was added to the library.

## Accessing the Media Library from a message composer

The Media Library acts as your dashboard's centralized location for assets, as all images are uploaded directly to it. This functionality gives you the flexibility to re-use images across different messages.

## Managing content

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) templates! Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert tip %} For more help with the Media Library, check out our [Templates & Media FAQs]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Image specifications

All images uploaded to the Media Library must be less than 5MB. Supported file types are PNG, JPEG, and GIF. For specific image recommendations by messaging channel, refer to the following sections.

### Content Cards

| Card type | Aspect ratio     | Image quality       |
| --------- | ---------------- | ------------------- |
| Classic   | 1:1 aspect ratio | 60px by 60px        |
| Captioned | 4:3 aspect ratio | 600px minimum width |
| Banner    | Any aspect ratio | 600px minimum width |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For more information, refer to [Content Card creative details]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

### Email

| Image type   | Aspect ratio     | Image quality       |
| ------------ | ---------------- | ------------------- |
| Header image | Any aspect ratio | 600px maximum width |
| Body image   | Any aspect ratio | 480px maximum width |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Smaller, high quality images will load faster, so we recommend that you use the smallest asset possible to achieve your desired output.

### In-app messages

{% tabs local %}
{% tab Full screen %}

| Layout | Aspect ratio | Image quality | Notes |
| ----- | ----- | ----- | ----- |
| Image and text | 6:5 aspect ratio | High resolution 1200px by 1000px<br><br>Minimum resolution 600px by 500px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport. |
| Image only | 3:5 aspect ratio | High resolution 1200px by 2000px<br><br>Minimum resolution 600px by 1000px | Cropping can occur on the left and right edges on taller devices. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Modal %}

| Layout | Aspect ratio | Image quality | Notes |
| ----- | ----- | ----- | ----- |
| Image and text | 29:10 aspect ratio | High resolution 1450px by 500px<br><br>Minimum resolution 600px by 205px | Tall images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
| Image only | Nearly any aspect ratio | High resolution 1200px by 2000px<br><br>Minimum resolution 600px by 600px | The message will resize to fit images of most aspect ratios.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Slideup %}

| Layout | Aspect ratio | Image quality | Notes |
| ----- | ----- | ----- | ----- |
| Image and text | 1:1 aspect ratio | High resolution 150px by 150px<br><br>Minimum resolution 50px by 50px | Images of various aspect ratios will fit into a square image container, without cropping.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% endtabs %}

For more information, refer to [In-app message creative details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% tabs local %}
{% tab iOS %}

| Aspect ratio | Image quality | Notes |
| ---- | ---- | ---- |
| 2:1 aspect ratio (recommended) | 1038px by 1038px maximum | As of January 2020, iOS rich push notifications can handle images 1038px by 1038px as long as they are under 10MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.|
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
| Expanded notification | 2:1 aspect ratio | Small: 512px by 256px<br>Medium: 1024px by 512px<br>Large: 2048px by 1024px |
| Inline image | 3:2 aspect ratio | N/A |

##### More resources

- [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Android rich notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)
- [Android inline image push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/)

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
