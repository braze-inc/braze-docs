---
nav_title: Overview
article_title: Content Card Overview for iOS
platform: iOS
page_order: 1
description: "This article covers customization options for your Content Cards in your iOS application."
channel:
  - content cards
---

# Customization

Customizing Content Cards and the feed they are located in must be done during the integration process. Before customizing, developers should work with their marketing team to determine what customization approach works best for your brand needs. At Braze, we highlight three approaches to customization based on the associated level of effort and flexibility provided: crawl, walk, or run. Learn more about these [customization approaches][1] in our user guide.

It's also important to consider whether you should use a subclassing strategy versus a complete view controller customization. For example, if you subclass the `ABKContentCardsTableViewController`, you can use the `populateContentCards` method ([below](#overriding-populated-content-cards)) to filter and order cards (recommended). However, if you use a complete view controller customization, you have more control over the card behavior—such as displaying in a carousel or adding interactive elements—but you then have to rely on an observer to implement ordering and filtering logic. You must also implement the respective analytics methods to ensure impressions, dismissal events, and clicks are properly logged.

## Overriding default images

{% alert important %}
Integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images within iOS in-app messages, News Feed, or Content Cards.
{% endalert %}

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app's image bundle. Then, rename the file with the image's name (see below) to override the default image in our library. Also, be sure to upload the `@2x` and `@3x` versions of the images to accommodate different phone sizes. Images available for override in Content Cards include:

- Placeholder image: `appboy_cc_noimage_lrg`
- Pinned icon image: `appboy_cc_icon_pinned`

Because Content Cards have a maximum size of 2 KB for content you enter in the dashboard (including message text, image URLs, links, and all key-value pairs), check the size before sending. Exceeding this amount will prevent the card from sending.

{% alert important %}
Overriding default images is currently not supported in our Xamarin iOS integration.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
