---
nav_title: Crie uma mensagem no app
article_title: Criar uma mensagem no app
page_order: 1
description: "Este artigo de referência aborda como criar uma mensagem no app usando a plataforma Braze por meio de campanhas ou do Canva."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Crie uma mensagem no app

> Você pode criar uma mensagem no app ou no navegador usando a plataforma Braze por meio de campanhas, Canvas ou como uma campanha API. É altamente recomendável planejar suas mensagens e preparar todos os materiais com antecedência usando nosso prático [guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Etapa 1: Escolha onde construir sua mensagem {#create-new-campaign-in-app}

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? Campanhas são melhores para campanhas de envio de mensagens únicas e direcionadas, enquanto canvases são melhores para jornadas de usuários em múltiplas etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Mensagem no app**. Observe que as mensagens no app não estão disponíveis em campanhas de vários canais.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário. Observe que as etapas que contêm mensagens no app não podem ser baseadas em ações.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções do público serão conferidas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de envio de mensagens que gostaria de associar à sua mensagem.

{% alert important %}
Não é possível ter várias variantes de mensagens no app em uma única etapa.
{% endalert %}

Você pode encontrar mais informações específicas do Canvas em [Mensagens no app do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 2: Especificar plataformas de entrega

Comece escolhendo quais plataformas devem receber a mensagem. Use essa seleção para limitar a entrega de uma campanha a um conjunto específico de aplicativos. Por exemplo, você pode escolher **navegadores da Web** para uma mensagem no navegador incentivando os usuários a baixar seu aplicativo móvel para garantir que eles não recebam a mensagem depois de já terem baixado o aplicativo. Como as seleções de plataforma são específicas para cada variante, você pode tentar testar o engajamento com mensagens por plataforma.

| Plataforma                        | Envio de mensagens        |
|---------------------------------|-------------------------|
| Apps móveis                     | iOS & SDKs Android      |
| Navegadores                    | SDK da Web                 |
| Ambos os aplicativos móveis & navegadores da web | iOS, Android & SDKs da web |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Especifique seus tipos de mensagens

Depois de selecionar uma plataforma de envio, navegue pelos tipos de mensagens, layouts e outras opções associadas a ela. Saiba mais sobre o comportamento esperado e a aparência de cada uma dessas mensagens em nossa página [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) ou clicando nos tipos de mensagem vinculados nas tabelas a seguir.

Ao decidir qual tipo de mensagem usar, considere quanto espaço sua mensagem ocupará e quão disruptiva ela pode ser para a experiência do usuário.

- **Slideup** mensagens são as menos intrusivas, aparecendo sutilmente sem bloquear o conteúdo.
- **Modal** mensagens ficam no meio—suficientemente proeminentes para chamar a atenção sem dominar completamente a tela.
- **Fullscreen** mensagens são as mais chamativas e melhores para anúncios ou promoções críticas.

Quanto mais complexo for seu conteúdo, mais espaço você precisará—e mais provável será que sua mensagem interrompa o fluxo do usuário.

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

![Um exemplo de mensagem no app de uma marca para dar as boas-vindas a novos clientes e solicitar que eles criem um perfil de usuário.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

O conteúdo da guia **Compose (Criar)** varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

### Idioma

Selecione **Add Languages (Adicionar idiomas)** e selecione os idiomas desejados na lista fornecida. Isso inserirá o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) em sua mensagem. Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que possa preencher o texto onde ele pertence no Liquid. Veja nossa [lista completa de idiomas disponíveis]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Imagem

Dependendo do tipo de mensagem, você pode fazer **upload de imagem**, **escolher um emblema** ou usar **Font Awesome**. Para fazer upload de uma imagem, selecione **Adicionar Imagem** ou forneça uma URL de imagem. Selecionar **Adicionar Imagem** abre a **Biblioteca de Mídia**, onde você pode selecionar uma imagem previamente carregada ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos—certifique-se de verificar quais são antes de encomendar ou criar uma imagem do zero.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Cabeçalho e corpo

Escreva o que você quiser! Inclua uma cópia totalmente personalizada (geralmente com recursos HTML personalizados) com as opções de incluir [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) e outros tipos de personalização. Quanto mais rápido você conseguir transmitir sua mensagem e fazer com que seu cliente clique, melhor! Recomendamos que os cabeçalhos e o conteúdo das mensagens sejam claros e concisos.

Alguns tipos de mensagens não precisam de cabeçalhos e, portanto, não os solicitam.

#### Dicas 

##### Geração de cópia de IA

Precisa de ajuda para criar um texto incrível? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Botão de Lançar IA Copywriter, localizado no campo de Mensagem do compositor de mensagens no app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Criação de mensagens da direita para a esquerda

Precisa de ajuda para criar mensagens da direita para a esquerda em idiomas como árabe e hebraico? Consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) para conhecer as práticas recomendadas.

### Texto do botão {#buttons}

Quando disponível para o seu tipo de mensagem, você pode fazer com que até dois botões apareçam sob o corpo do texto. Você pode criar e editar o texto e a cor do botão personalizado. Você também pode adicionar o link dos Termos de Serviço nos formulários de captura de e-mail.

Se você optar por usar apenas um botão, ele se ajustará automaticamente para ocupar o espaço disponível na parte inferior da mensagem, em vez de deixar espaço para um botão adicional.

#### Escolha de um botão principal

Se você decidir formatar esses botões com suas próprias cores, recomendamos que use o Botão 2 para obter o resultado desejado.

Em outras palavras, se quiser que o usuário clique mais em um botão do que no outro, certifique-se de que ele esteja à direita. O botão direito geralmente apresenta melhor potencial para ser clicado, especialmente se tiver uma cor contrastante ou que se destaque do restante da mensagem. Isso só é enfatizado quando o botão à esquerda combina mais visualmente com a mensagem.

![Botões primário e secundário em uma mensagem no app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamento ao clicar {#button-actions}

Quando o cliente clica em um botão em sua mensagem no app, as seguintes ações estão disponíveis. 

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abra uma página da Web não nativa. |
| [Deep linking no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Deep linking em uma tela existente em seu app. |
| Fechar mensagem | Fecha a mensagem ativa no momento. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para disparar. Pode ser usado para exibir outra mensagem no app ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) a ser definido para o usuário atual. |
| Solicitar permissão para push | Mostra a permissão de push nativa. Leia mais sobre o [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), bem como sobre [as práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) para preparar os usuários para o push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nota: as opções __Request Push Permission__, __Log Custom Event__ e __Log Custom Attribute__ exigem as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Opções de dispositivos iOS

Se desejar, você pode restringir sua mensagem no app para enviar apenas para dispositivos iOS. Para fazer isso, clique em **Alterar** e selecione **Enviar somente para dispositivos iOS**.

### Fechamento da mensagem

Escolha entre as seguintes opções:
 
- **Dispensar automaticamente:** Selecione quantos segundos a mensagem permanecerá na tela.
- **Aguarde o deslizamento ou o toque do usuário:** Requer uma opção de demissão ou encerramento.

### Posição de deslizamento para cima

Essa configuração só se aplica ao tipo de mensagem Slideup. Escolha entre fazer com que o slideup apareça **na parte inferior da tela do app** ou **na parte superior da tela do app**.

### HTML e ativos

Essa configuração se aplica apenas ao tipo de mensagem Código personalizado. Copie e cole o HTML no espaço disponível e faça upload de seus ativos usando um arquivo ZIP.

### Espaço reservado para entrada de captura de e-mail

Essa configuração só se aplica ao tipo de mensagem do formulário de captura de e-mail. Digite a cópia personalizada que aparecerá como texto de espaço reservado para o campo de entrada de e-mail. O padrão é "Digite seu endereço de e-mail".

## Etapa 5: Estilize sua mensagem no app

A guia **Style (Estilo** ) permite ajustar todos os aspectos visuais da sua mensagem. Faça upload de uma imagem ou crachá ou escolha um ícone de crachá predefinido. Altere as cores do texto do cabeçalho e do corpo, dos botões e do plano de fundo selecionando em uma paleta ou inserindo um código hexadecimal, RGB ou HSB.

O conteúdo da guia **Style (Estilo** ) varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

| Formatação | Entrada | Descrição |
|---|---|---|
|[Perfil de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Aplique a partir da galeria de modelos de mensagens no app. | Selecione **Aplicar Modelo** e escolha na galeria. Em seguida, selecione **Salvar**. |
|Alinhamento de texto | Esquerda, Centro ou Direita.  | Disponível apenas para as versões mais recentes do SDK da Braze. |
|Cabeçalho | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor.  |
|Texto | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
|Botões | Código de cores HEX. | As cores HEX desejadas serão exibidas. Você também poderá escolher a opacidade das cores. Você pode escolher cores para: o plano de fundo do botão Fechar da mensagem, bem como o plano de fundo, o texto e a borda de cada botão. |
| Borda do botão | Código de cores HEX. | Novo! Isso permitirá que você defina os botões primário e secundário separados um do outro. Sugerimos que os botões sejam contornados com cores contrastantes. |
|Cor de fundo | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Esse é o plano de fundo de toda a mensagem e será exibido claramente atrás do corpo do texto. |
|Sobreposição da tela | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Disponível apenas para as versões mais recentes do SDK da Braze. Essa é a moldura que envolve toda a mensagem. |
|Chevron ou outra opção de mensagem de fechamento | Código de cores HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sempre [faça uma prévia e teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) sua mensagem antes de enviá-la.

{% alert important %}
Alguns tipos de mensagens no app não têm a opção de estilização além de fazer upload de HTML personalizado (ou CSS ou JavaScript) e ativos usando um arquivo ZIP. O [Web Modal com CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) permite que você faça upload ou escreva CSS personalizado para criar mensagens bonitas e com estilo personalizado.
{% endalert %}

## Etapa 6: Configurar definições adicionais (opcional)

### Pares de valores chave

Você pode adicionar [pares chave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para enviar campos personalizados extras para os dispositivos dos usuários.

## Etapa 7: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campaign %}

Crie o restante de sua campanha; consulte as seções a seguir para obter mais orientações sobre a melhor forma de usar nossas ferramentas para criar mensagens no app.

#### Escolha um disparador

Selecione a ação que deseja disparar sua mensagem, bem como os horários de início e término de sua campanha ou do Canva.

{% alert important %}
Note que, se você pretende disparar sua mensagem no app com base em um evento personalizado, esse evento personalizado deve ser enviado usando o SDK.
{% endalert %}

![Campanha baseada em ação com a ação-gatilho definida como "Iniciar Sessão".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

A entrega de mensagens no app é totalmente baseada nos seguintes disparos de ação:

- Fazer uma compra
- Abrir o app/página da Web
- Realização de um evento personalizado (só funciona com eventos enviados usando o SDK)
- Abrir uma mensagem push específica
- Programe automaticamente o envio de campanhas em um determinado horário, de acordo com o fuso local de cada um de seus usuários.
- O envio de mensagens também pode ser configurado para ser recorrente em uma base diária, semanal (opcionalmente em dias específicos) ou mensal.

Uma data e hora de início devem ser selecionadas; no entanto, uma data de término é opcional. Uma data final impedirá que essa mensagem no app específica seja exibida nos dispositivos após a data/hora especificada.

Consulte nossa documentação para desenvolvedores sobre [disparo de eventos no lado do servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) e [envio local de mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Disparos on-line e off-line

As mensagens no app funcionam enviando a mensagem e os disparos para o dispositivo do usuário. Depois que as mensagens no app estiverem em um dispositivo, ele aguardará a exibição até que a condição de disparo seja atendida. Se as mensagens no app já estiverem armazenadas em cache no dispositivo do usuário, você poderá até mesmo disparar mensagens no app off-line sem conexão com o Braze (por exemplo, no modo Avião).

{% alert important %}
Depois que uma mensagem no app tiver sido interrompida, alguns usuários poderão continuar a ver a mensagem se tiverem iniciado uma sessão antes de a mensagem ser interrompida e, posteriormente, executarem o evento de gatilho. Esses usuários serão contados como uma impressão única, mesmo depois que a campanha for interrompida.
{% endalert %}

#### Escolha uma prioridade

Por fim, depois de selecionar a ação em que a mensagem no app será disparada, você também deverá definir uma prioridade. Se duas mensagens forem disparadas a partir da mesma ação, as mensagens de alta prioridade serão programadas para aparecer nos dispositivos dos usuários antes das mensagens com prioridades mais baixas. 

Você pode escolher entre as seguintes prioridades de mensagens:

- Alta prioridade (mostrado antes de outras mensagens)
- Prioridade média (padrão)
- Baixa prioridade (mostrado depois de outras mensagens)

As opções alta, média e baixa para prioridades de mensagens acionadas são categorias, e assim, várias mensagens podem ter a mesma prioridade selecionada. Quando várias mensagens compartilham a mesma prioridade, a mensagem criada ou atribuída mais recentemente tem precedência e é exibida primeiro:

- **Bucket de prioridade padrão:** Quando duas campanhas compartilham o mesmo gatilho e usam a prioridade padrão (média), a campanha que foi criada por último recebe o gatilho.
- **Bucket de prioridade específica:** Quando várias campanhas compartilham o mesmo gatilho e são atribuídas a um bucket de prioridade específica, a campanha mais recentemente atribuída a esse bucket recebe o gatilho.

Para definir prioridades dentro desses buckets, clique em **Definir Prioridade Exata**, e você pode arrastar e soltar campanhas para ordená-las com a prioridade correta.

![Um exemplo de como a prioridade é definida para uma campanha de mensagem no app e Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Escolha os usuários a serem direcionados

Em seguida, você deve [segmentar usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você recebe automaticamente uma visão geral de como é a população aproximada desse segmento. Tenha em mente que a associação exata ao segmento é sempre calculada antes que a mensagem seja enviada.

{% alert note %}
Se houver uma postergação na etapa da mensagem no app, a associação ao segmento será avaliada após o atraso. Se o usuário for elegível, a mensagem no app será sincronizada na próxima sessão disponível.
{% endalert %}

##### Reavaliar a elegibilidade da campanha e o Liquid

Em alguns cenários, talvez seja necessário reavaliar a elegibilidade de um usuário quando ele dispara uma mensagem no app para ser exibida. Os exemplos incluem campanhas que direcionam um atributo personalizado que muda com frequência ou mensagens que devem refletir qualquer alteração de perfil de última hora.

![Caixa de seleção para "Reavaliar a elegibilidade da campanha antes de exibir" selecionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Ao selecionar **Reavaliar a elegibilidade da campanha antes de** exibi-la, será feita uma solicitação adicional ao Braze para confirmar que o usuário ainda é elegível para essa mensagem antes do envio. Além disso, todas as variáveis [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) serão modeladas nesse momento, antes que a mensagem seja exibida.

Isso evita que mensagens no app sejam enviadas a usuários em campanhas expiradas ou arquivadas. Se você não reavaliar a elegibilidade de um usuário, ele receberá a mensagem no app mesmo depois que a campanha expirar ou for arquivada, porque a mensagem está no seu SDK e aguardando que os usuários a disparem.

{% alert note %}
Ativar esta opção resultará em um pequeno atraso (< 100ms) entre quando um usuário dispara uma mensagem no app e quando a mensagem é exibida devido à solicitação de elegibilidade e modelagem adicionada.
<br><br>
Não use essa opção para mensagens que possam ser disparadas enquanto o usuário estiver off-line ou quando a elegibilidade e a reavaliação do Liquid não forem necessárias.
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}
{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nossa documentação do Canvas.

Para obter informações sobre as opções de envio de mensagens no aplicativo específicas do Canva, consulte [Mensagens no aplicativo no Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 8: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canva, revise seus detalhes, [teste-a]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) e envie-a!

Em seguida, confira [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para saber como acessar os resultados de suas campanhas de mensagens.

## Coisas para saber

### Limites ativos da campanha de mensagens no app

A Braze valoriza a confiabilidade e a velocidade. Sugerimos que você envie apenas os dados que precisa para a Braze e desative quaisquer campanhas que não agreguem mais valor à sua marca.

O processamento de campanhas de mensagens no app baseadas em ações que ainda estão em um estado ativo, mas que não estão mais enviando mensagens ou que não são mais necessárias, diminui a performance geral dos serviços Braze para você e para outros clientes. Esse tempo extra necessário para processar esse grande número de campanhas sem atividades significa que qualquer mensagem no app levará mais tempo para aparecer nos dispositivos do usuário final, o que afeta a experiência do usuário final.

{% alert important %}
Você pode ter até 200 campanhas de mensagens no app ativas e baseadas em ação por espaço de trabalho para otimizar a velocidade de entrega de mensagens e evitar tempos limite. Isso não se aplica às telas.
{% endalert %}

A contagem de 200 inclui campanhas ativas de mensagens no app que ainda não atingiram o horário de término e aquelas que não têm horário de término. Campanhas ativas de mensagens no app que tenham ultrapassado o horário de término não serão contadas. O cliente Braze médio tem um total de 26 campanhas ativas ao mesmo tempo, portanto, é improvável que essa limitação afete você.

### Avaliação de entrega no horário local

Quando uma campanha de mensagem no app é agendada usando o fuso horário local do usuário, a avaliação do horário de início e término da campanha é feita no próprio dispositivo.

Campanhas de mensagem no app são normalmente enviadas para o dispositivo do usuário quando a sessão do app começa ou é atualizada. Nesse momento:

1. O SDK avalia se o usuário se qualifica para alguma mensagem no app baseada em gatilho.
2. O dispositivo verifica se o evento de gatilho do usuário ocorreu dentro do horário de início e término da campanha (conforme definido pelo fuso horário local do usuário).
3. Se ambas as condições forem atendidas, a mensagem no app é elegível para exibição.

#### Considerações

- Se um usuário dispara um evento (como um toque em botão) logo após a mensagem no app ser entregue, a mensagem pode não aparecer até a próxima atualização da sessão—supondo que todos os critérios de elegibilidade ainda sejam atendidos.
- Semelhante a outros tipos de canal, as campanhas de mensagem no app devem ser lançadas idealmente 24 a 48 horas antes. Esse intervalo dá aos usuários tempo suficiente para atender aos requisitos e iniciar uma sessão para que a mensagem seja avaliada e exibida.