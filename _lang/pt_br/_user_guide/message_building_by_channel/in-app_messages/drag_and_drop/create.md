---
nav_title: Como criar uma mensagem no app
article_title: "Criação de uma mensagem no app com o recurso arrastar e soltar"
description: "Este artigo de referência aborda a criação de uma mensagem no app com o editor de arrastar e soltar, pré-requisitos, detalhes criativos e muito mais."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# Criando uma mensagem no app com o recurso de arrastar e soltar

> Com o editor de arrastar e soltar, você pode criar mensagens no app totalmente personalizadas em campanhas ou no canva usando a experiência de edição de arrastar e soltar.

Se quiser usar seus modelos HTML personalizados existentes ou modelos criados por terceiros, eles deverão ser recriados no editor de arrastar e soltar.

Não tem certeza se sua mensagem no app deve ser enviada usando uma campanha ou um [Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas. Depois de selecionar onde criar sua mensagem, vamos nos aprofundar nas etapas para criar uma mensagem no app do tipo arrastar e soltar.

## Pré-requisitos

### Requisitos do SDK

| Versão mínima do SDK                                                          | Versão recomendada do SDK                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details Para saber mais sobre os SDKs mínimos %}

As mensagens criadas usando o editor de arrastar e soltar só podem ser enviadas a usuários com as versões mínimas do SDK (consulte a tabela acima). Se um usuário não tiver atualizado seu aplicativo (ou seja, se estiver em uma versão mais antiga do SDK), ele não receberá a mensagem no app.

Para aproveitar todos os recursos disponíveis no editor de arrastar e soltar, atualize seus SDKs para as versões recomendadas. Isso permite que você aproveite os seguintes recursos adicionais:

- Links de texto que não descartam a mensagem
- Botões de ação para solicitar um push primer

A seguir, são descritos os requisitos mínimos individuais do SDK para esses recursos:

| Links de texto*                                                         | Solicitar push primer                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*Se você incluir um link em sua mensagem no app que redirecione para um URL e o usuário final não estiver nas versões mínimas do SDK especificadas, a seleção do link fechará a mensagem e o usuário não poderá retornar à mensagem para enviar o formulário.

{% enddetails %}

### Pré-requisitos adicionais

- Para o SDK da Web, a opção de inicialização [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) deve ser definida como `true`. A opção `enableHtmlInAppMessages` também permitirá que essas mensagens funcionem, mas está obsoleta e deve ser atualizada para `allowUserSuppliedJavascript`.
- Se estiver usando o Google Tag Manager, é necessário ativar a opção "Allow HTML In-App Messages" (Permitir mensagens HTML no app) na configuração do GTM.

## Etapa 1: Crie uma mensagem no app

Crie uma nova mensagem no app ou etapa do Canva e selecione **Editor de arrastar e soltar** como sua experiência de mensagens.

## Etapa 2: Selecione seu modelo

Depois de selecionar o editor de arrastar e soltar como sua experiência de edição, você pode optar por:

- Comece com um modelo modal em branco
- Use um modelo de mensagem no app do Braze do tipo arrastar e soltar
- Selecione um modelo salvo de mensagem no app do tipo arrastar e soltar

Selecione **Criar mensagem** para começar a criar sua mensagem no app no editor de arrastar e soltar.

![A seção Braze Templates, na qual é possível escolher um modelo básico, de imagem de fundo, de captura de número de telefone ou em branco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Também é possível acessar todos os modelos na seção **Modelos** do dashboard.

## Etapa 3: Adicionar páginas adicionais (opcional) {#multi-page}

Adicionar páginas à sua mensagem no app permite orientar os usuários por meio de um fluxo sequencial, como um fluxo de integração ou uma jornada de boas-vindas. É possível gerenciar páginas na seção **Páginas** da guia **Construir**.

![Uma mensagem no app para uma empresa do setor de saúde, composta de três páginas.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Adicionar páginas %}

As mensagens no app começam com uma página por padrão. Para adicionar uma nova página:

1. Selecione **\+ Adicionar página**.
2. Selecione na lista de modelos personalizados ou fornecidos pelo Braze.
3. Dê um nome significativo à página. Isso ajudará você a conectar as páginas.

{% alert tip %}
Você pode adicionar até 10 páginas por mensagem no app.
{% endalert %}

Para duplicar uma página existente:

1. Passe o mouse sobre a página na lista e selecione <i class="fas fa-ellipsis-vertical"></i> para abrir mais opções.
2. Selecione **Duplicar**.
3. Dê um nome significativo à página. Isso ajudará você a conectar as páginas.

{% endtab %}
{% tab Exclusão ou renomeação de páginas %}

Para excluir ou renomear uma página:

1. Passe o mouse sobre a página na lista e selecione <i class="fas fa-ellipsis-vertical"></i> para abrir mais opções.
2. Selecione **Renomear** ou **Excluir**.

{% endtab %}
{% endtabs %}

### Etapa 3a: Conectar páginas

As mensagens no app de várias páginas são sequenciais, o que significa que os usuários interagem com a mensagem tocando ou clicando para passar para a próxima página do fluxo.

Para conectar páginas:

1. Selecione sua página inicial.
2. Selecione um botão ou elemento de imagem na tela.
3. Defina **o comportamento ao clicar** como **Acessar a página**.
4. Selecione a página para a qual você deseja criar um link na página inicial.
5. Continue até que todas as páginas estejam vinculadas.

![Um usuário está editando o botão de ação principal para ir para a Página 2 da mensagem no app.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Se uma página não estiver vinculada a nenhuma outra página, a mensagem não poderá ser iniciada.

{% alert note %}
Os usuários podem selecionar o botão fechar X para sair da mensagem a qualquer momento. Esse botão não pode ser removido.
{% endalert %}

## Etapa 4: Crie e projete sua mensagem no app

É aqui que sua mensagem pode desfilar pela passarela, vestida com o estilo característico de sua marca. Usando uma combinação de blocos do editor e configurações de estilo, você pode personalizar e criar sua mensagem no app.

- Para obter uma lista dos blocos de editor disponíveis e suas propriedades, consulte [Blocos de editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).
- Para obter ajuda na personalização da aparência de sua mensagem, consulte [Configurações de estilo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/).
- Para conhecer as práticas recomendadas de criação de mensagens da direita para a esquerda, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Etapa 5: Teste sua mensagem no app

A seção **Preview & Test** permite a prévia de suas mensagens no app em diferentes dispositivos e o envio de uma mensagem de teste para o seu dispositivo. Aqui, você pode garantir que os detalhes estejam alinhados em todas as suas plataformas para sua campanha de mensagens no app do tipo arrastar e soltar. 

É importante sempre testar suas mensagens no app antes de enviar suas campanhas para ajudá-lo a visualizar como será a mensagem final da perspectiva do usuário.

### Pré-visualização da mensagem como usuário

{% alert warning %}
Para enviar um teste para grupos de teste de conteúdo ou usuários individuais, o push deve ser ativado nos dispositivos de teste antes do envio.
{% endalert %}

É possível fazer a prévia das mensagens na guia **Preview & Test**, como se fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado:

- **Usuário aleatório:** O Braze selecionará aleatoriamente um usuário do banco de dados e fará a prévia da mensagem no app com base em suas atribuições ou informações de eventos.
- **Selecione usuário:** É possível selecionar um usuário específico com base em seu endereço de e-mail ou `external_id`. A mensagem no app será prévia com base nas atribuições do usuário e nas informações do evento.
- **Usuário personalizado:** Você pode personalizar um usuário. O Braze oferecerá entradas para todas as atribuições e eventos disponíveis. Insira as informações que você gostaria de ver no e-mail de prévia.

### Lista de verificação de teste

Considere as seguintes perguntas ao testar sua mensagem no app:

- Você testou a mensagem em diferentes dispositivos?
- As imagens e a mídia aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um valor de atribuição padrão no caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deve acessar?

## Perguntas frequentes

#### Por que os cliques no corpo não estão aparecendo em minha página de análise de dados?

Os cliques no corpo não são coletados automaticamente para mensagens no app criadas com o editor de arrastar e soltar. Para obter mais detalhes, consulte os changelogs do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### Posso segmentar com base em cliques em botões?

Sim, você pode segmentar com base em cliques em botões para até dois botões em sua mensagem. Para fazer isso, defina o **Identificador para relatórios** de seus botões como "0" e "1", que corresponderão aos filtros de segmento de mensagem "Clicou no botão de mensagem no app 1" e "Clicou no botão de mensagem no app 2", respectivamente.

![O campo "Identifier for Reporting" (Identificador para relatórios) com um valor de "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### Posso personalizar minha mensagem no app usando HTML ou JavaScript personalizado ou transferir mensagens HTML existentes para o editor?

Não é possível transferir diretamente mensagens HTML existentes para o editor, mas você pode inserir HTML, CSS e JavaScript brutos em um bloco de código personalizado. Você pode usar blocos de código personalizado para incorporar vídeos de terceiros e Liquid avançado, como conteúdo conectado ou declarações condicionais.

#### Como posso criar uma mensagem slideup no app?

Atualmente, o editor está limitado apenas a mensagens modais e de tela cheia. É possível alternar entre os tipos de exibição na seção **Contêiner de mensagens** do painel **Estilos de mensagem**.

#### Posso salvar minha mensagem no app como um modelo depois de criá-la em minha campanha ou no Canva?

Sim. Para qualquer mensagem no app que queira reutilizar em uma campanha futura ou etapa do Canva, é possível salvá-la como um modelo personalizado usando o botão **Salvar como modelo**, disponível depois que você sair do editor. Antes de poder salvá-la como modelo, você deve primeiro lançar a campanha OU salvá-la como rascunho.

![Uma prévia de uma mensagem no app para um tour de produto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Você também pode criar e salvar modelos de mensagens no app navegando até **Modelos** > **Modelos de mensagens no app**.
