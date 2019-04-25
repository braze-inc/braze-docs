---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with content cards! But you should know some of the guidelines, first! After all, you have to know that rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Classic
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#classic
  image: /assets/img/icon_modal.png
- name: Captioned Image
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#captioned_image
  image: /assets/img/icon_slideup.png
- name: Banner
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#banner
  image: /assets/img/icon_full_screen.png
---

# Creative Details {#general}

More on customizing Content Cards can be found on our [Customization page][4].

## Character and Image Limits

| Type                               | Aspect Ratio | Recommended Image Size | Max Image Size |   File Types  |
|------------------------------------|:------------:|:----------------------:|:--------------:|:-------------:|
| Portrait Full Screen (With Text)   |      5:4     |          500KB         |       5MB      | PNG, JPG, GIF |
| Portrait Full Screen (Image Only)  |     10:16    |          500KB         |       5MB      | PNG, JPG, GIF |
| Landscape Full Screen (With Text)  |     16:5     |          500KB         |       5MB      | PNG, JPG, GIF |
| Landscape Full Screen (Image Only) |     16:10    |          500KB         |       5MB      | PNG, JPG, GIF |git a
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


[1a]: {% image_buster /assets/img/modal-spec.png %}
[1b]: {% image_buster /assets/img/modal-large-viewport.png %}
[2a]: {% image_buster /assets/img/slideup-spec.png %}
[2b]: {% image_buster /assets/img/slideup-large-viewport.png %}
[3a]: {% image_buster /assets/img/full-screen-spec.png %}
[3b]: {% image_buster /assets/img/full-screen-large-viewport.png %}
[4]: {{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/customize/
