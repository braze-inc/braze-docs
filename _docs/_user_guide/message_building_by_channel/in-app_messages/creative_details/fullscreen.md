---
nav_title: "Full-Screen"
description: "This reference article covers the message and design requirements of full-screen in-app messages."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# Full-Screen In-App Messages

Full-screen messages take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.


![Full-Screen Specs][3a]{: style="max-width: 801px; border: none;"}

[3a]: {% image_buster /assets/img/full-screen-spec.png %}
[3b]: {% image_buster /assets/img/full-screen-large-viewport.png %}
[3c]: {% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %}

## Images

Full-screen in-app messages will fill the entire height of a device and crop horizontally (left and right sides) as needed. Image + text full-screen messages will fill 50% of the height of a device. All full-screen in-app messages will fill the status bar on "notched" devices.

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend that your images be 500KB.

{% alert tip %}Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

#### Portrait

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 6:5 aspect ratio<br>Hi-Res 1200 x 1000px<br> Min. 600 x 500px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport |
| Image Only | 3:5 aspect ratio<br>Hi-Res 1200 x 2000px<br> Min. 600 x 1000px | Cropping can occur on the left and right edges on taller devices |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Landscape

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 10:3 aspect ratio<br>Hi-Res 2000 x 600px<br> Min. 1000 x 300px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport |
| Image Only | 5:3 aspect ratio<br>Hi-Res 2000 x 1200px<br> Min. 1000 x 600px | Cropping can occur on the left and right edges on taller devices |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


### Image Safe Zone

When previewing a full-screen in-app message in the Braze platform, you can enable the Image Safe Zone to the area of the message that is safe from cropping when displayed across devices. In addition to testing the Image Safe Zone in the preview pane, we recommend you [test your message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) as always.

![Image Safe Zone][3c]


## Larger Screens

On a tablet or desktop browser, a full-screen in-app message will sit in the center of the app screen, as shown below.

![Full-Screen Viewport][3b]{: style="max-width: 800px; border: none;"}
