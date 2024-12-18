---
nav_title: Feed de notícias
article_title: Feed de notícias para tvOS
platform: tvOS
page_order: 10
page_type: reference
description: "Esta página descreve como buscar e exibir dados do feed de notícias em seu aplicativo tvOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração do Feed de notícias

> Este artigo aborda como configurar um feed de notícias para a plataforma tvOS.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Integração do feed do tvOS

Nosso SDK para tvOS é compatível com a obtenção de dados do seu feed de notícias, de modo que você possa exibir o feed de notícias em seu aplicativo com sua própria interface de usuário personalizada. Para buscar o feed de notícias, chame os seguintes métodos e, em seguida, analise cada cartão inspecionando sua classe.

{% tabs %}
{% tab OBJECTIVE C %}

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
