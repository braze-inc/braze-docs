---
nav_title: Mensagens no app em HTML
article_title: Mensagens no app em HTML personalizado
page_order: 0
page_type: reference
description: "Este artigo fornece uma visão geral das mensagens no app com código personalizado, incluindo métodos JavaScript, rastreamento de botões e uso da prévia HTML interativa na Braze."
channel:
  - in-app messages
---

# Mensagens no app em HTML personalizado {#custom-html-messages}

> Embora nossas mensagens no app padrão possam ser personalizadas de várias maneiras, você pode ter um controle ainda maior sobre a aparência de suas campanhas usando mensagens projetadas e criadas com HTML, CSS e JavaScript. Com algumas composições simples, você pode desbloquear a funcionalidade e a marca personalizadas para atender a qualquer uma de suas necessidades. 

As mensagens no app em HTML permitem maior controle sobre a aparência de uma mensagem, incluindo o seguinte:

- Fontes e estilos personalizados
- Vídeos
- Várias imagens
- Comportamentos ao clicar
- Componentes interativos
- Animações personalizadas

As mensagens HTML personalizadas podem usar os métodos [do JavaScript Bridge](#javascript-bridge) para registrar eventos, definir atributos personalizados, fechar a mensagem e muito mais! Confira nosso [repositório no GitHub](https://github.com/braze-inc/in-app-message-templates), que contém instruções detalhadas sobre como usar e personalizar mensagens no app em HTML para suas necessidades, e um conjunto de modelos de mensagens no app em HTML5 para ajudá-lo a começar.

{% alert note %}
Para ativar mensagens no app HTML através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para o Braze: por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no app podem executar JavaScript, portanto, exigimos que um mantenedor de site as ative.
{% endalert %}

## Ponte JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## Ações baseadas em links

Além do JavaScript personalizado, os SDKs da Braze também podem enviar dados de análises com esses convenientes atalhos de URL. Observe que esses parâmetros de consulta e esquemas de URL diferenciam maiúsculas de minúsculas.

### Rastreamento de cliques em botões (obsoleto)

{% alert warning %}
O uso do endereço `abButtonID` não é compatível com os tipos de mensagem [HTML com Prévia]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/). Para saber mais, consulte nosso [guia de upgrade]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Para registrar cliques em botões para análise de mensagens no app, é possível adicionar `abButtonId` como parâmetro de consulta a qualquer deep linking, URL de redirecionamento ou elemento âncora `<a>`. Use `?abButtonId=0` para registrar um clique no "Botão 1" e `?abButtonId=1` para registrar um clique no "Botão 2".

Como ocorre com outros parâmetros de URL, o primeiro parâmetro deve começar com um ponto de interrogação `?`, enquanto os parâmetros subsequentes devem ser separados por um "e comercial" `&`.

#### Exemplo de URLs

- `https://example.com/?abButtonId=0` - Botão 1 clique
- `https://example.com/?abButtonId=1` - Clique no botão 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Botão 1 clique com outros parâmetros de URL existentes
- `myApp://deep-link?page=home&abButtonId=1` - Deep link móvel com clique no botão 2
- `<a href="https://example.com/?abButtonId=1">` - Elemento de ancoragem `<a>` com o clique do Botão 2

{% alert note %}
As mensagens no app são compatíveis apenas com os cliques nos botões 1 e 2. Os URLs que não especificarem um desses dois IDs de botão serão registrados como "cliques no corpo" genéricos.
{% endalert %}

### Abrir link em uma nova janela (somente para celular)

Para abrir links fora de seu app em uma nova janela, defina `?abExternalOpen=true`. A mensagem será ignorada antes de abrir o link.

Para deep links, a Braze abrirá seu URL independentemente do valor de `abExternalOpen`.

### Abrir como link detalhado (somente para celular)

Para que a Braze trate seu link HTTP ou HTTPS como um deep linking, defina `?abDeepLink=true`.

Quando esse parâmetro de string de consulta estiver ausente ou definido como `false`, a Braze tentará abrir o link da Web em um navegador interno dentro do app host.

### Fechar mensagem no app

Para fechar uma mensagem no app, você pode usar o método javascript `brazeBridge.closeMessage()`.

Por exemplo, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` fechará a mensagem no app.

## Upload de HTML com prévia

Ao criar mensagens no app em HTML personalizado, você pode fazer uma prévia do seu conteúdo interativo diretamente no Braze. 

O painel de visualização de mensagens do editor mostra uma prévia realista que renderiza o JavaScript incluído em sua mensagem. Você pode fazer uma prévia e interagir com suas mensagens personalizadas no painel de visualização clicando na paginação, enviando formulários ou pesquisas, assistindo a animações em JavaScript e muito mais!

![Interagindo com a prévia HTML ao deslizar pelas páginas.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Todos os métodos JavaScript do `brazeBridge` que você usar no HTML não atualizarão os perfis de usuário durante a prévia no dashboard.
{% endalert %}

### Requisitos do SDK {#supported-sdk-versions}

Para usar a prévia em HTML para mensagens no app, você deve fazer upgrade para as seguintes versões mínimas do SDK da Braze:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Como esse tipo de mensagem só pode ser recebido por certas versões mais recentes do SDK, usuários que estão em versões de SDK não suportadas não receberão a mensagem. Considere adotar esse tipo de mensagem depois que uma parte significativa da sua base de usuários estiver acessível ou direcione apenas os usuários cuja versão do app seja posterior aos requisitos. Saiba mais sobre a [filtragem pela versão mais recente do app]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Criação de uma campanha {#instructions}

Seus usuários do app móvel precisam fazer upgrade para as versões de SDK suportadas para receber uma mensagem no app **Custom Code**. Recomendamos que você [incentive os usuários a fazer upgrade de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) seus apps móveis antes de lançar campanhas que dependam de versões mais recentes do SDK da Braze.

#### Arquivos de ativos

Ao criar mensagens no app com código personalizado com upload de HTML, você pode fazer upload de ativos de campanha para a [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para fazer referência na sua mensagem.

Os seguintes tipos de arquivos são suportados para fazer upload:

| Tipo de arquivo        | Extensão de arquivo                    |
| :--------------- | :-------------------------------- |
| Arquivos de fontes       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Imagens SVG       | `.svg`                            |
| Arquivos JavaScript | `.js`                             |
| Arquivos CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A Braze recomenda fazer upload de ativos para a biblioteca de mídia por dois motivos:

1. Ativos adicionados a uma campanha via a biblioteca de mídia permitem que suas mensagens sejam exibidas mesmo enquanto o usuário está offline ou tem uma conexão de internet ruim.
2. Os ativos feitos upload na Braze podem ser reutilizados em todas as campanhas.

##### Adição de arquivos de ativos

Você pode adicionar ativos novos ou existentes à sua campanha.

Para adicionar novos ativos à sua campanha, use a seção de arrastar e soltar para fazer upload de um arquivo. Os ativos adicionados nesta seção também serão adicionados automaticamente à biblioteca de mídia. Para adicionar ativos que já foram feitos upload na biblioteca de mídia, selecione **Adicionar da biblioteca de mídia**.

Depois que seus ativos forem adicionados, eles aparecerão na seção **Assets for this campaign (Ativos para esta campanha** ). 

Se o nome do arquivo de um ativo corresponder ao de um ativo HTML local, ele é substituído automaticamente (por exemplo, `cat.png` é enviado e `<img src="cat.png" />` existe). 

Caso contrário, passe o mouse sobre um ativo da lista e selecione <i class="fas fa-copy"></i> **Copy** para copiar o URL do arquivo para a área de transferência. Em seguida, cole o URL do ativo copiado em seu HTML como faria normalmente ao fazer referência a um ativo remoto.

### editor de HTML

As alterações feitas no HTML são renderizadas automaticamente no painel de prévia à medida que você digita. Todos os métodos [JavaScript do`brazeBridge` ](#bridge) que você usar no HTML não atualizarão os perfis de usuário durante a prévia no dashboard.

{% alert tip %}
Você pode selecionar <i class="fa-solid fa-magnifying-glass"></i> **Pesquisar** dentro do editor de HTML para buscar dentro do seu código!
{% endalert %}

### Rastreamento de botões {#button-tracking-improvements}

Você pode rastrear a performance em sua mensagem no app com código personalizado usando o método [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) JavaScript. Para a referência completa, veja [Métodos da Ponte JavaScript](#bridge) acima.

{% alert note %}
Esse método de rastreamento de botões substitui os métodos anteriores de rastreamento automático de cliques (como o `?abButtonId=0`), que foram removidos.
{% endalert %}

### Alterações incompatíveis com versões anteriores {#backward-incompatible-changes}

1. A mudança incompatível mais notável com esse novo tipo de mensagem são os requisitos do SDK. Os usuários cujo app SDK não atende aos [requisitos mínimos de versão do SDK](#supported-sdk-versions) não receberão a mensagem.
2. O deeplink `braze://close`, que era suportado anteriormente em apps móveis, foi removido em favor do JavaScript `brazeBridge.closeMessage()`. Isso permite o envio de mensagens HTML para várias plataformas, já que a Web não oferece suporte a links profundos.
3. O rastreamento automático de cliques, que usava `?abButtonId=0` para IDs de botões, e o rastreamento de "cliques no corpo" em botões de fechamento foram removidos. Os exemplos de código a seguir mostram como alterar seu HTML para usar nossos novos métodos JavaScript de rastreamento de cliques:

   | Antes | Após |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_1b109db0-e2b8-4f4b-9913-5faac46ae9ef/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_29093175-51a6-4ec2-9b04-a4624ae70fc8/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_08480904-4ef5-4e48-9d9e-ec805c3f3025/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_9e17ee79-d068-47b5-8db4-de7539127172/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_d97d9a73-1539-46a0-84fe-722e6ffeccdf/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

