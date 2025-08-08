---
nav_title: Criando uma tela
article_title: Criando uma tela
page_order: 0
page_type: reference
description: "Este artigo de referência aborda as etapas necessárias para criar, manter e testar um canva."
tool: Canvas
search_rank: 1
---

# Criando uma tela

> Este artigo de referência aborda as etapas necessárias para criar, manter e testar um canva. Siga este guia ou confira nosso [curso do Braze Learning sobre canvas](https://learning.braze.com/quick-overview-canvas-setup).

{% details Editor de tela original %}
Não é mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda a [clonagem de suas telas para o Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% enddetails %}

## Criando uma tela

### Etapa 1: Configurar um novo Canvas 

Primeiro, acesse Envio **de mensagens** > **Canvas** e selecione **Criar Canvas**.

O construtor do Canvas o guiará passo a passo na configuração do Canva, desde a nomeação até a definição de eventos de conversão e a inclusão dos usuários certos na jornada do cliente. Selecione cada uma das guias a seguir para visualizar as configurações que podem ser ajustadas para cada etapa do construtor.

{% tabs local %}
  {% tab Noções básicas %}
    Aqui, você configurará as noções básicas do seu Canva:
    \- Dê um nome à sua tela
    \- Adicionar equipes
    \- Adicionar tags
    \- Atribuir eventos de conversão e escolher seus tipos de eventos e prazos

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Cronograma de entrada %}
    Aqui, você decidirá como os usuários entrarão no seu Canva:
    \- Programado: Esta é uma entrada no Canva baseada em tempo
    \- Baseado em ações: Seu usuário entrará no Canva depois de executar uma ação definida
    \- Disparado pela API: Use uma solicitação de API para inserir usuários em seu Canva

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Público alvo %}
    Aqui, você selecionará seu público-alvo:
    \- Crie seu público adicionando segmentos e filtros
    \- Ajuste fino dos limites de entrada e reentrada do Canva
    \- Veja um resumo de seu público-alvo

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Configurações de envio %}
    Aqui, você selecionará as configurações de envio do canva:
    \- Selecione suas configurações de inscrição
    \- Defina um limite de frequência de envio para suas mensagens do Canva
    \- Ativar e definir o horário de silêncio

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Criar canvas %}
    Aqui, você criará sua Canva.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Resumo %}
    Aqui, você encontrará o resumo dos detalhes do seu Canva. Se o [fluxo de trabalho de aprovação do Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) estiver ativado, você poderá aprovar os detalhes do Canva listados antes do lançamento.

  {% endtab %}
{% endtabs %}

#### Etapa 1.1: Comece com o básico do canva

Aqui, você nomeará seu Canvas, atribuirá [equipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) e criará ou adicionará [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Você também pode atribuir eventos de conversão para o Canva.

{% alert tip %}
Coloque tags em suas telas para que seja fácil encontrá-las e criar relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
{% endalert %}

![A página de detalhes do Canvas, com campos para o nome, a descrição, o local e as tags do Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Selecionar eventos de conversão

Escolha o tipo de evento de conversão e, em seguida, selecione as conversões a serem registradas. Esses [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirão a eficiência de seu Canva. 

![Evento de conversão primária A com o tipo de evento de conversão Makes Purchase para registrar conversas de usuários que fazem qualquer compra dentro de um prazo de conversão de três dias.]({% image_buster /assets/img/add_canvas_conversions.png %})

Se a sua tela tiver várias variantes ou um grupo de controle, o Braze usará esse evento de conversão para determinar a melhor variação para atingir essa meta de conversão. Usando a mesma lógica, você pode criar vários eventos de conversão.

#### Etapa 1.2: Determine seu cronograma de entrada no Canva

Você pode escolher uma das três maneiras pelas quais os usuários podem entrar no seu Canva. 

##### Tipos de programação de entrada

{% tabs local %}
  {% tab Entrega programada %}
    Com a entrega programada, os usuários entrarão em uma programação de tempo, da mesma forma que você programaria uma campanha. É possível inscrever usuários em um Canva assim que ele for lançado, inseri-los em sua jornada em algum momento no futuro ou de forma recorrente (diária, semanal ou mensal). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Entrega baseada em ação %}
    Com a entrega baseada em ação, os usuários entrarão no Canvas e começarão a receber mensagens quando realizarem ações específicas, como abrir seu app, fazer uma compra ou disparar um evento personalizado.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab Entrega disparada por API %}
    Com o envio disparado pela API, os usuários entrarão no seu Canva e começarão a receber mensagens depois de serem adicionados usando o [ponto de extremidade`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) por meio da API. No dashboard, você pode encontrar um exemplo de solicitação cURL que faz isso, além de atribuir propriedades opcionais [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) usando o [objeto de propriedades de entrada do Canva]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Depois de selecionar o método de entrega, ajuste as configurações para corresponder ao seu caso de uso e, em seguida, continue definindo o público-alvo.

{% details Comportamento de deduplicação para Canvas usando o editor original %}
Se a janela de reelegibilidade for menor do que a duração máxima do Canva, um usuário terá permissão para entrar novamente e receber mais de uma mensagem de um componente. No caso extremo em que a reentrada de um usuário atinge o mesmo componente da entrada anterior, a Braze desduplicará as mensagens desse componente. 

Se um usuário entrar novamente no Canvas, chegar ao mesmo componente da entrada anterior e for elegível para uma mensagem no app para cada entrada, ele receberá a mensagem duas vezes (dependendo da prioridade da mensagem no app), desde que reabra a sessão duas vezes.
{% enddetails %}

#### Etapa 1.3: Defina seu público-alvo de entrada

Você pode definir o público-alvo do seu canva na etapa **Público-alvo** do canva. Somente os usuários que correspondem aos critérios definidos podem entrar na jornada, o que significa que o Braze avalia a elegibilidade do público-alvo antes que os usuários entrem na jornada do Canva. Por exemplo, se quiser direcionar novos usuários, poderá selecionar um segmento de usuários que usaram seu app pela primeira vez há menos de uma semana.

Em **Controles de entrada**, é possível limitar o número de usuários sempre que o Canva for programado para ser executado. Para canvas baseados em ações e disparos de API, esse limite ocorre a cada hora UTC. 

{% alert warning %}
Evite configurar uma campanha baseada em ação ou o Canva com o mesmo disparo do filtro de público (como um atributo alterado ou a realização de um evento personalizado). Pode ocorrer uma condição de corrida em que o usuário não esteja no público no momento em que executar o evento de gatilho, o que significa que ele não receberá a campanha nem entrará no Canva.  
{% endalert %}

##### Testar seu público

Depois de adicionar segmentos e filtros ao seu público-alvo, é possível testar se o público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![O campo "User Lookup", que permite pesquisar por ID de usuário externo ou ID do Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Seleção de controles de entrada

Os controles de entrada determinam se os usuários têm permissão para entrar novamente em um Canva. Você também pode limitar o número de pessoas que potencialmente entrariam nesse Canva por uma cadência selecionada (diariamente, durante toda a vida do Canvas ou sempre que o Canvas for programado). 

Por exemplo, se você selecionar **Limitar volume de** **envios** e definir o campo **Máximo de entradas** como 5.000 usuários com **Diário** como a cadência limite, o Canva enviará apenas para 5.000 usuários por dia.

![A página "Entry Controls" (Controles de entrada) exibe caixas de seleção para "Allow users to re-enter Canva" (Permitir que os usuários entrem novamente no Canvas) e "Limit entrance volume" (Limitar volume de envios). O último permite que você defina o máximo de entradas e se deseja limitar diariamente, durante toda a vida do Canvas ou toda vez que o Canvas for agendado.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze não recomenda o uso do recurso **Toda vez que o Canva for programado** para aquecimento de IP, pois isso pode levar a um aumento nos volumes de envio.
{% endalert %}

##### Definição de critérios de saída

A configuração dos [critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina quais usuários devem sair de um Canva. Se um usuário executar o evento de exceção ou corresponder aos segmentos e filtros, ele não receberá mais mensagens.

##### Cálculo do público-alvo

Na seção **Público-alvo**, é possível visualizar um resumo do seu público, como os segmentos selecionados e os filtros adicionais, e um detalhamento de quantos usuários podem ser alcançados por canal de envio de mensagens. Para calcular o número exato de usuários alcançáveis em seu público-alvo em vez da estimativa padrão, selecione [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Note que:

- O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.
- Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.

Para visualizar estatísticas adicionais, como a receita média vitalícia dos usuários direcionados, selecione **Show Additional Statistics (Mostrar estatísticas adicionais)**.

![Detalhamento do público-alvo com opção de calcular estatísticas exatas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Por que a contagem do público-alvo pode ser diferente da contagem de usuários alcançáveis

{% multi_lang_include segments.md section='Diferentes tamanhos de público' %}

#### Etapa 1.4: Selecione suas configurações de envio

Selecione **Send Settings (Configurações de envio** ) para editar suas configurações de inscrição, ativar o limite de frequência e ativar o Horário de silêncio. Ao ativar o [limite]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) [de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping) ou [o teto de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), é possível aliviar a pressão de marketing exercida sobre os usuários e garantir que não haja envio excessivo de mensagens a eles.

Para Canvas direcionados a canais de envio de e-mail e push, talvez você queira limitar seu Canvas para que somente os usuários com aceitação explícita recebam a mensagem (excluindo usuários inscritos ou cancelados). Por exemplo, digamos que você tenha três usuários com status de aceitação diferentes:

- **O usuário A** está inscrito no e-mail e tem a capacitação push ativada. Esse usuário não recebe o e-mail, mas receberá o push.
- O **usuário B** tem aceitação de e-mail, mas não tem a capacitação push ativada. Esse usuário receberá o e-mail, mas não receberá o push.
- O **usuário C** tem aceitação de e-mail e está ativado para push. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, defina as **Configurações de inscrição** para enviar esse canva como "apenas usuários que aceitaram". Essa opção garantirá que apenas os usuários com aceitação receberão seu e-mail, e o Braze enviará seu push apenas para os usuários que estiverem ativados para push por padrão. 

Essas configurações de inscrição são aplicadas por etapa, o que significa que não há efeito sobre o público de entrada. Portanto, essa configuração é usada para avaliar a elegibilidade de um usuário para receber cada etapa do Canva.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Target Audience** que limite o público a um único canal (por exemplo, `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Se desejar, especifique o Horário de silêncio (o tempo durante o qual as mensagens não serão enviadas) para o canva. Marque **Ativar Horário de Silêncio** em suas **Configurações de Envio**. Em seguida, selecione o Horário de silêncio no fuso local do usuário e a ação a ser seguida se a mensagem for disparada dentro desse Horário de silêncio.

![A página "Quiet Hours" exibe uma caixa de seleção para ativar o horário de silêncio. Se ativada, a hora de início, a hora de término e o comportamento de fallback podem ser definidos.]({% image_buster /assets/img/quiet_hours.png %})

### Etapa 2: Crie seu canva

{% alert tip %}
Economize tempo e agilize sua criação de telas usando os [modelos do Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Navegue em nossa biblioteca de modelos pré-criados para encontrar um que se adapte ao seu caso de uso e personalize-o para atender às suas necessidades específicas.
{% endalert %}

#### Etapa 2.1: Adicionar uma variante

![O botão "Add Variant" (Adicionar variante) selecionado para mostrar um menu de contexto com a opção "Add Variant" (Adicionar variante).]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecione **Add Variant (Adicionar variante**) e adicione uma nova variante ao seu Canva. As variantes representam uma jornada que seus usuários farão e podem conter várias etapas e ramificações.

Você pode adicionar outras variantes selecionando o botão de mais <i class="fas fa-plus-circle"></i>. Ao adicionar novas variantes, você poderá ajustar como seus usuários serão distribuídos entre elas para que possa comparar e analisar a eficácia de diferentes estratégias de engajamento.

![Dois exemplos de variantes em um Braze Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por padrão, a atribuição da variante do Canvas é bloqueada quando os usuários entram no Canvas, o que significa que, se um usuário inserir uma variante pela primeira vez, essa será sua variante sempre que ele entrar novamente no Canvas. No entanto, há maneiras de contornar esse comportamento. <br><br>Para isso, é possível criar um gerador de números aleatórios usando o Liquid, executá-lo no início da entrada de cada usuário no Canva, armazenar o valor como um atributo personalizado e usar esse atributo para dividir os usuários aleatoriamente.

{% details Expandir para etapas %}

1. Crie um atributo personalizado para armazenar seu número aleatório. Dê a ele um nome fácil de localizar, como "lottery_number" ou "random_assignment". Você pode criar a atribuição [em seu dashboard]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) ou por meio de chamadas de API para nosso [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crie uma campanha de webhook no início de seu Canva. Essa campanha será o meio no qual você criará seu número aleatório e o armazenará como um atributo personalizado. Para obter mais informações, consulte [Criação de um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Defina o URL para nosso endpoint `/users/track`.<br><br>
3. Crie o gerador de números aleatórios. Você pode fazer isso com o código [descrito aqui](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aproveita a hora de entrada exclusiva de cada usuário para criar um número aleatório. Defina o número resultante como uma variável Liquid em sua campanha de webhook.<br><br>
4. Formate a chamada `/users/track` em sua campanha webhook de modo que ela defina o atributo personalizado criado na etapa 1 como o número aleatório gerado no perfil do usuário atual. Quando essa etapa for executada, você terá criado com sucesso um número aleatório que muda cada vez que um usuário entra na sua campanha.<br><br>
5. Ajuste as ramificações de seu Canva para que, em vez de serem divididas por variantes escolhidas aleatoriamente, elas sejam divididas com base nas regras do público. Nas regras de público de cada filial, defina o filtro de público de acordo com seu atributo personalizado. <br><br>Por exemplo, um ramo pode ter "lottery_number is less than 3" como filtro de público, enquanto outro ramo pode ter "lottery_number is more than 3 and less than 6" como filtro de público.

{% enddetails %}
{% endalert %}

#### Etapa 2.2: Adicionar etapas do Canva

Você pode adicionar mais etapas ao seu fluxo de trabalho do Canva arrastando e soltando componentes da barra lateral **Components (Componentes** ). Ou selecione o botão <i class="fas fa-plus-circle"></i> plus para adicionar um componente com o menu popover.

{% alert tip %}
À medida que você começa a adicionar mais etapas, pode aumentar o nível de zoom para se concentrar nos detalhes ou observar toda a jornada do usuário. Aumente o zoom com <kbd>Shift</kbd> + <kbd>+</kbd> ou diminua o zoom com <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![A janela de pesquisa de componentes adiciona uma etapa do canva do Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert warning %}
Um canva criado com o Canvas Flow pode conter até 200 etapas. Se seu canva exceder 200 etapas, ocorrerão problemas de carregamento.
{% endalert %}

##### Duração máxima

À medida que a jornada do seu Canvas aumenta em etapas, a duração máxima é o tempo mais longo possível que um usuário pode levar para concluir esse Canvas. Isso é calculado pela adição das janelas de postergação e disparo de cada etapa para cada variante da jornada mais longa. Por exemplo, se seu canva tiver uma etapa de atraso com uma postergação de 3 dias e uma etapa de Mensagem, a duração máxima de seu canva será de 3 dias.

##### Edição de uma etapa

Deseja editar uma etapa da jornada do usuário? Veja como fazer isso de acordo com seu fluxo de trabalho do Canva!

Você pode editar qualquer etapa do fluxo de trabalho do Canvas Flow selecionando qualquer um dos componentes. Por exemplo, digamos que você queira editar a primeira etapa, um componente de [postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), em seu fluxo de trabalho para um dia específico. Selecione a etapa para visualizar suas configurações e ajustar sua postergação para 1º de março. Isso significa que, em 1º de março, seus usuários passarão para a próxima etapa do seu canva.

![Um exemplo de etapa "Delay" (Atraso) com a postergação definida como "Until a specific day" (Até um dia específico).]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Ou pode editar e ajustar rapidamente as **configurações de ação** da etapa [Jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) para reter os usuários por um período de tempo. Isso prioriza sua próxima jornada com base nas ações durante esse período de avaliação.

![A segunda etapa do canva, "Configurações de ação", com uma janela de avaliação definida como 1 dia.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Os componentes leves do canva permitem uma experiência de edição simples, portanto, o ajuste dos detalhes mais finos do canva é facilitado. 

##### Envio de mensagens no Canva

Edite as mensagens em um componente do Canva para controlar as mensagens que uma etapa específica enviará. O canva pode enviar mensagens de e-mail, push para mobile e web, além de webhooks para integração com outros sistemas. Da mesma forma que as campanhas, você pode usar determinados modelos [do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar suas mensagens.

{% alert tip %}
Você sabia que pode incluir nomes de componentes do Canva em suas mensagens e modelos de links?<br>
Use a tag `campaign.${name}` Liquid no canva para exibir o nome do componente atual do canva.
{% endalert %}

O componente Message gerencia as mensagens enviadas aos usuários. Você pode selecionar seus **canais de envio de mensagens** e ajustar **as configurações de entrega** para otimizar o envio de mensagens do Canva. Para obter mais detalhes sobre esse componente, consulte [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![A etapa "Set up Messages" (Configurar mensagens), com "Messaging Channels" (Canais de mensagens) selecionado, exibe a lista de canais de envio de mensagens disponíveis, como Android Push, cartões de conteúdo, e-mail e muito mais.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecione **Concluído** depois de terminar de configurar o componente Canva.

{% tabs local %}
{% tab Propriedades de entrada da tela %}

O `canvas_entry_properties` é configurado na etapa do Cronograma de entrada da criação de um canva e indica o disparo que insere um usuário em um canva. Essas propriedades também podem acessar as propriedades de cargas úteis de entrada em canvas disparados por API. Note que o objeto `canvas_entry_properties` pode ter até 50 KB. 

Use o seguinte Liquid ao fazer referência a essas propriedades de entrada: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Você pode adicionar a palavra "sapatos" a uma mensagem com este Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Propriedades do evento %}
As propriedades de eventos são as propriedades definidas por você em eventos personalizados e compras. Esses `event_properties` podem ser usados em campanhas com entrega baseada em ação, bem como em Canvas. 

No Canvas Flow, as propriedades de eventos personalizados e de compra podem ser usadas no Liquid em qualquer etapa de mensagens que siga uma etapa de jornadas de ação. Use este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} ao fazer referência a estes `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente Message.

Na primeira etapa de mensagem após uma jornada de ação, você pode usar `event_properties` relacionado ao evento referenciado nessa jornada de ação. Você pode ter outras etapas (que não sejam outras jornadas de ação ou etapa de mensagem) entre essa etapa de jornadas de ação e a etapa de mensagem. Note que você só terá acesso a `event_properties` se a etapa de Mensagem puder ser rastreada até uma jornada que não seja Todos os Outros em uma etapa de Caminho de Ação.

{% endtab %}
{% endtabs %}

#### Etapa 2.3: Editar conexões

Para mover uma conexão entre etapas, selecione a seta que conecta os dois componentes e selecione um componente diferente. Para remover a conexão, selecione a seta seguida de **Cancelar conexão** no rodapé do criador do canva.

### Etapa 3: Adicionar um grupo de controle

É possível adicionar um grupo de controle ao seu Canva selecionando o botão <i class="fas fa-plus-circle"></i> plus para adicionar uma nova variante. 

O Braze rastreará as conversões dos usuários que forem colocados no grupo de controle, embora eles não recebam nenhuma mensagem. Para preservar um teste preciso, rastrearemos o número de conversões das suas variantes e do grupo de controle exatamente pelo mesmo período de tempo, conforme mostrado na tela de seleção de eventos de conversão. 

Você pode ajustar a distribuição entre suas mensagens clicando duas vezes nos cabeçalhos **Variant Name**.

Neste exemplo, temos nosso canva dividido em duas variantes. A variante 1 tem 70% dos usuários. A segunda variante é um grupo de controle com os 30% restantes de usuários.

![Um exemplo de variante em um Braze Canvas, em que 70% acessam a "Variante 1", que posterga por 1 dia na primeira etapa e, em seguida, envia uma mensagem na segunda etapa. Os outros 30% acessam um "Controle" que não tem nenhuma etapa de acompanhamento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Seleção inteligente para o Canva

Os recursos de Seleção Inteligente agora estão disponíveis em Canvas multivariantes. Semelhante ao recurso [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para campanhas multivariantes, o Intelligent Selection for Canvas analisa a performance de cada variante do Canvas e ajusta a porcentagem de usuários que estão sendo canalizados por meio de cada variante. Essa distribuição é baseada nas métricas de performance de cada variante para maximizar o número total esperado de conversões.

Lembre-se de que as telas multivariantes permitem que você teste mais do que o texto, mas também o tempo e os canais. Por meio do Intelligent Selection, é possível testar Canvas com mais eficiência e ter a certeza de que seus usuários serão enviados para a melhor jornada de Canvas possível.

![A opção "Intelligent Selection" (Seleção inteligente) está ativada na página "Edit Variant Distribution" (Editar distribuição de variantes). Ao analisar e otimizar o Canva, ele exibe uma barra horizontal na página que é dividida em várias seções, cada uma variando em cor e tamanho. Essa é apenas uma representação visual e não está correlacionada a nenhuma análise de dados específica.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

O Intelligent Selection for Canvas otimiza os resultados do Canvas, fazendo ajustes graduais em tempo real na distribuição de usuários classificados em cada variante. Quando o algoritmo estatístico determinar um vencedor decisivo entre suas variantes, ele excluirá as variantes de baixo desempenho e incluirá todos os futuros destinatários elegíveis do Canva nas Variantes vencedoras. 

Por esse motivo, o Intelligent Selection funciona melhor em Canvas que têm novos usuários entrando com frequência.

### Etapa 4: Salvar e lançar

Quando terminar de criar o canva, selecione **Lançar canva** para salvar e iniciar o canvas. Depois de lançar o Canvas, você poderá visualizar a análise de dados da sua jornada à medida que eles chegam na página **Detalhes do Canvas**. 

Você também pode salvar seu Canva como rascunho se precisar voltar a ele.

![Um exemplo de tela em Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Precisa fazer edições em seu Canva após o lançamento? Bem, você pode! Para saber mais, dê [uma]({{site.baseurl}}/post-launch_edits/) olhada no [Editing Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

