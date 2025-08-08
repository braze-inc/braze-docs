---
nav_title: Criação de um cartão de conteúdo
article_title: Criação de um cartão de conteúdo
page_order: 0
description: "Este artigo de referência aborda como criar, criar, configurar e enviar cartões de conteúdo usando campanhas e canvas do Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Criação de um cartão de conteúdo

> Este artigo aborda como criar um cartão de conteúdo no Braze ao construir campanhas e canvases. Aqui, vamos guiá-lo na escolha de um tipo de envio de mensagens, na composição do seu cartão e no agendamento da entrega da sua mensagem.

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada com uma campanha ou um canva? As campanhas são melhores para campanhas de envio de mensagens simples e únicas (como informar os usuários sobre um novo produto com uma única mensagem), enquanto os canvases são melhores para jornadas de usuários em várias etapas (como enviar sugestões de produtos personalizadas com base no comportamento do usuário ao longo do tempo).

{% tabs %}
{% tab Campanha %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Cartões de Conteúdo** ou, para campanhas de direcionamento em múltiplos canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Construtor de Relatórios]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar pelos tags relevantes.
5. Adicione e nomeie quantas variantes desejar para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para mais informações sobre variantes, consulte [multivariante e Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Você pode então selecionar **Copiar da Variante** no menu suspenso **Adicionar Variante**.
{% endalert %}

{% endtab %}
{% tab Canva %}

1. [Crie seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Após configurar seu canva, adicione uma etapa de Mensagem no construtor de canva. Dê um nome claro e significativo à sua etapa.
3. Selecione **Cartões de conteúdo** como seu canal de envio de mensagens.
4. Escolha quando o Braze calcula a elegibilidade do público e a personalização do cartão de conteúdo. Isso pode ser feito na entrada da etapa ou na primeira impressão (recomendado). As etapas que contêm cartões de conteúdo podem ser programadas ou baseadas em ações.
5. Escolha se deseja remover os cartões de conteúdo quando os usuários concluírem uma compra ou realizarem um evento personalizado.
6. Defina uma expiração para o cartão de conteúdo (tempo no feed). Isso pode ser feito após um período de tempo ou em um horário específico.
7. Filtre seu público, ou os destinatários, para esta etapa conforme necessário nas **Configurações de Entrega**. Você pode refinar ainda mais seu público especificando segmentos e adicionando filtros adicionais. As opções do público serão conferidas após a postergação, no momento em que as mensagens forem enviadas.
8. Escolha quaisquer outros canais de envio de mensagens que você deseja emparelhar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Especifique seus tipos de mensagens

Selecione um dos três tipos essenciais de cartão de conteúdo: **Clássico**, **Imagem Legendada**, e **Imagem Somente**. 

Para saber mais sobre o comportamento e a aparência esperados de cada tipo, consulte [Detalhes Criativos]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), ou confira os links na tabela a seguir. Esses tipos de cartão de conteúdo são aceitos tanto por aplicativos móveis quanto por aplicativos da Web.

| Tipo de mensagem | Exemplo | Descrição |
|---|---|---|
|[Clássico]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Um cartão de conteúdo clássico com um pequeno ícone e texto para incentivar a reserva de uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |O cartão clássico tem um layout simples com um título em negrito, texto da mensagem e uma imagem opcional que fica à esquerda do título e do texto. É melhor usar uma imagem ou ícone quadrado com o cartão clássico. |
|[Imagem com legenda]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Um cartão de conteúdo com legenda, com uma imagem de um levantador de peso e texto para incentivar a reserva de uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | O Cartão de Imagem Legendada apresenta seu conteúdo com texto e uma imagem que chama a atenção. |
|[Somente imagem]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Um cartão de conteúdo apenas com imagem e texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | O cartão de imagem apenas chama a atenção com espaço para imagens, GIFs e outros conteúdos criativos não textuais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 3: Crie um cartão de conteúdo

É possível editar todos os aspectos do conteúdo e do comportamento de sua mensagem na guia **Compose (Compor)** do editor de mensagens.

![Detalhes do cartão de conteúdo de amostra na guia Compor do criador de mensagens.]({% image_buster /assets/img/content_card_compose.png %})

O conteúdo aqui varia de acordo com o **tipo de cartão** escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

#### Idioma

Selecione **Adicionar Idiomas** para adicionar os idiomas desejados da lista fornecida. Isso inserirá o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) em sua mensagem. Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que possa preencher o texto onde ele pertence no Liquid. Para nossa lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Uma janela com inglês, espanhol e francês selecionados para os idiomas e título, descrição e texto do link selecionados para os campos a serem internacionalizados.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre o envio de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e mensagem

Escreva o que você quiser. Não há limites, mas quanto mais rápido você conseguir transmitir sua mensagem e fazer seu cliente clicar, melhor! Recomendamos títulos e conteúdos de mensagens claros e concisos. Nota que esses campos não são fornecidos para Cartões Somente de Imagem.

#### Imagem

Adicione uma imagem ao seu cartão de conteúdo selecionando **Add Image** ou fornecendo uma URL de imagem. Selecionar **Adicionar Imagem** abre a **Biblioteca de Mídia**, onde você pode selecionar uma imagem previamente carregada ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos, então certifique-se de verificar quais são antes de encomendar ou criar uma imagem do zero! Tenha em mente que os campos de mensagem do cartão de conteúdo são limitados a 2 KB no tamanho total.

#### Fixar no topo

Um cartão fixado será exibido na parte superior do feed de um usuário e não poderá ser descartado pelo usuário. Se mais de um cartão no feed de um usuário for fixado, os cartões fixados serão exibidos em ordem cronológica. Depois que um cartão foi enviado, você não pode atualizar retroativamente sua opção fixada. A alteração dessa opção após o envio de uma campanha afetará apenas os envios futuros.

![Lado a lado da prévia do cartão de conteúdo no Braze para celular e Web com a opção "Fixar este cartão na parte superior do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamento ao clicar

Quando o cliente clica em um link apresentado no cartão, o link pode levá-lo mais profundamente em seu app ou a outro site. Se você escolher um comportamento ao clicar para o seu cartão de conteúdo, lembre-se de atualizar seu **Texto do Link** de acordo.

As seguintes ações estão disponíveis para os links do cartão de conteúdo:

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abra uma página da Web não nativa. |
| [Deep linking no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Deep link em uma tela existente em seu app. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para disparar. Pode ser usado para exibir outro cartão de conteúdo ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) a ser definido para o usuário atual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As opções **Registrar evento personalizado** e **Registrar atributo personalizado** exigem a seguinte compatibilidade de versão do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Etapa 4: Configurar definições adicionais (opcional)

Você pode usar [pares-chave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para criar categorias para seus Cartões, criar [vários feeds de Cartão de Conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) e personalizar como os cartões são classificados.

Para adicionar pares de valores-chave à sua mensagem, acesse a guia **Settings (Configurações)** e selecione **Add New Pair (Adicionar novo par)**.

## Etapa 5: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}

Crie o restante de sua campanha. Continue para as próximas seções para mais detalhes sobre como usar melhor nossas ferramentas para construir Cartões de Conteúdo.

#### Escolha uma programação ou disparo de entrega

Os Cartões de Conteúdo podem ser entregues com base em um horário agendado, uma ação ou um disparo de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Você também pode definir a duração e o [horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) da campanha e determinar a expiração do cartão de conteúdo. Defina uma data de expiração específica ou os dias até a expiração de um cartão, até 30 dias. Todas as variantes têm datas de expiração idênticas.

{% alert note %}
A limitação de frequência não se aplica aos Cartões de Conteúdo.
{% endalert %}

##### Entrega programada

Para campanhas de cartão de conteúdo com entrega programada, você pode escolher quando o Braze avalia a elegibilidade e a personalização do público para novas campanhas de cartão de conteúdo, especificando quando o cartão é criado. Para obter mais informações, consulte a [criação de cartões]({{site.baseurl}}/card_creation).

#### Escolha os usuários a serem direcionados

Em seguida, [usuários-alvo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para mais detalhes sobre como construir o restante do seu canva, implemente [testes multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), e mais, consulte a [Etapa de Construção do seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do canva.

{% endtab %}
{% endtabs %}

## Etapa 6: Revisão e implementação

Depois de terminar de construir o último da sua campanha ou canva, revise seus detalhes, [teste-o]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/), e então envie quando estiver pronto.

{% alert warning %}
Depois que um cartão de conteúdo é lançado, ele não pode ser editado. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Consulte [Atualização de cartões enviados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) para entender como você pode abordar esse cenário.
{% endalert %}

Em seguida, confira [os relatórios do Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) para saber como acessar os resultados de suas campanhas do Content Card.

## Coisas para saber

### Tamanhos de campos de mensagens

Os campos de mensagem do cartão de conteúdo podem ter até 2 KB de tamanho total. Isso é calculado pela adição do comprimento do tamanho de byte dos seguintes campos: **Título**, **Mensagem**, **URL da imagem**, **Texto do link**, **URL(s) do link** e **Pares de chave-valor** (nomes e valores). As mensagens que excederem 2 KB não serão enviadas. Observe que isso não inclui o tamanho da imagem, mas sim o comprimento do URL da imagem.

{% alert important %}
Durante os envios de teste, os cartões de conteúdo que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

### Número de cartões no feed

Cada usuário pode ter até 250 cartões de conteúdo não expirados em seu feed a qualquer momento. Quando esse limite for excedido, o Braze deixará de devolver os cartões mais antigos, mesmo que não tenham sido lidos. Os cartões descartados também contam para esse limite, o que significa que um grande número de cartões descartados pode reduzir o espaço disponível para novos cartões.

### Comportamento de envio

Após os Cartões de Conteúdo serem enviados, eles ficam aguardando em uma "caixa de entrada" prontos para serem entregues ao usuário (semelhante ao que acontece com os e-mails). Depois que o conteúdo é inserido no cartão de conteúdo (no momento da exibição), ele não pode ser alterado durante sua vida útil. Isso se aplica mesmo que você esteja chamando uma API através do Conteúdo Conectado, e os dados do endpoint mudem. Esses dados não serão atualizados. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Se você modificar uma campanha, somente os cartões futuros que forem enviados terão a atualização.

Se você precisar remover cartões antigos, primeiro deve parar a campanha. Para interromper uma campanha, abra sua campanha do Content Card e selecione **Stop Campaign (Interromper campanha)** A interrupção da campanha solicitará que você decida como lidar com os usuários que já receberam o cartão. 

Se você quiser remover o cartão de conteúdo dos feeds dos seus usuários, selecione **Remover cartão do feed**. O cartão será então ocultado pelo SDK na próxima sincronização.

![Caixa de diálogo para confirmar a desativação do cartão de conteúdo]({% image_buster /assets/img/cc_remove.png %}){: style="max-width:75%" }

{% alert tip %}
Você quer que seus Cartões de Conteúdo pareçam durar mais do que o máximo de 30 dias? Uma maneira de realizar isso é fazer o seguinte:<br><br>

1. Defina a duração do cartão de conteúdo para 30 dias.
2. Defina a reelegibilidade da campanha para 30 dias.
3. Defina a campanha para disparar no "Início da sessão".
{% endalert %}

### Eventos de remoção de cartões {#action-based-card-removal}

Alguns cartões de conteúdo só são relevantes até que o usuário realize alguma ação. Por exemplo, um cartão que incentiva os usuários a ativar sua conta não deve ser exibido depois que o usuário concluir essa tarefa de integração.

Em uma campanha ou mensagem do Canvas, você pode adicionar opcionalmente um **evento de remoção** para especificar quais eventos personalizados ou compras devem fazer com que os cartões enviados anteriormente sejam removidos do feed do usuário, disparados pelo SDK ou pela API REST.

Os cartões serão removidos nas atualizações subsequentes depois que o Braze tiver processado o evento especificado.

{% alert tip %}
É possível especificar vários eventos personalizados e compras que devem remover um cartão do feed de um usuário. Quando **qualquer uma** dessas ações for executada pelo usuário, todos os cartões existentes enviados pelos cartões da campanha serão removidos. Todos os cartões elegíveis futuros continuarão a ser enviados de acordo com a programação da mensagem.
{% endalert %}

![Condições de Remoção do Cartão de Conteúdo painel com opção de Evento de Remoção do Cartão de Conteúdo.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Atualização de cartões lançados

Os cartões de conteúdo não podem ser editados após serem enviados. Se você perceber que precisa fazer alterações em cartões que já foram enviados, considere usar [reelegibilidade da campanha]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) conforme mostrado nas opções a seguir.

{% alert note %}
Quando um cartão de conteúdo se torna reelegível, ele pode ser enviado novamente quando o cartão original ainda estiver no app do usuário. Para evitar cartões duplicados no app de um usuário, é possível desativar a reelegibilidade ou estender a janela de reelegibilidade para que os usuários não recebam um novo cartão até que o original tenha expirado.
{% endalert %}

Observe também que os cartões de conteúdo que usam [a primeira impressão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) usam o tempo de impressão para calcular a reelegibilidade. No entanto, os cartões de conteúdo criados no lançamento da campanha ou na entrada da etapa do Canva usam o tempo de envio ou impressão mais recente.

#### Opção 1: Duplicação da campanha

Uma abordagem é arquivar a campanha e remover os cartões ativos do feed. Em seguida, é possível duplicar a campanha e lançá-la com atualizações para que todos os usuários elegíveis recebam os cartões atualizados.

* Se os usuários nunca devem ser elegíveis novamente para um cartão de conteúdo, você pode filtrar os usuários que não receberam a versão anterior do cartão de conteúdo definindo o filtro `Received Message from Campaign` para a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser reelegíveis em X dias, você pode definir o filtro para `Last Received Message from specific campaign` como mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

##### Caso de uso

Digamos que você tenha definido uma campanha para ser disparada pelo início de uma sessão e que a reelegibilidade esteja definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, você arquivaria a campanha e removeria os cartões do feed. Em segundo lugar, você duplicaria a campanha e relançaria com o novo texto. Se o usuário tiver outra sessão, ele receberá imediatamente o novo cartão.

##### Impacto

* **Relatórios:** Cada versão do cartão teria uma análise de dados separada.
* **Beneficiários existentes:** Os destinatários novos e existentes verão o cartão atualizado na próxima atualização do feed, se forem elegíveis.

{% alert tip %}
Recomendamos esta opção para mensagens onde você está mostrando o conteúdo mais recente no cartão (como banners da página inicial), as mudanças devem ser mostradas imediatamente, ou quando a re-eligibilidade está desativada.
{% endalert %}

#### Opção 2: Parar e reiniciar

Se um cartão tiver a reelegibilidade ativada, você poderá optar por:

1. Interrompa sua campanha.
2. Remova os cartões de conteúdo ativos dos feeds dos usuários.
3. Edite sua campanha conforme necessário.
4. Reinicie sua campanha.

Com essa abordagem, os usuários recém-elegíveis receberão o novo cartão, e os destinatários anteriores receberão o novo cartão quando forem novamente elegíveis.

##### Caso de uso

Vamos supor que você tenha uma campanha que é acionada pelo início de uma sessão e tem reeligibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, interrompa a campanha e remova o cartão do feed. Em segundo lugar, republicar a campanha com o novo texto. Se o usuário tiver outra sessão, ele receberá o novo cartão em 28 dias.

##### Impacto

* **Relatórios:** Uma campanha conterá todas as análises de dados de relatórios para as versões de cartões lançadas. Braze não diferenciará entre as versões lançadas.
* **Destinatários existentes:** Os usuários que já receberam o cartão não receberão os cartões atualizados até que se tornem elegíveis novamente. Se a reelegibilidade for desativada, eles nunca receberão o novo cartão.

{% alert tip %}
Recomendamos o uso dessa opção para mensagens exclusivas em uma central de notificações ou caixa de entrada de mensagens (como promoções), quando for importante que a análise de dados seja unificada ou quando a pontualidade da mensagem não for uma preocupação (por exemplo, os destinatários existentes podem aguardar a janela de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

#### Manter os cartões nos feeds dos usuários

Se desejar, é possível manter uma campanha de cartão de conteúdo ativa nos feeds dos usuários e não removê-la. Quando a campanha ativa for editada, a versão anterior não editada do cartão da campanha ainda estará ativa, e somente os usuários que atenderem aos critérios após as edições verão a nova versão. No entanto, os usuários já expostos à campanha poderão ver duas versões do cartão.

