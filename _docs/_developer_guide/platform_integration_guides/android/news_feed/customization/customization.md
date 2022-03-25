---
nav_title: Custom Styling
article_title: Custom News Feed Styling for Android and FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "This reference article covers how to customize your News Feed in your Android application."
channel:
  - news feed
  
---

# Custom styling 

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. You can see these default styles in the `res/values/style.xml` file in the Braze SDK distribution:

```xml
  <style name="Braze"/>
  <!-- Feed -->
  <style name="Braze.Feed"/>
  <style name="Braze.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16.0dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5.0dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
  ...
  </style>
```

If you would prefer, you can override these styles to create a look and feel that better suits your app. To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The whole style must be copied over to your local `styles.xml` file for all of the attributes to be correctly set.

{% tabs local %}
{% tab Correct style override %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```
{% endtab %}
{% tab Incorrect style override %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## Feed style elements

Below is a description of the themeable Braze UI elements and their names for styling purposes:

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## Setting a custom font

Braze allows setting a custom font using the [font family guide][40]. To use it, override a style for cards and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on all titles for short news cards, override the `Appboy.Cards.ShortNews.Title` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

## Adding a badge

You can request the number of unread cards at any time by calling:

```java
getUnreadCardCount()
```

Refer to our [KDoc][17] for more information.

## Read and unread indicators

Braze allows you to optionally toggle on unread and read indicators on News Feed cards as pictured below:

![A News Feed card showing an image of a watch along with some text. In the upper right corner of the text is a blue or grey triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.][25]

### Enabling the indicators

To enable this functionality add the following line to your `braze.xml` file:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

### Customizing the indicators

These indicators can be customized by altering the `icon_read` and `icon_unread` drawables.

[18]: {% image_buster /assets/img_archive/Image27Theming.png %} "Android Feed"
[19]: {% image_buster /assets/img_archive/Image28Theming.png %} "Android Cards"
[20]: {% image_buster /assets/img_archive/Image29Theming.png %} "Android Empty"
[21]: {% image_buster /assets/img_archive/Image30Theming.png %} "Android Network Error"
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[17]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.events/-feed-updated-event/get-unread-card-count.html
[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_unread.png
[27]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_read.png
