---
nav_title: Font Customization
article_title: Font Customization for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "This reference article covers font customization options such as defining a font family and shows how to reference it throughout your Android or FireOS application."

---

# Font customization

Fonts in the Braze SDK can be set via XML using the AndroidX libraries according to [Font in XML][1]. To use your custom font with the Braze SDK, you'll first need to create a font family.

## Create a font family

The following is an example custom font family definition using the [font family guide][2]. For this example, we use the [Bungee Shade font][3].

```XML
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      to ensure your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

After storing the font family definition in `/res/font/bungee_font_family.xml`, we can refer to it in XML as `@font/bungee_font_family`.

## Referencing your font family

Now that the font family is created, you can override Braze style defaults in your `styles.xml` to include references to the font family.

For example, the following styles override would use the `bungee` font family for all Braze in-app messages and a different font family for all Braze News Feed cards.

```
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
Both `android:fontFamily` and `fontFamily` style attributes must be set to maintain compatibility across all SDK versions.
{% endalert %}

[1]: https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html
[2]: https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family
[3]: https://fonts.google.com/specimen/Bungee+Shade
