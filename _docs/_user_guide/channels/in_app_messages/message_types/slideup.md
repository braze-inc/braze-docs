---
nav_title: Slideup
article_title: Slideup In-app Messages
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "This reference article covers the message and design requirements of slideup in-app messages."

---

# Slideup in-app messages

> Our slideups typically appear at the top or bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information. These are non-obtrusive and allow your users to continue to interact with your app while the message displays.

![Two slide-up in-app messages, one appearing from the top of the screen and the other from the bottom, detailing the image and text recommendations. See following sections for details.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Image and copy behavior

Slideup messages can contain up to three lines of copy before truncation with ellipses. Images in slideups will never be cropped or clipped—they will always scale down to fit within the 50 x 50 pixel image container.

- All images must be less than 5&nbsp;MB.
- We only accept PNG, JPEG, and GIF file types.
- We recommend that your images be 500&nbsp;KB.

{% alert tip %} Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 1:1 aspect ratio<br>High-res 150 x 150&nbsp;px<br> Minimum 50 x 50&nbsp;px | Images of various aspect ratios will fit into a square image container, without cropping. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

You should always [preview and test your messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) on a variety of devices to ensure that the most important areas of your image and message appear as expected. Note that when previewing your message on the composer, the actual rendering on devices may differ.

## Mobile devices

On mobile devices, slideups appear at the top or bottom of the app screen. You can specify this when you create your message. Users can swipe to dismiss the slideup, or tap to open it if a click action is included. If a click action is added to the slideup, a chevron ">" is shown.

## Larger screens

{% tabs %}
{% tab Desktop %}

On a desktop browser, a slideup in-app message will sit in the corner of the screen as shown in the following screenshot (unless designated otherwise when creating the in-app message). Users can click the close "X" button to dismiss the slideup.

![Slideup in-app message as it appears on a desktop browser. The message appears in the bottom-right corner of the screen and does not take up the full width of the screen.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

On a tablet, a slideup in-app message appears on the bottom of the screen. Similar to on mobile devices, users can swipe to dismiss the slideup, or tap to open it if a click action is included. If a click action is added to the slideup, a chevron ">" is shown. A close "X" button is not shown by default.

![Slideup in-app message as it appears on a tablet screen. The message appears in the bottom-middle of the screen and does not take up the full width of the screen.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}

