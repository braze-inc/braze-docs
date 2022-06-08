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

Braze allows you to optionally toggle on unread and read indicators on News Feed cards, as pictured in the following:

![A News Feed card showing an image of a watch along with some text. In the upper corner of the text is a blue or grey triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.][25]

## Enabling the indicators

To enable this functionality add the following line to your `braze.xml` file:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Customizing the indicators

These indicators can be customized by altering the `icon_read` and `icon_unread` drawables.

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
