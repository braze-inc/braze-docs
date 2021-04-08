---
nav_title: Android SDK Accessibility
page_order: 4

platform: Android
---

# Accessibility

The Braze Android SDK follows the [Android Accessibility Guidelines][1].

## In-App Message Talkback

In order to have Android Talkback/"VoiceOver" not read the contents behind an in-app message during display, enable the following SDK configuration:

{% tabs %}
{% tab braze.xml %}

```xml
<bool name="com_appboy_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val appboyConfigBuilder = AppboyConfig.Builder()
appboyConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Appboy.configure(this, appboyConfigBuilder.build())
```

{% endtab %}
{% tab JAVA %}

```java
AppboyConfig.Builder appboyConfigBuilder = new AppboyConfig.Builder()
appboyConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Appboy.configure(this, appboyConfigBuilder.build());
```

{% endtab %}
{% endtabs %}


[1]: https://developer.android.com/guide/topics/ui/accessibility
