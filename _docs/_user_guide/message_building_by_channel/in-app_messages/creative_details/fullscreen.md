---
nav_title: "Fullscreen"
article_title: Fullscreen In-App Messages
description: "This reference article covers the message and design requirements of fullscreen in-app messages."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# Fullscreen in-app messages

> Fullscreen messages take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

{% tabs %}
{% tab Portrait %}

![Two fullscreen in-app messages side-by-side in portrait orientation, detailing the image and text recommendations. See following sections for details.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

![Two fullscreen in-app messages side-by-side in landscape orientation, detailing the image and text recommendations. See following sections for details.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Images

Fullscreen in-app messages will fill the entire height of a device and crop horizontally (left and right sides) as needed. Image and text fullscreen messages will fill 50% of the height of a device. All fullscreen in-app messages will fill the status bar on "notched" devices.

- All images must be less than 5&nbsp;MB.
- We only accept PNG, JPEG, and [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs) file types.
- We recommend that your images be 500&nbsp;KB.

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Portrait

| layout | asset size | notes |
|--- | --- | --- |
| Image and text | 6:5 aspect ratio<br> High-res 1200 x 1000&nbsp;px<br> Minimum 600 x 500&nbsp;px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport |
| Image only | 3:5 aspect ratio<br> High-res 1200 x 2000&nbsp;px<br> Minimum 600 x 1000&nbsp;px | Cropping can occur on the left and right edges on taller devices |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Landscape

| layout | asset size | notes |
|--- | --- | --- |
| Image and text | 10:3 aspect ratio<br> High-res 2000 x 600px<br> Minimum 1000 x 300&nbsp;px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport |
| Image only | 5:3 aspect ratio<br> High-res 2000 x 1200px<br> Minimum 1000 x 600&nbsp;px | Cropping can occur on the left and right edges on taller devices |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Image safe zone

When previewing a fullscreen in-app message in the Braze platform, you can enable the Image Safe Zone to the area of the message that is safe from cropping when displayed across devices. In addition to testing the Image Safe Zone in the preview pane, we recommend you [test your message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) as always.

![Previewing an in-app message in Braze with "Show Image Safe Zone" enabled. The image safe zone is an overlay over the image that visualizes what parts of the image will be safe from cropping.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Larger screens

On a tablet or desktop browser, a fullscreen in-app message will sit in the center of the app screen, as shown in the following screenshot.

{% tabs %}
{% tab Portrait %}

![Fullscreen in-app message as it would appear on a large screen in portrait orientation. The message appears as a large modal that sits in the center of the screen.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

![Fullscreen in-app message as it would appear on a large screen in landscape orientation. The message appears as a large modal that sits in the center of the screen.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

