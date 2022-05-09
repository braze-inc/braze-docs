---
nav_title: Custom Styling
article_title: Custom Content Card Styling for iOS
platform: iOS
page_order: 1
description: "This article covers Content Card custom styling options for your iOS application."
channel:
  - content cards
---

# Custom Styling

## Overriding default images

{% alert important %}
Integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images within iOS in-app messages, News Feed, or Content Cards.
{% endalert %}

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app's image bundle. Then, rename the file with the image's name to override the default image in our library. Also, be sure to upload the `@2x` and `@3x` versions of the images to accommodate different phone sizes. Images available for override in Content Cards include:

- Placeholder image: `appboy_cc_noimage_lrg`
- Pinned icon image: `appboy_cc_icon_pinned`

Because Content Cards have a maximum size of 2 KB for content you enter in the dashboard (including message text, image URLs, links, and all key-value pairs), check the size before sending. Exceeding this amount will prevent the card from sending.

{% alert important %}
Overriding default images is currently not supported in our Xamarin iOS integration.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
