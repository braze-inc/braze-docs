---
nav_title: Criar um cartão de conteúdo
article_title: Criar um cartão de conteúdo
page_order: 0
description: "Este artigo de referência cobre como criar, redigir, configurar e enviar Cartões de conteúdo usando campanhas e Canvas da Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Criar um cartão de conteúdo

> Este artigo aborda como criar um cartão de conteúdo na Braze ao construir campanhas e canvas. Aqui, vamos guiar você na escolha de um tipo de envio de mensagens, na composição do seu cartão e no agendamento da entrega da sua mensagem.

## Etapa 1: Escolha onde construir sua mensagem

Use campanhas para envio de mensagens simples e únicas (como informar os usuários sobre um produto com uma mensagem). Use Canvas para jornadas de usuários em múltiplas etapas (como enviar sugestões de produtos personalizadas com base no comportamento do usuário ao longo do tempo).

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Cartões de conteúdo** ou, para campanhas direcionadas a múltiplos canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Construtor de Relatórios]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar pelas tags relevantes.
5. Adicione e nomeie quantas variantes desejar para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma das variantes adicionadas. Para mais informações sobre variantes, consulte [Testes multivariantes e Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Depois, selecione **Copiar da Variante** no menu suspenso **Adicionar Variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Após configurar seu canva, adicione uma etapa de Mensagem no construtor de canva. Dê um nome claro e significativo à sua etapa.
3. Selecione **Cartões de conteúdo** como seu canal de envio de mensagens.
4. Escolha quando a Braze calcula a elegibilidade do público e a personalização do cartão de conteúdo. Isso pode ser na entrada da etapa ou na primeira impressão (recomendado). As etapas que contêm cartões de conteúdo podem ser programadas ou baseadas em ação.
5. Escolha se deseja remover os cartões de conteúdo quando os usuários concluírem uma compra ou realizarem um evento personalizado.
6. Defina uma expiração para o cartão de conteúdo (tempo no feed). Isso pode ser após um período de tempo ou em um horário específico.
7. Filtre seu público, ou os destinatários, para esta etapa conforme necessário nas **Configurações de Entrega**. Você pode refinar ainda mais seu público especificando segmentos e adicionando filtros adicionais. As opções do público serão conferidas após a postergação, no momento em que as mensagens forem enviadas.
8. Escolha quaisquer outros canais de envio de mensagens que você deseja combinar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Especifique seus tipos de mensagens

Selecione um dos três tipos essenciais de cartão de conteúdo: **Clássico**, **Imagem com legenda** e **Somente imagem**. 

Para saber mais sobre o comportamento e a aparência esperados de cada tipo, consulte [Detalhes criativos]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), ou confira os links na tabela a seguir. Esses tipos de cartão de conteúdo são aceitos tanto por apps móveis quanto por aplicações web.

| Tipo de mensagem | Exemplo | Descrição |
|---|---|---|
|[Clássico]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Um cartão de conteúdo clássico com um pequeno ícone e texto para incentivar a reserva de uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |O cartão clássico tem um layout simples com um título em negrito, texto da mensagem e uma imagem opcional que fica à esquerda do título e do texto. É melhor usar uma imagem ou ícone quadrado com o cartão clássico. |
|[Imagem com legenda]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Um cartão de conteúdo com legenda com uma imagem de um levantador de peso e texto para incentivar a reserva de uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | O cartão de imagem com legenda apresenta seu conteúdo com texto e uma imagem que chama a atenção. |
|[Somente imagem]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Um cartão de conteúdo somente imagem com texto apenas.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | O cartão somente imagem chama a atenção com espaço para imagens, GIFs e outros conteúdos criativos não textuais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 3: Crie um cartão de conteúdo

É possível editar todos os aspectos do conteúdo e do comportamento da sua mensagem na guia **Redigir** do editor de mensagens.

![Detalhes de exemplo do cartão de conteúdo na guia Redigir do editor de mensagens.]({% image_buster /assets/img/content_card_compose.png %})

O conteúdo aqui varia de acordo com o **Tipo de cartão** escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

#### Idioma

Selecione **Adicionar idiomas** para adicionar os idiomas desejados da lista fornecida. Isso inserirá o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) na sua mensagem. Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que você possa preencher o texto onde ele pertence no Liquid. Para ver a lista completa de idiomas disponíveis, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Uma janela com inglês, espanhol e francês selecionados para os idiomas, e título, descrição e texto do link selecionados para os campos a serem internacionalizados.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e mensagem

Escreva o que quiser. Não há limites, mas quanto mais rápido você conseguir transmitir sua mensagem e fazer seu cliente clicar, melhor! Recomendamos títulos e conteúdos de mensagens claros e concisos. Note que esses campos não são fornecidos para cartões somente de imagem.

#### Imagem

Adicione uma imagem ao seu cartão de conteúdo selecionando **Adicionar imagem** ou fornecendo uma URL de imagem. Selecionar **Adicionar imagem** abre a **Biblioteca de mídia**, onde você pode selecionar uma imagem já carregada ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos, então certifique-se de verificar quais são antes de encomendar ou criar uma imagem do zero! Tenha em mente que os campos de mensagem do cartão de conteúdo são limitados a 2&nbsp;KB no tamanho total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Fixar no topo

A Braze exibe um cartão fixado no topo do feed de um usuário, e o usuário não pode descartá-lo. Se o feed de um usuário tiver vários cartões fixados, a Braze os ordena cronologicamente. Depois de enviar um cartão, não é possível atualizar retroativamente sua opção de fixação. Alterar essa opção após enviar uma campanha afeta apenas envios futuros.

![Lado a lado da prévia do cartão de conteúdo na Braze para celular e web com a opção "Fixar este cartão no topo do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamento ao clicar

Quando o cliente clica em um link apresentado no cartão, o link pode levá-lo para dentro do seu app ou para outro site. Se você escolher um comportamento ao clicar para o seu cartão de conteúdo, lembre-se de atualizar o **Texto do link** de acordo.

As seguintes ações estão disponíveis para links de cartão de conteúdo:

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abrir uma página da web não nativa. |
| [Deep link no app]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Deep link para uma tela existente no seu app. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para disparar. Pode ser usado para exibir outro cartão de conteúdo ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) a ser definido para o usuário atual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As opções **Registrar evento personalizado** e **Registrar atributo personalizado** requerem a seguinte compatibilidade de versão do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Etapa 4: Configurar definições adicionais (opcional)

Você pode usar [pares chave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para criar categorias para seus cartões, criar [vários feeds de cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) e personalizar como os cartões são classificados.

Para adicionar pares chave-valor à sua mensagem, acesse a guia **Configurações** e selecione **Adicionar novo par**.

## Etapa 5: Crie o restante da sua campanha ou canva

{% tabs %}
{% tab Campaign %}

Crie o restante da sua campanha. Continue para as próximas seções para mais detalhes sobre como usar melhor nossas ferramentas para construir Cartões de conteúdo.

#### Escolha uma programação ou gatilho de entrega

Os Cartões de conteúdo podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para mais informações, consulte [Agendamento da sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Você também pode definir a duração e o [horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) da campanha e determinar a expiração do cartão de conteúdo. Defina uma data de expiração específica ou os dias até a expiração de um cartão, até 30 dias. Todas as variantes têm datas de expiração idênticas.

Se você optar por expirar um cartão após uma duração definida (por exemplo, após duas semanas), a expiração é calculada a partir do horário de envio do cartão. Para campanhas agendadas, esse é o horário de lançamento programado. Para campanhas baseadas em ação, esse é o horário em que o usuário realiza a ação de gatilho. Por exemplo, se um cartão baseado em ação for enviado às 14h hoje com expiração de 1 dia, ele expira às 14h do dia seguinte.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Para entrega baseada em ação, há um pequeno atraso esperado antes que o cartão de conteúdo apareça. Por exemplo, quando uma campanha é disparada no início da sessão, esse evento de gatilho precisa primeiro ser enviado aos servidores da Braze. Em seguida, a elegibilidade do usuário para a campanha é registrada. Quando o SDK sincroniza, o cartão é criado e retornado na mesma resposta de sincronização. Se a sincronização do SDK aconteceu antes da elegibilidade do usuário ser registrada, ele não recebe o cartão. Para usuários de primeira sessão, esse atraso é inevitável. Para usuários existentes que precisam de disponibilidade instantânea, considere usar entrega programada.

##### Entrega programada

Para campanhas de cartão de conteúdo com entrega programada, você pode escolher quando a Braze avalia a elegibilidade e a personalização do público para novas campanhas de cartão de conteúdo, especificando quando o cartão é criado. Para mais informações, consulte [criação de cartões]({{site.baseurl}}/card_creation).

#### Escolha os usuários a serem direcionados

Em seguida, [direcione usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você recebe automaticamente uma prévia de como é a população aproximada desse segmento. Tenha em mente que a associação exata ao segmento é sempre calculada antes que a mensagem seja enviada.

{% multi_lang_include target_audiences.md %}

#### Selecionar eventos de conversão

A Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do canva. Para mais detalhes sobre como construir o restante do seu canva, implementar [testes multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), e mais, consulte a etapa [Construa seu canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 6: Revisão e implementação

Depois de terminar de construir sua campanha ou canva, revise os detalhes, [teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) e envie quando estiver pronto.

{% alert warning %}
Depois que um cartão de conteúdo é lançado, ele não pode ser editado. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Consulte [Atualização de cartões lançados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) para entender como você pode lidar com esse cenário.
{% endalert %}

Em seguida, confira [Relatórios de cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) para saber como acessar os resultados das suas campanhas de cartão de conteúdo.

## O que você precisa saber

### Limitações de carga útil e feed

Para garantir a performance, os Cartões de conteúdo têm duas restrições principais: um limite no tamanho da carga útil para cada cartão e um número máximo de cartões que podem aparecer em um feed.

#### Limitações de tamanho para Cartões de conteúdo

A carga útil de dados total para um único cartão de conteúdo não pode exceder 2 KB **depois** que qualquer personalização Liquid é renderizada. Isso inclui:

* Título
* Mensagem
* URL da imagem (o comprimento da string da URL em si, não o tamanho do arquivo da imagem)
* Texto do link
* URLs de link para todas as plataformas especificadas (URLs separadas para iOS, Android e Web contam para o total)
* Pares chave-valor (tanto os nomes das chaves quanto seus valores)

Usar Liquid para puxar strings longas de texto (como de atributos personalizados) pode fazer você exceder o limite.

O criador da campanha exibirá um aviso se seu conteúdo estático exceder o limite. (Não é possível prever o tamanho para conteúdo dinâmico usando Liquid.) **Se o tamanho da mensagem exceder 2 KB, ela será abortada no momento do envio.** Você pode ver esses abortos no Registro de Atividade da Mensagem com o motivo `Content card maximum size exceeded`.

{% alert important %}
Durante envios de teste, Cartões de conteúdo que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

Aqui estão algumas práticas recomendadas para gerenciar o tamanho da carga útil dos Cartões de conteúdo:

* Use encurtadores de URL para links longos. URLs, especialmente aquelas com parâmetros de rastreamento extensos, podem enfrentar problemas de limite de tamanho. Usar um serviço de encurtamento de URL pode reduzir drasticamente a contagem de caracteres e liberar espaço na carga útil.
* Trunque conteúdo dinâmico com Liquid. Ao personalizar cartões com texto dinâmico de atributos de usuário ou chamadas de API, o comprimento do conteúdo pode ser imprevisível. Use proativamente filtros Liquid como `truncate` para limitar o comprimento de qualquer texto dinâmico.
* Seja eficiente com URLs de múltiplas plataformas. O limite de 2 KB inclui as URLs para todas as plataformas que você definir. Usar URLs longas e únicas para cada plataforma pode multiplicar o tamanho da carga útil. Se possível, use um único link que funcione em todas as plataformas, ou use encurtadores de URL conforme necessário.
* Considere Banners para conteúdo mais rico. Para casos de uso que exigem consistentemente grandes quantidades de conteúdo, os Cartões de conteúdo podem não ser o canal certo. Banners não têm a mesma limitação de carga útil de 2 KB e são mais adequados para incorporar conteúdo mais rico diretamente em uma experiência de app ou site.

#### Número de cartões no feed

Cada usuário pode ter até 250 cartões de conteúdo não expirados em seu feed a qualquer momento. Quando esse limite é excedido, a Braze deixa de retornar os cartões mais antigos, mesmo que não tenham sido lidos. Cartões descartados também contam para esse limite, o que significa que um número alto de cartões descartados pode reduzir o espaço disponível para os mais antigos.

Para evitar problemas com o limite de cartões, recomendamos as seguintes práticas:

- **Use datas de expiração mais curtas:** Para campanhas sensíveis ao tempo (como uma promoção de fim de semana), defina uma data de expiração específica. Dessa forma, os cartões são removidos automaticamente do feed e não contarão para o limite após não serem mais relevantes.
- **Aproveite a remoção baseada em ação:** Configure eventos de remoção para cartões transacionais ou baseados em metas. Por exemplo, um cartão que solicita a um usuário que complete seu perfil deve ser removido assim que um evento `profile_completed` for registrado.
- **Audite campanhas de longa duração:** Revise campanhas recorrentes ou em andamento para garantir que não estejam criando uma experiência ruim para seus usuários, preenchendo o feed com muitos cartões ao longo do tempo.

### Entendendo a re-elegibilidade para Cartões de conteúdo

A re-elegibilidade determina se e quando um usuário pode receber uma mensagem da mesma campanha mais de uma vez. Para Cartões de conteúdo, entender como isso funciona é fundamental para gerenciar campanhas recorrentes e garantir que os usuários não recebam mensagens duplicadas ou desatualizadas.

{% alert tip %}
Quer que seu conteúdo dure mais de 30 dias? Experimente [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

#### Como a re-elegibilidade é calculada

Se você ativar a re-elegibilidade, a contagem regressiva para quando um usuário pode "reentrar" em uma campanha começa após o envio da mensagem. O momento específico em que essa contagem regressiva começa depende das configurações de criação do seu cartão:

* Os Cartões de conteúdo que usam [na primeira impressão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) utilizam o tempo de impressão para calcular a re-elegibilidade.
* Os Cartões de conteúdo criados no lançamento da campanha ou na entrada da etapa do canva usam o horário de envio ou o horário de impressão mais recente, o que for mais tardio.

#### A expiração de 30 dias e a re-elegibilidade

Uma fonte comum de confusão é a interação entre a re-elegibilidade da campanha e a expiração automática de 30 dias de todos os Cartões de conteúdo.

Todos os Cartões de conteúdo são automaticamente removidos dos sistemas da Braze 30 dias após serem enviados ou removidos. Se você tiver uma campanha recorrente de longa duração com a re-elegibilidade **desativada**, um usuário ainda pode receber o mesmo cartão novamente após 30 dias. Quando o cartão original é removido, o sistema não vê mais um registro de que aquele usuário recebeu a campanha, tornando-o elegível novamente na próxima sessão.

Para que os usuários recebam uma mensagem de uma campanha específica apenas uma vez, adicione um filtro de público à sua campanha ou etapa do canva para usuários que não receberam uma mensagem desta campanha. Esse filtro é a maneira mais confiável de evitar envios duplicados de campanhas de longa duração.

### Gerenciando Cartões de conteúdo ativos

Após os Cartões de conteúdo serem enviados, eles ficam aguardando em uma "caixa de entrada" prontos para serem entregues ao usuário (semelhante ao que acontece com e-mails). Depois que o conteúdo é carregado no cartão de conteúdo (no momento da exibição), ele não pode ser alterado durante sua vida útil. Isso se aplica mesmo que você esteja chamando uma API por meio do Conteúdo conectado e os dados do endpoint mudem. Esses dados não serão atualizados. O cartão só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Se você modificar uma campanha, somente os cartões futuros que forem enviados terão a atualização.

#### Atualização de cartões lançados

Para alterar um cartão para usuários que já o receberam, você deve usar um dos seguintes métodos:

##### Opção 1: Duplicar a campanha (recomendado para alterações imediatas)

{% alert tip %}
Recomendamos essa opção para mensagens em que você está mostrando o conteúdo mais recente no cartão, as alterações devem ser mostradas imediatamente ou quando a re-elegibilidade está desativada.
{% endalert %}

A primeira abordagem é arquivar a campanha e lançar uma nova campanha duplicada:

1. Pare a campanha original e, quando solicitado, selecione `Remove card after the next sync`.
2. Duplique a campanha, faça suas edições e lance a nova versão.

Quando você duplica a campanha, precisa definir o público para a nova versão. Use filtros de segmentação para controlar quem recebe o cartão atualizado:
* Se os usuários nunca devem ser elegíveis novamente para um cartão de conteúdo, você pode filtrar os usuários que não receberam a versão anterior do cartão de conteúdo definindo o filtro `Received Message from Campaign` com a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser re-elegíveis em X dias, você pode definir o filtro para `Last Received Message from specific campaign` como mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

###### Impacto

* **Destinatários existentes:** Os destinatários novos e existentes verão o cartão atualizado na próxima atualização do feed, se forem elegíveis.
* **Relatórios:** Cada versão do cartão terá análise de dados separada.

Digamos que você tenha configurado uma campanha para ser disparada pelo início de uma sessão, com re-elegibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você quer alterar o texto. Primeiro, você arquivaria a campanha e removeria os cartões do feed. Depois, duplicaria a campanha e relançaria com o novo texto. Se o usuário tiver outra sessão, receberá imediatamente o novo cartão.

##### Opção 2: Parar e relançar a mesma campanha

{% alert tip %}
Recomendamos usar esta opção para mensagens únicas em uma central de notificações ou caixa de mensagens (como promoções), quando é importante que a análise de dados esteja unificada, ou quando a pontualidade da mensagem não é uma preocupação (ou seja, os destinatários existentes podem esperar pela janela de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

Essa abordagem mantém toda a sua análise de dados unificada em uma única campanha. Usuários recém-elegíveis receberão o novo cartão, mas isso atrasa a atualização para os destinatários existentes até que se tornem re-elegíveis:

1. Pare sua campanha e, quando solicitado, selecione **Remover cartão após a próxima sincronização**.
2. Edite sua campanha conforme necessário.
3. Reinicie sua campanha.

###### Impacto

* **Destinatários existentes:** Os usuários que já receberam o cartão não receberão os cartões atualizados até que se tornem elegíveis novamente. Se a re-elegibilidade estiver desativada, eles nunca receberão o novo cartão.
* **Relatórios:** Uma campanha conterá toda a análise de dados de relatórios para as versões de cartões lançadas. A Braze não diferenciará entre as versões lançadas.

Digamos que você tenha uma campanha disparada pelo início de uma sessão com re-elegibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você quer alterar o texto. Primeiro, pare a campanha e remova o cartão do feed. Depois, republique a campanha com o novo texto. Se o usuário tiver outra sessão, receberá o novo cartão em 28 dias.

#### Removendo e expirando cartões

##### Remoção manual de cartões

Você pode remover manualmente cartões dos feeds de todos os usuários a qualquer momento, parando a campanha.

1. Abra a campanha do cartão de conteúdo e selecione Parar campanha.
2. Quando solicitado, selecione **Remover cartão após a próxima sincronização**. O cartão será removido na próxima atualização do feed.

##### Remoção automatizada de cartões {#action-based-card-removal}

Você pode remover automaticamente um cartão quando um usuário realiza uma ação específica, como completar uma compra ou ativar um recurso.

Na sua campanha ou etapa do canva, especifique um evento de remoção. Quando um usuário realiza esse evento, o cartão será removido do feed dele em uma atualização subsequente após a Braze processar o evento.

{% alert note %}
Essa remoção não é instantânea. Há um atraso no processamento, então pode levar vários minutos e mais de uma atualização do feed para o cartão desaparecer.
{% endalert %}

{% alert tip %}
É possível especificar vários eventos personalizados e compras que devem remover um cartão do feed de um usuário. Quando **qualquer uma** dessas ações for executada pelo usuário, todos os cartões existentes enviados pela campanha serão removidos. Todos os cartões elegíveis futuros continuarão a ser enviados de acordo com a programação da mensagem.
{% endalert %}

![Painel de Condições de Remoção de Cartão de Conteúdo com a opção de Evento de Remoção de Cartão de Conteúdo.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiração do cartão

Os Cartões de conteúdo permanecem disponíveis por até 30 dias a partir do momento em que são enviados; após 30 dias, a Braze os remove dos feeds dos usuários e os exclui dos sistemas da Braze.

#### Fazendo os cartões durarem mais de 30 dias

{% alert tip %}
Para casos de uso que exigem que as mensagens persistam por mais de 30 dias, considere usar Banners. Os Banners são projetados para persistência e não têm uma data de expiração obrigatória, permitindo que permaneçam visíveis enquanto forem necessários.
{% endalert %}

Se você quiser que um cartão pareça sempre disponível (ou seja, dure mais do que o máximo de 30 dias), você pode criar uma campanha recorrente que efetivamente substitui o cartão a cada 30 dias:

1. Defina a duração do cartão de conteúdo para 30 dias.
2. Defina a re-elegibilidade da campanha para 30 dias.
3. Defina a campanha para disparar no "Início da sessão".