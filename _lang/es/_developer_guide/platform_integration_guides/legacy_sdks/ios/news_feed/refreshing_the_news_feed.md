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

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

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

Para más información, consulta el [archivo de cabecera `Appboy.h` [](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Archivo de cabecera").


