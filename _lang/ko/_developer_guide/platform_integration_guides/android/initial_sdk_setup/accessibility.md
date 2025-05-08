---
nav_title: 접근성
article_title: Android 및 FireOS용 접근성
page_order: 4
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 인앱 메시지 토크백과 같은 특정 Android SDK 접근성 기능을 Android 또는 FireOS 애플리케이션에 구현하는 방법을 다룹니다."

---

# 접근성

> 이 참조 문서에서는 인앱 메시지 토크백과 같은 특정 Android SDK 접근성 기능을 Android 또는 FireOS 애플리케이션에 구현하는 방법을 다룹니다. Braze Android SDK는 [Android 접근성 지침](https://developer.android.com/guide/topics/ui/accessibility)을 따릅니다.

## 인앱 메시지 토크백

Android 토크백/'보이스오버'가 표시되는 중에 인앱 메시지 뒤에 있는 콘텐츠를 읽지 않도록 하려면 다음 SDK 구성을 활성화합니다.

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


