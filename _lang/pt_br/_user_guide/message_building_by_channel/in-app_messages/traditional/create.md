---
nav_title: Criação de uma mensagem in-app
article_title: Criação de uma mensagem no aplicativo
page_order: 1
description: "Este artigo de referência aborda como criar uma mensagem in-app usando a plataforma Braze por meio de campanhas ou Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Criação de uma mensagem in-app

> Você pode criar uma mensagem in-app ou in-browser usando a plataforma Braze por meio de campanhas, Canvas ou como uma campanha de API. É altamente recomendável planejar suas mensagens e preparar todos os materiais com antecedência usando nosso prático [guia de preparação de mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Etapa 1: Escolha onde construir sua mensagem {#create-new-campaign-in-app}

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canvas? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto os Canvases são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

1. Vá para **Messaging** > **Campaigns** ( **Mensagens** > **Campanhas** ) e selecione **Create Campaign (Criar campanha**).
2. Selecione **Mensagem no aplicativo**. Observe que as mensagens in-app não estão disponíveis em campanhas multicanal.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para obter mais informações sobre esse tópico, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar outras variantes. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor do Canvas. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique um atraso conforme necessário. Observe que as etapas que contêm mensagens in-app não podem ser baseadas em ações.
4. Filtre seu Audience para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e acrescentando filtros adicionais. As opções de público serão verificadas após o atraso, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de mensagens que você gostaria de associar à sua mensagem.

{% alert important %}
Não é possível ter várias variantes de mensagens in-app em uma única etapa.
{% endalert %}

Você pode encontrar mais informações específicas do Canvas em [Mensagens no aplicativo no Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 2: Especificar plataformas de entrega

Comece escolhendo quais plataformas devem receber a mensagem. Use essa seleção para limitar a entrega de uma campanha a um conjunto específico de aplicativos. Por exemplo, você pode escolher **navegadores da Web** para uma mensagem no navegador incentivando os usuários a baixar seu aplicativo móvel para garantir que eles não recebam a mensagem depois de já terem baixado o aplicativo. Como as seleções de plataforma são específicas para cada variante, você pode tentar testar o envolvimento da mensagem por plataforma.

| Plataforma                        | Entrega de mensagens        |
|---------------------------------|-------------------------|
| Aplicativos móveis                     | iOS & Android SDKs      |
| Navegadores da Web                    | SDK da Web                 |
| Ambos os aplicativos móveis & Navegadores da Web | iOS, Android & Web SDKs |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Especifique seus tipos de mensagem

Depois de selecionar uma plataforma de envio, navegue pelos tipos de mensagens, layouts e outras opções associadas a ela. Saiba mais sobre o comportamento esperado e a aparência de cada uma dessas mensagens em nossa página [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) ou clicando nos tipos de mensagem vinculados nas tabelas a seguir.

Ao decidir qual tipo de mensagem usar, considere o espaço que a mensagem ocupará e o quanto ela pode atrapalhar a experiência do usuário.

- As mensagens **do Slideup** são as menos intrusivas, aparecendo sutilmente sem bloquear o conteúdo.
- As mensagens **modais** ficam no meio, com destaque suficiente para chamar a atenção sem ocupar totalmente a tela.
- As mensagens **em tela cheia** são as que mais chamam a atenção e são melhores para anúncios ou promoções importantes.

Quanto mais complexo for o conteúdo, mais espaço será necessário e maior será a probabilidade de a mensagem interromper o fluxo do usuário.

### Tipos de mensagem

Essas mensagens no aplicativo são aceitas tanto por aplicativos móveis quanto por aplicativos da Web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensagem</th>
    <th>Tipo Descrição</th>
    <th>Layouts disponíveis</th>
    <th>Outras opções</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Tela cheia</a></td>
    <td>Mensagens que cobrem a tela inteira com um bloco de mensagens.</td>
    <td>
      <ul>
      <li>Imagem e texto</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>Orientação forçada do dispositivo (retrato ou paisagem)</td>
    <td>Grande e ousado! Use-o quando quiser garantir que os usuários vejam seu conteúdo, como suas campanhas mais críticas, notificações importantes ou promoções em massa.<br><br>Observe que, em dispositivos móveis, as mensagens em retrato e paisagem não serão exibidas se a orientação do dispositivo não corresponder à orientação da mensagem.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Mensagens que cobrem a tela inteira com uma sobreposição de tela e um bloco de mensagens.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Um bom meio-termo. Use-o quando precisar de uma maneira aparente de chamar a atenção do usuário, como, por exemplo, incentivar os usuários a experimentar um novo recurso ou aproveitar uma promoção.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Slideup</a></td>
    <td>Mensagens que deslizam para exibição em um local designado sem bloquear o restante da tela.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discreto - ocupa o mínimo de espaço na tela. Use para alertar os usuários sobre pequenos trechos de informações, como novos recursos, anúncios, uso de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Tipos de mensagens avançadas

Essas mensagens no aplicativo podem ser personalizadas de acordo com suas necessidades.

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensagem</th>
    <th>Tipo Descrição</th>
    <th>Layouts disponíveis</th>
    <th>Requisitos</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Mensagem HTML personalizada</a></td>
    <td>Mensagens personalizadas que funcionam conforme definido em seu código personalizado (HTML, CSS e/ou JavaScript).</td>
    <td>N/A</td>
    <td>Deve definir <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> como <code>true</code> para que sua mensagem in-app funcione.</td>
    <td>Essa é uma boa opção se você quiser todas as vantagens dos IAMs, mas precisar de funcionalidade adicional ou para que a aparência permaneça "na marca". Você pode alterar cada pequeno detalhe da mensagem: fonte, cor, forma, tamanho, botões, etc. <br><br>Exemplos de casos de uso incluem a solicitação de feedback do aplicativo aos usuários, formulários de captura de e-mail ou mensagens paginadas</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulário de captura de e-mail</a></td>
    <td>Normalmente usado para capturar o e-mail do visualizador.</td>
    <td>N/A</td>
    <td>Deve definir <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> como <code>true</code> para que sua mensagem in-app funcione.</td>
    <td>Ao solicitar que os usuários enviem seus endereços de e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Modal da Web com CSS</a></td>
    <td>Mensagens modais para a Web com CSS personalizável.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>O Web Modal com CSS é exclusivo do Web SDK e só pode ser usado após a seleção de <b>navegadores da Web</b>.</td>
    <td>Quando você quiser fazer upload ou escrever CSS personalizado para criar mensagens bonitas e com estilo personalizado. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Se o Braze detectar que você não tem um botão de fechar ou dispensar incluído em seu código, solicitaremos que você adicione um. Para sua conveniência, fornecemos um snippet que pode ser copiado e colado em seu código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Etapa 4: Escreva sua mensagem no aplicativo

A guia **Compose** permite que você edite todos os aspectos do conteúdo e do comportamento da sua mensagem.

Exemplo de mensagem no aplicativo de uma marca para dar as boas-vindas a novos clientes e solicitar que eles criem um perfil de usuário.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

O conteúdo da guia **Compose** varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

### Idioma

Selecione **Add Languages (Adicionar idiomas** ) e selecione os idiomas desejados na lista fornecida. Isso inserirá [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) em sua mensagem. Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto onde ele pertence no Liquid. Veja nossa [lista completa de idiomas disponíveis]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Imagem

Dependendo do tipo de mensagem, você pode fazer **upload de imagem**, **escolher um emblema** ou usar **Font Awesome**. Para carregar uma imagem, clique em **Add Image (Adicionar imagem** ) ou forneça o URL da imagem. Clicar em **Add Image (Adicionar imagem** ) abre a **Media Library (Biblioteca de mídia**), onde é possível selecionar uma imagem carregada anteriormente ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos. Certifique-se de verificar quais são eles antes de encomendar ou criar uma imagem do zero!

### Cabeçalho e corpo

Escreva o que você quiser! Inclua uma cópia totalmente personalizada (geralmente com recursos de HTML personalizados) com as opções de incluir [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) e outros tipos de personalização. Quanto mais rápido você conseguir transmitir sua mensagem e fazer com que seu cliente clique, melhor! Recomendamos que os cabeçalhos e o conteúdo da mensagem sejam claros e concisos.

Alguns tipos de mensagem não precisam de cabeçalhos e, portanto, não os solicitam.

#### Dicas 

##### Geração de cópia de IA

Precisa de ajuda para criar um texto incrível? Tente usar o [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará um texto de marketing semelhante ao humano para ser usado em suas mensagens.

Abra o botão AI Copywriter, localizado no campo Message (Mensagem) do compositor de mensagens no aplicativo.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Criação de mensagens da direita para a esquerda

Precisa de ajuda para criar mensagens da direita para a esquerda em idiomas como o árabe e o hebraico? Consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) para conhecer as práticas recomendadas.

### Texto do botão {#buttons}

Quando disponível para o seu tipo de mensagem, você pode fazer com que até dois botões apareçam sob o corpo do texto. Você pode criar e editar o texto e a cor do botão personalizado. Você também pode adicionar o link dos Termos de Serviço nos formulários de captura de e-mail.

Se você optar por usar apenas um botão, ele será ajustado automaticamente para ocupar o espaço disponível na parte inferior da mensagem, em vez de deixar espaço para um botão adicional.

#### Escolha de um botão principal

Se você decidir formatar esses botões com suas próprias cores, recomendamos que use o Botão 2 para obter o resultado desejado.

Em outras palavras, se quiser que o usuário clique mais em um botão do que no outro, certifique-se de que ele esteja à direita. O botão direito geralmente apresenta maior potencial de ser clicado, especialmente se tiver uma cor contrastante ou que se destaque do restante da mensagem. Isso só é enfatizado quando o botão à esquerda combina mais visualmente com a mensagem.

Botões primários e secundários em uma mensagem no aplicativo]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamento no clique {#button-actions}

Quando o cliente clica em um botão em sua mensagem in-app, as seguintes ações estão disponíveis. 

| Ação | Descrição |
|---|---|
| Redirecionar para URL da Web | Abra uma página da Web não nativa. |
| [Deep Link no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Faça um deep link para uma tela existente em seu aplicativo. |
| Fechar mensagem | Fecha a mensagem ativa no momento. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para acionar. Pode ser usado para exibir outra mensagem no aplicativo ou acionar mensagens adicionais. |
| Atributo personalizado de registro | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) a ser definido para o usuário atual. |
| Solicitar permissão de envio | Mostra a permissão de envio nativa. Leia mais sobre a [preparação]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para o push, bem como sobre [as práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) para preparar os usuários para o push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Observação: as opções __Request Push Permission__, __Log Custom Event__ e __Log Custom Attribute__ exigem as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Opções de dispositivos iOS

Se desejar, você pode restringir sua mensagem no aplicativo para enviar apenas para dispositivos iOS. Para fazer isso, clique em **Alterar** e selecione **Enviar somente para dispositivos iOS**.

### Fechamento de mensagem

Escolha entre as seguintes opções:
 
- **Dispensar automaticamente:** Selecione quantos segundos a mensagem permanecerá na tela.
- **Aguarde o deslizamento ou o toque do usuário:** Requer uma opção de demissão ou encerramento.

### Posição de deslizamento para cima

Essa configuração só se aplica ao tipo de mensagem Slideup. Escolha entre fazer com que o slideup apareça **na parte inferior da tela do aplicativo** ou **na parte superior da tela do aplicativo**.

### HTML e ativos

Essa configuração só se aplica ao tipo de mensagem Código personalizado. Copie e cole o HTML no espaço disponível e carregue seus ativos usando um arquivo ZIP.

### Espaço reservado para entrada de captura de e-mail

Essa configuração só se aplica ao tipo de mensagem do formulário de captura de e-mail. Digite a cópia personalizada que aparecerá como texto de espaço reservado para o campo de entrada de e-mail. O padrão é "Enter your email address" (Digite seu endereço de e-mail).

## Etapa 5: Estilize sua mensagem no aplicativo

A guia **Style** permite que você ajuste todos os aspectos visuais da sua mensagem. Carregue uma imagem ou crachá ou escolha um ícone de crachá predefinido. Altere as cores do texto do cabeçalho e do corpo, dos botões e do plano de fundo selecionando em uma paleta ou inserindo um código hexadecimal, RGB ou HSB.

O conteúdo da guia **Style (Estilo** ) varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

| Formatação | Entrada | Descrição |
|---|---|---|
|[Perfil de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Aplique a partir da galeria de modelos de mensagens no aplicativo. | Selecione **Apply Template (Aplicar modelo** ) e escolha na galeria. Em seguida, selecione **Salvar**. |
|Alinhamento de texto | Esquerda, Centro ou Direita.  | Disponível apenas para versões mais recentes do Braze SDK. |
|Cabeçalho | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor.  |
|Texto | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
|Botões | Código de cores HEX. | Suas cores HEX desejadas serão exibidas. Você também poderá escolher a opacidade das cores. Você pode escolher cores para: o plano de fundo do botão Fechar da mensagem, bem como o plano de fundo, o texto e a borda de cada botão. |
| Borda do botão | Código de cores HEX. | Novo! Isso permitirá que você defina os botões primário e secundário separados um do outro. Sugerimos que os botões sejam contornados com cores contrastantes. |
|Cor de fundo | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Esse é o plano de fundo de toda a mensagem e será exibido claramente atrás do corpo do texto. |
|Sobreposição de tela | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Disponível apenas para versões mais recentes do Braze SDK. Essa é a moldura que envolve toda a mensagem. |
|Chevron ou outra opção de mensagem de fechamento | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sempre visualize [e teste]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sua mensagem antes de enviá-la.

{% alert important %}
Alguns tipos de mensagens in-app não têm a opção de estilização além do upload de HTML (ou CSS ou JavaScript) e ativos personalizados usando um arquivo ZIP. [O Web Modal com CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) permite que você carregue ou escreva CSS personalizado para criar mensagens bonitas e com estilo totalmente personalizado.
{% endalert %}

## Etapa 6: Configurar definições adicionais (opcional)

### Pares de valores-chave

Você pode adicionar [pares de valores-chave]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para enviar campos personalizados adicionais aos dispositivos dos usuários.

## Etapa 7: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Crie o restante da sua campanha; consulte as seções a seguir para obter mais orientações sobre a melhor forma de usar nossas ferramentas para criar mensagens in-app.

#### Escolha um acionador

Selecione a ação da qual deseja disparar sua mensagem, bem como os horários de início e término de sua campanha ou Canvas.

{% alert important %}
Observe que, se você pretende acionar sua mensagem in-app com base em um evento personalizado, esse evento personalizado deve ser enviado usando o SDK.
{% endalert %}

Campanha baseada em ação com a ação de acionamento definida como "Iniciar sessão".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

A entrega de mensagens in-app é totalmente baseada nos seguintes acionadores de ação:

- Fazer uma compra
- Abrir o aplicativo/página da Web
- Realização de um evento personalizado (só funciona com eventos enviados usando o SDK)
- Abrir uma mensagem push específica
- Programe automaticamente campanhas para serem enviadas em um determinado horário, de acordo com o horário local de cada um dos seus usuários.
- As mensagens também podem ser configuradas para serem repetidas diariamente, semanalmente (opcionalmente em dias específicos) ou mensalmente.

Uma data e hora de início devem ser selecionadas; no entanto, uma data de término é opcional. Uma data final impedirá que essa mensagem in-app específica seja exibida nos dispositivos após a data/hora especificada.

Consulte a documentação do desenvolvedor para saber como [acionar eventos no lado do servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) e [enviar mensagens locais no aplicativo]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Acionamento on-line versus off-line

As mensagens no aplicativo funcionam enviando a mensagem e os acionadores para o dispositivo do usuário. Depois que as mensagens in-app estão em um dispositivo, elas aguardam para serem exibidas até que a condição de acionamento seja atendida. Se as mensagens in-app já estiverem armazenadas em cache no dispositivo do usuário, você poderá até mesmo acionar mensagens in-app off-line sem conexão com o Braze (por exemplo, no modo Avião).

{% alert important %}
Depois que uma mensagem in-app for interrompida, alguns usuários poderão continuar a ver a mensagem se tiverem iniciado uma sessão antes de a mensagem ser interrompida e, posteriormente, executarem o evento de disparo. Esses usuários serão contados como uma impressão única mesmo depois que a campanha for interrompida.
{% endalert %}

#### Escolha uma prioridade

Por fim, depois de selecionar a ação a partir da qual a mensagem in-app será acionada, você também deve definir uma prioridade. Se duas mensagens forem acionadas a partir da mesma ação, as mensagens de alta prioridade serão programadas para aparecer nos dispositivos dos usuários antes das mensagens com prioridades mais baixas. 

Você pode escolher entre as seguintes prioridades de mensagem:

- Baixa prioridade (exibida após outras mensagens)
- Prioridade média
- Alta prioridade (exibida antes de outras mensagens)

As opções alta, média e baixa para as prioridades de mensagens acionadas são compartimentos e, portanto, várias mensagens podem ter a mesma prioridade selecionada. Para definir prioridades dentro desses compartimentos, clique em **Set Exact Priority (Definir prioridade exata**), e você poderá arrastar e soltar campanhas para ordená-las com a prioridade correta.

\![Um exemplo de como a prioridade é definida para uma campanha de mensagem in-app e o Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Escolha os usuários a serem alvos

Em seguida, você precisa [segmentar os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

{% alert note %}
Se houver um atraso na etapa da mensagem in-app, a associação ao segmento será avaliada após o atraso. Se o usuário for elegível, a mensagem in-app será sincronizada na próxima sessão disponível.
{% endalert %}

##### Reavaliar a elegibilidade da campanha e o Liquid

Em alguns cenários, você pode querer reavaliar a elegibilidade de um usuário quando ele aciona uma mensagem in-app para ser exibida. Os exemplos incluem campanhas que têm como alvo um atributo personalizado que muda com frequência ou mensagens que devem refletir qualquer mudança de perfil de última hora.

Caixa de seleção para "Reavaliar a elegibilidade da campanha antes de exibi-la" selecionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Ao selecionar **Reavaliar a elegibilidade da campanha antes de** exibi-la, será feita uma solicitação adicional ao Braze para confirmar se o usuário ainda está qualificado para essa mensagem antes do envio. Além disso, todas as variáveis [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) serão modeladas nesse momento, antes que a mensagem seja exibida.

Isso impede que mensagens in-app sejam enviadas a usuários em campanhas expiradas ou arquivadas. Se você não reavaliar a elegibilidade de um usuário, ele receberá a mensagem in-app mesmo depois que a campanha expirar ou for arquivada, porque a mensagem está no seu SDK e aguardando que os usuários a acionem.

{% alert note %}
A ativação dessa opção resultará em um pequeno atraso ( (< 100ms) entre o momento em que o usuário aciona uma mensagem in-app e o momento em que a mensagem é exibida, devido à solicitação adicional de elegibilidade e modelagem.
<br><br>
Não use essa opção para mensagens que possam ser acionadas enquanto o usuário estiver off-line ou quando a elegibilidade e a reavaliação do Liquid não forem necessárias.
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}
{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canvas. Para obter mais detalhes sobre como criar o restante do seu Canvas, implementar testes multivariados e Intelligent Selection e muito mais, consulte a etapa [Criar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.

Para obter informações sobre as opções de mensagens in-app específicas do Canvas, consulte [Mensagens in-app no Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 8: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canvas, revise seus detalhes, [teste-a]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) e envie-a!

Em seguida, confira [os relatórios de mensagens in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para saber como acessar os resultados de suas campanhas de mensagens.

## Coisas para saber

### Limites de campanha de mensagens in-app ativas

A Braze valoriza a confiabilidade e a velocidade. Da mesma forma que sugerimos que você envie ao Braze apenas os dados necessários, também recomendamos desativar todas as campanhas que não estejam mais agregando valor à sua marca.

O processamento de campanhas de mensagens in-app baseadas em ações que ainda estão em um estado ativo, mas que não estão mais enviando mensagens ou não são mais necessárias, diminui o desempenho geral dos serviços Braze para você e outros clientes. Esse tempo extra necessário para processar esse grande número de campanhas ociosas significa que qualquer mensagem no aplicativo levará mais tempo para aparecer nos dispositivos do usuário final, o que afeta a experiência do usuário final.

{% alert important %}
Você pode ter até 200 campanhas de mensagens in-app ativas e baseadas em ações por espaço de trabalho para otimizar a velocidade de entrega de mensagens e evitar tempos limite. Isso não se aplica a Canvases.
{% endalert %}

A contagem de 200 inclui campanhas ativas de mensagens in-app que ainda não atingiram o horário de término e aquelas que não têm horário de término. Campanhas ativas de mensagens in-app que tenham ultrapassado seus prazos finais não serão contadas. O cliente Braze médio tem um total de 26 campanhas ativas ao mesmo tempo - portanto, é improvável que essa limitação afete você.


