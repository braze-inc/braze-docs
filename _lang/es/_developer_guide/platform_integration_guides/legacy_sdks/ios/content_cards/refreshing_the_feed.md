---
nav_title: Actualizar la fuente
article_title: Actualizar la fuente de la tarjeta de contenido para iOS
platform: iOS
page_order: 4
description: "En este artículo de referencia se cubre la implementación de la actualización de tarjetas de contenido en tu aplicación iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Actualizar la fuente

## Actualizar tarjetas de contenido

Puedes solicitar manualmente a Braze que actualice las tarjetas de contenido del usuario utilizando el método `requestContentCardsRefresh:` en la interfaz `Appboy`:
{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

Para más información, consulta el [archivo de encabezado](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
