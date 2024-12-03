---
nav_title: Acessibilidade
article_title: Acessibilidade para Android e FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "Este artigo de referência explica como implementar recursos específicos de acessibilidade do Android SDK, como o talkback de mensagem no app, no seu aplicativo Android ou FireOS."

---

# Acessibilidade

> Este artigo de referência explica como implementar recursos específicos de acessibilidade do Android SDK, como o talkback de mensagem no app, no seu aplicativo Android ou FireOS. O SDK do Braze Android segue as [diretrizes de acessibilidade do Android](https://developer.android.com/guide/topics/ui/accessibility).

## Talkback de mensagem no app

Para que o Android Talkback/"VoiceOver" não leia o conteúdo por trás de uma mensagem no app durante a exibição, ative a seguinte configuração do SDK:

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


