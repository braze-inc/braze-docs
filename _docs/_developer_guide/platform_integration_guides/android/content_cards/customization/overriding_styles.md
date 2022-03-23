---
nav_title: Overriding Styles
article_title: Overriding Content Card Styles for Android and FireOS
page_order: 2
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android application."
channel:
  - content cards

---

# Overriding styles {#overriding-styles-for-android}

If you would prefer, you can override these styles to create a look and feel that better suits your app. To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The whole style must be copied over to your local `styles.xml` file for all attributes to be correctly set.

## Correct style override {#correct-style-override-for-android}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

## Incorrect style override {#incorrect-style-override-for-android}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
