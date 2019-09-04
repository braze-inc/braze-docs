---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/icon_modal.png
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/icon_slideup.png
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/icon_full_screen.png
---

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.


{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}


## Character and Copy Limits

While there are no _hard limits_ on the number of characters in in-app message bodies or headers, we recommend you keep it short and sweet - one to two lines for headers; up to three for bodies. After three lines, users might need to scroll through the content to read it all. The threshold that triggers the scroll can vary depending on the end user’s device size, custom handling, or presence of images within messages, but three lines is usually safe!

__Always__ [preview and test your messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) before sending.


## Image Limits

We do have some limits to images in in-app messages:

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend that your images be 500KB.

### Device Variation
Each message type is designed to adapt to device sizes and shapes, so you may occasionally see a few pixels cropped on the side or a slideup message with more copy than image. You should __always__ [preview and test your messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) on a variety of devices to ensure that the most important areas of your image and message appear as expected.

| Message Type | Recommended Aspect Ratio | Behavior |
|--- | --- | --- |
| Full Screen (with Text) | 5:4 | Image will fill the entire height of a device, including the open space and status bars on "notched" devices, and will stay true to aspect ratio. |
| Full Screen (Image Only) | 10:16 | Image will fill the entire height of a device, including the open space and status bars on "notched" devices, and will crop horizontally (left and right sides) as needed. |
| Slideup | 1:1 | Can contain up to three lines of copy before truncation with ellipses. Images will never be cropped or clipped - they will always scale down to fit within the 50X50 image container. |
| Modal (Image Only) | Any | Will adapt to fit the image to be as large as possible on any device. |
| Modal (with Text) | Any | A modal's image container will adapt to fit the image to be as large as possible on any device. |


#### Safe Zone

An Image Safe Zone in an in-app message designates the area that is guaranteed to show in your message, no matter the device on which the message is displayed. To prevent your message's media from being cut off, we recommend that you put a safe amount of padding around the bulk of your image.  

A Device Safe Zone in an in-app message designates the area within which your message will show on a device. This safe zone will buffer your message from disappearing behind the borders and the edges of almost any device.

__Image Safe Zone Dimensions__

|Message Type | Dimensions |
|---|---|
| Full-Screen | 10% Margin around the top and bottom of the device. <br> 14% Margin around the left and right sides of the device. |
| Modal | 15px Margin around the edges of the device. |
| Slideup | 10px Margin around the edges of the device. |

## Font Defaults
If you are using the newest generation of in-app messages (Generation 3), you'll find that the fonts default to the Operating System default Sans Serif for iOS and Android. Web in-app messages will default to Helvetica.

## Gifs & Videos

Braze currently supports gifs for Web (included), [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/gifs/), and iOS (included) in-app messaging, given that it has been enabled during the desired platform integration. For more on video in in-app messages, see our [Customization documentation]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#video).
