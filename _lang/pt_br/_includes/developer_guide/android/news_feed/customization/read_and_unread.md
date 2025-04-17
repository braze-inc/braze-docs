# Indicadores de leitura e não leitura

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> O Braze permite que você ative opcionalmente os indicadores de não lido e lido nos cartões do feed de notícias.

![Um cartão do feed de notícias que mostra a imagem de um relógio junto com algum texto. No canto superior do texto, há um triângulo azul ou cinza que indica se um cartão foi lido ou não. Um triângulo azul significa que um cartão foi lido.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Capacitação dos indicadores

Para ativar essa funcionalidade, adicione a seguinte linha ao seu arquivo `braze.xml`:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Personalização dos indicadores

É possível personalizar esses indicadores alterando os drawables `icon_read` e `icon_unread`.

