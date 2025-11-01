---
nav_title: Criação de um cartão de conteúdo
article_title: Criação de um cartão de conteúdo
page_order: 0
description: "Este artigo de referência aborda como criar, compor, configurar e enviar Content Cards usando campanhas e Canvases do Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Criação de um cartão de conteúdo

> Este artigo aborda como criar um Content Card no Braze quando você cria campanhas e Canvases. Aqui, vamos orientá-lo na escolha de um tipo de mensagem, na composição do cartão e na programação da entrega da mensagem.

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada com uma campanha ou com um Canvas? As campanhas são melhores para campanhas de mensagens únicas e simples (como informar os usuários sobre um novo produto com uma única mensagem), enquanto os Canvases são melhores para jornadas de usuários em várias etapas (como enviar sugestões de produtos personalizados com base no comportamento do usuário ao longo do tempo).

{% tabs %}
{% tab Campaign %}

1. Vá para **Messaging** > **Campaigns** ( **Mensagens** > **Campanhas** ) e selecione **Create Campaign (Criar campanha**).
2. Selecione **Content Cards** ou, para campanhas direcionadas a vários canais, selecione **Multichannel**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar pelas tags relevantes.
5. Adicione e nomeie quantas variantes você quiser para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre variantes, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar outras variantes. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa de Mensagem no construtor do Canvas. Dê um nome claro e significativo à sua etapa.
3. Selecione **Content Cards** como seu canal de mensagens.
4. Escolha quando o Braze calcula a elegibilidade e a personalização do público-alvo para o Content Card. Isso pode ser feito na entrada da etapa ou na primeira impressão (recomendado). As etapas que contêm Content Cards podem ser programadas ou baseadas em ações.
5. Escolha se deseja remover os Content Cards quando os usuários concluírem uma compra ou realizarem um evento personalizado.
6. Defina uma expiração para o Content Card (tempo no feed). Isso pode ser feito após um período de tempo ou em um horário específico.
7. Filtre seu público-alvo, ou os destinatários, para essa etapa, conforme necessário, nas **Configurações de entrega**. Você pode refinar ainda mais seu público especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após o atraso, no momento em que as mensagens forem enviadas.
8. Escolha qualquer outro canal de mensagens que você queira associar à sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Especifique seus tipos de mensagem

Selecione um dos três tipos essenciais de Content Card: **Clássico**, **Imagem com legenda** e **Somente imagem**. 

Para saber mais sobre o comportamento esperado e a aparência de cada tipo, consulte [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) ou confira os links na tabela a seguir. Esses tipos de Content Card são aceitos tanto por aplicativos móveis quanto por aplicativos da Web.

| Tipo de mensagem | Exemplo | Descrição |
|---|---|---|
|[Clássico]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| Um cartão de conteúdo clássico com um pequeno ícone e texto para incentivar a reserva de uma aula de ginástica.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |O cartão clássico tem um layout simples com um título em negrito, texto da mensagem e uma imagem opcional que fica à esquerda do título e do texto. É melhor usar uma imagem ou ícone quadrado com o cartão clássico. |
|[Imagem legendada]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| \![Um cartão de conteúdo legendado com a imagem de um halterofilista e texto para incentivar a reserva de uma aula de ginástica.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | O cartão com imagem legendada mostra seu conteúdo com um texto e uma imagem que chama a atenção. |
|[Somente imagem]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| \![Um cartão de conteúdo somente de imagem com apenas texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | O Image Only Card chama a atenção com espaço para imagens, GIFs e outros conteúdos criativos não textuais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 3: Escreva um cartão de conteúdo

Você pode editar todos os aspectos do conteúdo e do comportamento da sua mensagem na guia **Compose (Compor** ) do editor de mensagens.

Detalhes do cartão de conteúdo de amostra na guia Compor do editor de mensagens.]({% image_buster /assets/img/content_card_compose.png %})

O conteúdo aqui varia de acordo com o **tipo de cartão** escolhido na etapa anterior, mas pode incluir qualquer uma das opções a seguir:

#### Idioma

Selecione **Add Languages (Adicionar idiomas** ) para adicionar os idiomas desejados da lista fornecida. Isso inserirá [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) em sua mensagem. Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto onde ele pertence no Liquid. Para ver a lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

\![Uma janela com inglês, espanhol e francês selecionados como idiomas e título, descrição e texto do link selecionados como campos a serem internacionalizados.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviços as processam. Para obter práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e mensagem

Escreva o que você quiser. Não há limites, mas quanto mais rápido você conseguir transmitir sua mensagem e fazer com que seu cliente clique, melhor! Recomendamos títulos e conteúdo de mensagens claros e concisos. Observe que esses campos não são fornecidos para cartões Image Only.

#### Imagem

Adicione uma imagem ao seu Content Card selecionando **Add Image (Adicionar imagem** ) ou fornecendo o URL da imagem. A seleção de **Add Image (Adicionar imagem** ) abre a **Media Library (Biblioteca de mídia**), onde é possível selecionar uma imagem carregada anteriormente ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos, portanto, certifique-se de verificar quais são eles antes de encomendar ou criar uma imagem do zero! Lembre-se de que os campos de mensagem do Content Card são limitados a 2 KB de tamanho total.

#### Fixar no topo

Um cartão fixado será exibido na parte superior do feed de um usuário e não poderá ser descartado por ele. Se mais de um cartão no feed de um usuário for fixado, os cartões fixados serão exibidos em ordem cronológica. Após o envio de um cartão, não é possível atualizar retroativamente a opção fixada. A alteração dessa opção após o envio de uma campanha afetará apenas os envios futuros.

Visualização lado a lado do Content Card no Braze para celular e Web com a opção "Fixar este cartão na parte superior do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamento no clique

Quando o cliente clica em um link apresentado no cartão, esse link pode levá-lo mais profundamente em seu aplicativo ou a outro site. Se você escolher um comportamento de clique para seu Content Card, lembre-se de atualizar seu **Link Text de** acordo.

As seguintes ações estão disponíveis para os links do Content Card:

| Ação | Descrição |
|---|---|
| Redirecionar para URL da Web | Abra uma página da Web não nativa. |
| [Deep Link no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Faça um deep link para uma tela existente em seu aplicativo. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para acionar. Pode ser usado para exibir outro Content Card ou acionar mensagens adicionais. |
| Atributo personalizado de registro | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) a ser definido para o usuário atual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As opções **Log Custom Event** e **Log Custom Attribute** exigem a seguinte compatibilidade de versão do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Etapa 4: Configurar definições adicionais (opcional)

Você pode usar [pares de valores-chave]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para criar categorias para seus cartões, criar [vários feeds de cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) e personalizar como os cartões são classificados.

Para adicionar pares de valores-chave à sua mensagem, vá para a guia **Settings (Configurações** ) e selecione **Add New Pair (Adicionar novo par**).

## Etapa 5: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Crie o restante de sua campanha. Continue nas próximas seções para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar Content Cards.

#### Escolha uma programação de entrega ou um acionador

Os Content Cards podem ser entregues com base em um horário programado, uma ação ou um acionador de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Você também pode definir a duração da campanha e o [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) e determinar a expiração do Content Card. Defina uma data de expiração específica ou os dias até a expiração do cartão, até 30 dias. Todas as variantes têm datas de validade idênticas.

{% alert note %}
O limite de frequência não se aplica aos cartões de conteúdo.
{% endalert %}

##### Entrega programada

Para campanhas de Content Card com entrega programada, você pode escolher quando o Braze avalia a elegibilidade e a personalização do público-alvo para novas campanhas de Content Card, especificando quando o cartão é criado. Para saber mais, consulte a [criação de cartões]({{site.baseurl}}/card_creation).

#### Escolha os usuários a serem alvos

Em seguida, segmente [os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente uma prévia de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

{% multi_lang_include target_audiences.md %}

#### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canvas. Para obter mais detalhes sobre como criar o restante do seu Canvas, implementar [testes multivariados]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) e muito mais, consulte a etapa [Criar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 6: Revisão e implementação

Depois de terminar de criar a última campanha ou Canvas, revise os detalhes, [teste-a]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/) e envie-a quando estiver pronta.

{% alert warning %}
Depois que um Content Card é lançado, ele não pode ser editado. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Consulte [Atualização de cartões enviados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) para entender como você pode abordar esse cenário.
{% endalert %}

Em seguida, confira [os relatórios do Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) para saber como você pode acessar os resultados de suas campanhas de Content Card.

## Coisas para saber

### Limitações de tamanho para cartões de conteúdo

O tamanho da carga útil de um Content Card pode ser de até 2 KB após a renderização do Liquid. Isso inclui o **título**, **a mensagem**, o **URL da imagem**, o **texto do link**, **o(s) URL(s) do link** e **os pares chave-valor** (nomes e valores). No entanto, esse limite não inclui o tamanho da imagem - apenas o comprimento do URL da imagem.

{% alert important %}
Mensagens com mais de 2 KB não serão enviadas. Durante os envios de teste, os Content Cards que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

### Número de cartões no feed

Cada usuário pode ter até 250 Content Cards não expirados em seu feed a qualquer momento. Quando esse limite for ultrapassado, o Braze deixará de devolver os cartões mais antigos, mesmo que não tenham sido lidos. Os cartões descartados também contam para esse limite, o que significa que um grande número de cartões descartados pode reduzir o espaço disponível para novos cartões.

### Comportamento de envio

Depois que os Content Cards são enviados, eles ficam aguardando em uma "caixa de entrada", prontos para serem entregues ao usuário (semelhante ao que acontece com os e-mails). Depois que o conteúdo é inserido no Content Card (no momento da exibição), ele não pode ser alterado durante sua vida útil. Isso se aplica mesmo se você estiver chamando uma API por meio do Connected Content e os dados do endpoint forem alterados. Esses dados não serão atualizados. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Se você modificar uma campanha, somente os cartões futuros que forem enviados terão a atualização.

Se precisar remover cartões antigos, você deverá primeiro interromper a campanha. Para interromper uma campanha, abra sua campanha do Content Card e selecione **Stop Campaign (Interromper campanha**). A interrupção da campanha solicitará que você decida como lidar com os usuários que já receberam o cartão. 

Se quiser remover o Content Card dos feeds de seus usuários, selecione **Remove card from feed (Remover cartão do feed**). O cartão será então ocultado pelo SDK na próxima sincronização.

\![Caixa de diálogo para confirmar a desativação do Content Card]({% image_buster /assets/img/cc_remove.png %}){: style="max-width:75%" }

{% alert tip %}
Deseja que seu conteúdo dure mais de 30 dias? Experimente [os banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

### Eventos de remoção de cartões {#action-based-card-removal}

Alguns Content Cards só são relevantes até que o usuário realize alguma ação. Por exemplo, um cartão que incentiva os usuários a ativar a conta não deve ser exibido depois que o usuário concluir essa tarefa de integração.

Em uma campanha ou mensagem do Canvas, você pode adicionar opcionalmente um **Removal Event (Evento de remoção** ) para especificar quais eventos personalizados ou compras devem fazer com que os cartões enviados anteriormente sejam removidos do feed do usuário, acionados pelo SDK ou pela API REST.

Os cartões serão removidos nas atualizações subsequentes depois que o Braze tiver processado o evento especificado.

{% alert tip %}
Você pode especificar vários eventos e compras personalizados que devem remover um cartão do feed de um usuário. Quando **qualquer** uma dessas ações for executada pelo usuário, todos os cartões existentes enviados pelos cartões da campanha serão removidos. Todos os cartões elegíveis futuros continuarão a ser enviados de acordo com a programação da mensagem.
{% endalert %}

Painel Content Card Removal Conditions (Condições de remoção do cartão de conteúdo) com a opção Content Card Removal Event (Evento de remoção do cartão de conteúdo).]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Atualização de cartões lançados

Os Content Cards não podem ser editados após serem enviados. Se você achar que precisa fazer alterações em cartões que já foram enviados, considere usar a [reelegibilidade da campanha]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/), conforme mostrado nas opções a seguir.

{% alert note %}
Quando um Content Card se torna reelegível, ele pode ser enviado novamente quando o cartão original ainda estiver no aplicativo de um usuário. Para evitar cartões duplicados no aplicativo de um usuário, você pode desativar a reelegibilidade ou estender a janela de reelegibilidade para que os usuários não recebam um novo cartão até que o original tenha expirado.
{% endalert %}

Observe também que os Cartões de Conteúdo que usam [a primeira impressão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) utilizam o tempo de impressão para calcular a reelegibilidade. No entanto, os Content Cards criados no lançamento da campanha ou na entrada da etapa do Canvas usam o horário de envio ou de impressão mais recente.

#### Opção 1: Duplicação da campanha

Uma abordagem é arquivar a campanha e remover os cartões ativos do feed. Em seguida, você pode duplicar a campanha e lançá-la com atualizações para que todos os usuários qualificados recebam os cartões atualizados.

* Se os usuários nunca devem ser reelegíveis para um Content Card, você pode filtrar os usuários que não receberam a versão anterior do Content Card definindo o filtro `Received Message from Campaign` para a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser reelegíveis em X dias, você pode definir o filtro para `Last Received Message from specific campaign` como mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

##### Caso de uso

Digamos que você tenha definido uma campanha para ser acionada pelo início de uma sessão e que ela tenha a reelegibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, você arquivaria a campanha e removeria os cartões do feed. Em segundo lugar, você duplicaria a campanha e a relançaria com o novo texto. Se o usuário tiver outra sessão, ele receberá imediatamente o novo cartão.

##### Impacto

* **Relatórios:** Cada versão do cartão teria uma análise separada.
* **Beneficiários existentes:** Os destinatários novos e existentes verão o cartão atualizado na próxima atualização do feed, se estiverem qualificados.

{% alert tip %}
Recomendamos essa opção para mensagens em que você está mostrando o conteúdo mais recente no cartão (como banners da página inicial), as alterações devem ser mostradas imediatamente ou quando a reelegibilidade está desativada.
{% endalert %}

#### Opção 2: Parar e reiniciar

Se um cartão tiver a reelegibilidade ativada, você poderá optar por:

1. Interrompa sua campanha.
2. Remova os Content Cards ativos dos feeds dos usuários.
3. Edite sua campanha conforme necessário.
4. Reinicie sua campanha.

Com essa abordagem, os usuários recém-elegíveis receberão o novo cartão, e os destinatários anteriores receberão o novo cartão quando voltarem a ser elegíveis.

##### Caso de uso

Digamos que você tenha uma campanha que é acionada por um início de sessão e tem a reelegibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, interrompa a campanha e remova o cartão do feed. Em segundo lugar, publique novamente a campanha com o novo texto. Se o usuário tiver outra sessão, ele receberá o novo cartão em 28 dias.

##### Impacto

* **Relatórios:** Uma campanha conterá todas as análises de relatórios para as versões de cartão lançadas. O Braze não diferencia as versões lançadas.
* **Destinatários existentes:** Os usuários que já receberam o cartão não receberão os cartões atualizados até que se tornem reelegíveis. Se a reelegibilidade for desativada, eles nunca receberão o novo cartão.

{% alert tip %}
Recomendamos o uso dessa opção para mensagens exclusivas em uma central de notificações ou caixa de entrada de mensagens (como promoções), quando for importante que a análise seja unificada ou quando a pontualidade da mensagem não for uma preocupação (por exemplo, os destinatários existentes podem aguardar a janela de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

#### Manter os cartões nos feeds dos usuários

Se desejar, você pode manter uma campanha de Content Card ativa nos feeds dos usuários e não removê-la. Quando a campanha ativa for editada, a versão anterior não editada do cartão da campanha ainda estará ativa, e somente os usuários que atenderem aos critérios após as edições verão a nova versão. No entanto, os usuários já expostos à campanha poderão ver duas versões do cartão.

