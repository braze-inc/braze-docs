# Enabling Android Talkback for in-app messages

> Learn how to enable Android Talkback for in-app messages, so you can offer your users a VoiceOver accessibility option. The Braze Android SDK follows the [Android accessibility guidelines](https://developer.android.com/guide/topics/ui/accessibility).

## Enabling Talkback

To ensure Android Talkback does not read the contents behind an in-app message during display, enable the following:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}
