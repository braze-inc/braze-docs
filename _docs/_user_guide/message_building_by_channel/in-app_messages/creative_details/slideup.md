---
nav_title: Slideup
article_title: Slideup In-app Messages
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "This reference article covers the message and design requirements of sliedup in-app messages."

---

# Slideup in-app messages

Our slideups typically appear at the top or bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information. These are non-obtrusive and allow your end users to continue to interact with your app while the message displays.

![Two slide-up in-app messages, one appearing from the top of the screen and the other from the bottom, detailing the image and text recommendations. See following sections for details.][2a]{: style="max-width: 40%; border: none;"}

## Image and copy behavior

Slideup messages can contain up to three lines of copy before truncation with ellipses. Images in slideups will never be cropped or clipped - they will always scale down to fit within the 50X50 image container.

- All images must be less than 5MB.
- We only accept PNG, JPG, and GIF file types.
- We recommend that your images be 500KB.

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 1:1 aspect ratio<br>Hi-Res 150 x 150px<br> Min. 50 x 50px | Images of various aspect ratios will fit into a square image container, without cropping. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

You should always [preview and test your messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) on a variety of devices to ensure that the most important areas of your image and message appear as expected.

[2a]: {% image_buster /assets/img/slideup-spec.png %}
[2b]: {% image_buster /assets/img/slideup-large-viewport.png %}

### Larger screens

On a tablet or desktop browser, a slideup in-app message will sit in the corner of the app screen as shown in the following screenshot (unless designated otherwise when creating the in-app message).

![Slideup in-app message as it appears on a larger screen. The message appears in the bottom-right corner of the screen and does not take up the full width of the screen.][2b]{: style="max-width: 800px; border: none;"}
