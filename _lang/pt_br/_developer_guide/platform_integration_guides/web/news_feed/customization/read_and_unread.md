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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

O Braze fornece um indicador de não lido e lido nos cartões do Feed de notícias, conforme mostrado na imagem a seguir:

![Um cartão do feed de notícias que mostra a imagem de um relógio junto com algum texto. No canto superior do texto, há um triângulo azul ou cinza que indica se um cartão foi lido ou não. Um triângulo azul significa que um cartão foi lido.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Desativação dos indicadores

Para desativar essa funcionalidade, adicione o seguinte estilo ao seu CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

