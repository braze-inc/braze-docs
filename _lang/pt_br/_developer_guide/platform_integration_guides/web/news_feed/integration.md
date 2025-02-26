---
nav_title: Integração
article_title: Integração do feed de notícias para a Web
platform: Web
page_order: 0
page_type: reference
description: "Este artigo aborda o tipo de cartão de feed de notícias e como integrá-lo ao seu app web por meio do SDK da Braze."
channel: news feed

---

# Integração do Feed de notícias

> Este artigo aborda como configurar o feed de notícias para o Braze Web SDK.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

O News Feed é um feed de conteúdo no aplicativo totalmente personalizável para seus usuários. Nosso direcionamento e segmentação permitem que você crie um fluxo de conteúdo que atenda individualmente aos interesses de cada usuário. Dependendo da posição no ciclo de vida do usuário e da natureza do seu aplicativo, pode ser um servidor de conteúdo de integração, um centro de anúncios, um centro de conquistas ou um centro de notícias genérico.

## Exemplo de feed de notícias

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="Um exemplo de feed de notícias exibindo várias notificações, como solicitação para seguir, avisos de atualização, anúncios e muito mais." height="600" />

## Integração

Para alternar a exibição do feed de notícias pelo Braze Web SDK, basta chamar:

``` javascript
braze.toggleFeed();
```

Isso exibirá os cartões do Feed de notícias mais recentes armazenados em cache (iniciando uma atualização se esses cartões estiverem desatualizados há mais de 1 minuto ou se o Feed de notícias nunca tiver sido atualizado) e atualizará automaticamente a exibição quando novos cartões forem recebidos dos servidores do Braze, enquanto estiver na tela.

Por padrão, o feed será exibido em uma barra lateral de posição fixa no lado direito do site (ou como uma sobreposição de tela cheia em dispositivos móveis, por meio de CSS responsivo). Se você quiser substituir esse comportamento e exibir um Feed de notícias posicionado estaticamente dentro de seu próprio elemento pai, forneça o seguinte elemento como primeiro argumento para `showFeed`:

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

Se desejar exibir um conjunto estático específico de cartões do Feed de notícias, filtrar os cartões do servidor ou fornecer sua própria semântica de atualização, você poderá desativar a atualização automática e fornecer seus próprios cartões:

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

Consulte o [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed) para obter a documentação completa sobre `showFeed`, `destroyFeed` e `toggleFeed`.

## Tipos de cartão

O Braze Web SDK oferece suporte a três tipos exclusivos de cartões de feed de notícias, [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) e [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), que compartilham um modelo básico, [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html).

### Solicitação de contagem de cartões não lidos

Você pode solicitar o número de cartões não lidos a qualquer momento, ligando para o telefone:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Isso é usado com frequência para fortalecer os emblemas que indicam quantos cartões do Feed de notícias não lidos existem. Consulte os [documentos de referência do JS](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) para obter mais informações. Observe que o Braze não atualizará os cartões do Feed de notícias em novos carregamentos de página (e, portanto, essa função retornará 0) até que você mostre o feed ou chame `braze.requestFeedRefresh();`

### Pares chave-valor

Objetos `Card` podem carregar pares chave-valor como `extras`. Eles podem ser usados para enviar dados para baixo junto com um cartão para tratamento posterior pelo aplicativo. Basta chamar `card.extras` para acessar esses valores.

## Personalização

Os elementos da interface do usuário do Braze vêm com uma aparência padrão que corresponde aos compositores no painel do Braze e visa à consistência com outras plataformas móveis do Braze. Os estilos padrão na Braze são definidos em CSS dentro do SDK da Braze. Substituindo estilos selecionados em seu aplicativo, é possível personalizar nosso feed padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e mais.

Por exemplo, a seguir está uma substituição de exemplo que fará com que o feed de notícias apareça com 800 px de largura:

``` css
body .ab-feed {
  width: 800px;
}
```

## Categorias

As instâncias do feed de notícias da Braze podem ser configuradas para receber apenas cartões de uma determinada "categoria". Isso permite a integração eficaz de vários fluxos do Feed de notícias em um único aplicativo.

Categorias de feed de notícias podem ser definidas fornecendo o terceiro parâmetro `allowedCategories` para `toggleFeed`:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Você também pode preencher um feed com uma combinação de categorias, como no exemplo a seguir:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## Indicadores de leitura e não leitura

O Braze fornece um indicador de não lido e lido nos cartões do Feed de notícias, conforme a figura abaixo:

![Um cartão do feed de notícias que mostra a imagem de um relógio junto com algum texto. No canto superior direito do texto, há um triângulo azul ou cinza que indica se uma carta foi lida ou não. Um triângulo azul significa que um cartão foi lido.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

### Desativação dos indicadores

Para desativar essa funcionalidade, adicione o seguinte estilo ao seu CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

