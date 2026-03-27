{% multi_lang_include archive/web-v4-rename.md %}

## Pré-requisitos

Antes de poder usar os Cartões de conteúdo, você precisará [integrar o Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) em seu app. No entanto, não é necessária nenhuma configuração adicional. Para criar sua própria interface do usuário, consulte o [Guia de personalização do cartão de conteúdo]({{site.baseurl}}/developer_guide/content_cards/).

## Interface do usuário do feed padrão

Para usar a interface de usuário dos Cartões de conteúdo incluída, você precisará especificar onde mostrar o feed em seu site. 

Neste exemplo, temos um `<div id="feed"></div>` no qual queremos colocar o feed dos Cartões de conteúdo. Usaremos três botões para ocultar, mostrar ou alternar (ocultar ou mostrar com base no estado atual) o feed.

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

Ao usar os métodos `toggleContentCards(parentNode, filterFunction)` e `showContentCards(parentNode, filterFunction)`, se nenhum argumento for fornecido, todos os Cartões de conteúdo serão mostrados em uma barra lateral de posição fixa no lado direito da página. Caso contrário, o feed será colocado na opção `parentNode` especificada.

|Parâmetros | Descrição |
|---|---|
|`parentNode` | O nó HTML no qual os Cartões de conteúdo serão renderizados. Se o nó pai já tiver uma visualização de Cartões de conteúdo da Braze como descendente direto, os Cartões de conteúdo existentes serão substituídos. Por exemplo, você deve passar `document.querySelector(".my-container")`.|
|`filterFunction` | Uma função de filtro ou classificação para os cartões exibidos nessa visualização. Invocada com o vetor de objetos `Card`, classificado por `{pinned, date}`. Espera-se que retorne um vetor de objetos `Card` ordenados para renderizar para esse usuário. Se omitida, todos os cartões serão exibidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Consulte os documentos de referência do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) para saber mais sobre a alternância do cartão de conteúdo.

## Testando Cartões de conteúdo na web

Você pode testar sua integração de Cartões de conteúdo usando as ferramentas de desenvolvedor do seu navegador.

1. Crie uma campanha de cartão de conteúdo e direcione-a ao seu usuário teste.
2. Faça login no site que possui sua integração do Web SDK.
3. Abra o console do navegador. No Chrome, clique com o botão direito na página, selecione **Inspecionar** e depois selecione a guia **Console**.
4. Execute estes comandos no console:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Tipos e propriedades do cartão

O modelo de dados dos Cartões de conteúdo está disponível no Web SDK e oferece os seguintes tipos de Cartões de conteúdo: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) e [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo herda propriedades comuns de um modelo base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) e tem as seguintes propriedades adicionais.

{% alert tip %}
Para registrar os dados do cartão de conteúdo, consulte [Registro de análise de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Modelo de cartão base

Todos os Cartões de conteúdo têm essas propriedades compartilhadas:

|Propriedade|Descrição|
|---|---|
| `expiresAt` | O registro de data e hora UNIX do tempo de expiração do cartão.|
| `extras`| (Opcional) Dados de par chave-valor formatados como um objeto de string com uma string de valor. |
| `id` | (Opcional) O ID do cartão. Isso será informado à Braze com eventos para fins de análise de dados. |
| `pinned` | Essa propriedade reflete se o cartão foi configurado como "fixado" no dashboard.|
| `updated` | O registro de data e hora UNIX de quando esse cartão foi modificado pela última vez. |
| `viewed` | Essa propriedade reflete se o usuário visualizou o cartão ou não.|
| `isControl` | Essa propriedade é `true` quando um cartão é um grupo de "controle" em um teste A/B.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Somente imagem

Os cartões [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) são imagens clicáveis em tamanho real.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão, que serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O registro de data e hora UNIX do horário de criação do cartão na Braze. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição da URL. |
| `url` | A URL que será aberta depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem legendada

Os cartões [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) são imagens clicáveis em tamanho real com texto descritivo.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão, que serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O registro de data e hora UNIX do horário de criação do cartão na Braze. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição da URL. |
| `title` | O texto do título desse cartão. |
| `url` | A URL que será aberta depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clássico

O modelo [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) pode conter uma imagem sem texto ou um texto com imagem.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão, que serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O registro de data e hora UNIX do horário de criação do cartão na Braze. |
| `description` | O texto do corpo deste cartão. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição da URL. |
| `title` | O texto do título desse cartão. |
| `url` | A URL que será aberta depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Grupo de controle

Se você usar o feed padrão dos Cartões de conteúdo, as impressões e os cliques serão automaticamente rastreados.

Se você usar uma integração personalizada para Cartões de conteúdo, precisará [registrar impressões]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) quando um cartão de controle tiver sido visto. Nessa iniciativa, lide com os cartões de controle ao registrar impressões em um teste A/B. Esses cartões estão em branco e, embora não sejam vistos pelos usuários, você ainda deve registrar as impressões para comparar a performance deles com os cartões que não são de controle.

Para determinar se um cartão de conteúdo está no grupo de controle de um teste A/B, verifique a propriedade `card.isControl` (Web SDK v4.5.0+) ou verifique se o cartão é uma instância `ControlCard` (`card instanceof braze.ControlCard`).

## Métodos do cartão

### Métodos do feed padrão

Use estes métodos ao exibir Cartões de conteúdo usando a interface padrão da Braze:

|Método | Descrição |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Exibe o feed padrão de Cartões de conteúdo. Renderiza os cartões em um elemento HTML `parentNode` fornecido, ou como uma barra lateral de posição fixa no lado direito da página se nenhum elemento for fornecido. Aceita uma `filterFunction` opcional para classificar ou filtrar os cartões antes da exibição. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Oculta o feed padrão de Cartões de conteúdo se ele estiver sendo exibido no momento. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Mostra o feed padrão de Cartões de conteúdo se estiver oculto, ou o oculta se estiver visível. Se você precisar exibir vários feeds de Cartões de conteúdo simultaneamente, use `showContentCards` e `hideContentCards`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Métodos do feed personalizado

Use estes métodos ao criar sua própria interface de Cartões de conteúdo:

|Método | Descrição |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Registra uma função de retorno de chamada que é invocada sempre que os Cartões de conteúdo são atualizados para o usuário atual, como no início da sessão. Use isso como a forma principal de receber dados de cartões para seu feed personalizado. Deve ser chamado antes de `openSession()` para receber atualizações na sessão inicial. |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| Retorna todos os cartões disponíveis no momento a partir da atualização mais recente dos Cartões de conteúdo. Use isso para exibir cartões imediatamente ao carregar a página sem aguardar uma nova solicitação ao servidor, como quando o usuário retorna a uma página durante uma sessão ativa. |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Solicita uma atualização imediata dos Cartões de conteúdo dos servidores da Braze. Por padrão, os cartões são atualizados no início da sessão e quando o feed padrão é reaberto. Use isso para forçar uma atualização em outros momentos, como após uma ação específica do usuário. Esteja ciente dos [limites de taxa]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/#rate-limit). |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Registra eventos de impressão para um vetor de cartões. Chame isso quando os cartões forem renderizados e visíveis para o usuário. Necessário para relatórios precisos de campanha ao usar uma interface personalizada, pois as impressões não são rastreadas automaticamente fora do feed padrão. |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Registra um evento de clique para um único cartão. Chame isso quando um usuário interagir com um cartão em sua interface personalizada. Necessário para relatórios precisos de campanha, pois os cliques não são rastreados automaticamente fora do feed padrão. |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| Processa a URL de um cartão e executa o comportamento ao clicar configurado, incluindo ações da Braze (URLs `brazeActions://`) e navegação de URL padrão. Chame isso no manipulador de clique do seu cartão para garantir que os comportamentos ao clicar configurados no dashboard da Braze sejam executados. |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| Descarta programaticamente um cartão, removendo-o do feed do usuário. Use isso para permitir que os usuários descartem cartões em sua interface personalizada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para mais informações, consulte a [documentação de referência do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Práticas recomendadas

### Chame os métodos na ordem correta

Para feeds personalizados, os Cartões de conteúdo são atualizados apenas no início da sessão se `subscribeToContentCardsUpdates()` for chamado antes de `openSession()`. Chame os métodos da Braze nesta ordem:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Use cartões em cache para manter o conteúdo entre carregamentos de página

Como `subscribeToContentCardsUpdates()` invoca seu retorno de chamada apenas quando há novas atualizações (como no início da sessão), os cartões podem desaparecer do seu feed personalizado se o usuário atualizar a página no meio da sessão. Para evitar isso, use `getCachedContentCards()` para renderizar imediatamente os cartões do cache local, junto com sua inscrição para novas atualizações:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Registre análise de dados para feeds personalizados

Ao usar uma interface personalizada, impressões, cliques e descartes não são rastreados automaticamente. Você deve registrar cada evento manualmente:

- **Impressões:** Chame `logContentCardImpressions([card1, card2, ...])` com um vetor de objetos de cartão quando os cartões se tornarem visíveis para o usuário.
- **Cliques:** Chame `logContentCardClick(card)` quando um usuário interagir com um cartão.
- **Comportamento ao clicar:** Chame `handleBrazeAction(card.url)` para executar o comportamento ao clicar configurado no cartão (como navegar para uma URL ou registrar um evento personalizado).

{% alert warning %}
O argumento passado para `logContentCardClick()` deve ser um objeto `Card` original da Braze. Se você transformar ou reconstruir os dados do cartão (por exemplo, serializando e desserializando), os cliques não serão registrados e você verá o erro: "card must be a Card object."
{% endalert %}

## Usando o Google Tag Manager

O Google Tag Manager funciona injetando o [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (uma versão do nosso Web SDK) diretamente no código do seu site, o que significa que todos os métodos do SDK estão disponíveis como se você tivesse integrado o SDK sem o Google Tag Manager, exceto ao implementar Cartões de conteúdo.

### Configuração de Cartões de conteúdo

{% tabs local %}
{% tab google tag manager %}
Para uma integração padrão do feed do cartão de conteúdo, você pode usar uma tag **HTML personalizada** no Google Tag Manager. Adicione o seguinte à sua tag HTML personalizada, que ativará o feed padrão do cartão de conteúdo:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuração de tag no Google Tag Manager de uma tag HTML personalizada que mostra o feed do Content Card.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Para ter mais liberdade na personalização da aparência dos Cartões de conteúdo e de seu feed, é possível integrar diretamente os Cartões de conteúdo em seu site nativo. Há duas abordagens que você pode adotar: usar a interface de usuário de feed padrão ou criar uma interface de usuário de feed personalizada.

{% subtabs local %}
{% subtab standard feed %}
Ao implementar a [UI de feed padrão]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), os métodos da Braze devem ter `window.` adicionado ao início do método. Por exemplo, `braze.showContentCards` deve ser `window.braze.showContentCards`.
{% endsubtab %}

{% subtab custom feed %}
Para o estilo de [feed personalizado]({{site.baseurl}}/developer_guide/content_cards/creating_cards/), as etapas são as mesmas que se você tivesse integrado o SDK sem o GTM. Por exemplo, se quiser personalizar a largura do feed do cartão de conteúdo, você pode colar o seguinte em seu arquivo CSS:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Fazendo upgrade de modelos {#upgrading}

Para fazer upgrade para a versão mais recente do Braze Web SDK, siga as três etapas a seguir no seu dashboard do Google Tag Manager:

1. **Atualizar modelo de tag**<br>Acesse a página **Modelos** em seu espaço de trabalho. Aqui você verá um ícone indicando que há uma atualização disponível.<br><br>![Página de modelos mostrando que uma atualização está disponível]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Clique nesse ícone e, após revisar a alteração, clique em **Accept Update (Aceitar atualização)**.<br><br>![Uma tela comparando os modelos de tag antigos e novos com um botão para "Aceitar atualização"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Atualizar o número da versão**<br>Depois que seu modelo de tag tiver sido atualizado, edite a tag de inicialização da Braze e atualize a versão do SDK para a versão mais recente `major.minor`. Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Você pode ver uma lista das versões do SDK em nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modelo de inicialização da Braze com um campo de entrada para alterar a versão do SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Controle de qualidade e publicação**<br>Verifique se a nova versão do SDK está funcionando usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager antes de publicar uma atualização no seu contêiner de tags.

### Solução de problemas {#troubleshooting}

#### Ativar a depuração de tag {#debugging}

Cada modelo de tag da Braze tem uma caixa de seleção opcional **de depuração de tag GTM** que pode ser usada para registrar mensagens de depuração no console JavaScript da sua página da web.

![Ferramenta de debug do Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrar no modo de depuração

Outra maneira de ajudar a depurar sua integração com o Google Tag Manager é usar o recurso de [modo de prévia](https://support.google.com/tagmanager/answer/6107056) do Google.

Isso ajudará a identificar quais valores estão sendo enviados da camada de dados da sua página da web para cada tag da Braze disparada e também explicará quais tags foram ou não disparadas.

![A página de resumo da tag de inicialização da Braze fornece uma visão geral da tag, incluindo informações sobre quais tags foram disparadas.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Verificar o sequenciamento de tags para eventos personalizados {#tag-sequencing}

Se eventos personalizados ou outras ações não estiverem sendo registrados na Braze, uma causa comum é uma condição de corrida em que uma tag de ação (como **Evento personalizado** ou **Compra**) é disparada antes que a tag de **Inicialização da Braze** tenha sido concluída. Para corrigir isso, configure o [sequenciamento de tags](https://support.google.com/tagmanager/answer/6238868) no GTM:

1. Abra a tag de ação que não está registrando corretamente.
2. Em **Configurações avançadas** > **Sequenciamento de tags**, selecione **Uma tag que é disparada antes de \[esta tag\]**.
3. Escolha sua tag de **Inicialização da Braze** como a tag de configuração.

Isso garante que o SDK esteja totalmente inicializado antes que qualquer tag de ação tente enviar dados para a Braze.

#### Ativar o registro detalhado

Para capturar registros detalhados para solução de problemas, você pode ativar o registro detalhado na sua integração com o Google Tag Manager. Esses registros serão exibidos na guia **Console** das [ferramentas de desenvolvedor](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) do seu navegador.

Em sua integração do Google Tag Manager, navegue até a tag de inicialização da Braze e selecione **Ativar registro do Web SDK**.

![A página de resumo da tag de inicialização da Braze com a opção de ativar o registro do Web SDK.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md