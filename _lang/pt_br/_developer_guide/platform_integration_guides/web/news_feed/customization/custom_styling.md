---
nav_title: Estilo Personalizado
article_title: Estilo personalizado do feed de notícias para a web
platform: Web
page_order: 0
page_type: reference
description: "Este artigo relata as opções de estilo personalizadas para Feeds de Notícias para seu aplicativo web."
channel: news feed

---

# Estilo Personalizado

> Este artigo relata as opções de estilo personalizadas para Feeds de Notícias para seu aplicativo web.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Os elementos da interface do usuário do Braze vêm com uma aparência padrão que corresponde aos compositores dentro do dashboard do Braze e visa a consistência com outras plataformas móveis do Braze. Os estilos padrão na Braze são definidos em CSS dentro do SDK da Braze. Substituindo estilos selecionados em seu aplicativo, é possível personalizar nosso feed padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e mais.

Por exemplo, a seguir está uma substituição de exemplo que fará com que o feed de notícias apareça com 800 px de largura:

``` css
body .ab-feed {
  width: 800px;
}
```