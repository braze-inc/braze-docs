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

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Os elementos da interface do usuário do Braze vêm com uma aparência padrão que corresponde aos compositores dentro do dashboard do Braze e visa a consistência com outras plataformas móveis do Braze. Os estilos padrão na Braze são definidos em CSS dentro do SDK da Braze. Substituindo estilos selecionados em seu aplicativo, é possível personalizar nosso feed padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e mais.

Por exemplo, a seguir está uma substituição de exemplo que fará com que o feed de notícias apareça com 800 px de largura:

``` css
body .ab-feed {
  width: 800px;
}
```