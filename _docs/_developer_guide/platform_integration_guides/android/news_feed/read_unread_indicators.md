---
nav_title: Read & Unread Indicators
article_title: News Feed Read & Unread Indicators for Android/FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "This reference article covers how to implement read and unread indicators in your News Feed for your Android application."
channel:
  - news feed

---

# Read & unread indicators

Braze allows you to optionally toggle on an Unread/Read indicator on News Feed cards as pictured below:

![UnreadvsRead][25]

## Enabling the indicators

In order to enable this functionality add the following line to your `braze.xml` file:

```xml
<bool name="com_appboy_newsfeed_unread_visual_indicator_on">true</bool>
```

## Customizing the indicators
These indicators can be customized by altering the "icon_read" and "icon_unread" drawables.

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_unread.png
[27]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_read.png
