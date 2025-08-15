---
nav_title: Barrierefreiheit
article_title: Barrierefreiheit für Android und FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel beschreibt, wie Sie bestimmte Features des Android SDK für die Barrierefreiheit, z. B. Talkback für In-App-Nachrichten, in Ihre Android oder FireOS Anwendung implementieren."

---

# Barrierefreiheit

> Dieser Referenzartikel beschreibt, wie Sie bestimmte Features des Android SDK für die Barrierefreiheit, z. B. Talkback für In-App-Nachrichten, in Ihre Android oder FireOS Anwendung implementieren. Das Braze Android SDK entspricht den [Android-Richtlinien für Barrierefreiheit](https://developer.android.com/guide/topics/ui/accessibility).

## Talkback für In-App-Nachrichten

Damit Android Talkback/"VoiceOver" den Inhalt einer In-App-Nachricht während der Anzeige nicht mitliest, aktivieren Sie die folgende SDK-Konfiguration:

{% tabs %}
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


