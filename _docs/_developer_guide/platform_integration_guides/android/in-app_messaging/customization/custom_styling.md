---
nav_title: Custom Styling
article_title: In-App Message Custom Styling for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "This reference article covers custom in-app messaging styling for your Android or FireOS application."
channel:
  - in-app messages

---

# Custom styling

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. You can see these default styles in the Braze SDK's [`styles.xml`][6] file:

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

If you would prefer, you can override these styles to create a look and feel that better suits your app.

To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The whole style must be copied over to your local `styles.xml` file for all attributes to be correctly set. Note that these custom styles are for changes to individual UI elements, not wholesale changes to layouts. Layout-level changes need to be handled with custom views.

## Custom font

Braze allows setting a custom font using the [font family guide][79]. To use it, override the style for message text, headers, and button text and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on your in-app message button text, override the `Braze.InAppMessage.Button` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Aside from the `Braze.InAppMessage.Button` style for button text, the style for message text is `Braze.InAppMessage.Message` and the style for message headers is `Braze.InAppMessage.Header`. If you want to use your custom font family across all possible in-app message text, you can set your font family on the `Braze.InAppMessage` style, which is the parent style for all in-app messages.

{% alert important %}
As with other custom styles, the entire style must be copied over to your local `styles.xml` file for all attributes to be correctly set.
{% endalert %}

## Setting a fixed orientation

To set a fixed orientation for an in-app message, first [set a custom in-app message manager listener][19]. Then, call `setOrientation()` on the `IInAppMessage` object in the `beforeInAppMessageDisplayed()` delegate method:

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

For tablet devices, in-app messages will appear in the user's preferred orientation style regardless of actual screen orientation.

[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-custom-listeners
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[79]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
