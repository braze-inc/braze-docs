---
nav_title: Overview
article_title: Content Card Overview for Android and FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android application."
channel:
  - content cards

---

# Customization

Customizing Content Cards and the feed they are located in must be done during the integration process. Before customizing, developers should work with their marketing team to determine what customization approach works best for your brand needs. At Braze, we highlight three approaches to customization based on the associated level of effort and flexibility provided: crawl, walk, or run. Learn more about these [customization approaches][1] in our user guide.

## Key-value pairs

`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data along with a `Card` for further handling by the application.

See our [KDoc][36] for more information.

{% alert note %}
Content Cards have a maximum size limit of 2 KB for content you enter in the Braze dashboard. This includes message text, image URLs, links, and key-value pairs. Exceeding that amount will prevent the card from sending.
{% endalert %}

## Default styling {#default-styling-for-android}

Braze in-app messages and Content Cards come with a default look and feel that matches the Android standard UI guidelines and provide a seamless experience. You can see these default styles in the [`res/values/styles.xml`][42] file in the Braze SDK distribution:

```xml
  <!-- Content Cards Example -->
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_appboy_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_appboy_content_cards_captioned_image_card_title_container</item>
  </style>
```

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
[36]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/get-extras.html
