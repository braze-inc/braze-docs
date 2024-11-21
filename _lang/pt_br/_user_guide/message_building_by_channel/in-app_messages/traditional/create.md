---
nav_title: Como criar uma mensagem no app
article_title: Como criar uma mensagem no app
page_order: 1
description: "Este artigo de referência aborda como criar uma mensagem no app usando a plataforma Braze por meio de campanhas ou do Canva."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
---

# Criar uma mensagem no app

> Você pode criar uma mensagem no app ou no navegador usando a plataforma Braze por meio de campanhas, Canvas ou como uma campanha API. É altamente recomendável planejar suas mensagens e preparar todos os materiais com antecedência usando nosso prático [guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Etapa 1: Escolha onde construir sua mensagem {#create-new-campaign-in-app}

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campanha %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **Campaigns** em **Engagement (Engajamento**).
{% endalert %}

{:start="2"}
2\. Selecione **Mensagem no app**. Observe que as mensagens no app não estão disponíveis em campanhas de vários canais.
3\. Dê à sua campanha um nome claro e significativo.
4\. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário. Observe que as etapas que contêm mensagens no app não podem ser baseadas em ações.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções do público serão conferidas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de envio de mensagens que gostaria de associar à sua mensagem.

{% alert important %}
Não é possível ter várias variantes de mensagens no app em uma única etapa.
{% endalert %}

Você pode encontrar mais informações específicas do Canvas em [Mensagens no app do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 2: Especificar plataformas de entrega

Comece escolhendo quais plataformas devem receber a mensagem. Use essa seleção para limitar a entrega de uma campanha a um conjunto específico de aplicativos. Por exemplo, você pode escolher **navegadores da Web** para uma mensagem no navegador incentivando os usuários a baixar seu aplicativo móvel para garantir que eles não recebam a mensagem depois de já terem baixado o aplicativo. Como as seleções de plataforma são específicas para cada variante, você pode tentar testar o engajamento com mensagens por plataforma.

| Plataforma                        | Envio de mensagens        |
|---------------------------------|-------------------------|
| Apps móveis                     | SDKs para iOS e Android      |
| Navegadores                    | SDK da Web                 |
| Apps móveis e navegadores de internet | SDKs para iOS, Android e Web |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Especifique seus tipos de mensagens

Depois de selecionar uma plataforma de envio, navegue pelos tipos de mensagens, layouts e outras opções associadas a ela. Saiba mais sobre o comportamento esperado e a aparência de cada uma dessas mensagens em nossa página [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) ou clicando nos tipos de mensagem vinculados nas tabelas a seguir.

Ao decidir qual tipo de mensagem usar, você deve considerar o quão intrusiva sua campanha de mensagens no app precisa ser. Essa é uma medida da quantidade de espaço na tela que a mensagem ocupará e o quanto isso interrompe a experiência regular do cliente no app ou no site. Quanto mais rico for o conteúdo que você deseja fornecer, mais intrusiva precisará ser sua mensagem.

![Gráfico mostrando uma escala de menos intrusivo a mais intrusivo, com o controle deslizante sendo o menos intrusivo, seguido pelo modal, e a tela cheia sendo o mais intrusivo]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

### Tipos de mensagens

Essas mensagens no app são aceitas tanto por aplicativos móveis quanto por aplicativos da Internet.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensagem</th>
    <th>Descrição do tipo</th>
    <th>Layouts disponíveis</th>
    <th>Outras opções</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Tela inteira</a></td>
    <td>Envio de mensagens que cobrem a tela inteira com um bloco de mensagens.</td>
    <td>
      <ul>
      <li>Imagem e texto</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>Orientação forçada do dispositivo (retrato ou paisagem)</td>
    <td>Grande e ousado! Use quando quiser ter certeza de que os usuários vejam seu conteúdo, como suas campanhas mais críticas, notificações importantes ou promoções em massa.<br><br>Observe que, em dispositivos móveis, as mensagens em retrato e paisagem não serão exibidas se a orientação do dispositivo não corresponder à orientação da mensagem.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Mensagens que cobrem toda a tela com uma sobreposição de tela e um bloco de mensagens.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>N/D</td>
    <td>Um bom meio-termo. Use-o quando precisar de uma forma aparente de chamar a atenção do usuário, como, por exemplo, incentivar os usuários a experimentar um novo recurso ou aproveitar uma promoção.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Slideup</a></td>
    <td>Envio de mensagens que deslizam para exibição em um local designado sem bloquear o resto da tela.</td>
    <td>N/D</td>
    <td>N/D</td>
    <td>Discreto - ocupa o mínimo de espaço na tela. Use para alertar os usuários sobre pequenos trechos de informações, como novos recursos, anúncios, uso de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Tipos avançados de mensagens

Essas mensagens no app podem ser personalizadas de acordo com suas necessidades.

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensagem</th>
    <th>Descrição do tipo</th>
    <th>Layouts disponíveis</th>
    <th>Solicitações</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Envio de mensagens HTML personalizadas</a></td>
    <td>Envios de mensagens personalizadas que têm a performance definida em seu código personalizado (HTML, CSS e/ou JavaScript).</td>
    <td>N/D</td>
    <td>Precisa ser definido <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> opção de inicialização para <code>true</code> para que sua mensagem no app funcione.</td>
    <td>Essa é uma boa opção se você quiser todas as vantagens dos IAMs, mas precisar de funcionalidade adicional ou para que a aparência permaneça "na marca". Você pode alterar cada pequeno detalhe da mensagem: fonte, cor, forma, tamanho, botões, etc. <br><br>Exemplos de casos de uso incluem solicitar feedback do app aos usuários, formulários de captura de e-mail ou mensagens paginadas</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulário de captura de e-mail</a></td>
    <td>Normalmente usado para capturar o e-mail do visualizador.</td>
    <td>N/D</td>
    <td>Precisa ser definido <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> opção de inicialização para <code>true</code> para que sua mensagem no app funcione.</td>
    <td>Ao solicitar que os usuários enviem seus endereços de e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Modal da Web com CSS</a></td>
    <td>Mensagens modais pela internet com CSS personalizável.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>O Web Modal com CSS é exclusivo do Web SDK e só pode ser usado após a seleção de <b>navegadores da Web</b>.</td>
    <td>Quando você quiser fazer upload ou escrever CSS personalizado para criar um envio de mensagens bonito e com estilo personalizado. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Se o Braze detectar que você não tem um botão de fechar ou dispensar incluído em seu código, solicitaremos que você adicione um. Para sua conveniência, fornecemos um snippet que pode ser copiado e colado em seu código: <br><br>`<a href= "appboy://close">X</a>`
{% endalert %}

## Etapa 4: Crie sua mensagem no app

A guia **Criar** permite que você edite todos os aspectos do conteúdo e do comportamento da sua mensagem.

![Um exemplo de mensagem no app de uma marca para dar as boas-vindas a novos clientes e solicitar que eles criem um perfil de usuário.][24]{: style="max-width:85%" }

O conteúdo da guia **Compose (Criar** ) varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

#### Idioma

Selecione **Add Languages (Adicionar idiomas** ) e selecione os idiomas desejados na lista fornecida. Isso inserirá [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) em sua mensagem. Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que possa preencher o texto onde ele pertence no Liquid. Consulte nossa [lista completa de idiomas disponíveis][18].

#### Imagem

Dependendo do tipo de mensagem, você pode fazer **upload de imagem**, **escolher um emblema** ou usar **Font Awesome**. Para fazer upload de uma imagem, clique em **Add Image (Adicionar imagem** ) ou forneça o URL da imagem. Clicar em **Add Image (Adicionar imagem** ) abre a **Media Library (Biblioteca de mídia)**, onde é possível selecionar uma imagem feita upload anteriormente ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos. Certifique-se de verificar quais são eles antes de encomendar ou criar uma imagem do zero!

#### Cabeçalho e corpo

Escreva o que você quiser! Inclua uma cópia totalmente personalizada (geralmente com recursos HTML personalizados) com as opções de incluir [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) e outros tipos de personalização. Quanto mais rápido você conseguir transmitir sua mensagem e fazer com que seu cliente clique, melhor! Recomendamos que os cabeçalhos e o conteúdo das mensagens sejam claros e concisos.

Alguns tipos de mensagens não precisam de cabeçalhos e, portanto, não os solicitam.

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Insira o nome ou a descrição de um produto e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Inicie o botão IA Copywriter, localizado no campo Mensagem do criador de mensagens no app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}
{% endalert %}

#### Texto do botão {#buttons}

Quando disponível para o seu tipo de mensagem, você pode fazer com que até dois botões apareçam sob o corpo do texto. Você pode criar e editar o texto e a cor do botão personalizado. Você também pode adicionar o link dos Termos de Serviço nos formulários de captura de e-mail.

![Botões primário e secundário em uma mensagem no app]({% image_buster /assets/img/primary-secondary-buttons.png %}){: style="float:right;margin-left:15px;height:30%;width:30%"}

Se você optar por usar apenas um botão, ele se ajustará automaticamente para ocupar o espaço disponível na parte inferior da mensagem, em vez de deixar espaço para um botão adicional.

##### Escolha de um botão principal

Se você decidir formatar esses botões com suas próprias cores, recomendamos que use o Botão 2 para obter o resultado desejado. Em outras palavras, se quiser que o usuário clique mais em um botão do que no outro, certifique-se de que ele esteja à direita. O botão direito geralmente apresenta melhor potencial para ser clicado, especialmente se tiver uma cor contrastante ou que se destaque do restante da mensagem. Isso só é enfatizado quando o botão à esquerda combina mais visualmente com a mensagem.

#### Comportamento ao clicar {#button-actions}

Quando o cliente clica em um botão em sua mensagem no app, as seguintes ações estão disponíveis. 

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abra uma página da Web não nativa. |
| [Deep linking no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Deep linking em uma tela existente em seu app. |
| Fechar mensagem | Fecha a mensagem ativa no momento. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) para disparar. Pode ser usado para exibir outra mensagem no app ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) a ser definido para o usuário atual. |
| Solicitar permissão para push | Mostra a permissão de push nativa. Leia mais sobre o [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/), bem como sobre [as práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) para preparar os usuários para o push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nota: as opções __Request Push Permission__, __Log Custom Event__ e __Log Custom Attribute__ exigem as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

#### Opções de dispositivos iOS

Se desejar, você pode restringir sua mensagem no app para enviar apenas para dispositivos iOS. Para fazer isso, clique em **Alterar** e selecione **Enviar somente para dispositivos iOS**.

#### Fechamento da mensagem

Escolha entre as seguintes opções:
 
- **Dispensar automaticamente:** Selecione quantos segundos a mensagem permanecerá na tela.
- **Aguarde o deslizamento ou o toque do usuário:** Requer uma opção de demissão ou encerramento.

#### Posição de deslizamento para cima

Essa configuração só se aplica ao tipo de mensagem Slideup. Escolha entre fazer com que o slideup apareça **na parte inferior da tela do app** ou **na parte superior da tela do app**.

#### HTML e ativos

Essa configuração se aplica apenas ao tipo de mensagem Código personalizado. Copie e cole o HTML no espaço disponível e faça upload de seus ativos usando um arquivo ZIP.

#### Espaço reservado para entrada de captura de e-mail

Essa configuração só se aplica ao tipo de mensagem do formulário de captura de e-mail. Digite a cópia personalizada que aparecerá como texto de espaço reservado para o campo de entrada de e-mail. O padrão é "Digite seu endereço de e-mail".

## Etapa 5: Estilize sua mensagem no app

A guia **Style (Estilo** ) permite ajustar todos os aspectos visuais da sua mensagem. Faça upload de uma imagem ou crachá ou escolha um ícone de crachá predefinido. Altere as cores do texto do cabeçalho e do corpo, dos botões e do plano de fundo selecionando em uma paleta ou inserindo um código hexadecimal, RGB ou HSB.

O conteúdo da guia **Style (Estilo** ) varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

| Formatação | Entrada | Descrição |
|---|---|---|
|Perfil de cores | Aplique a partir da galeria de modelos de mensagens no app. | Clique em **Apply Template (Aplicar modelo** ) e selecione na galeria. Em seguida, clique em **Salvar**. |
|Alinhamento de texto | Esquerda, Centro ou Direita.  | Disponível apenas para as versões mais recentes do SDK da Braze. |
|Cabeçalho | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor.  |
|Texto | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
|Botões | Código de cores HEX. | As cores HEX desejadas serão exibidas. Você também poderá escolher a opacidade das cores. Você pode escolher cores para: o plano de fundo do botão Fechar da mensagem, bem como o plano de fundo, o texto e a borda de cada botão. |
| Borda do botão | Código de cores HEX. | Novo! Isso permitirá que você defina os botões primário e secundário separados um do outro. Sugerimos que os botões sejam contornados com cores contrastantes. |
|Cor de fundo | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Esse é o plano de fundo de toda a mensagem e será exibido claramente atrás do corpo do texto. |
|Sobreposição da tela | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Disponível apenas para as versões mais recentes do SDK da Braze. Essa é a moldura que envolve toda a mensagem. |
|Chevron ou outra opção de mensagem de fechamento | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sempre [faça uma prévia e teste]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sua mensagem antes de enviá-la.

{% alert important %}
Alguns tipos de mensagens no app não têm a opção de estilização além de fazer upload de HTML personalizado (ou CSS ou JavaScript) e ativos usando um arquivo ZIP. [O Web Modal com CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) permite que você faça upload ou escreva CSS personalizado para criar mensagens bonitas e com estilo personalizado.
{% endalert %}

## Etapa 6: Configurar definições adicionais (opcional)

### Pares de valores chave

É possível adicionar [key-value pairs][19] para enviar campos personalizados adicionais aos dispositivos do usuário.

## Etapa 7: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}

Crie o restante de sua campanha; consulte as seções a seguir para obter mais orientações sobre a melhor forma de usar nossas ferramentas para criar mensagens no app.

#### Escolha um disparador

Selecione a ação que deseja disparar sua mensagem, bem como os horários de início e término de sua campanha ou do Canva.

{% alert important %}
Note que, se você pretende disparar sua mensagem no app com base em um evento personalizado, esse evento personalizado deve ser enviado usando o SDK.
{% endalert %}

![Campanha baseada em ação com a ação-gatilho definida como "Iniciar sessão".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

A entrega de mensagens no app é totalmente baseada nos seguintes disparos de ação:

- Fazer uma compra
- Abrir o app/página da Web
- Realização de um evento personalizado (só funciona com eventos enviados usando o SDK)
- Abrir uma mensagem push específica
- Programe automaticamente o envio de campanhas em um determinado horário, de acordo com o fuso local de cada um de seus usuários.
- O envio de mensagens também pode ser configurado para ser recorrente em uma base diária, semanal (opcionalmente em dias específicos) ou mensal.

Uma data e hora de início devem ser selecionadas; no entanto, uma data de término é opcional. Uma data final impedirá que essa mensagem no app específica seja exibida nos dispositivos após a data/hora especificada.

Consulte nossa documentação para desenvolvedores sobre [disparo de eventos no lado do servidor]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) e [envio local de mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Disparos on-line e off-line

As mensagens no app funcionam enviando a mensagem e os disparos para o dispositivo do usuário. Depois que as mensagens no app estiverem em um dispositivo, ele aguardará a exibição até que a condição de disparo seja atendida. Se as mensagens no app já estiverem armazenadas em cache no dispositivo do usuário, você poderá até mesmo disparar mensagens no app off-line sem conexão com o Braze (por exemplo, no modo Avião).

{% alert important %}
Depois que uma mensagem no app tiver sido interrompida, alguns usuários poderão continuar a ver a mensagem se tiverem iniciado uma sessão antes de a mensagem ser interrompida e, posteriormente, executarem o evento de gatilho. Esses usuários serão contados como uma impressão única, mesmo depois que a campanha for interrompida.
{% endalert %}

#### Escolha uma prioridade

Por fim, depois de selecionar a ação em que a mensagem no app será disparada, você também deverá definir uma prioridade. Se duas mensagens forem disparadas a partir da mesma ação, as mensagens de alta prioridade serão programadas para aparecer nos dispositivos dos usuários antes das mensagens com prioridades mais baixas. 

Você pode escolher entre as seguintes prioridades de mensagens:

- Baixa prioridade (mostrado depois de outras mensagens)
- Prioridade média
- Alta prioridade (mostrado antes de outras mensagens)

As opções alta, média e baixa para as prioridades das mensagens disparadas são compartimentos e, portanto, várias mensagens podem ter a mesma prioridade selecionada. Para definir prioridades dentro desses compartimentos, clique em **Set Exact Priority (Definir prioridade exata**), e você poderá arrastar e soltar campanhas para ordená-las com a prioridade correta.

![Um exemplo de como a prioridade é definida para uma campanha de mensagens no app e no Canva.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Escolha os usuários a serem direcionados

Em seguida, é necessário direcionar [os usuários]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

{% alert note %}
Se houver uma postergação na etapa da mensagem no app, a associação ao segmento será avaliada após o atraso. Se o usuário for elegível, a mensagem no app será sincronizada na próxima sessão disponível.
{% endalert %}

##### Reavaliar a elegibilidade da campanha e o Liquid

Em alguns cenários, talvez seja necessário reavaliar a elegibilidade de um usuário quando ele dispara uma mensagem no app para ser exibida. Os exemplos incluem campanhas que direcionam um atributo personalizado que muda com frequência ou mensagens que devem refletir qualquer alteração de perfil de última hora.

![Seção Resumo do público da etapa Usuários-alvo com a opção "Reavaliar elegibilidade da campanha antes de exibir" selecionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %})

Ao selecionar **Reavaliar a elegibilidade da campanha antes de** exibi-la, será feita uma solicitação adicional ao Braze para confirmar que o usuário ainda é elegível para essa mensagem antes do envio. Além disso, todas as variáveis [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) serão modeladas nesse momento, antes que a mensagem seja exibida.

Isso evita que mensagens no app sejam enviadas a usuários em campanhas expiradas ou arquivadas. Se você não reavaliar a elegibilidade de um usuário, ele receberá a mensagem no app mesmo depois que a campanha expirar ou for arquivada, porque a mensagem está no seu SDK e aguardando que os usuários a disparem.

{% alert note %}
A capacitação dessa opção resultará em uma pequena postergação (< 100 ms) entre o momento em que um usuário dispara uma mensagem no app e o momento em que a mensagem é exibida, devido à elegibilidade adicionada e à solicitação de modelo.
<br><br>
Não use essa opção para mensagens que possam ser disparadas enquanto o usuário estiver off-line ou quando a elegibilidade e a reavaliação do Liquid não forem necessárias.
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}
{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nossa documentação do Canvas.

Para obter informações sobre as opções de envio de mensagens no aplicativo específicas do Canva, consulte [Mensagens no aplicativo no Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 8: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canva, revise seus detalhes, [teste-a]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) e envie-a!

Em seguida, confira [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para saber como acessar os resultados de suas campanhas de mensagens.

## Coisas para saber

### Limites ativos da campanha de mensagens no app

A Braze valoriza a confiabilidade e a velocidade. Assim como sugerimos que você envie ao Braze apenas os dados necessários, também recomendamos desativar as campanhas que não estejam mais agregando valor à sua marca.

O processamento de campanhas de mensagens no app baseadas em ações que ainda estão em um estado ativo, mas que não estão mais enviando mensagens ou que não são mais necessárias, diminui a performance geral dos serviços Braze para você e para outros clientes. Esse tempo extra necessário para processar esse grande número de campanhas sem atividades significa que qualquer mensagem no app levará mais tempo para aparecer nos dispositivos do usuário final, o que afeta a experiência do usuário final.

{% alert important %}
Você pode ter até 200 campanhas de mensagens no app ativas e baseadas em ação por espaço de trabalho para otimizar a velocidade de entrega de mensagens e evitar tempos limite. Isso não se aplica às telas.
{% endalert %}

A contagem de 200 inclui campanhas ativas de mensagens no app que ainda não atingiram o horário de término e aquelas que não têm horário de término. Campanhas ativas de mensagens no app que tenham ultrapassado o horário de término não serão contadas. O cliente Braze médio tem um total de 26 campanhas ativas ao mesmo tempo, portanto, é improvável que essa limitação afete você.


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engajamento_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img_archive/iam_compose.png %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
