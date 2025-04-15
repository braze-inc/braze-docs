---
nav_title: Integração
article_title: Integração do cartão de conteúdo para a Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "Este artigo aborda a integração do cartão de conteúdo para a Web, incluindo modelos de dados do cartão de conteúdo, opções de interface do usuário de feed padrão e métodos de cartão adicionais."
search_rank: 1
---

# Integração do cartão de conteúdo

> Este artigo aborda a integração do cartão de conteúdo para a Web, incluindo modelos de dados do cartão de conteúdo, opções de interface do usuário de feed padrão e métodos de cartão adicionais.

{% multi_lang_include archive/web-v4-rename.md %}

O SDK da Braze para web inclui uma interface de usuário de feed de cartões de conteúdo para acelerar seus esforços de integração. Se preferir criar sua própria interface do usuário, consulte o [Guia de personalização do cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards).

## Interface do usuário do feed padrão

Para usar a interface de usuário dos cartões de conteúdo incluídos, você precisará especificar onde mostrar o feed em seu site. 

Neste exemplo, temos um `<div id="feed"></div>` no qual queremos colocar o feed dos cartões de conteúdo. Usaremos três botões para ocultar, mostrar ou alternar (ocultar ou mostrar com base em seu estado atual) o feed.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

Ao usar os métodos `toggleContentCards(parentNode, filterFunction)` e `showContentCards(parentNode, filterFunction)`, se nenhum argumento for fornecido, todos os cartões de conteúdo serão mostrados em uma barra lateral de posição fixa no lado direito da página. Caso contrário, o feed será colocado na opção `parentNode` especificada.

|Parâmetros | Descrição |
|---|---|
|`parentNode` | O nó HTML no qual os cartões de conteúdo serão renderizados. Se o nó pai já tiver uma visualização de cartões de conteúdo da Braze como um descendente direto, os cartões de conteúdo existentes serão substituídos. Por exemplo, você deve passar em `document.querySelector(".my-container")`.|
|`filterFunction` | Uma função de filtro ou classificação para os cartões exibidos nessa visualização. Invocado com o vetor de objetos `Card`, classificado por `{pinned, date}`. Espera-se que retorne um vetor de objetos `Card` ordenados para renderizar para esse usuário. Se omitido, todos os cartões serão exibidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Consulte os documentos de referência do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) para saber mais sobre a alternância do cartão de conteúdo.

## Modelo de dados do cartão de conteúdo {#data-models}

O modelo de dados dos cartões de conteúdo está disponível no SDK para web.

O SDK da Braze para Web oferece três tipos de cartões de conteúdo: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) e [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo herda propriedades comuns de um [cartão](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) de modelo básico e tem as seguintes propriedades adicionais.

Consulte [Análise de registros]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) para obter informações sobre a assinatura de dados do cartão.

### Propriedades do modelo do cartão de conteúdo básico - Cartão

Todos os cartões de conteúdo têm essas propriedades compartilhadas:

|Propriedade|Descrição|
|---|---|
| `expiresAt` | O registro de data e hora UNIX do tempo de expiração do cartão.|
| `extras`| (Opcional) Dados do par chave-valor formatados como um objeto de string com uma string de valor. |
| `id` | (Opcional) O ID do cartão. Isso será informado à Braze com eventos para fins de análise de dados. |
| `pinned` | Essa propriedade reflete se o cartão foi configurado como "fixado" no dashboard.|
| `updated` | O registro de data e hora UNIX de quando esse cartão foi modificado pela última vez. |
| `viewed` | Essa propriedade reflete se o usuário visualizou o cartão ou não.|
| `isControl` | Essa propriedade é `true` quando um cartão é um grupo de "controle" em um teste A/B.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de conteúdo somente para imagens - ImageOnly

Os cartões [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) são imagens clicáveis em tamanho real.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão e serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O registro de data e hora UNIX da hora de criação do cartão na Braze. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição do URL. |
| `url` | O URL que será aberto depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de conteúdo da imagem legendada - CaptionedImage

Os cartões [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) são imagens clicáveis, em tamanho real, com texto descritivo.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão e serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O registro de data e hora UNIX da hora de criação do cartão na Braze. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição do URL. |
| `title` | O texto do título desse cartão. |
| `url` | O URL que será aberto depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de conteúdo clássico - ClassicCard

O modelo [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) pode conter uma imagem sem texto ou um texto com imagem.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão e serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O registro de data e hora UNIX da hora de criação do cartão na Braze. |
| `description` | O texto do corpo deste cartão. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição do URL. |
| `title` | O texto do título desse cartão. |
| `url` | O URL que será aberto depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Grupo de controle 

Se você usar o feed padrão dos cartões de conteúdo, as impressões e os cliques serão automaticamente rastreados.

Se você usar uma integração personalizada para Cartões de conteúdo, precisará [registrar impressões]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/) quando um Cartão de controle tiver sido visto. Nessa iniciativa, lide com os cartões de controle ao registrar impressões em um Teste A/B. Esses cartões estão em branco e, embora não sejam vistos pelos usuários, você ainda deve registrar as impressões para comparar a performance deles com os cartões que não são de controle.

Para determinar se um cartão de conteúdo está no grupo de controle para um teste A/B, verifique a propriedade `card.isControl` (Web SDK v4.5.0+) ou verifique se o cartão é uma instância `ControlCard` (`card instanceof braze.ControlCard`).

## Métodos do cartão

|Método | Descrição |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Registra um evento de impressão para a lista de cartões fornecida. Isso é necessário para usar uma UI personalizada e não a UI da Braze.|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Registra um evento de clique para um determinado cartão. Isso é necessário para usar uma UI personalizada e não a UI da Braze.| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Exibir os cartões de conteúdo do usuário. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Ocultar os cartões de conteúdo do Braze exibidos no momento. | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Exibir os cartões de conteúdo do usuário. | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|Obtenha todos os cartões atualmente disponíveis na última atualização dos cartões de conteúdo.|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Assine as atualizações dos cartões de conteúdo. <br> O retorno de chamada do assinante será chamado sempre que os cartões de conteúdo forem atualizados. | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|Descarte o cartão programaticamente (disponível na versão 2.4.1).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais, consulte a [documentação de referência do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)

{% alert note %}
Que tal ir mais longe? Quando você entender os conceitos básicos dos cartões de conteúdo, consulte o [Guia de personalização de cartões de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards) para começar a personalizá-los.
{% endalert %}
