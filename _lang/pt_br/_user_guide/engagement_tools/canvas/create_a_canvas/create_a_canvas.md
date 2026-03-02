---
nav_title: Criar um canva
article_title: Criar um canva
page_order: 0
page_type: reference
description: "Este artigo de referência aborda as etapas necessárias para criar, manter e testar um canva."
tool: Canvas
search_rank: 1
---

# Criar um canva

> Este artigo de referência aborda as etapas necessárias para criar, manter e testar um canva. Siga este guia ou confira nosso [curso do Braze Learning sobre Canvas](https://learning.braze.com/quick-overview-canvas-setup).

{% details Expandir para detalhes do editor original do Canvas %}
Você não pode mais criar ou duplicar canvas usando a experiência original do Canvas. A Braze recomenda [clonar seus canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) para o editor mais atual.
{% enddetails %}

## Criando um canva

### Etapa 1: Configure um novo canva 

Primeiro, acesse **Envio de Mensagens** > **Canvas** e selecione **Criar Canvas**.

O construtor do Canvas o guiará passo a passo na configuração do seu canva — desde a nomeação até a definição de eventos de conversão e a inclusão dos usuários certos na jornada do cliente. Selecione cada uma das guias a seguir para visualizar as configurações que podem ser ajustadas para cada etapa do construtor.

{% tabs local %}
  {% tab Basics %}
    Aqui, você configurará as noções básicas do seu canva:
    - Dê um nome ao seu canva
    - Adicionar equipes
    - Adicionar tags
    - Atribuir eventos de conversão e escolher seus tipos de eventos e prazos

    Saiba mais sobre a [etapa Básico](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Aqui, você decidirá como e quando seus usuários entrarão no seu canva:
    - Programado: Esta é uma entrada no canva baseada em tempo
    - Baseado em ações: Seu usuário entrará no canva depois de executar uma ação definida
    - Disparado pela API: Use uma solicitação de API para inserir usuários em seu canva

    Saiba mais sobre a [etapa Cronograma de Entrada](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Aqui, você selecionará seu público-alvo:
    - Crie seu público adicionando segmentos e filtros
    - Ajuste os limites de entrada e reentrada do canva
    - Veja um resumo do seu público-alvo

    Saiba mais sobre a [etapa Público-Alvo](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Aqui, você selecionará as configurações de envio do canva:
    - Selecione suas configurações de inscrição
    - Defina um limite de frequência de envio para as mensagens do canva
    - Ative e defina o horário de silêncio

    Saiba mais sobre a [etapa Configurações de Envio](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Aqui, você criará seu canva.

    Saiba como [criar seu canva](#step-3-build-your-canvas) usando o construtor do Canvas.
  {% endtab %}
  {% tab Summary %}
    Aqui, você encontrará o resumo dos detalhes do seu canva. Se o [fluxo de trabalho de aprovação do Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) estiver ativado, você poderá aprovar os detalhes do canva listados antes do lançamento.

  {% endtab %}
{% endtabs %}

#### Etapa 1.1: Comece com o básico do canva

Aqui, você nomeará seu canva, atribuirá [equipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) e criará ou adicionará [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Você também pode atribuir eventos de conversão para o canva.

{% alert tip %}
Coloque tags em seus canvas para que seja fácil encontrá-los e criar relatórios a partir deles. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
{% endalert %}

![A página de detalhes do Canvas, com campos para o nome do canva, descrição, local e tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Selecionar eventos de conversão

Escolha o tipo de evento de conversão e, em seguida, selecione as conversões a serem registradas. Esses [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirão a eficiência do seu canva. 

![Evento de conversão primária A com o tipo de evento de conversão Realiza Compra para registrar conversões de usuários que fazem qualquer compra dentro de um prazo de conversão de três dias.]({% image_buster /assets/img/add_canvas_conversions.png %})

Se o seu canva tiver várias variantes ou um grupo de controle, a Braze usará esse evento de conversão para determinar a melhor variação para atingir essa meta de conversão. Usando a mesma lógica, você pode criar vários eventos de conversão.

#### Etapa 1.2: Determine seu cronograma de entrada no canva

Você pode escolher uma das três maneiras pelas quais os usuários podem entrar no seu canva. 

##### Tipos de cronograma de entrada

{% tabs local %}
  {% tab Scheduled Delivery %}
    Com a entrega programada, os usuários entrarão em um cronograma de tempo, da mesma forma que você programaria uma campanha. É possível inscrever usuários em um canva assim que ele for lançado, inseri-los em sua jornada em algum momento no futuro ou de forma recorrente (diária, semanal ou mensal). 

    Neste exemplo, com base nas opções baseadas em tempo, os usuários entrarão neste canva toda terça-feira às 12h no fuso local, toda semana, começando em 14 de novembro de 2025 até 31 de dezembro de 2025.

    ![A página "Cronograma de Entrada" com o tipo definido como "Programado". Devido à seleção, opções baseadas em tempo são exibidas, incluindo frequência, hora de início, recorrência, dias e mais.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Com a entrega baseada em ação, os usuários entrarão no canva e começarão a receber mensagens quando realizarem ações específicas, como abrir seu app, fazer uma compra ou disparar um evento personalizado.

    Você pode controlar outros aspectos do comportamento do canva na janela **Público de Entrada**, incluindo regras de reelegibilidade e configurações de limite de frequência. Note que a entrega baseada em ação não está disponível para componentes do Canvas com mensagens no app.

    ![Um exemplo de entrega baseada em ação. Os usuários entrarão no canva se fizerem uma compra com uma janela de entrada começando às 13h30 em 10 de junho de 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Com o envio disparado pela API, os usuários entrarão no seu canva e começarão a receber mensagens depois de serem adicionados usando o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) por meio da API. No dashboard, você pode encontrar um exemplo de solicitação cURL que faz isso, além de atribuir [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) opcional usando o [objeto de contexto]({{site.baseurl}}/api/objects_filters/context_object/). 

    ![Um exemplo de envio disparado pela API com um ID do Canvas e um exemplo de solicitação cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Você pode usar os seguintes endpoints para envio disparado pela API:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Depois de selecionar o método de entrega, ajuste as configurações para corresponder ao seu caso de uso e, em seguida, continue definindo o público-alvo.

{% details Comportamento de deduplicação para canvas usando o editor original %}
Se a janela de reelegibilidade for menor do que a duração máxima do canva, um usuário terá permissão para entrar novamente e receber mais de uma mensagem de um componente. No caso extremo em que a reentrada de um usuário atinge o mesmo componente da entrada anterior, a Braze desduplicará as mensagens desse componente. 

Se um usuário entrar novamente no canva, chegar ao mesmo componente da entrada anterior e for elegível para uma mensagem no app para cada entrada, ele receberá a mensagem duas vezes (dependendo da prioridade da mensagem no app), desde que reabra a sessão duas vezes.
{% enddetails %}

#### Etapa 1.3: Defina seu público-alvo de entrada

Apenas os usuários que correspondem aos seus critérios definidos podem entrar na jornada na etapa **Público-Alvo**, o que significa que a Braze avalia a elegibilidade do público-alvo primeiro **antes** que os usuários entrem na jornada do canva. Por exemplo, se quiser direcionar novos usuários, poderá selecionar um segmento de usuários que usaram seu app pela primeira vez há menos de uma semana.

Em **Controles de Entrada**, você pode limitar o número de usuários toda vez que o canva estiver programado para ser executado. Para canvas baseados em ações e disparados por API, esse limite ocorre a cada hora UTC. 

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

##### Testar seu público

Depois de adicionar segmentos e filtros ao seu público-alvo, é possível testar se o público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![O campo "Pesquisa de Usuário", que permite que você busque por ID de usuário externo ou ID da Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

##### Seleção de controles de entrada

Os controles de entrada determinam se os usuários têm permissão para entrar novamente em um canva. Você também pode limitar o número de pessoas que potencialmente entrariam neste canva por uma cadência selecionada, dependendo do tipo de cronograma de entrada:

- **Programado:** Duração do canva ou toda vez que o canva estiver programado
- **Baseado em ações:** Por hora, diariamente ou duração do canva
- **Disparado pela API:** Por hora, diariamente ou duração do canva

Por exemplo, se você tiver um canva baseado em ações e selecionar **Limitar volume de entrada** e definir o campo **Entradas máximas** para 5.000 usuários com **Diário** como a cadência limite, então o canva enviará apenas para 5.000 usuários por dia.

![A página "Controles de Entrada" exibindo caixas de seleção para "Permitir que os usuários reentrem no Canvas" e "Limitar volume de entrada". O último permite que você defina as entradas máximas e escolha uma cadência que depende do tipo de cronograma de entrada (por exemplo, duração do canva ou toda vez que o canva estiver programado para entrada programada, e por hora, diariamente ou duração do canva para entrada baseada em ações e disparada pela API).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
A Braze não recomenda selecionar **Toda vez que o Canvas estiver programado** para aquecimento de IP, pois isso pode levar a volumes de envio aumentados.
{% endalert %}

##### Definição de critérios de saída

A configuração dos [critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina quais usuários devem sair de um canva. Se um usuário executar o evento de exceção ou corresponder aos segmentos e filtros, ele não receberá mais mensagens.

##### Cálculo do público-alvo

Na seção **Público-Alvo**, é possível visualizar um resumo do seu público, como os segmentos selecionados e os filtros adicionais, e um detalhamento de quantos usuários podem ser alcançados por canal de envio de mensagens. Para calcular o número exato de usuários alcançáveis em seu público-alvo em vez da estimativa padrão, selecione [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Note que:

- O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.
- Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.

Para visualizar estatísticas adicionais, como a receita média vitalícia dos usuários direcionados, selecione **Mostrar Estatísticas Adicionais**.

![Detalhamento do público-alvo com opção de calcular estatísticas exatas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Por que a contagem do público-alvo pode diferir da contagem de usuários alcançáveis

{% multi_lang_include segments.md section='Differing audience size' %}

#### Etapa 1.4: Selecione suas configurações de envio

Selecione **Configurações de Envio** para editar suas configurações de inscrição, ativar o limite de frequência e ativar o horário de silêncio. Ao ativar a [limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) ou a [limitação de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), você pode aliviar a pressão de marketing sobre seus usuários e garantir que não os sobrecarregue com mensagens.

Para canvas direcionados a canais de e-mail e push, talvez você queira limitar seu canva para que somente os usuários com aceitação explícita recebam a mensagem (excluindo usuários inscritos ou que cancelaram a inscrição). Por exemplo, digamos que você tenha três usuários com status de aceitação diferentes:

- **O usuário A** está inscrito no e-mail e tem push ativado. Esse usuário não recebe o e-mail, mas receberá o push.
- O **usuário B** tem aceitação de e-mail, mas não tem push ativado. Esse usuário receberá o e-mail, mas não receberá o push.
- O **usuário C** tem aceitação de e-mail e está com push ativado. Esse usuário receberá tanto o e-mail quanto o push.

Para fazer isso, defina as **Configurações de Inscrição** para enviar esse canva como "apenas usuários que aceitaram". Essa opção garantirá que apenas os usuários com aceitação receberão seu e-mail, e a Braze enviará seu push apenas para os usuários que estiverem com push ativado por padrão. 

Essas configurações de inscrição são aplicadas por etapa, o que significa que não há efeito sobre o público de entrada. Portanto, essa configuração é usada para avaliar a elegibilidade de um usuário para receber cada etapa do canva.

{% alert important %}
Com esta configuração, não inclua filtros na etapa **Público-Alvo** que limitem o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Se desejar, especifique o horário de silêncio (o período durante o qual as mensagens não serão enviadas) para o canva. Marque **Ativar Horário de Silêncio** em suas **Configurações de Envio**. Em seguida, selecione o horário de silêncio no fuso local do usuário e a ação a ser seguida se a mensagem for disparada dentro desse horário de silêncio.

![A página "Horário de Silêncio" exibe uma caixa de seleção para ativar o horário de silêncio. Se ativada, a hora de início, a hora de término e o comportamento de fallback podem ser definidos.]({% image_buster /assets/img/quiet_hours.png %})

### Etapa 2: Crie seu canva

{% alert tip %}
Economize tempo e agilize a criação do seu canva usando os [modelos do Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Navegue em nossa biblioteca de modelos pré-criados para encontrar um que se adapte ao seu caso de uso e personalize-o para atender às suas necessidades específicas.
{% endalert %}

#### Etapa 2.1: Adicione uma variante

![O botão "Adicionar Variante" selecionado para mostrar um menu de contexto com a opção "Adicionar Variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecione **Adicionar Variante** e adicione uma nova variante ao seu canva. As variantes representam uma jornada que seus usuários farão e podem conter várias etapas e ramificações.

Você pode adicionar outras variantes selecionando o botão de mais <i class="fas fa-plus-circle"></i>. Ao adicionar novas variantes, você poderá ajustar como seus usuários serão distribuídos entre elas para comparar e analisar a eficácia de diferentes estratégias de engajamento.

![Dois exemplos de variantes em um Braze Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por padrão, a atribuição da variante do canva é bloqueada quando os usuários entram no canva, o que significa que, se um usuário entrar em uma variante pela primeira vez, essa será sua variante sempre que ele entrar novamente no canva. No entanto, há maneiras de contornar esse comportamento. <br><br>Para isso, é possível criar um gerador de números aleatórios usando Liquid, executá-lo no início da entrada de cada usuário no canva, armazenar o valor como um atributo personalizado e usar esse atributo para dividir os usuários aleatoriamente.

{% details Expandir para ver as etapas %}

1. Crie um atributo personalizado para armazenar seu número aleatório. Nomeie algo fácil de localizar, como "lottery_number" ou "random_assignment". Você pode criar o atributo [no seu dashboard]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) ou por meio de chamadas de API para nosso [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crie uma campanha de webhook no início do seu canva. Essa campanha será o meio no qual você criará seu número aleatório e o armazenará como um atributo personalizado. Consulte [Criar um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) para saber mais. Defina a URL para nosso endpoint `/users/track`.<br><br>
3. Crie o gerador de números aleatórios. Você pode fazer isso com o código [especificado aqui](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aproveita o tempo único de entrada de cada usuário para criar um número aleatório. Defina o número resultante como uma variável Liquid em sua campanha de webhook.<br><br>
4. Formate a chamada `/users/track` em sua campanha de webhook de modo que ela defina o atributo personalizado criado na etapa 1 como o número aleatório gerado no perfil do usuário atual. Quando essa etapa for executada, você terá criado com sucesso um número aleatório que muda cada vez que um usuário entra na sua campanha.<br><br>
5. Ajuste as ramificações do seu canva para que, em vez de serem divididas por variantes escolhidas aleatoriamente, elas sejam divididas com base nas regras do público. Nas regras de público de cada ramificação, defina o filtro de público de acordo com seu atributo personalizado. <br><br>Por exemplo, uma ramificação pode ter "lottery_number é menor que 3" como filtro de público, enquanto outra ramificação pode ter "lottery_number é maior que 3 e menor que 6" como filtro de público.

{% enddetails %}
{% endalert %}

#### Etapa 2.2: Adicione etapas ao canva

Você pode adicionar mais etapas ao fluxo de trabalho do seu canva arrastando e soltando componentes da barra lateral **Componentes**. Ou selecione o botão <i class="fas fa-plus-circle"></i> de mais para adicionar um componente com o menu popover.

{% alert tip %}
À medida que você começa a adicionar mais etapas, pode ajustar o nível de zoom para se concentrar nos detalhes ou observar toda a jornada do usuário. Aumente o zoom com <kbd>Shift</kbd> + <kbd>+</kbd> ou diminua o zoom com <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![A janela de busca de componentes adicionando uma etapa de postergação ao canva da Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Você pode adicionar até 200 etapas em um canva. Se o seu canva exceder 200 etapas, podem ocorrer problemas de carregamento.
{% endalert %}

##### Duração máxima

À medida que a jornada do seu canva aumenta em etapas, a duração máxima é o tempo mais longo possível que um usuário pode levar para concluir esse canva. Isso é calculado pela adição das janelas de postergação e disparo de cada etapa para cada variante da jornada mais longa. Por exemplo, se seu canva tiver uma etapa de postergação com uma postergação de 3 dias e uma etapa de Mensagem, a duração máxima do seu canva será de 3 dias.

##### Edição de uma etapa

Deseja editar uma etapa da jornada do usuário? Veja como fazer isso de acordo com o fluxo de trabalho do seu canva!

Você pode editar qualquer etapa no fluxo de trabalho do seu canva selecionando qualquer um dos componentes. Por exemplo, digamos que você queira editar a primeira etapa, um componente de [Postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), em seu fluxo de trabalho para um dia específico. Selecione a etapa para visualizar suas configurações e ajustar sua postergação para 1º de março. Isso significa que, em 1º de março, seus usuários passarão para a próxima etapa do seu canva.

![Um exemplo de etapa "Postergação" com a postergação definida para "Até um dia específico."]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Ou você pode editar e ajustar rapidamente as **Configurações de Ação** da etapa [Jornadas de Ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) para reter os usuários por um período de tempo. Isso prioriza a próxima jornada com base nas ações durante esse período de avaliação.

![A segunda etapa no canva, "Configurações de Ação", com uma janela de avaliação definida para 1 dia.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Os componentes leves do canva permitem uma experiência de edição simples, facilitando o ajuste dos detalhes mais finos do canva. 

##### Envio de mensagens no canva

Edite as mensagens em um componente do canva para controlar as mensagens que uma etapa específica enviará. O canva pode enviar mensagens de e-mail, push para mobile e web, além de webhooks para integração com outros sistemas. Da mesma forma que as campanhas, você pode usar determinados modelos do [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar suas mensagens.

{% alert tip %}
Você sabia que pode incluir nomes de componentes do canva em suas mensagens e modelos de links?<br>
Use a Liquid tag `campaign.${name}` no canva para exibir o nome do componente atual do canva.
{% endalert %}

O componente Message gerencia as mensagens enviadas aos usuários. Você pode selecionar seus **Canais de Envio de Mensagens** e ajustar as **Configurações de Entrega** para otimizar o envio de mensagens do canva. Para saber mais sobre esse componente, consulte [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![A etapa "Configurar Mensagens", com "Canais de Mensagens" selecionados que exibe a lista de canais de mensagens disponíveis, como push do Android, cartões de conteúdo, e-mail e mais.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecione **Concluído** depois de terminar de configurar o componente do canva.

{% tabs local %}
{% tab Canvas Entry Properties %}

O [objeto `context`]({{site.baseurl}}/api/objects_filters/context_object) é configurado na etapa **Cronograma de Entrada** da criação de um canva e indica o disparo que insere um usuário em um canva. Essas propriedades também podem acessar as propriedades de cargas úteis de entrada em canvas disparados por API. Observe que o objeto `context` pode ter até 50 KB. 

Use o seguinte Liquid ao fazer referência a essas propriedades criadas ao entrar no canva: {% raw %} ``context.${property_name}`` {% endraw %}. Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte solicitação: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Você pode adicionar a palavra "shoes" a uma mensagem com este Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
As propriedades de eventos são as propriedades definidas por você em eventos personalizados e compras. Esses `event_properties` podem ser usados em campanhas com entrega baseada em ação, bem como em canvas. 

No Canvas, propriedades de evento personalizado e evento de compra podem ser usadas em Liquid em qualquer etapa de Mensagem que siga uma etapa de Jornadas de Ação. Use este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} ao fazer referência a esses `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente Message.

Na primeira etapa de Mensagem após uma Jornada de Ação, você pode usar `event_properties` relacionadas ao evento referenciado nessa Jornada de Ação. Você pode ter outras etapas (que não sejam outras Jornadas de Ação ou etapa de Mensagem) entre essa etapa de Jornadas de Ação e a etapa de Mensagem. Note que você só terá acesso a `event_properties` se a etapa de Mensagem puder ser rastreada até uma jornada que não seja Todos os Outros em uma etapa de Jornadas de Ação.

{% endtab %}
{% endtabs %}

#### Etapa 2.3: Editar conexões

Para mover uma conexão entre etapas, selecione a seta que conecta os dois componentes e selecione um componente diferente. Para remover a conexão, selecione a seta seguida de **Cancelar Conexão** no rodapé do criador do canva.

### Etapa 3: Adicionar um grupo de controle

É possível adicionar um grupo de controle ao seu canva selecionando o botão <i class="fas fa-plus-circle"></i> de mais para adicionar uma nova variante. 

A Braze rastreará as conversões dos usuários que forem colocados no grupo de controle, embora eles não recebam nenhuma mensagem. Para preservar um teste preciso, rastrearemos o número de conversões das suas variantes e do grupo de controle exatamente pelo mesmo período de tempo, conforme mostrado na tela de seleção de eventos de conversão. 

Você pode ajustar a distribuição entre suas mensagens clicando duas vezes nos cabeçalhos **Nome da Variante**.

Neste exemplo, temos nosso canva dividido em duas variantes. A Variante 1 tem 70% dos usuários. A segunda variante é um grupo de controle com os 30% restantes de usuários.

![Um exemplo de variante em um Braze Canvas, em que 70% acessam a "Variante 1", que posterga por 1 dia na primeira etapa e, em seguida, envia uma mensagem na segunda etapa. Os outros 30% vão para um "Controle" que não tem nenhuma etapa de acompanhamento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Seleção Inteligente para o Canvas

Os recursos de Seleção Inteligente agora estão disponíveis em canvas multivariantes. Semelhante ao recurso [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para campanhas multivariantes, a Seleção Inteligente para Canvas analisa a performance de cada variante do canva e ajusta a porcentagem de usuários sendo direcionados por cada variante. Essa distribuição é baseada nas métricas de performance de cada variante para maximizar o número total esperado de conversões.

Lembre-se de que os canvas multivariantes permitem que você teste mais do que o texto, mas também o tempo e os canais. Por meio da Seleção Inteligente, é possível testar canvas com mais eficiência e ter a certeza de que seus usuários serão direcionados para a melhor jornada de canva possível.

![A opção "Seleção Inteligente" está ativada na página "Editar Distribuição de Variantes". Ao analisar e otimizar o canva, ela exibe uma barra horizontal na página que é dividida em várias seções, cada uma variando em cor e tamanho. Esta é apenas uma representação visual e não se correlaciona a nenhuma análise de dados específica.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

A Seleção Inteligente para Canvas otimiza os resultados do canva, fazendo ajustes graduais em tempo real na distribuição de usuários classificados em cada variante. Quando o algoritmo estatístico determina um vencedor decisivo entre suas variantes, ele descartará as variantes de baixo desempenho e alocará todos os futuros destinatários elegíveis do canva nas Variantes Vencedoras. 

Por esse motivo, a Seleção Inteligente funciona melhor em canvas que têm novos usuários entrando com frequência.

### Etapa 4: Salvar e lançar

Quando terminar de criar o canva, selecione **Lançar Canvas** para salvar e iniciar o canva. Depois de lançar o canva, você poderá visualizar a análise de dados da sua jornada à medida que eles chegam na página **Detalhes do Canvas**. 

Você também pode salvar seu canva como rascunho se precisar voltar a ele.

![Um exemplo de canva na Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Precisa fazer edições em seu canva após o lançamento? Bem, você pode! Para saber mais, confira [Editando canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}