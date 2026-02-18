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

Use campanhas para mensagens únicas e simples (como informar os usuários sobre um produto com uma mensagem). Use Canvases para jornadas de usuários em múltiplas etapas (como enviar sugestões de produtos personalizadas com base no comportamento do usuário ao longo do tempo).

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

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Fixar no topo

O Braze exibe um cartão fixado no topo do feed de um usuário e o usuário não pode descartá-lo. Se o feed de um usuário tiver vários cartões fixados, o Braze os ordena cronologicamente. Depois de enviar um cartão, você não pode atualizar retroativamente sua opção fixada. Alterar esta opção após enviar uma campanha afeta apenas envios futuros.

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

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

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

### Limitações de carga útil e feed

Para suportar a performance, os Cartões de Conteúdo têm duas restrições principais: um limite no tamanho da carga útil para cada cartão e um número máximo de cartões que podem aparecer em um feed.

#### Limitações de tamanho para Cartões de Conteúdo

A carga útil de dados total para um único Cartão de Conteúdo não pode exceder 2 KB **depois** que qualquer personalização Liquid é renderizada. Isso inclui:

* Título
* Mensagem
* URL da imagem (o comprimento da própria string da URL, não o tamanho do arquivo da imagem)
* Texto do link
* URLs de link para todas as plataformas especificadas (URLs separadas para iOS, Android e Web contam para o total)
* Pares chave-valor (tanto os nomes das chaves quanto seus valores)

Usar Liquid para puxar longas strings de texto (como de atributos personalizados) pode fazer você exceder o limite. 

O criador da campanha exibirá um aviso se seu conteúdo estático exceder o limite. (Não prevemos o tamanho para conteúdo dinâmico usando Liquid.) **Se o tamanho da mensagem exceder 2 KB, será abortada no momento do envio.** Você pode ver esses abortos no Registro de Atividade da Mensagem com o motivo `Content card maximum size exceeded`.

{% alert important %}
Durante envios de teste, Cartões de Conteúdo que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

Aqui estão algumas melhores práticas para gerenciar o tamanho da carga útil do Cartão de Conteúdo:

* Use encurtadores de URL para links longos. URLs, especialmente aquelas com parâmetros de rastreamento extensos, podem enfrentar problemas de limite de tamanho. Usar um serviço de encurtamento de URL pode reduzir drasticamente a contagem de caracteres e liberar espaço na carga útil.
* Truncar conteúdo dinâmico com Liquid. Ao personalizar cartões com texto dinâmico de atributos de usuário ou chamadas de API, o comprimento do conteúdo pode ser imprevisível. Use proativamente filtros Liquid como `truncate` para limitar o comprimento de qualquer texto dinâmico.
* Seja eficiente com URLs de múltiplas plataformas. O limite de 2 KB inclui as URLs para todas as plataformas que você define. Usar URLs longas e únicas para cada plataforma pode multiplicar o tamanho da carga útil. Se possível, use um único link que funcione em todas as plataformas, ou use encurtadores de URL conforme necessário.
* Considere Banners para um conteúdo mais rico. Para casos de uso que exigem consistentemente grandes quantidades de conteúdo, os Cartões de Conteúdo podem não ser o canal certo. Banners não têm a mesma limitação de carga útil de 2 KB e são mais adequados para embutir conteúdo mais rico diretamente em uma experiência de app ou site.

#### Número de cartões no feed

Cada usuário pode ter até 250 cartões de conteúdo não expirados em seu feed a qualquer momento. Quando esse limite for excedido, o Braze deixará de devolver os cartões mais antigos, mesmo que não tenham sido lidos. Cartões descartados também contam para esse limite, o que significa que um alto número de cartões descartados pode reduzir o espaço disponível para os mais antigos.

Para evitar problemas com o limite de cartões, recomendamos as seguintes melhores práticas:

- **Use datas de expiração mais curtas:** Para campanhas que são sensíveis ao tempo (como uma venda de fim de semana), defina uma data de expiração específica. Dessa forma, os cartões são removidos automaticamente do feed e não contarão para o limite após não serem mais relevantes.
- **Aproveite a remoção baseada em ação:** Configure eventos de remoção para cartões transacionais ou baseados em metas. Por exemplo, um cartão que solicita a um usuário que complete seu perfil deve ser removido assim que um `profile_completed` evento for registrado.
- **Audite campanhas de longa duração:** Revise campanhas recorrentes ou em andamento para garantir que não estejam criando uma experiência ruim para seus usuários, preenchendo o feed com muitos cartões ao longo do tempo.

### Entendendo a re-eligibilidade para Cartões de Conteúdo

A re-eligibilidade determina se e quando um usuário pode receber uma mensagem da mesma campanha mais de uma vez. Para Cartões de Conteúdo, entender como isso funciona é crítico para gerenciar campanhas recorrentes e garantir que os usuários não recebam mensagens duplicadas ou desatualizadas.

{% alert tip %}
Você quer que seu conteúdo dure mais de 30 dias? Experimente [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

#### Como a re-eligibilidade é calculada

Se você ativar a re-elegibilidade, a contagem regressiva para quando um usuário pode "reentrar" em uma campanha começa após o envio da mensagem. O momento específico em que essa contagem regressiva começa depende das configurações de criação do seu cartão:

* Os Cartões de Conteúdo usando [na primeira impressão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) usam o tempo de impressão para calcular a re-elegibilidade.
* Os Cartões de Conteúdo criados no lançamento da campanha ou na entrada da etapa do Canvas usam o tempo de envio ou o tempo de impressão mais recente.

#### A expiração de 30 dias e a re-elegibilidade

Uma fonte comum de confusão é a interação entre a re-elegibilidade da campanha e a expiração automática de 30 dias de todos os Cartões de Conteúdo. 

Todos os Cartões de Conteúdo são automaticamente removidos dos sistemas da Braze 30 dias após serem enviados ou removidos. Se você tiver uma campanha recorrente de longa duração com a re-elegibilidade desativada **off**, um usuário ainda pode receber o mesmo cartão novamente após 30 dias. Quando o cartão original é removido, o sistema não vê mais um registro de que aquele usuário recebeu a campanha, tornando-o elegível novamente na próxima sessão. 

Para que os usuários recebam uma mensagem de uma campanha específica apenas uma vez, adicione um filtro de público à sua campanha ou etapa do Canvas para usuários que não receberam uma mensagem desta campanha. Esse filtro é a maneira mais confiável de evitar envios duplicados de campanhas de longa duração.

### Gerenciando Cartões de Conteúdo ao vivo

Após os Cartões de Conteúdo serem enviados, eles ficam aguardando em uma "caixa de entrada" prontos para serem entregues ao usuário (semelhante ao que acontece com os e-mails). Depois que o conteúdo é puxado para o Cartão de Conteúdo (no momento da exibição), ele não pode ser alterado durante sua vida útil. Isso se aplica mesmo que você esteja chamando uma API através do Conteúdo Conectado, e os dados do endpoint mudem. Esses dados não serão atualizados. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Se você modificar uma campanha, somente os cartões futuros que forem enviados terão a atualização.

#### Atualização de cartões lançados

Para alterar um cartão para usuários que já o receberam, você deve usar um dos seguintes métodos:

##### Opção 1: Duplicar a campanha (recomendado para alterações imediatas)

{% alert tip %}
Recomendamos essa opção para mensagens em que você está mostrando o conteúdo mais recente no cartão, as alterações devem ser mostradas imediatamente ou quando a re-elegibilidade estiver desativada.
{% endalert %}

A primeira abordagem é arquivar a campanha e lançar uma nova campanha duplicada:

1. Pare a campanha original e, quando solicitado, selecione `Remove card after the next sync`.
2. Duplique a campanha, faça suas edições e lance a nova versão.

Quando você duplica a campanha, precisa definir o público para a nova versão. Use filtros de segmentação para controlar quem recebe o cartão atualizado:
* Se os usuários nunca devem ser elegíveis novamente para um cartão de conteúdo, você pode filtrar os usuários que não receberam a versão anterior do cartão de conteúdo definindo o filtro `Received Message from Campaign` para a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser reelegíveis em X dias, você pode definir o filtro para `Last Received Message from specific campaign` como mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

###### Impacto

* **Destinatários existentes:** Os destinatários novos e existentes verão o cartão atualizado na próxima atualização do feed, se forem elegíveis.
* **Relatórios:** Cada versão do cartão teria uma análise de dados separada.

Vamos supor que você tenha configurado uma campanha para ser acionada pelo início de uma sessão, e que tenha a re-elegibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, você arquivaria a campanha e removeria os cartões do feed. Em segundo lugar, você duplicaria a campanha e relançaria com o novo texto. Se o usuário tiver outra sessão, ele receberá imediatamente o novo cartão.

##### Opção 2: Pare e relance a mesma campanha

{% alert tip %}
Recomendamos usar esta opção para mensagens únicas em um centro de notificações ou caixa de mensagens (como promoções), quando é importante que a análise de dados esteja unificada, ou quando a pontualidade da mensagem não é uma preocupação (como os destinatários existentes podem esperar pela janela de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

Essa abordagem mantém todas as suas análises unificadas em uma única campanha. Usuários recém-elegíveis receberão o novo cartão, mas isso atrasa a atualização para os destinatários existentes até que eles se tornem re-elegíveis:

1. Pare sua campanha e, quando solicitado, selecione **Remover cartão após a próxima sincronização**.
2. Edite sua campanha conforme necessário.
3. Reinicie sua campanha.

###### Impacto

* **Destinatários existentes:** Os usuários que já receberam o cartão não receberão os cartões atualizados até que se tornem elegíveis novamente. Se a reelegibilidade for desativada, eles nunca receberão o novo cartão.
* **Relatórios:** Uma campanha conterá todas as análises de dados de relatórios para as versões de cartões lançadas. Braze não diferenciará entre as versões lançadas.

Vamos supor que você tenha uma campanha que é acionada pelo início de uma sessão e tem reeligibilidade definida para 30 dias. Um usuário recebeu a campanha há dois dias e você deseja alterar a cópia. Primeiro, interrompa a campanha e remova o cartão do feed. Em segundo lugar, republicar a campanha com o novo texto. Se o usuário tiver outra sessão, ele receberá o novo cartão em 28 dias.

#### Removendo e expirando cartões

##### Remoção manual de cartões

Você pode remover manualmente cartões para os feeds de todos os usuários a qualquer momento, parando a campanha.

1. Abra a campanha do Cartão de Conteúdo e selecione Parar Campanha.
2. Quando solicitado, selecione **Remover cartão após a próxima sincronização**. O cartão será removido na próxima atualização do feed.

##### Remoção automatizada de cartões {#action-based-card-removal}

Você pode remover automaticamente um cartão quando um usuário realiza uma ação específica, como completar uma compra ou ativar um recurso.

Na sua campanha ou etapa do canva, especifique um evento de remoção. Quando um usuário realiza esse evento, o cartão será removido do feed dele em uma atualização subsequente após o Braze processar o evento. 

{% alert note %}
Essa remoção não é instantânea. Há um atraso no processamento, então pode levar vários minutos e mais de uma atualização do feed para o cartão desaparecer.
{% endalert %}

{% alert tip %}
É possível especificar vários eventos personalizados e compras que devem remover um cartão do feed de um usuário. Quando **qualquer uma** dessas ações for executada pelo usuário, todos os cartões existentes enviados pelos cartões da campanha serão removidos. Todos os cartões elegíveis futuros continuarão a ser enviados de acordo com a programação da mensagem.
{% endalert %}

![Condições do painel de remoção de cartão de conteúdo com a opção de evento de remoção de cartão de conteúdo.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiração do cartão

Os cartões de conteúdo permanecem disponíveis por até 30 dias a partir do momento em que são enviados; após 30 dias, a Braze os remove dos feeds dos usuários e os exclui dos sistemas da Braze.

#### Fazendo os cartões durarem mais de 30 dias

{% alert tip %}
Para casos de uso que exigem que as mensagens persistam por mais de 30 dias, considere usar Banners. Os Banners são projetados para persistência e não têm uma data de expiração obrigatória, permitindo que permaneçam visíveis enquanto forem necessários.
{% endalert %}

Se você quiser que um cartão pareça sempre disponível (i.e., dure mais do que o máximo de 30 dias), você pode criar uma campanha recorrente que efetivamente substitui o cartão a cada 30 dias:

1. Defina a duração do cartão de conteúdo para 30 dias.
2. Defina a reelegibilidade da campanha para 30 dias.
3. Defina a campanha para disparar no "Início da sessão".
