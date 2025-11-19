{% multi_lang_include archive/web-v4-rename.md %}

## Pré-requisitos

Antes de poder usar os cartões de conteúdo, você precisará [integrar o Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) em seu app. No entanto, não é necessária nenhuma configuração adicional. Para criar sua própria interface do usuário, consulte o [Guia de personalização do cartão de conteúdo]({{site.baseurl}}/developer_guide/content_cards/).

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

## Tipos e propriedades do cartão

O modelo de dados dos cartões de conteúdo está disponível no Web SDK e oferece os seguintes tipos de cartões de conteúdo: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) e [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo herda propriedades comuns de um [cartão](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) de modelo básico e tem as seguintes propriedades adicionais.

{% alert tip %}
Para registrar os dados do cartão de conteúdo, consulte [Registro de análises]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Modelo de cartão básico

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

### Somente imagem

Os cartões [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) são imagens clicáveis em tamanho real.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão e serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O carimbo de data/hora UNIX do horário de criação do cartão do Braze. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição do URL. |
| `url` | O URL que será aberto depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem legendada

Os cartões [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) são imagens clicáveis, em tamanho real, com texto descritivo.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão e serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O carimbo de data/hora UNIX do horário de criação do cartão do Braze. |
| `dismissed` | Essa propriedade indica se esse cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão.|
| `linkText` | O texto de exibição do URL. |
| `title` | O texto do título desse cartão. |
| `url` | O URL que será aberto depois que o cartão for clicado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clássico

O modelo [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) pode conter uma imagem sem texto ou um texto com imagem.

|Propriedade|Descrição|
|---|---|
| `aspectRatio` | A proporção da imagem do cartão e serve como uma dica antes da conclusão do carregamento da imagem. Observe que a propriedade pode não ser fornecida em determinadas circunstâncias. |
| `categories` | Essa propriedade serve apenas para organização em sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se esse cartão já foi clicado nesse dispositivo. |
| `created` | O carimbo de data/hora UNIX do horário de criação do cartão do Braze. |
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

Se você usar uma integração personalizada para Cartões de conteúdo, precisará [registrar impressões]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) quando um Cartão de controle tiver sido visto. Nessa iniciativa, lide com os cartões de controle ao registrar impressões em um Teste A/B. Esses cartões estão em branco e, embora não sejam vistos pelos usuários, você ainda deve registrar as impressões para comparar a performance deles com os cartões que não são de controle.

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

## Usando o Google Tag Manager

O Google Tag Manager funciona injetando o [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (uma versão do nosso Web SDK) diretamente no código do seu site, o que significa que todos os métodos do SDK estão disponíveis como se você tivesse integrado o SDK sem o Google Tag Manager, exceto ao implementar cartões de conteúdo.

### Configuração de cartões de conteúdo

{% tabs local %}
{% tab Google Tag Manager %}
Para uma integração padrão do feed do cartão de conteúdo, você pode usar uma tag **HTML personalizada** no Google Tag Manager. Adicione o seguinte em sua tag HTML personalizada, que ativará o feed padrão do cartão de conteúdo:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuração de tag no Google Tag Manager de uma tag HTML personalizada que mostra o feed do cartão de conteúdo.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Para ter mais liberdade na personalização da aparência dos cartões de conteúdo e de seu feed, é possível integrar diretamente os cartões de conteúdo em seu site nativo. Há duas abordagens que você pode adotar: usar a interface de usuário de feed padrão ou criar uma interface de usuário de feed personalizada.

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

Para fazer upgrade para a versão mais recente do SDK da Braze para Web, siga as três etapas a seguir em seu dashboard do Google Tag Manager:

1. **Atualizar modelo de tag**<br>Acesse a página **Modelos** em seu espaço de trabalho. Aqui você verá um ícone indicando que há uma atualização disponível.<br><br>![Página de modelos mostrando que uma atualização está disponível]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Clique nesse ícone e, após revisar a alteração, clique em **Accept Update (Aceitar atualização)**.<br><br>![Uma tela comparando os modelos de tag antigos e novos com um botão para "Aceitar atualização"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Atualizar o número da versão**<br>Depois que seu modelo de tag tiver sido atualizado, edite a tag de inicialização da Braze e atualize a versão do SDK para a versão mais recente `major.minor`. Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Você pode ver uma lista das versões do SDK em nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modelo de inicialização do Braze com um campo de entrada para alterar a versão do SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Controle de qualidade e publicação**<br>Verifique se a nova versão do SDK está funcionando usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager antes de publicar uma atualização no seu contêiner de tags.

### Solução de problemas {#troubleshooting}

#### Ativar a depuração de tag {#debugging}

Cada modelo de tag do Braze tem uma caixa de seleção opcional **de depuração de tag GTM** que pode ser usada para registrar mensagens de depuração no console JavaScript da sua página da Web.

![Ferramenta de debug do Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrar no modo de depuração

Outra maneira de ajudar a depurar sua integração com o Google Tag Manager é usar o recurso de [modo de prévia](https://support.google.com/tagmanager/answer/6107056) do Google.

Isso ajudará a identificar quais valores estão sendo enviados da camada de dados da sua página da Web para cada tag do Braze disparada e também explicará quais tags foram ou não disparadas.

![A página de resumo da tag de inicialização do Braze fornece uma visão geral da tag, incluindo informações sobre quais tags foram disparadas.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Ativar o registro detalhado

Para permitir que o suporte técnico da Braze acesse os registros durante os testes, é possível ativar o registro detalhado na integração com o Google Tag Manager. Esses registros serão exibidos na guia **Console** das ferramentas de desenvolvedor do seu navegador [.](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)

Em sua integração do Google Tag Manager, navegue até a tag de inicialização da Braze e selecione **Ativar registro do SDK para Web**.

![A página de resumo da tag de inicialização do Braze com a opção de ativar o registro do SDK da Web.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
