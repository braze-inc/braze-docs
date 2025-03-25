---
nav_title: Actualizar la fuente
article_title: Actualizar la fuente de noticias para iOS
platform: iOS
page_order: 6
description: "Este artículo de referencia muestra cómo actualizar la fuente de noticias en tu aplicación iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Actualizar el canal de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Puedes solicitar manualmente a Braze que actualice la fuente de noticias del usuario en `Appboy.h` utilizando `- (void) requestFeedRefresh;`. Por ejemplo:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestFeedRefresh()
```

{% endtab %}
{% endtabs %}

Para más información, consulta el `Appboy.h` [archivo de cabecera](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Archivo de cabecera").


