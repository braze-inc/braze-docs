---
nav_title: Accesibilidad
article_title: Accesibilidad para Android y FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "En este artículo de referencia se explica cómo implementar características específicas de accesibilidad del SDK de Android, como la devolución de mensajes dentro de la aplicación, en tu aplicación Android o FireOS."

---

# Accesibilidad

> En este artículo de referencia se explica cómo implementar características específicas de accesibilidad del SDK de Android, como la devolución de mensajes dentro de la aplicación, en tu aplicación Android o FireOS. El SDK para Android de Braze sigue las [directrices de accesibilidad de Android](https://developer.android.com/guide/topics/ui/accessibility).

## Retransmisión de mensajes dentro de la aplicación

Para que Android Talkback/"VoiceOver" no lea el contenido detrás de un mensaje dentro de la aplicación durante la visualización, habilita la siguiente configuración del SDK:

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


