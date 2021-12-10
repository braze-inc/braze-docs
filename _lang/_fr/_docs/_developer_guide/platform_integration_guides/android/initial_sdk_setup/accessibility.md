---
nav_title: Accessibilité
article_title: Accessibilité pour Android/FireOS
page_order: 4
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la façon d'implémenter des fonctionnalités spécifiques d'accessibilité de SDK Android telles que les messages dans l'application Talkback dans votre application Android."
---

# Accessibilité

Le SDK Android Braze suit les [directives d'accessibilité Android][1].

## Discussion de message dans l'application

Pour que Android Talkback/"VoiceOver" ne lise pas le contenu derrière un message dans l'application pendant l'écran, activez la configuration SDK suivante :

{% tabs %}
{% tab braze.xml %}

```xml
<bool name="com_appboy_device_in_app_message_accessibility_exclusive_mode_enabled">vrai</bool>
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

{% endtab %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

{% endtab %}
{% endtabs %}


[1]: https://developer.android.com/guide/topics/ui/accessibility
