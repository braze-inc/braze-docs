---
nav_title: Read & Unread Indicators
article_title: News Feed Read & Unread Indicators for Android and FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "This reference article covers how to implement read and unread indicators in your News Feed for your Android application."
channel:
  - news feed

---

# Read and unread indicators

Braze allows you to optionally toggle on unread and read indicators on News Feed cards as pictured below:

![A News Feed card showing an image of a watch along with some text. In the upper right corner of the text is a blue or grey triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.][25]

## Enabling the indicators

To enable this functionality add the following line to your `braze.xml` file:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Customizing the indicators

These indicators can be customized by altering the `icon_read` and `icon_unread` drawables.

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_unread.png
[27]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_read.png
