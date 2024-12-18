---
nav_title: Indicadores de Leitura e Não Lida
article_title: Indicadores de leitura e não leitura do feed de notícias para Android e FireOS
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda os indicadores de leitura e não leitura do feed de notícias em seu aplicativo para Android ou FireOS."
channel:
  - news feed
  
---

# Indicadores de leitura e não lidos

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

> O Braze permite que você ative opcionalmente os indicadores de não lido e lido nos cartões do feed de notícias.

![Um cartão do feed de notícias que mostra a imagem de um relógio junto com algum texto. No canto superior do texto, há um triângulo azul ou cinza que indica se um cartão foi lido ou não. Um triângulo azul significa que um cartão foi lido.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Capacitação dos indicadores

Para ativar essa funcionalidade, adicione a seguinte linha ao seu arquivo `braze.xml`:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Personalização dos indicadores

É possível personalizar esses indicadores alterando os drawables `icon_read` e `icon_unread`.

