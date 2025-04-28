---
nav_title: アクセシビリティ
article_title: Android と FireOS のアクセシビリティ
page_order: 4
platform: 
  - Android
  - FireOS
description: "この参考記事では、Android または FireOS アプリケーションへのアプリ内メッセージの読み上げなど、特定の Android SDK アクセシビリティ機能を実装する方法について説明します。"

---

# アクセシビリティ

> この参考記事では、Android または FireOS アプリケーションへのアプリ内メッセージの読み上げなど、特定の Android SDK アクセシビリティ機能を実装する方法について説明します。Braze Android SDK は、[Android アクセシビリティガイドライン](https://developer.android.com/guide/topics/ui/accessibility)に従っています。

## アプリ内メッセージの読み上げ

Android の読み上げ / 「VoiceOver」で、アプリ内メッセージの表示中にその背後にある内容が読み取られないようにするには、以下の SDK 設定を有効にしてください。

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


