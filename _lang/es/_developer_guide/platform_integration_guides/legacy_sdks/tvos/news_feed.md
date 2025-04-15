---
nav_title: Canal de noticias
article_title: Fuente de noticias para tvOS
platform: tvOS
page_order: 10
page_type: reference
description: "Esta página describe cómo obtener y mostrar datos de fuentes de noticias en tu aplicación tvOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de la fuente de noticias

> Este artículo explica cómo configurar una fuente de noticias para la plataforma tvOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Integración de la fuente de tvOS

Nuestro SDK para tvOS permite obtener los datos de tu fuente de noticias, de forma que puedas mostrar la fuente de noticias en tu aplicación con tu propia interfaz personalizada. Para obtener el canal de noticias, llama a los siguientes métodos y, a continuación, analiza cada tarjeta inspeccionando su clase.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
NSArray *feedCards =  [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab swift %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}
