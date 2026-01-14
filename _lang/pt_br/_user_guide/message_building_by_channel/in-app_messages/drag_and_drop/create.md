---
nav_title: Criação de uma mensagem in-app
article_title: "Criação de uma mensagem no aplicativo com o recurso arrastar e soltar"
description: "Este artigo de referência aborda a criação de uma mensagem in-app com o editor de arrastar e soltar, pré-requisitos, detalhes criativos e muito mais."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# Criação de uma mensagem in-app com o recurso de arrastar e soltar

> Com o editor de arrastar e soltar, você pode criar mensagens in-app totalmente personalizadas em campanhas ou no Canvas usando a experiência de edição de arrastar e soltar.


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Se você quiser usar seus modelos HTML personalizados existentes ou modelos criados por terceiros, eles deverão ser recriados no editor de arrastar e soltar.

Não tem certeza se sua mensagem in-app deve ser enviada usando uma campanha ou um [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto os Canvases são melhores para jornadas de usuários em várias etapas. Depois de selecionar onde criar sua mensagem, vamos nos aprofundar nas etapas para criar uma mensagem in-app do tipo arrastar e soltar.

## Pré-requisitos

### Requisitos do SDK

| Versão mínima do SDK                                                          | Versão recomendada do SDK                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details More information on minimum SDKs %}

As mensagens criadas com o editor de arrastar e soltar só podem ser enviadas a usuários com as versões mínimas do SDK (consulte a tabela acima). Se um usuário não tiver atualizado seu aplicativo (ou seja, se estiver em uma versão mais antiga do SDK), ele não receberá a mensagem no aplicativo.

Para aproveitar todos os recursos disponíveis no editor de arrastar e soltar, atualize seus SDKs para as versões recomendadas. Isso permite que você aproveite os seguintes recursos adicionais:

- Links de texto que não descartam a mensagem
- Ação do botão para solicitar o push primer

A seguir, são descritos os requisitos mínimos individuais do SDK para esses recursos:

| Links de texto*                                                         | Solicitar push primer                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*Se você incluir um link na sua mensagem in-app que redireciona para um URL e o usuário final não estiver nas versões mínimas do SDK especificadas, a seleção do link fechará a mensagem e o usuário não poderá retornar à mensagem para enviar o formulário.

{% enddetails %}

### Pré-requisitos adicionais

- Para o SDK da Web, a opção de inicialização [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) deve ser definida como `true`. A opção `enableHtmlInAppMessages` também permitirá que essas mensagens funcionem, mas está obsoleta e deve ser atualizada para `allowUserSuppliedJavascript`.
- Se você estiver usando o Google Tag Manager, deverá ativar a opção "Allow HTML In-App Messages" (Permitir mensagens HTML no aplicativo) na configuração do GTM.

## Etapa 1: Crie uma mensagem no aplicativo

Crie uma nova mensagem no aplicativo ou etapa do Canvas e selecione **Drag-And-Drop Editor** como sua experiência de edição.

## Etapa 2: Selecione seu modelo

Depois de selecionar o editor de arrastar e soltar como sua experiência de edição, você pode optar por:

- Comece com um modelo modal em branco
- Use um modelo de mensagem no aplicativo Braze do tipo arrastar e soltar
- Selecione um modelo de mensagem in-app de arrastar e soltar salvo

Selecione **Criar mensagem** para começar a criar sua mensagem in-app no editor de arrastar e soltar.

A seção Braze Templates, onde você pode escolher um modelo básico, de imagem de fundo, de captura de número de telefone ou em branco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Você também pode acessar todos os modelos na seção **Modelos** do painel.

## Etapa 3: Adicionar páginas adicionais (opcional) {#multi-page}

A adição de páginas à sua mensagem in-app permite orientar os usuários por meio de um fluxo sequencial, como um fluxo de integração ou uma jornada de boas-vindas. Você pode gerenciar páginas na seção **Páginas** da guia **Construir**.

Uma mensagem no aplicativo para uma empresa de saúde composta de três páginas.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Adding pages %}

As mensagens in-app começam com uma página por padrão. Para adicionar uma nova página:

1. Selecione **\+ Adicionar página**.
2. Selecione na lista de modelos personalizados ou fornecidos pela Braze.
3. Dê um nome significativo à página. Isso o ajudará a conectar as páginas.

{% alert tip %}
Você pode adicionar até 10 páginas por mensagem no aplicativo.
{% endalert %}

Para duplicar uma página existente:

1. Passe o mouse sobre a página na lista e selecione <i class="fas fa-ellipsis-vertical"></i> para abrir mais opções.
2. Selecione **Duplicar**.
3. Dê um nome significativo à página. Isso o ajudará a conectar as páginas.

{% endtab %}
{% tab Deleting or renaming pages %}

Para excluir ou renomear uma página:

1. Passe o mouse sobre a página na lista e selecione <i class="fas fa-ellipsis-vertical"></i> para abrir mais opções.
2. Selecione **Renomear** ou **Excluir**.

{% endtab %}
{% endtabs %}

### Etapa 3a: Conectar páginas

As mensagens in-app de várias páginas são sequenciais, o que significa que os usuários interagem com a mensagem tocando ou clicando para passar para a próxima página do fluxo.

Para conectar páginas:

1. Selecione sua página inicial.
2. Selecione um botão ou elemento de imagem na tela.
3. Defina **o comportamento ao clicar** como **Ir para a página**.
4. Selecione a página para a qual você deseja criar um link na página inicial.
5. Continue até que todas as páginas estejam vinculadas.

\![Um usuário está editando o botão de ação principal para ir para a página 2 da mensagem in-app.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Se uma página não estiver vinculada a nenhuma outra página, a mensagem não poderá ser iniciada.

{% alert note %}
Os usuários podem selecionar o botão Fechar X para sair da mensagem a qualquer momento. Esse botão não pode ser removido.
{% endalert %}

## Etapa 4: Crie e projete sua mensagem in-app

É aqui que a sua mensagem pode desfilar pela passarela, vestida com o estilo característico da sua marca. Usando uma combinação de blocos do editor e configurações de estilo, você pode personalizar e criar sua mensagem no aplicativo.

- Para obter uma lista dos blocos de editor disponíveis e suas propriedades, consulte [Blocos de editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).
- Para obter ajuda na personalização da aparência de sua mensagem, consulte [Configurações de estilo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/).
- Para conhecer as práticas recomendadas de criação de mensagens da direita para a esquerda, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Etapa 5: Teste sua mensagem in-app

A seção **Preview & Test** permite que você visualize suas mensagens in-app em diferentes dispositivos e envie uma mensagem de teste para o seu dispositivo. Aqui, você pode garantir que os detalhes estejam alinhados em todas as suas plataformas para sua campanha de mensagens in-app do tipo arrastar e soltar. 

É importante sempre testar suas mensagens in-app antes de enviar suas campanhas para ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário.

### Visualizar mensagem como um usuário

{% alert warning %}
Para enviar um teste para grupos de teste de conteúdo ou usuários individuais, o push deve estar ativado nos dispositivos de teste antes do envio.
{% endalert %}

É possível visualizar mensagens na guia **Preview & Test**, como se você fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado:

- **Usuário aleatório:** O Braze selecionará aleatoriamente um usuário do banco de dados e visualizará a mensagem no aplicativo com base em seus atributos ou informações de eventos.
- **Selecione Usuário:** Você pode selecionar um usuário específico com base em seu endereço de e-mail ou `external_id`. A mensagem in-app será visualizada com base nos atributos do usuário e nas informações do evento.
- **Usuário personalizado:** Você pode personalizar um usuário. O Braze oferecerá entradas para todos os atributos e eventos disponíveis. Insira as informações que você gostaria de ver no e-mail de visualização.

### Lista de verificação de teste

Considere as seguintes perguntas ao testar sua mensagem in-app:

- Você testou a mensagem em diferentes dispositivos?
- As imagens e a mídia aparecem e funcionam como esperado?
- O Liquid funciona conforme o esperado? Você considerou um valor de atributo padrão para o caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deve ir?

## Perguntas frequentes

#### Por que os cliques no corpo não estão aparecendo na minha página de análise?

Os cliques no corpo não são coletados automaticamente para mensagens in-app criadas com o editor de arrastar e soltar. Para obter mais detalhes, consulte os registros de alterações do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### Posso segmentar com base em cliques em botões?

Sim, você pode segmentar com base em cliques em botões para até dois botões em sua mensagem. Para fazer isso, defina o **Identificador para relatórios** de seus botões como "0" e "1", que corresponderão aos filtros de segmentação "Botão de mensagem in-app clicado 1" e "Botão de mensagem in-app clicado 2", respectivamente.

\![O campo "Identifier for Reporting" (Identificador para relatórios) com valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### Posso personalizar minha mensagem in-app usando HTML ou JavaScript personalizado ou transferir mensagens HTML existentes para o editor?

Não é possível transferir diretamente mensagens HTML existentes para o editor, mas você pode inserir HTML, CSS e JavaScript brutos em um bloco de código personalizado. Você pode usar blocos de Custom Code para incorporar vídeos de terceiros e Liquid avançado, como Connected Content ou declarações condicionais.

#### Como posso criar uma mensagem de slideup no aplicativo?

Atualmente, o editor está limitado apenas a mensagens modais e de tela cheia. É possível alternar entre os tipos de exibição na seção **Contêiner de mensagem** do painel **Estilos de mensagem**.

#### Posso salvar minha mensagem in-app como um modelo depois de criá-la em minha campanha ou no Canvas?

Sim. Para qualquer mensagem in-app que você queira reutilizar em uma campanha futura ou etapa do Canvas, é possível salvá-la como um modelo personalizado usando o botão **Salvar como modelo**, disponível depois que você sair do editor. Antes de poder salvá-la como modelo, você deve primeiro lançar a campanha OU salvá-la como rascunho.

\![Uma visualização de uma mensagem no aplicativo para um tour de produto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Você também pode criar e salvar modelos de mensagens in-app navegando até **Modelos** > **Modelos de mensagens in-app**.
