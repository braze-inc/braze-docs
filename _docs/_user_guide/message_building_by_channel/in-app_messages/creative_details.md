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

There are no true "limits" on the number of characters in in-app messages, though there is a general threshold on the number of lines of text a message can hold before it triggers a scroll function in the message to show any content that has overflowed the content block. The threshold can vary depending on the end user’s device size, custom handling, or presence of images within messages

### Application to Your Message Content

We recommend at most 3 lines of message/body text, but you should __always__ [test your messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) before sending to prevent the need for the message to scroll.


### Font Awesome

Though Braze supports using [Font Awesome](https://fontawesome.com/) in our in-app messages, we recommend testing your message before sending if you are using Font Awesome.

## Image Limits

We do have some limits to images in in-app messages:

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend that your images be 500KB.

### Adaptation to Device
Each message type is designed to adapt to a device in a certain way and, despite our attempts to recommend aspect ratios that work for every device, you may occasionally see a few pixels cropped on the side or a slideup message with more copy than image. We've outlined some expectations below so you can understand what could happen when content doesn't fit recommended ratios or if a device doesn't adhere to those ratios.

- Full-screen in-app messages are designed to fill the entire height of a device.
- Slideup messages are designed to contain at least three lines of copy as well as a 50X50 image, whichever criteria hits the max first.
- Modals are designed to fit to the largest ratio possible, first respecting the device, then the image.

| Message Type                       | Recommended Aspect Ratio | Deviant Behavior <br> _When your content is over or under the recommended ratios._ |
|------------------------------------|:------------------------:|:--------------------------------------:|
| Portrait Full Screen (with Text)   |      5:4                 | __Image:__ You may see cropping off the sides of your image. Notched devices may crop top of image. <br> __Text:__ |
| Portrait Full Screen (Image Only)  |     10:16                |  |
| Landscape Full Screen (with Text)  |     16:5                 |  |
| Landscape Full Screen (Image Only) |     16:10                |  |
| Slideup                            |      1:1                 |   |
| Modal (Image Only)                 |      1:1                 |   |
| Modal (with Text)                  |     29:10                |  |

### Notch Support

Notched mobile devices, where parts of the screen are blocked to hold camera or speaker ports, often distort the look and expansion of in-app messages. This can result in odd overlays or distortion from status bars situated on either side of the notch.

In August 2019, Braze introduced improved support for notched devices. With this new behavior, our in-app messages will consider notches when expanding and filling a device. Where some fullscreen in-app messages will stop at the bottom limit of the notch and allow view of the status bar, our fullscreen messages will fill the notched negative spaces, including the status bar, and provide a fully immersive experience in your message. 

#### Safe Zone

{% alert update %}
In August 2019, Braze introduced adaptive Notch Support for mobile devices. This renders the idea of a specific "image safe zone". Instead, consider designing your message content with Notch Support (above) in mind.
{% endalert %}

{% details Previous Behavior %}

An Image Safe Zone in an in-app message designates the area that is guaranteed to show in your message, no matter the device on which the message is displayed. To prevent your message's media from being cut off, we recommend that you put a safe amount of padding around the bulk of your image.  

A Device Safe Zone in an in-app message designates the area within which your message will show on a device. This safe zone will buffer your message from disappearing behind the borders and the edges of almost any device.

__Image Safe Zone Dimensions (Deprecated August 2019)__
|Message Type | Dimensions |
|---|---|
| Full-Screen | 10% Top & Bottom Safe Zone <br> 14% Left & Right Safe Zone |
| Modal | 15px Margin around the edges of the device. |
| Slideup | 10px Margin around the edges of the device. |

{% enddetails %}

<br>

## Font Defaults
If you are using the newest generation of in-app messages (Generation 3), you'll find that the fonts default to the Operating System default Sans Serif for iOS and Android. Web in-app messages will default to Helvetica.

## Gifs & Videos

Braze currently supports gifs for Web (included), [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/gifs/), and iOS (included) in-app messaging, given that it has been enabled during the desired platform integration. For more on video in in-app messages, see our [Customization documentation]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#video).
