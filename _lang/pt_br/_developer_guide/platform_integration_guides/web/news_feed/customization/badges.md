---
nav_title: Ícones
article_title: Emblemas de feed de notícias para a Web
platform: Web
page_order: 3
page_type: reference
description: "Este artigo aborda como solicitar a contagem de cartões de feeds de notícias não lidos e usar essas informações para alimentar emblemas em seu aplicativo da Web."
channel: news feed

---

# Ícones

> Este artigo aborda como solicitar a contagem de cartões de feeds de notícias não lidos e usar essas informações para alimentar emblemas em seu aplicativo da Web.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Solicitação de contagem de cartões não lidos do Feed de notícias

Você pode solicitar o número de cartões não lidos a qualquer momento, ligando para o telefone:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Isso é usado com frequência para fortalecer os emblemas que indicam quantos cartões do Feed de notícias não lidos existem. Consulte os [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) para saber mais. Observe que o Braze não atualizará os cartões do Feed de notícias em novos carregamentos de página (e, portanto, essa função retornará 0) até que você mostre o feed ou chame `braze.requestFeedRefresh();`

