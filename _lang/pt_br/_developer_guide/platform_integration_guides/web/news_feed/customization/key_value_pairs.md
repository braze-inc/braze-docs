---
nav_title: Pares Chave-Valor
article_title: Feed de notícias Pares chave-valor para a web
platform: Web
page_order: 1
page_type: reference
description: "Este artigo aborda como usar pares chave-valor em seus cartões de feeds de notícia por meio do SDK da Braze."
channel: news feed

---

# Pares chave-valor

> Este artigo aborda como usar pares chave-valor em seus cartões de feeds de notícia por meio do SDK da Braze.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Objetos `Card` podem carregar pares chave-valor como `extras`. Estes podem ser usados para enviar dados junto com um cartão para processamento adicional pelo aplicativo. Ligue `card.extras` para acessar esses valores.

Consulte o JSDocs para saber mais sobre [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) e [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html).

