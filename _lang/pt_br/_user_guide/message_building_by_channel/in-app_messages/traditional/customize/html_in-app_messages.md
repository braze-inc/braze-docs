---
nav_title: Mensagens HTML no aplicativo
article_title: Mensagens HTML personalizadas no aplicativo
page_order: 0
page_type: reference
description: "Este artigo fornece uma visão geral das mensagens in-app de código personalizado, incluindo métodos JavaScript, rastreamento de botões e uso da visualização HTML interativa no Braze."
channel:
  - in-app messages
---

# Mensagens HTML personalizadas no aplicativo {#custom-html-messages}

> Embora nossas mensagens padrão no aplicativo possam ser personalizadas de várias maneiras, você pode ter um controle ainda maior sobre a aparência de suas campanhas usando mensagens projetadas e criadas com HTML, CSS e JavaScript. Com algumas composições simples, você pode desbloquear a funcionalidade e a marca personalizadas para atender a qualquer uma de suas necessidades. 

As mensagens in-app em HTML permitem maior controle sobre a aparência de uma mensagem, incluindo o seguinte:

- Fontes e estilos personalizados
- Vídeos
- Várias imagens
- Comportamentos no clique
- Componentes interativos
- Animações personalizadas

As mensagens HTML personalizadas podem usar os métodos [do JavaScript Bridge](#javascript-bridge) para registrar eventos, definir atributos personalizados, fechar a mensagem e muito mais! Confira nosso [repositório do GitHub](https://github.com/braze-inc/in-app-message-templates) que contém instruções detalhadas sobre como usar e personalizar mensagens HTML in-app para suas necessidades e um conjunto de modelos de mensagens HTML5 in-app para ajudá-lo a começar.

{% alert note %}
Para habilitar mensagens HTML no aplicativo por meio do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` ao Braze: por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no aplicativo podem executar JavaScript, portanto, exigimos que um mantenedor de site as habilite.
{% endalert %}

## Ponte JavaScript {#javascript-bridge}

As mensagens HTML no aplicativo para SDKs da Web, Android, iOS e Swift suportam uma "ponte" JavaScript para fazer a interface com o SDK do Braze, permitindo que você acione ações personalizadas do Braze quando os usuários clicarem em elementos com links ou se envolverem com o seu conteúdo. Esses métodos existem com a variável global `brazeBridge` ou `appboyBridge`.

{% alert important %}
A Braze recomenda que você use a variável global `brazeBridge`. A variável global `appboyBridge` está obsoleta, mas continuará a funcionar para os usuários existentes. Se estiver usando `appboyBridge`, sugerimos que migre para `brazeBridge`. <br><br> `appboyBridge` foi preterido nas seguintes versões do SDK:
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Por exemplo, para registrar um atributo personalizado e um evento personalizado e, em seguida, fechar a mensagem, você pode usar o seguinte JavaScript na sua mensagem HTML in-app:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close this in-app message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### Métodos do JavaScript Bridge {#bridge}

Os seguintes métodos JavaScript são compatíveis com as mensagens in-app em HTML do Braze:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Você não pode fazer referência ao Liquid para inserir <code>customAttributes</code> nos métodos do JavaScript Bridge.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## Ações baseadas em links

Além do JavaScript personalizado, os SDKs do Braze também podem enviar dados analíticos com esses convenientes atalhos de URL. Observe que esses parâmetros de consulta e esquemas de URL diferenciam maiúsculas de minúsculas.

### Rastreamento de cliques em botões (obsoleto)

{% alert warning %}
O uso do endereço `abButtonID` não é compatível com os tipos de mensagem [HTML com visualização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/). Para obter mais informações, consulte nosso [guia de upgrade]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Para registrar cliques em botões para análise de mensagens in-app, é possível adicionar `abButtonId` como parâmetro de consulta a qualquer deep link, URL de redirecionamento ou elemento âncora `<a>`. Use `?abButtonId=0` para registrar um clique no "Botão 1" e `?abButtonId=1` para registrar um clique no "Botão 2".

Como ocorre com outros parâmetros de URL, o primeiro parâmetro deve começar com um ponto de interrogação `?`, enquanto os parâmetros subsequentes devem ser separados por um "e comercial" `&`.

#### Exemplo de URLs

- `https://example.com/?abButtonId=0` - Botão 1 clique
- `https://example.com/?abButtonId=1` - Clique no botão 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Botão 1 clique com outros parâmetros de URL existentes
- `myApp://deep-link?page=home&abButtonId=1` - Deeplink móvel com clique no botão 2
- `<a href="https://example.com/?abButtonId=1">` - Elemento de ancoragem `<a>` com o clique do Botão 2

{% alert note %}
As mensagens no aplicativo são compatíveis apenas com os cliques nos botões 1 e 2. Os URLs que não especificarem um desses dois IDs de botão serão registrados como "cliques no corpo" genéricos.
{% endalert %}

### Abrir link em uma nova janela (somente para celular)

Para abrir links fora do seu aplicativo em uma nova janela, defina `?abExternalOpen=true`. A mensagem será ignorada antes de abrir o link.

Para deep linking, o Braze abrirá seu URL independentemente do valor de `abExternalOpen`.

### Abrir como link detalhado (somente para celular)

Para que o Braze trate seu link HTTP ou HTTPS como um deep link, defina `?abDeepLink=true`.

Quando esse parâmetro de string de consulta estiver ausente ou definido como `false`, o Braze tentará abrir o link da Web em um navegador interno dentro do aplicativo host.

### Fechar mensagem no aplicativo

Para fechar uma mensagem no aplicativo, você pode usar o método javascript `brazeBridge.closeMessage()`.

Por exemplo, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` fechará a mensagem no aplicativo.

## Upload de HTML com visualização

Ao criar mensagens HTML personalizadas no aplicativo, você pode visualizar seu conteúdo interativo diretamente no Braze. 

O painel de visualização da mensagem do editor mostra uma visualização realista que renderiza o JavaScript incluído em sua mensagem. Você pode visualizar e interagir com suas mensagens personalizadas no painel de visualização clicando na paginação, enviando formulários ou pesquisas, assistindo a animações em JavaScript e muito mais!

Interagir com a visualização de HTML passando o dedo pelas páginas.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Qualquer método JavaScript `brazeBridge` que você usar no seu HTML não atualizará os perfis de usuário durante a visualização no painel.
{% endalert %}

### Requisitos do SDK {#supported-sdk-versions}

Para usar a visualização em HTML para mensagens no aplicativo, você deve atualizar para as seguintes versões mínimas do Braze SDK:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Como esse tipo de mensagem só pode ser recebido por determinadas versões posteriores do SDK, os usuários que estiverem em versões não compatíveis do SDK não receberão a mensagem. Considere adotar esse tipo de mensagem depois que uma parte significativa da sua base de usuários estiver acessível ou segmente apenas os usuários cuja versão do aplicativo seja posterior aos requisitos. Saiba mais sobre a [filtragem pela versão mais recente do aplicativo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Criação de uma campanha {#instructions}

Os usuários do seu aplicativo móvel precisam atualizar para as versões do SDK compatíveis para receber uma mensagem in-app do **Custom Code**. Recomendamos que você [incentive os usuários a atualizar]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) seus aplicativos móveis antes de lançar campanhas que dependam de versões mais recentes do Braze SDK.

#### Arquivos de ativos

Ao criar mensagens in-app de código personalizado com upload de HTML, você pode fazer upload de ativos de campanha para a [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para fazer referência na sua mensagem.

Os seguintes tipos de arquivos são suportados para upload:

| Tipo de arquivo        | Extensão de arquivo                    |
| :--------------- | :-------------------------------- |
| Arquivos de fonte       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Imagens SVG       | `.svg`                            |
| Arquivos JavaScript | `.js`                             |
| Arquivos CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A Braze recomenda o upload de ativos para a biblioteca de mídia por dois motivos:

1. Os ativos adicionados a uma campanha por meio da biblioteca de mídia permitem que suas mensagens sejam exibidas mesmo quando o usuário estiver off-line ou com uma conexão de Internet ruim.
2. Os ativos carregados no Braze podem ser reutilizados em todas as campanhas.

##### Adição de arquivos de ativos

Você pode adicionar ativos novos ou existentes à sua campanha.

Para adicionar novos ativos à sua campanha, use a seção de arrastar e soltar para carregar um arquivo. Os ativos adicionados nessa seção também serão adicionados automaticamente à biblioteca de mídia. Para adicionar ativos que você já carregou na biblioteca de mídia, selecione **Add from Media Library (Adicionar da biblioteca de mídia**).

Depois que seus ativos forem adicionados, eles aparecerão na seção **Assets for this campaign (Ativos para esta campanha** ). 

Se o nome de arquivo de um ativo corresponder ao de um ativo HTML local, ele será substituído automaticamente (por exemplo, `cat.png` é carregado e `<img src="cat.png" />` existe). 

Caso contrário, passe o mouse sobre um ativo da lista e selecione <i class="fas fa-copy"></i> **Copy** para copiar o URL do arquivo para a área de transferência. Em seguida, cole o URL do ativo copiado em seu HTML, como faria normalmente ao fazer referência a um ativo remoto.


### Editor HTML

As alterações que você faz no HTML são renderizadas automaticamente no painel de visualização à medida que você digita. Qualquer método [JavaScript`brazeBridge` ](#bridge) que você usar no seu HTML não atualizará os perfis de usuário durante a visualização no painel.

{% alert tip %}
Você pode selecionar <i class="fa-solid fa-magnifying-glass"></i> **Search** no editor de HTML para pesquisar em seu código!
{% endalert %}

### Rastreamento de botões {#button-tracking-improvements}

Você pode acompanhar o desempenho em seu código personalizado na mensagem in-app usando o método [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) método JavaScript. Isso permite que você rastreie programaticamente o "Botão 1", o "Botão 2" e os "Cliques no corpo" usando `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` ou `brazeBridge.logClick()`, respectivamente.

| Cliques     | Método                       |
| ---------- | ---------------------------- |
| Botão 1   | `brazeBridge.logClick('0')` |
| Botão 2   | `brazeBridge.logClick('1')` |
| Clique no corpo | `brazeBridge.logClick()`    |
| Rastreamento de botões personalizados |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Esse método de rastreamento de botões substitui os métodos anteriores de rastreamento automático de cliques (como o `?abButtonId=0`), que foram removidos.
{% endalert %}

Você pode rastrear vários eventos de clique de botão por impressão. Por exemplo, para fechar uma mensagem e registrar um clique no Botão 2, você pode usar o seguinte:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

Você também pode rastrear novos nomes de botões personalizados - até 100 nomes exclusivos por campanha. Por exemplo, `brazeBridge.logClick('blue button')` ou `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Ao usar métodos JavaScript dentro de um atributo `onclick`, coloque os valores da cadeia de caracteres entre aspas simples para evitar conflitos com o atributo HTML entre aspas duplas.
{% endalert %}

#### Limitações

- Você pode ter até 100 IDs de botão exclusivos por campanha.
- Os IDs de botão podem ter até 255 caracteres cada.
- Os IDs de botão só podem incluir letras, números, espaços, traços e sublinhados.

### Alterações incompatíveis com versões anteriores {#backward-incompatible-changes}

1. A mudança incompatível mais notável com esse novo tipo de mensagem são os requisitos do SDK. Os usuários cujo aplicativo SDK não atende aos [requisitos](#supported-sdk-versions) mínimos [de versão do SDK](#supported-sdk-versions) não receberão a mensagem.
<br>

2. O deeplink `braze://close`, que era suportado anteriormente em aplicativos móveis, foi removido em favor do JavaScript `brazeBridge.closeMessage()`. Isso permite mensagens HTML entre plataformas, já que a Web não oferece suporte a links profundos.

3. O rastreamento automático de cliques, que usava `?abButtonId=0` para IDs de botões, e o rastreamento de "cliques no corpo" em botões de fechamento foram removidos. Os exemplos de código a seguir mostram como alterar seu HTML para usar nossos novos métodos JavaScript de rastreamento de cliques:

   | Antes de | Depois de |
   |:-------- |:------------|
   |<code><a href="braze://close">Botão Fechar</a></code>|<code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">Botão Fechar</a></code>|
   |<code><a href="braze://close?abButtonId=0">Botão Fechar</a></code>|<code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">Botão Fechar</a></code>|
   |<code><a href="app://deeplink?abButtonId=0">Botão de trilha 1</a></code>|<code><a href="app://deeplink" onclick="brazeBridge.logClick('0')">Botão de trilha 1</a></code>|
   |<code><script><br>location.href = "braze://close?abButtonId=1"<br></script></code>|<code><script><br>window.addEventListener("ab.BridgeReady", function(){<br>  brazeBridge.logClick("1");<br>  brazeBridge.closeMessage();<br>});<br></script></code>|

