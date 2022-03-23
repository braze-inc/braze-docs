---
nav_title: Fixed Orientation
article_title: Fixed In-App Message Orientation for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "This reference article covers in-app messaging customization options for your Android application."
channel:
  - in-app messages

---

# Setting fixed orientation

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
