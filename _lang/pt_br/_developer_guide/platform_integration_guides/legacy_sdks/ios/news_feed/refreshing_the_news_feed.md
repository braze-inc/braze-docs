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

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

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

Para saber mais, veja o `Appboy.h` [arquivo de cabeçalho](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Arquivo de Cabeçalho").


