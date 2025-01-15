---
nav_title: Atualizando o feed
article_title: Atualizando o feed de notícias para iOS
platform: iOS
page_order: 6
description: "Este artigo de referência mostra como atualizar o feed de notícias em seu aplicativo iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Atualizando o feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Você pode solicitar manualmente que a Braze atualize o feed de notícias do usuário em `Appboy.h` usando `- (void) requestFeedRefresh;`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

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

Para saber mais, veja o arquivo de cabeçalho `Appboy.h` [](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Arquivo de Cabeçalho").


