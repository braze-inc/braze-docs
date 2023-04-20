---
nav_title: Creative Details
article_title: Creative Details
page_order: 4
layout: dev_guide
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! All in-app messages templates are designed to display varying lengths of text and sizes of images across modern devices. In order to ensure your message displays well on all phones, tablets, and computers, we recommend you follow these guidelines and always <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>test your messages</a> before launching. Check out the following individual message type's Creative Specs or the global Creative Details article."
description: "This landing hub covers the design and content requirements for the three types of in-app messages, modal, slideup, and fullscreen."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Specifications for Each Message Type"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/icon_modal.png
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/icon_slideup.png
- name: "Fullscreen"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/icon_full_screen.png

---

## Content guidelines

### Text

For in-app message bodies or headers, we recommend you keep it short and sweet - one to two lines for headers; up to three for bodies. After three lines, the message will likely need to vertically scroll, and users might not engage with all of the content. The threshold that triggers the scroll can vary depending on the end user's device size, custom styling, or presence of images within messages, but three lines is usually safe!

If you are using the newest generation of in-app messages (Generation 3), you'll find that the fonts default to the Operating System default Sans Serif for iOS and Android. Web in-app messages will default to Helvetica.

### Images

Our guidelines for images are more structured than those for text, as we want to ensure your messages display as-intended, and beautifully across phones, tablets, and computers of all models and sizes.

In general, Braze recommends using images that fit into a 16:10 screen.

- **All images must be less than 5MB.**
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend hosting images in the [Braze Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) to enable the Braze SDK to download assets from our CDN for offline message display.
- For fullscreen messages, follow our guidelines for [image safe zone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab FullScreen %}

![Fullscreen in-app message taking over an app screen. The fullscreen message includes a large image, header, message body, and two buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 6:5 aspect ratio<br>Hi-Res 1200 x 1000px<br> Min. 600 x 500px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport |
| Image Only | 3:5 aspect ratio<br>Hi-Res 1200 x 2000px<br> Min. 600 x 1000px | Cropping can occur on the left and right edges on taller devices |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Further details for fullscreens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

![Modal in-app message appearing in the center of an app and website as a dialog. The modal includes an image, header, message body, and two buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Layout | Asset Size | Notes |
|--- | --- | ------ |
| Image + Text | 29:10 aspect ratio<br>Hi-Res 1450 x 500px<br> Min. 600 x 205px | Tall images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
| Image Only | Nearly any aspect ratio<br>Hi-Res up to 1200 x 2000px<br> Min. 600 x 600px | The message will resize to fit images of most aspect ratios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Further details for modals]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

![Slideup in-app message appearing from the bottom of the app screen. The slideup includes an icon image and a brief message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 1:1 aspect ratio<br>Hi-Res 150 x 150px<br> Min. 50 x 50px | Images of various aspect ratios will fit into a square image container, without cropping. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Further details for slideups]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIFs and videos

Braze currently supports GIFs for Web (included), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/), and iOS (included) in-app messaging, given that it has been enabled during the desired platform integration. For more on video in in-app messages, see our [Customization documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Additional considerations

Braze in-app messages have both global and individual creative specifications. For more information about fully customizing in-app messages, go to our [Customization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

<br>
