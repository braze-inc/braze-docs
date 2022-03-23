---
nav_title: Customizing Feed
article_title: Customizing Content Card Feed for Android and FireOS
page_order: 4.1
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android application."
channel:
  - content cards

---

# Customizing the default Content Card feed {#content-cards-fragment-customization}

This section covers customization of the [ContentCardsFragment][49] whose source can be found [here][54].

## Customizing the network connection error message

If the [`ContentCardsFragment`][49] determines that a Content Card refresh has failed, it will display a network connection error message.

A special adapter, the [`AppboyEmptyContentCardsAdapter`][50] replaces the standard [`AppboyCardAdapter`][53] to display the error message. To set the custom message itself, override the string resource `com_appboy_feed_empty`.

The style used to display this message can be found via [`Appboy.ContentCardsDisplay.Empty`][52] and is reproduced below:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_appboy_feed_empty</item>
  <item name="android:textColor">@color/com_appboy_title</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

[49]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[52]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml#L552-L560
[53]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.contentcards/-appboy-empty-content-cards-adapter/index.html
[54]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.java
To fully customize the network error behavior, you can extend the [`ContentCardsFragment`][54] and set the `mShowNetworkUnavailableRunnable` variable to perform some other action.
