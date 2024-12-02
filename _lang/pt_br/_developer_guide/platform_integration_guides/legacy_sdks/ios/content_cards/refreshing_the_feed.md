---
nav_title: Atualizando o feed
article_title: Atualização do feed do cartão de conteúdo para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência aborda a implementação de atualizações de cartões de conteúdo em seu app para iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Atualizar o feed

## Atualizando os cartões de conteúdo

Você pode solicitar manualmente que o Braze atualize os cartões de conteúdo do usuário usando o método `requestContentCardsRefresh:` na interface `Appboy`:
{% tabs %}
{% tab OBJECTIVE C %}

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

Para saber mais, consulte o [arquivo de cabeçalho](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
