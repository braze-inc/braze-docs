---
nav_title: Read & Unread Indicators
article_title: News Feed Read & Unread Indicators for Android and FireOS
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "This reference article covers News Feed read and unread indicators in your Android or FireOS application."
channel:
  - news feed
  
---

# Read and unread indicators

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

> Braze allows you to optionally toggle on unread and read indicators on News Feed cards.

![A News Feed card showing an image of a watch along with some text. In the upper corner of the text is a blue or gray triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Enabling the indicators

To enable this functionality add the following line to your `braze.xml` file:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Customizing the indicators

These indicators can be customized by altering the `icon_read` and `icon_unread` drawables.

