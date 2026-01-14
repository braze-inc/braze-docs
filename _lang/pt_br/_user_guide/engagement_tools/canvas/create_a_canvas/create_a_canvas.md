---
nav_title: Criando uma tela
article_title: Criando uma tela
page_order: 0
page_type: reference
description: "Este artigo de referência aborda as etapas necessárias para criar, manter e testar um Canvas."
tool: Canvas
search_rank: 1
---

# Criando uma tela

> Este artigo de referência aborda as etapas necessárias para criar, manter e testar um Canvas. Siga este guia ou confira nosso [curso Canvas Braze Learning](https://learning.braze.com/quick-overview-canvas-setup).

{% details Original Canvas editor %}
Não é mais possível criar ou duplicar Canvases usando a experiência original do Canvas. A Braze recomenda [clonar seus Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) para o editor mais atual.
{% enddetails %}

## Criando uma tela

### Etapa 1: Configurar um novo Canvas 

Primeiro, vá para **Messaging** > **Canvas** e selecione **Create Canvas**.

O construtor do Canvas o guiará passo a passo na configuração do Canvas - desde a nomeação até a definição de eventos de conversão e a inclusão dos usuários certos na jornada do cliente. Selecione cada uma das guias a seguir para visualizar as configurações que podem ser ajustadas para cada etapa do construtor.

{% tabs local %}
  {% tab Basics %}
    Aqui, você configurará os princípios básicos do Canvas:
    \- Dê um nome ao seu Canvas
    \- Adicionar equipes
    \- Adicionar etiquetas
    \- Atribuir eventos de conversão e escolher seus tipos de eventos e prazos

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Aqui, você decidirá como e quando os usuários entrarão no Canvas:
    \- Programado: Esta é uma entrada no Canvas baseada em tempo
    \- Baseado em ações: Seu usuário entrará no Canvas depois de executar uma ação definida
    \- Acionado pela API: Use uma solicitação de API para inserir usuários em seu Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Aqui, você selecionará seu público-alvo:
    \- Crie seu público-alvo adicionando segmentos e filtros
    \- Ajuste fino da reentrada do Canvas e dos limites de entrada
    \- Veja um resumo de seu público-alvo

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Aqui, você selecionará as configurações de envio do Canvas:
    \- Selecione suas configurações de assinatura
    \- Defina um limite de taxa de envio para suas mensagens do Canvas
    \- Ativar e definir as horas de silêncio

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Aqui, você criará seu Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Aqui, você encontrará o resumo dos detalhes do Canvas. Se o [fluxo de trabalho de aprovação do Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) estiver ativado, você poderá aprovar os detalhes do Canvas listados antes do lançamento.

  {% endtab %}
{% endtabs %}

#### Etapa 1.1: Comece com o básico do Canvas

Aqui, você nomeará seu Canvas, atribuirá [equipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) e criará ou adicionará [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Você também pode atribuir eventos de conversão para o Canvas.

{% alert tip %}
Marque seus Canvases para que seja fácil encontrá-los e criar relatórios a partir deles. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
{% endalert %}

\![A página de detalhes do Canvas, com campos para o nome, a descrição, o local e as tags do Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Selecionar eventos de conversão

Escolha o tipo de evento de conversão e, em seguida, selecione as conversões a serem registradas. Esses [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirão a eficiência de seu Canvas. 

\![Primary Conversion Event A com o tipo de evento de conversão Makes Purchase para registrar conversas de usuários que fazem qualquer compra dentro de um prazo de conversão de três dias.]({% image_buster /assets/img/add_canvas_conversions.png %})

Se o seu Canvas tiver várias variantes ou um grupo de controle, o Braze usará esse evento de conversão para determinar a melhor variação para atingir essa meta de conversão. Usando a mesma lógica, você pode criar vários eventos de conversão.

#### Etapa 1.2: Determine seu cronograma de entrada no Canvas

Você pode escolher uma das três maneiras pelas quais os usuários podem entrar no seu Canvas. 

##### Tipos de programação de entrada

{% tabs local %}
  {% tab Scheduled Delivery %}
    Com a entrega programada, os usuários entrarão em uma programação de tempo, da mesma forma que você programaria uma campanha. Você pode inscrever usuários em um Canvas assim que ele for lançado, inseri-los em sua jornada em algum momento no futuro ou de forma recorrente (diária, semanal ou mensal). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Com a entrega baseada em ação, os usuários entrarão no Canvas e começarão a receber mensagens quando realizarem ações específicas, como abrir seu aplicativo, fazer uma compra ou acionar um evento personalizado.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Com a entrega acionada pela API, os usuários entrarão no Canvas e começarão a receber mensagens depois de terem sido adicionados usando o [ponto de extremidade`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) por meio da API. No painel, você pode encontrar um exemplo de solicitação cURL que faz isso, além de atribuir propriedades opcionais [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) usando o [objeto de propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Depois de selecionar o método de entrega, ajuste as configurações para corresponder ao seu caso de uso e, em seguida, continue definindo o público-alvo.

{% details Deduplicate behavior for Canvases using the original editor %}
Se a janela de reelegibilidade for menor do que a duração máxima do Canvas, um usuário terá permissão para entrar novamente e receber mais de uma mensagem de um componente. No caso extremo em que a reentrada de um usuário atinge o mesmo componente da entrada anterior, o Braze desduplicará as mensagens desse componente. 

Se um usuário entrar novamente no Canvas, chegar ao mesmo componente da entrada anterior e estiver qualificado para uma mensagem in-app para cada entrada, ele receberá a mensagem duas vezes (dependendo da prioridade da mensagem in-app), desde que reabra a sessão duas vezes.
{% enddetails %}

#### Etapa 1.3: Defina seu público-alvo de entrada

Somente os usuários que correspondem aos critérios definidos podem entrar na jornada na etapa **Target Audience**, o que significa que o Braze avalia a elegibilidade do público-alvo **antes que** os usuários entrem na jornada do Canvas. Por exemplo, se você quiser segmentar novos usuários, poderá selecionar um segmento de usuários que usaram seu aplicativo pela primeira vez há menos de uma semana.

Em **Entry Controls**, você pode limitar o número de usuários sempre que o Canvas estiver programado para ser executado. Para Canvases baseados em gatilho de API e baseados em ação, esse limite ocorre a cada hora UTC. 

{% alert important %}
Evite configurar uma campanha baseada em ação ou um Canvas com o mesmo acionador que o filtro de público-alvo (como um atributo alterado ou um evento personalizado realizado). Pode ocorrer uma [condição de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) em que o usuário não esteja no público no momento em que executa o evento de acionamento, o que significa que ele não receberá a campanha nem entrará no Canvas.
{% endalert %}

##### Testar seu público-alvo

Depois de adicionar segmentos e filtros ao seu público-alvo, você pode testar se o seu público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

O campo "User Lookup", que permite pesquisar por ID de usuário externo ou ID Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Seleção de controles de entrada

Os controles de entrada determinam se os usuários têm permissão para entrar novamente em um Canvas. Você também pode limitar o número de pessoas que potencialmente entrariam nesse Canvas por uma cadência selecionada (diariamente, durante toda a vida do Canvas ou sempre que o Canvas for programado). 

Por exemplo, se você selecionar **Limitar volume de entrada** e definir o campo **Máximo de entradas** como 5.000 usuários com **Diário** como a cadência limite, o Canvas só enviará para 5.000 usuários por dia.

A página "Entry Controls" (Controles de entrada) exibe caixas de seleção para "Allow users to re-enter Canvas" (Permitir que os usuários entrem novamente no Canvas) e "Limit entrance volume" (Limitar volume de entrada). O último permite que você defina o máximo de entradas e se deseja limitar diariamente, durante toda a vida do Canvas ou sempre que o Canvas for agendado.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
A Braze não recomenda o uso do recurso **Toda vez que o Canvas for agendado** para aquecimento de IP, pois isso pode levar a um aumento nos volumes de envio.
{% endalert %}

##### Definição de critérios de saída

A configuração dos [critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina quais usuários você deseja que saiam do Canvas. Se um usuário realizar o evento de exceção ou corresponder aos segmentos e filtros, ele não receberá mais nenhuma mensagem.

##### Cálculo da população-alvo

Na seção **Target Population (População-alvo** ), é possível visualizar um resumo do seu público, como os segmentos selecionados e os filtros adicionais, e um detalhamento de quantos usuários podem ser alcançados por canal de mensagens. Para calcular o número exato de usuários alcançáveis em seu público-alvo em vez da estimativa padrão, selecione [Calculate exact statistics (Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics)).

Observe que:

- O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.
- Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.

Para visualizar estatísticas adicionais, como a receita média vitalícia dos usuários-alvo, selecione **Show Additional Statistics (Mostrar estatísticas adicionais**).

Detalhamento da população-alvo com opção de calcular estatísticas exatas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Por que a contagem do público-alvo pode ser diferente da contagem de usuários alcançáveis

{% multi_lang_include segments.md section='Differing audience size' %}

#### Etapa 1.4: Selecione suas configurações de envio

Selecione **Send Settings (Configurações de envio** ) para editar suas configurações de assinatura, ativar a limitação de taxa e ativar o Quiet Hours (Horas de silêncio). Ao ativar [a limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) ou [o limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), você pode aliviar a pressão de marketing exercida sobre seus usuários e garantir que não esteja enviando mensagens demais para eles.

No caso de Canvases direcionados a canais de e-mail e push, talvez você queira limitar o Canvas para que somente os usuários que tenham optado explicitamente por receber a mensagem (excluindo usuários inscritos ou não inscritos). Por exemplo, digamos que você tenha três usuários com status de opt-in diferentes:

- **O usuário A** está inscrito no e-mail e está habilitado para push. Esse usuário não recebe o e-mail, mas receberá o push.
- **O usuário B** optou por receber e-mail, mas não está habilitado para push. Esse usuário receberá o e-mail, mas não receberá o push.
- **O usuário C** optou por receber e-mail e está habilitado para envio. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, defina **as Configurações de assinatura** para enviar esse Canvas para "somente usuários opt-in". Essa opção garantirá que apenas os usuários opt-in recebam seu e-mail, e o Braze enviará seu push apenas para os usuários que têm o push ativado por padrão. 

Essas configurações de assinatura são aplicadas por etapa, o que significa que não há efeito sobre o público-alvo de entrada. Portanto, essa configuração é usada para avaliar a elegibilidade de um usuário para receber cada etapa do Canvas.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Target Audience** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Se desejar, especifique o Quiet Hours (horário em que as mensagens não serão enviadas) para seu Canvas. Marque **Ativar horas de silêncio** em suas **Configurações de envio**. Em seguida, selecione o horário de silêncio no horário local do usuário e a ação a ser seguida se a mensagem for acionada dentro desse horário de silêncio.

A página "Quiet Hours" exibe uma caixa de seleção para ativar as horas de silêncio. Se ativado, a hora de início, a hora de término e o comportamento de fallback podem ser definidos.]({% image_buster /assets/img/quiet_hours.png %})

### Etapa 2: Crie seu Canvas

{% alert tip %}
Economize tempo e agilize a criação de seu Canvas usando [os modelos do Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Navegue em nossa biblioteca de modelos pré-criados para encontrar um que se adapte ao seu caso de uso e personalize-o para atender às suas necessidades específicas.
{% endalert %}

#### Etapa 2.1: Adicionar uma variante

O botão "Add Variant" (Adicionar variante) foi selecionado para mostrar um menu de contexto com a opção "Add Variant" (Adicionar variante).]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecione **Add Variant (Adicionar variante**) e adicione uma nova variante ao seu Canvas. As variantes representam uma jornada que seus usuários percorrerão e podem conter várias etapas e ramificações.

Você pode adicionar outras variantes selecionando o botão <i class="fas fa-plus-circle"></i> plus. Ao adicionar novas variantes, você poderá ajustar como seus usuários serão distribuídos entre elas para que possa comparar e analisar a eficácia de diferentes estratégias de envolvimento.

\![Dois exemplos de variantes em um Braze Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por padrão, a atribuição da variante do Canvas é bloqueada quando os usuários entram no Canvas, o que significa que, se um usuário inserir uma variante pela primeira vez, essa será sua variante sempre que ele entrar novamente no Canvas. No entanto, há maneiras de contornar esse comportamento. <br><br>Para isso, você pode criar um gerador de números aleatórios usando o Liquid, executá-lo no início da entrada do Canvas de cada usuário, armazenar o valor como um atributo personalizado e, em seguida, usar esse atributo para dividir os usuários aleatoriamente.

{% details Expand for steps %}

1. Crie um atributo personalizado para armazenar seu número aleatório. Dê a ele um nome fácil de localizar, como "lottery_number" ou "random_assignment".. Você pode criar o atributo [em seu painel]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) ou por meio de chamadas de API para nosso [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crie uma campanha de webhook no início de seu Canvas. Essa campanha será o meio no qual você criará seu número aleatório e o armazenará como um atributo personalizado. Para obter mais informações, consulte [Criação de um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Defina o URL para nosso endpoint `/users/track`.<br><br>
3. Crie o gerador de números aleatórios. Você pode fazer isso com o código [descrito aqui](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aproveita a hora de entrada exclusiva de cada usuário para criar um número aleatório. Defina o número resultante como uma variável Liquid em sua campanha de webhook.<br><br>
4. Formate a chamada `/users/track` na sua campanha webhook de modo que ela defina o atributo personalizado que você criou na etapa 1 como o número aleatório que você gerou no perfil do usuário atual. Quando essa etapa for executada, você terá criado com êxito um número aleatório que muda sempre que um usuário entra na sua campanha.<br><br>
5. Ajuste as ramificações de seu Canvas para que, em vez de serem divididas por variantes escolhidas aleatoriamente, elas sejam divididas com base nas regras do público. Nas regras de público de cada filial, defina o filtro de público de acordo com seu atributo personalizado. <br><br>Por exemplo, uma ramificação pode ter "lottery_number is less than 3" como filtro de público-alvo, enquanto outra ramificação pode ter "lottery_number is more than 3 and less than 6" como filtro de público-alvo.

{% enddetails %}
{% endalert %}

#### Etapa 2.2: Adicionar etapas do Canvas

Você pode adicionar mais etapas ao seu fluxo de trabalho do Canvas arrastando e soltando componentes da barra lateral **Components (Componentes** ). Ou selecione o botão <i class="fas fa-plus-circle"></i> plus para adicionar um componente com o menu popover.

{% alert tip %}
À medida que você começa a adicionar mais etapas, pode aumentar o nível de zoom para se concentrar nos detalhes ou analisar toda a jornada do usuário. Aumente o zoom com <kbd>Shift</kbd> + <kbd>+</kbd> ou diminua o zoom com <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

\![A janela de pesquisa de componentes adiciona uma etapa de atraso ao Braze Canvas.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Você pode adicionar até 200 etapas em um Canvas. Se seu Canvas exceder 200 etapas, poderão ocorrer problemas de carregamento.
{% endalert %}

##### Duração máxima

À medida que a jornada do seu Canvas aumenta em etapas, a duração máxima é o tempo mais longo possível que um usuário pode levar para concluir esse Canvas. Isso é calculado somando-se os atrasos e as janelas de acionamento de cada etapa para cada variante do caminho mais longo. Por exemplo, se o seu Canvas tiver uma etapa de Atraso com um atraso de 3 dias e uma etapa de Mensagem, a duração máxima do seu Canvas será de 3 dias.

##### Edição de uma etapa

Deseja editar uma etapa da jornada do usuário? Veja como fazer isso de acordo com seu fluxo de trabalho do Canvas!

Você pode editar qualquer etapa do fluxo de trabalho do Canvas selecionando qualquer um dos componentes. Por exemplo, digamos que você queira editar a primeira etapa, um componente [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), em seu fluxo de trabalho para um dia específico. Selecione a etapa para visualizar suas configurações e ajustar seu atraso para 1º de março. Isso significa que, em 1º de março, seus usuários passarão para a próxima etapa do seu Canvas.

\![Um exemplo de etapa "Delay" (Atraso) com o atraso definido como "Until a specific day" (Até um dia específico).]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Ou você pode editar e ajustar rapidamente as **Action Settings (Configurações de ação** ) da etapa [Action Paths (Caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) ) para reter os usuários por um período de tempo. Isso prioriza seu próximo caminho com base nas ações durante esse período de avaliação.

A segunda etapa da tela, "Configurações de ação", com uma janela de avaliação definida como 1 dia.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Os componentes leves do Canvas permitem uma experiência de edição simples, facilitando o ajuste dos detalhes mais finos do seu Canvas. 

##### Mensagens no Canvas

Edite as mensagens em um componente Canvas para controlar as mensagens que uma determinada etapa enviará. O Canvas pode enviar mensagens push por e-mail, celular e web, além de webhooks para integração com outros sistemas. Semelhante às campanhas, você pode usar determinados modelos [do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar suas mensagens.

{% alert tip %}
Você sabia que pode incluir nomes de componentes do Canvas em suas mensagens e modelos de links?<br>
Use a tag `campaign.${name}` Liquid no Canvas para exibir o nome do componente atual do Canvas.
{% endalert %}

O componente Message gerencia as mensagens enviadas aos usuários. Você pode selecionar seus **canais de mensagens** e ajustar **as configurações de entrega** para otimizar suas mensagens do Canvas. Para obter mais detalhes sobre esse componente, consulte [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

A etapa "Set up Messages" (Configurar mensagens), com a opção "Messaging Channels" (Canais de mensagens) selecionada, exibe a lista de canais de mensagens disponíveis, como o Android Push, cartões de conteúdo, e-mail e outros.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecione **Concluído** após terminar de configurar o componente Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

O `canvas_entry_properties` é configurado na etapa Entry Schedule da criação de um Canvas e indica o acionador que insere um usuário em um Canvas. Essas propriedades também podem acessar as propriedades de cargas úteis de entrada em Canvases acionados por API. Observe que o objeto `canvas_entry_properties` pode ter até 50 KB. 

Use o seguinte Liquid ao fazer referência a essas propriedades de entrada: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Observe que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Você pode adicionar a palavra "shoes" (sapatos) a uma mensagem com este Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
As propriedades do evento são as propriedades definidas por você em eventos e compras personalizados. Esses `event_properties` podem ser usados em campanhas com entrega baseada em ação, bem como em Canvases. 

No Canvas, as propriedades de evento personalizado e evento de compra podem ser usadas no Liquid em qualquer etapa de mensagem que siga uma etapa de Caminhos de ação. Use este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} ao fazer referência a estes `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente Message.

Na primeira etapa da mensagem após um caminho de ação, você pode usar o site `event_properties` relacionado ao evento referenciado nesse caminho de ação. Você pode ter outras etapas (que não sejam outros Caminhos de Ação ou etapa de Mensagem) entre essa etapa de Caminhos de Ação e a etapa de Mensagem. Observe que você só terá acesso a `event_properties` se a etapa Mensagem puder ser rastreada até um caminho que não seja Todos os outros em uma etapa Caminho de ação

{% endtab %}
{% endtabs %}

#### Etapa 2.3: Editar conexões

Para mover uma conexão entre etapas, selecione a seta que conecta os dois componentes e selecione um componente diferente. Para remover a conexão, selecione a seta seguida de **Cancelar conexão** no rodapé do compositor do Canvas.

### Etapa 3: Adicionar um grupo de controle

Você pode adicionar um grupo de controle ao seu Canvas selecionando o botão <i class="fas fa-plus-circle"></i> plus para adicionar uma nova variante. 

A Braze acompanhará as conversões dos usuários que forem colocados no grupo de controle, embora eles não recebam nenhuma mensagem. Para preservar um teste preciso, rastrearemos o número de conversões de suas variantes e do grupo de controle exatamente pelo mesmo período de tempo, conforme mostrado na tela de seleção de eventos de conversão. 

Você pode ajustar a distribuição entre suas mensagens clicando duas vezes nos cabeçalhos **Variant Name**.

Neste exemplo, temos nosso Canvas dividido em duas variantes. A variante 1 tem 70% dos usuários. A segunda variante é um grupo de controle com os 30% restantes de usuários.

\![Um exemplo de variante em um Braze Canvas, em que 70% vão para a "Variante 1", que atrasa 1 dia na primeira etapa e, em seguida, envia uma mensagem na segunda etapa. Os outros 30% vão para um "Controle" que não tem nenhuma etapa de acompanhamento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Seleção inteligente para o Canvas

Os recursos de seleção inteligente agora estão disponíveis em Canvases multivariados. Semelhante ao recurso [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para campanhas multivariadas, o Intelligent Selection for Canvas analisa o desempenho de cada variante do Canvas e ajusta a porcentagem de usuários que estão sendo canalizados por meio de cada variante. Essa distribuição é baseada nas métricas de desempenho de cada variante para maximizar o número total esperado de conversões.

Lembre-se de que as telas multivariadas permitem que você teste mais do que o texto, mas também o tempo e os canais. Com o Intelligent Selection, você pode testar Canvases com mais eficiência e ter a certeza de que seus usuários serão enviados para a melhor jornada possível do Canvas.

A opção "Intelligent Selection" (Seleção inteligente) está ativada na página "Edit Variant Distribution" (Editar distribuição de variantes). À medida que analisa e otimiza o Canvas, ele exibe uma barra horizontal na página que é dividida em várias seções, cada uma variando em cor e tamanho. Essa é apenas uma representação visual e não está correlacionada a nenhuma análise específica.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

O Intelligent Selection for Canvas otimiza os resultados do Canvas fazendo ajustes graduais em tempo real na distribuição de usuários classificados em cada variante. Quando o algoritmo estatístico determinar um vencedor decisivo entre suas variantes, ele excluirá as variantes com desempenho inferior e incluirá todos os futuros destinatários qualificados do Canvas nas Variantes vencedoras. 

Por esse motivo, o Intelligent Selection funciona melhor em Canvases que têm novos usuários entrando com frequência.

### Etapa 4: Salvar e iniciar

Quando terminar de criar o Canvas, selecione **Launch Canvas** para salvar e iniciar o Canvas. Depois de lançar seu Canvas, você poderá ver as análises da sua jornada à medida que elas chegam na página **Detalhes do Canvas**. 

Você também pode salvar seu Canvas como rascunho se precisar voltar a ele.

\![Um exemplo de tela no Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Precisa fazer edições em seu Canvas após o lançamento? Bem, você pode! Confira [Editing Canvases após o lançamento]({{site.baseurl}}/post-launch_edits/) para obter mais informações.
{% endalert %}

