---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know that rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/icon_modal.png
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/icon_slideup.png
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/icon_full_screen.png
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.


{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}


## Character and Image Limits

There are no true "limits" on the number of characters in in-app messages, though there is a general threshold on the number of lines of text a message can hold before it triggers a scroll function in the message to show any content that has overflowed the content block. The threshold can vary depending on the end user’s device size, custom handling, or presence of images within messages

We recommend at most 3 lines of message/body text, but you should __always__ [test your messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) before sending to prevent the need for the message to scroll.

| Type                               | Aspect Ratio | Recommended Image Size | Max Image Size |   File Types  |
|------------------------------------|:------------:|:----------------------:|:--------------:|:-------------:|
| Portrait Full Screen (With Text)   |      5:4     |          500KB         |       5MB      | PNG, JPG, GIF |
| Portrait Full Screen (Image Only)  |     10:16    |          500KB         |       5MB      | PNG, JPG, GIF |
| Landscape Full Screen (With Text)  |     16:5     |          500KB         |       5MB      | PNG, JPG, GIF |
| Landscape Full Screen (Image Only) |     16:10    |          500KB         |       5MB      | PNG, JPG, GIF |
| Slideup                            |      1:1     |          500KB         |       5MB      | PNG, JPG, GIF |
| Modal (Image Only)                 |      1:1     |          500KB         |       5MB      | PNG, JPG, GIF |
| Modal (With Text)                  |     29:10    |          500KB         |       5MB      | PNG, JPG, GIF |

## Font Awesome

Though Braze supports using [Font Awesome](https://fontawesome.com/) in our in-app messages, we recommend testing your message before sending if you are using Font Awesome.

## Safe Zone

An Image Safe Zone in an in-app message designates the area that is guaranteed to show in your message, no matter the device on which the message is displayed. To prevent your message's media from being cut off, we recommend that you put a safe amount of padding around the bulk of your image. See our [Creative Specs](#creative-specs) below for each message type for more information on these specs.  

A Device Safe Zone in an in-app message designates the area within which your message will show on a device. This safe zone will buffer your message from disappearing behind the borders and the edges of almost any device.

## Font Defaults
If you are using the newest generation of in-app messages (Generation 3), you'll find that the fonts default to the Operating System default Sans Serif for iOS and Android. Web in-app messages will default to Helvetica.

## Gifs & Videos

Braze currently supports gifs for Web (included), [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/gifs/), and iOS (included) in-app messaging, given that it has been enabled during the desired platform integration. For more on video in in-app messages, see our [Customization documentation]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

# Creative Specs

In-app messages aren't just messaging, they're an extension of your app, directly to your customer. We understand that they're a work of art and these things require precision. To ease the guesswork, we've provided maps of our specs for each of our message types ([Modal](#modal), [Slideup](#slideup), [Full-Screen](#full-screen)). Check them out and get messaging!

## Modal

Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

<br>

![Modal Specs][1a]{: style="max-width: 80%;" }

<br>

| Element | Specification | Details |
|---|---|---|
| Modal Size |450px Maximum Width <br> 720px Maximum Height | There is a 720px maximum height, at which point the message scrolls vertically.|
| Image Size | 29:10 Aspect Ratio <br> 450px by 155px Image Container | Accepts high resolution, PNG, JPEG, GIF. |
| Copy | 20px Header Text - Bolded <br> 14px Message Text - Regular Weight | We cannot recommend character or word limits.|
| Primary & Secondary Action Buttons | Secondary on the Left <br> Primary on the Right | We recommend contrasting your buttons to present the desired choice to the user with the right button, designating it as the Primary Action. |
| Screen Overlay | Transparent | This is a customizable, transparent film that lays between your app and the message.
| Device Safe Zone | 15px Margin | This margin is additional padding around the edges of the device. |

### Modal Viewport

On a tablet or desktop browser, a modal in-app message will still sit in the center of the app screen as shown below.

<br>

![Modal Viewport][1b]{: style="max-width: 80%;" }

<br>

## Slideup

Our Slideups typically appear at the top or bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information.

<br>

![Slideup Specs][2a]{: style="max-width: 50%;" }

<br>

| Element | Specification | Details |
|---|---|---|
| Slideup Size | 450px Maximum Width | 3-Line maximum height, at which point the message is truncated with an ellipsis. |
| Image/Icon Size | 50px by 50px | These images are optional, but always appear on the left side of the message. |
| Copy | 14px - Bolded | Three lines of text will appear before being truncated with an ellipsis. |
| Device Safe Zone | 10px Margin | This margin is additional padding around the edges of the device. |

### Slideup Viewport

On a tablet or desktop browser, a slideup in-app message will sit in the corner of the app screen as shown below (unless designated otherwise when creating the in-app message).

<br>
![Slideup Viewport][2b]{: style="max-width: 80%;" }
<br>

## Full-Screen

Full-Screen messages take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

<br>

![Full-Screen Specs][3a]{: style="max-width: 80%;" }

<br>

| Element | Specification | Details |
|---|---|---|
| Text & Image - Image Size | 5:4 Aspect Ratio <br> 450px by 360px Image Container | Accepts high resolution, PNG, JPEG, GIF. |
| Image Only - Image Size | 10:16 Aspect Ratio <br> 450px by 720px Image Container | Accepts high resolution, PNG, JPEG, GIF. |
| Image Safe Zone | 10% Top & Bottom Safe Zone <br> 14% Left & Right Safe Zone | These safe zones act as recommended boundaries. You should keep the most important parts of your image to it's center.
| Copy | 20px Header Text - Bolded <br> 14px Message Text - Regular Weight | We cannot recommend character or word limits.|
| Primary & Secondary Action Buttons | Secondary on the Left <br> Primary on the Right | We recommend contrasting your buttons to present the desired choice to the user with the right button, designating it as the Primary Action. |

### Full-Screen Viewport

On a tablet or desktop browser, a full-screen in-app message will sit in the center of the app screen as shown below.

<br>
![Full-Screen Viewport][3b]{: style="max-width: 80%;" }
<br>

[1a]: {% image_buster /assets/img/modal-spec.png %}
[1b]: {% image_buster /assets/img/modal-large-viewport.png %}
[2a]: {% image_buster /assets/img/slideup-spec.png %}
[2b]: {% image_buster /assets/img/slideup-large-viewport.png %}
[3a]: {% image_buster /assets/img/full-screen-spec.png %}
[3b]: {% image_buster /assets/img/full-screen-large-viewport.png %}
