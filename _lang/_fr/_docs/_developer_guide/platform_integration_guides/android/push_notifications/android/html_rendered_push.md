---
nav_title: Notifications Push HTML
article_title: Notifications Push HTML pour Android
platform: Android
page_order: 6
description: "Cet article couvre hwo pour implémenter les notifications HTML push dans votre application Android."
channel:
  - Pousser
---

# Notifications push HTML

Dans Braze SDK version 3.1.1, le HTML peut être envoyé à un appareil pour afficher du texte multicouleur dans les notifications push.

!\[Exemple de poussée multicouleur\]\[1\]{: style="max-width:30%;"}

L'exemple ci-dessus est rendu avec le HTML suivant :

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

> Android OS limite quels éléments/tags HTML sont valides dans les notifications push. Par exemple, `marquee` n'est pas autorisée.

## Implémentation

Dans votre `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">vrai</bool>
```

Ou dans votre [BrazeConfig][2]:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(ceci, brazeConfig)
```

{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img/multicolor_android_push.png %}

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
