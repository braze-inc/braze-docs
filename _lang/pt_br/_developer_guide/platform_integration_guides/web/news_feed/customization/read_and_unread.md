---
nav_title: Indicadores de leitura e não leitura
article_title: Indicadores de leitura e não leitura de feed de notícias para a Web
platform: Web
page_order: 2
page_type: reference
description: "Este artigo aborda como definir indicadores de leitura e não leitura em seus cartões do Feed de notícias por meio do Braze SDK."
channel: news feed

---

# Indicadores de leitura e não leitura

> Este artigo aborda como definir indicadores de leitura e não leitura em seus cartões do Feed de notícias por meio do Braze SDK.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

O Braze fornece um indicador de não lido e lido nos cartões do Feed de notícias, conforme mostrado na imagem a seguir:

![Um cartão do feed de notícias que mostra a imagem de um relógio junto com algum texto. No canto superior do texto, há um triângulo azul ou cinza que indica se um cartão foi lido ou não. Um triângulo azul significa que um cartão foi lido.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Desativação dos indicadores

Para desativar essa funcionalidade, adicione o seguinte estilo ao seu CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

