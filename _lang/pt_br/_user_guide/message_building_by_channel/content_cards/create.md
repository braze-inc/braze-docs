---
nav_title: Criar um cartão de conteúdo
article_title: Criar um cartão de conteúdo
page_order: 0
description: "Este artigo de referência cobre como criar, compor, configurar e enviar Cartões de Conteúdo usando campanhas e Canvases do Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Criar um cartão de conteúdo

> Este artigo aborda como criar um cartão de conteúdo no Braze ao construir campanhas e canvases. Aqui, vamos guiá-lo na escolha de um tipo de envio de mensagens, na composição do seu cartão e no agendamento da entrega da sua mensagem.

## Etapa 1: Escolha onde construir sua mensagem

Use campanhas para envio único e simples de mensagens (como informar os usuários sobre um produto com uma mensagem). Use Canvases para jornadas de usuários em múltiplas etapas (como enviar sugestões de produtos personalizadas com base no comportamento do usuário ao longo do tempo).

{% tabs %}
{% tab Campaign %}

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
{% tab Canvas %}

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
|[Clássico]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Um Cartão de Conteúdo Clássico com um pequeno ícone e texto para incentivar a reserva de uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |O Cartão Clássico tem um layout simples com um título em negrito, texto da mensagem e uma imagem opcional que fica à esquerda do título e do texto. É melhor usar uma imagem ou ícone quadrado com o cartão clássico. |
|[Imagem com legenda]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Um Cartão de Conteúdo com Legenda com uma imagem de um levantador de peso e texto para incentivar a reserva de uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | O Cartão de Imagem Legendada apresenta seu conteúdo com texto e uma imagem que chama a atenção. |
|[Somente imagem]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Um Cartão de Conteúdo Apenas com Imagem com texto apenas.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | O cartão de imagem apenas chama a atenção com espaço para imagens, GIFs e outros conteúdos criativos não textuais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 3: Crie um cartão de conteúdo

É possível editar todos os aspectos do conteúdo e do comportamento de sua mensagem na guia **Compose (Compor)** do editor de mensagens.

![Detalhes do cartão de conteúdo de amostra na guia de composição do editor de mensagens.]({% image_buster /assets/img/content_card_compose.png %})

O conteúdo aqui varia de acordo com o **tipo de cartão** escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

#### Idioma

Selecione **Adicionar Idiomas** para adicionar os idiomas desejados da lista fornecida. Isso inserirá o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) em sua mensagem. Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que possa preencher o texto onde ele pertence no Liquid. Para nossa lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Uma janela com inglês, espanhol e francês selecionados para os idiomas, e título, descrição e texto do link selecionados para os campos a serem internacionalizados.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre o envio de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e mensagem

Escreva o que você quiser. Não há limites, mas quanto mais rápido você conseguir transmitir sua mensagem e fazer seu cliente clicar, melhor! Recomendamos títulos e conteúdos de mensagens claros e concisos. Nota que esses campos não são fornecidos para Cartões Somente de Imagem.

#### Imagem

Adicione uma imagem ao seu cartão de conteúdo selecionando **Add Image** ou fornecendo uma URL de imagem. Selecionar **Adicionar Imagem** abre a **Biblioteca de Mídia**, onde você pode selecionar uma imagem previamente carregada ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos, então certifique-se de verificar quais são antes de encomendar ou criar uma imagem do zero! Tenha em mente que os campos de mensagem do cartão de conteúdo são limitados a 2 KB no tamanho total.

#### Fixar no topo

O Braze exibe um cartão fixado no topo do feed de um usuário e o usuário não pode descartá-lo. Se o feed de um usuário tiver vários cartões fixados, o Braze os ordena cronologicamente. Depois de enviar um cartão, você não pode atualizar retroativamente sua opção de fixação. Alterar esta opção após enviar uma campanha afeta apenas envios futuros.

![Lado a lado da prévia do cartão de conteúdo na Braze para Mobile e Web com a opção "Fixar este cartão no topo do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamento ao clicar

Quando o cliente clica em um link apresentado no cartão, o link pode levá-lo mais profundamente em seu app ou a outro site. Se você escolher um comportamento ao clicar para o seu cartão de conteúdo, lembre-se de atualizar seu **Texto do Link** de acordo.

As seguintes ações estão disponíveis para links de Cartão de Conteúdo:

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abra uma página da Web não nativa. |
| [Deep linking no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Deep link em uma tela existente em seu app. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para disparar. Pode ser usado para exibir outro cartão de conteúdo ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) a ser definido para o usuário atual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As opções **Registrar Evento Personalizado** e **Registrar Atributo Personalizado** requerem a seguinte compatibilidade de versão do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Etapa 4: Configurar definições adicionais (opcional)

Você pode usar [pares-chave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para criar categorias para seus Cartões, criar [vários feeds de Cartão de Conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) e personalizar como os cartões são classificados.

Para adicionar pares de valores-chave à sua mensagem, acesse a guia **Settings (Configurações)** e selecione **Add New Pair (Adicionar novo par)**.

## Etapa 5: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campaign %}

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

Em seguida, [alvo usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você recebe automaticamente uma prévia de como é a população aproximada desse segmento. Tenha em mente que a associação exata ao segmento é sempre calculada antes que a mensagem seja enviada.

{% multi_lang_include target_audiences.md %}

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para mais detalhes sobre como construir o restante do seu canva, implemente [testes multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), e mais, consulte a [Etapa de Construção do seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do canva.

{% endtab %}
{% endtabs %}

## Etapa 6: Revisão e implementação

Depois de terminar de construir o último da sua campanha ou canva, revise seus detalhes, [teste-o]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), e então envie quando estiver pronto.

{% alert warning %}
Depois que um cartão de conteúdo é lançado, ele não pode ser editado. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Consulte [Atualização de cartões enviados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) para entender como você pode abordar esse cenário.
{% endalert %}

Em seguida, confira [os relatórios do Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) para saber como acessar os resultados de suas campanhas do Content Card.

## Coisas para saber

### Limitações de tamanho para Cartões de Conteúdo

O tamanho de uma carga útil de Cartão de Conteúdo pode ser de até 2 KB após a renderização do Liquid. Isso inclui o **Título**, **Mensagem**, **URL da Imagem**, **Texto do Link**, **URL(s) do Link** e **Pares Chave-Valor** (nomes e valores). No entanto, esse limite não inclui o tamanho da imagem—apenas o comprimento da URL da imagem.

{% alert important %}
Mensagens maiores que 2 KB não serão enviadas. Durante envios de teste, os Cartões de Conteúdo que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

### Número de cartões no feed

Cada usuário pode ter até 250 cartões de conteúdo não expirados em seu feed a qualquer momento. Quando esse limite for excedido, o Braze deixará de devolver os cartões mais antigos, mesmo que não tenham sido lidos. Cartões dispensados também contam para esse limite, o que significa que um alto número de cartões dispensados pode reduzir o espaço disponível para novos.

### Comportamento de envio

Após o Braze enviar Cartões de Conteúdo, eles ficam em uma "caixa de entrada" prontos para serem entregues ao usuário (semelhante a e-mails). Após o Braze puxar conteúdo para o Cartão de Conteúdo no momento da exibição, o conteúdo não muda durante a vida útil do cartão. Isso inclui chamadas de API através de Conteúdo Conectado se os dados do endpoint mudarem. O Braze não atualiza esses dados. Você só pode parar de enviar novos cartões e remover cartões existentes dos feeds. Se você modificar uma campanha, apenas os cartões futuros refletem a atualização.

Se você precisar remover cartões antigos, primeiro deve parar a campanha. Para interromper uma campanha, abra sua campanha do Content Card e selecione **Stop Campaign (Interromper campanha)** Parar a campanha solicitará que você decida como lidar com os usuários que já receberam seu cartão. 

Se você quiser remover o cartão de conteúdo dos feeds dos seus usuários, selecione **Remover cartão do feed**. O cartão será então ocultado pelo SDK na próxima sincronização.

![Caixa de diálogo para confirmar a desativação do cartão de conteúdo]({% image_buster /assets/img/cc_remove.png %}){: style="max-width:75%" }

{% alert tip %}
Você quer que seu conteúdo dure mais de 30 dias? Experimente [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

### Eventos de remoção de cartões {#action-based-card-removal}

Alguns Cartões de Conteúdo são relevantes apenas até que um usuário realize alguma ação. Por exemplo, um cartão que incentiva os usuários a ativar sua conta não deve ser exibido depois que o usuário concluir essa tarefa de integração.

Dentro de uma campanha ou mensagem do Canvas, você pode opcionalmente adicionar um **Evento de Remoção** para especificar quais eventos ou compras personalizados devem fazer com que cartões enviados anteriormente sejam removidos do feed desse usuário, acionados pelo SDK ou API REST.

O Braze remove cartões em atualizações subsequentes após processar o evento especificado.

{% alert tip %}
É possível especificar vários eventos personalizados e compras que devem remover um cartão do feed de um usuário. Quando **qualquer uma** dessas ações for executada pelo usuário, todos os cartões existentes enviados pelos cartões da campanha serão removidos. Todos os cartões elegíveis futuros continuarão a ser enviados de acordo com a programação da mensagem.
{% endalert %}

![Painel de Condições de Remoção de Cartão de Conteúdo com opção de Evento de Remoção de Cartão de Conteúdo.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Atualização de cartões lançados

Você não pode editar Cartões de Conteúdo após enviá-los. Se você precisar alterar cartões enviados, considere usar [re-eligibilidade da campanha]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) com as seguintes opções.

{% alert note %}
Quando um cartão de conteúdo se torna reelegível, ele pode ser enviado novamente quando o cartão original ainda estiver no app do usuário. Para evitar cartões duplicados no app de um usuário, é possível desativar a reelegibilidade ou estender a janela de reelegibilidade para que os usuários não recebam um novo cartão até que o original tenha expirado.
{% endalert %}

Observe também que os cartões de conteúdo que usam [a primeira impressão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) usam o tempo de impressão para calcular a reelegibilidade. No entanto, os cartões de conteúdo criados no lançamento da campanha ou na entrada da etapa do Canva usam o tempo de envio ou impressão mais recente.

#### Opção 1: Duplicação da campanha

Uma abordagem é arquivar a campanha e remover os cartões ativos do feed. Então você pode duplicar a campanha e lançá-la com atualizações para que quaisquer usuários elegíveis recebam os cartões atualizados.

* Se os usuários nunca devem ser elegíveis novamente para um cartão de conteúdo, você pode filtrar os usuários que não receberam a versão anterior do cartão de conteúdo definindo o filtro `Received Message from Campaign` para a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser reelegíveis em X dias, você pode definir o filtro para `Last Received Message from specific campaign` como mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

##### Caso de uso

Vamos supor que você configurou uma campanha para ser acionada pelo início de uma sessão, e ela tem a re-elegibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, você arquivaria a campanha e removeria os cartões do feed. Em segundo lugar, você duplicaria a campanha e relançaria com o novo texto. Se o usuário tiver outra sessão, ele receberá imediatamente o novo cartão.

##### Impacto

* **Relatórios:** Cada versão do cartão tem análises separadas.
* **Beneficiários existentes:** Novos e existentes destinatários veem o cartão atualizado na próxima atualização do feed, se forem elegíveis.

{% alert tip %}
Recomendamos esta opção para mensagens onde você está mostrando o conteúdo mais recente no cartão (como banners da página inicial), as mudanças devem ser mostradas imediatamente, ou quando a re-eligibilidade está desativada.
{% endalert %}

#### Opção 2: Parar e reiniciar

Se um cartão tiver a re-elegibilidade ativada, você pode escolher:

1. Interrompa sua campanha.
2. Remova os cartões de conteúdo ativos dos feeds dos usuários.
3. Edite sua campanha conforme necessário.
4. Reinicie sua campanha.

Com essa abordagem, usuários recém-elegíveis receberão o novo cartão, e destinatários anteriores receberão o novo cartão quando forem re-elegíveis.

##### Caso de uso

Vamos supor que você tenha uma campanha que é acionada pelo início de uma sessão e tem reeligibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, interrompa a campanha e remova o cartão do feed. Em segundo lugar, republicar a campanha com o novo texto. Se o usuário tiver outra sessão, ele receberá o novo cartão em 28 dias.

##### Impacto

* **Relatórios:** Uma campanha contém todas as análises para todas as versões de cartão lançadas. A Braze não diferencia entre versões.
* **Destinatários existentes:** Usuários que já receberam o cartão não recebem cartões atualizados até se tornarem re-elegíveis. Se a re-elegibilidade estiver desativada, eles nunca receberão o novo cartão.

{% alert tip %}
Recomendamos usar esta opção para mensagens exclusivas em um centro de notificações ou caixa de mensagens (como promoções), quando é importante que as análises sejam unificadas, ou quando a pontualidade da mensagem não é uma preocupação (como destinatários existentes podem esperar pela janela de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

#### Manter os cartões nos feeds dos usuários

Se desejado, você pode manter uma campanha ativa de Cartão de Conteúdo nos feeds dos usuários e não removê-la. Quando a campanha ativa é editada, a versão anterior não editada do cartão da campanha ainda estará ativa, e apenas usuários que atendem aos critérios após as edições verão a nova versão. No entanto, os usuários já expostos à campanha poderão ver duas versões do cartão.

