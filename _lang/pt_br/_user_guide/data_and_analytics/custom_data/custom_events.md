---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 9
page_type: reference
description: "Este artigo descreve eventos e propriedades personalizados, segmentação, uso, propriedades de entrada no canva, onde visualizar análises de dados relevantes e muito mais."
search_rank: 2
---

# [![Curso do Braze Learning] ( {% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados

> Este artigo descreve eventos e propriedades personalizados, filtros de segmentação relacionados, propriedades de entrada do Canva, análises de dados relevantes e muito mais. Para saber mais sobre os eventos do Braze em geral, consulte [Eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events).

Os eventos personalizados são ações realizadas por seus usuários ou atualizações sobre eles. Quando os eventos personalizados são registrados, eles podem disparar qualquer número e tipo de campanhas de acompanhamento. Em seguida, é possível usar os [filtros de segmentação](#segmentation-filters) para segmentar os usuários com base na frequência e na frequência com que esses eventos personalizados ocorreram recentemente. Isso faz com que os eventos personalizados sejam mais adequados para o rastreamento de interações de alto valor com o usuário dentro do seu aplicativo.

## Casos de uso

Alguns casos de uso comuns de eventos personalizados incluem:
- Acionamento de uma campanha ou Canva com base em um evento personalizado usando a [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmentação de usuários por quantas vezes eles realizaram um evento personalizado, quando foi a última vez que o evento ocorreu e similares
- Usar a [análise de eventos personalizada]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) do dashboard para visualizar um agregado da frequência com que cada evento ocorreu
- Encontrar análises de dados adicionais usando relatórios de [funil]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) e [retenção]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/) 
- Aproveitamento das [propriedades de entrada persistente]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) para usar metadados do evento do cliente para personalização nas etapas do Canva
- Geração de análises de dados mais sofisticadas com o [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)
- Configuração de [eventos de exceção]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) do Canvas para definir quando os usuários não devem avançar para a próxima etapa do Canva

## Gerenciamento de eventos personalizados

Você pode gerenciar, criar ou colocar em lista de bloqueio eventos personalizados no dashboard acessando **Configurações de dados** > **Eventos personalizados**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **os eventos personalizados** em **Manage Settings (Gerenciar configurações)**.
{% endalert %}

Selecione o menu ao lado de um evento personalizado para as seguintes ações:

### Colocando na lista de bloqueio

Você pode colocar em uma lista de bloqueio eventos personalizados individuais por meio do menu de ações ou selecionar e colocar em uma lista de bloqueio até 10 eventos em massa. 

Quando você bloqueia um evento personalizado:

- Os dados futuros não serão coletados para esse evento.
- Os dados existentes não estarão disponíveis a menos que esse evento seja desbloqueado.
- Esse evento não será exibido em filtros ou gráficos.

Além disso, se um evento personalizado bloqueado for atualmente referenciado por filtros ou disparadores em outras áreas do Braze, será exibido um modal de aviso explicando que todas as instâncias dos filtros ou disparadores que o referenciam serão removidas e arquivadas.

### Adição de descrições

É possível adicionar uma descrição a um evento personalizado depois que ele for criado se você tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Selecione **Editar descrição** para o evento personalizado e insira o que quiser, como uma nota para sua equipe.

## Adição de tags

Você pode adicionar tags a um evento personalizado depois que ele for criado se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Manage Events, Attributes, Purchases" (Gerenciar eventos, atributos e compras). As tags podem então ser usadas para filtrar a lista de eventos. 

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

### Visualização de relatórios de uso

O relatório de uso lista todos os canvas, campanhas e segmentos que usam um evento personalizado específico. A lista não inclui os usos do Liquid. 

Você pode visualizar até 10 relatórios de utilização ao mesmo tempo, marcando as caixas de seleção de vários eventos personalizados e, em seguida, selecionando **Exibir relatório de utilização**.

## Exportação de dados

Para exportar a lista de eventos personalizados como um arquivo CSV, selecione o botão **Exportar tudo** na parte superior da página. O arquivo CSV será gerado e um link para baixar será enviado para você por e-mail.

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

## Registro de eventos personalizados

Os eventos personalizados exigem configuração adicional. Consulte a lista abaixo para obter a documentação sobre cada plataforma, onde encontrará informações sobre os métodos usados para registrar eventos personalizados e como adicionar propriedades e quantidades aos seus eventos personalizados.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Armazenamento de eventos personalizados

Todos os dados armazenados no **perfil do usuário**, inclusive os metadados de eventos personalizados (primeira ou última ocorrência, contagem total e X em Y durante 30 dias), são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtros de segmentação

A tabela a seguir mostra os filtros disponíveis para segmentar usuários por eventos personalizados.

| Opções de segmentação | Filtro suspenso | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o evento personalizado ocorreu **mais de um número X de vezes** | **MAIS DO QUE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu **menos de um número X de vezes** | **MENOS QUE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu **exatamente X vezes** | **EXATAMENTE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu pela última vez **após a data X** | **DEPOIS** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **antes da data X** | **ANTES** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **há mais de X dias** | **MAIS DO QUE** | **NÚMERO DE DIAS ANTES** (número positivo) |
| Verificar se o evento personalizado ocorreu pela última vez **há menos de X dias** | **MENOS QUE** | **NÚMERO DE DIAS ANTES** (número positivo) |
| Verificar se o evento personalizado ocorreu **mais de X (máx. = 50) vezes** | **MAIS DO QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **menos de X (máx. = 50) vezes** | **MENOS QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **exatamente X (máx. = 50) vezes** | **EXATAMENTE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Análise de dados

O Braze nota o número de vezes que os eventos personalizados ocorreram e a última vez que foram realizados por cada usuário para segmentação. Visualize essas análises de dados acessando **Analytics** > **Relatório de eventos personalizados**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar o relatório **Eventos personalizados** em **Dados**.
{% endalert %}

Na página **Custom Events Report (Relatório de eventos personalizados)** no dashboard, você pode visualizar de forma agregada a frequência com que cada evento personalizado ocorre. As linhas cinzas sobrepostas na série temporal indicam a última vez que uma campanha foi enviada, o que é útil para visualizar como suas campanhas afetaram a atividade do evento personalizado.

![Gráfico de contagens de eventos personalizados na página Eventos personalizados no dashboard, mostrando as tendências de um evento personalizado][8]

Também é possível usar **filtros** para dividir os eventos personalizados por hora, usuários médios mensais (MAU), segmentos ou fórmulas de KPI. 

![Filtros de gráficos de eventos personalizados][9]{: style="max-width:40%;"}

{% alert tip %}
[Incremente os atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) para manter um contador em uma ação do usuário semelhante a um evento personalizado. No entanto, não é possível visualizar dados de atributos personalizados em uma série temporal. As ações do usuário que não precisam ser analisadas em uma série temporal devem ser registradas usando esse método.
{% endalert %}

### Por que a análise de dados de eventos personalizados não está sendo exibida

Os segmentos criados com dados de eventos personalizados não podem mostrar dados históricos anteriores à sua criação.

## Propriedades de eventos personalizados

As propriedades de eventos personalizados são metadados ou atributos personalizados de eventos que descrevem uma ocorrência específica de um evento. Essas propriedades podem ser usadas para qualificar ainda mais as condições de disparo, aumentar a personalização no envio de mensagens, rastrear conversões e gerar análises mais sofisticadas por meio da exportação de dados brutos.

As propriedades de eventos personalizados não são armazenadas no perfil do Braze e, portanto, não consomem pontos de dados (consulte [Pontos de dados](#data-points) para exceções).

{% alert important %}
Cada evento personalizado ou compra pode ter até 256 propriedades distintas de evento personalizado. Se um evento personalizado ou uma compra for registrado com mais de 256 propriedades, apenas as primeiras 256 serão capturadas e estarão disponíveis para uso.
{% endalert %}

### Formato esperado

Os valores de propriedade devem ser um objeto em que as chaves são os nomes de propriedade e os valores são os valores de propriedade. Os nomes de propriedades devem ser strings não vazias com 255 caracteres ou menos, sem cifrões à esquerda (`$`).

Os valores de propriedade podem ser qualquer um dos seguintes tipos de dados:

| Tipo de dados | Descrição |
| --- | --- |
| Números | Como [números inteiros](https://en.wikipedia.org/wiki/Integer) ou [flutuantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | Valor de `true` ou `false`. |
| Datetimes | Formatado como strings no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Não é compatível com matrizes. |
| Strings | 255 caracteres ou menos. |
| Matrizes | As matrizes não podem incluir datas e horários. |
| Objetos | Os objetos serão ingeridos como strings. |
| Objetos aninhados | Objetos que estão dentro de outros objetos. Para saber mais, consulte a seção deste artigo sobre [objetos aninhados](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Os objetos de propriedade de evento que contêm valores de vetor ou objeto podem ter uma carga útil de propriedade de evento de até 100 KB.

É possível alterar o tipo de dados da propriedade do evento personalizado, mas esteja ciente dos impactos da [alteração dos tipos de dados]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) após a coleta dos dados.

### Uso de propriedades de eventos personalizados

As propriedades de eventos personalizados podem ser usadas para qualificar os disparos de campanhas, rastrear conversões e personalizar o envio de mensagens.

#### Mensagens de gatilho

Use as propriedades de eventos personalizados para restringir ainda mais seu público para uma determinada campanha ou Canva. Por exemplo, se você tiver um aplicativo de comércio eletrônico e quiser enviar uma mensagem a um usuário quando ele abandonar o carrinho, poderá adicionar uma propriedade de evento personalizado de `cart value` para melhorar o público-alvo e permitir maior personalização da campanha.

![Filtros de propriedades de eventos personalizados para um cartão abandonado. Dois filtros são combinados com um operador AND para enviar essa campanha aos usuários que abandonaram o cartão com um valor de carrinho entre 100 e 200 dólares][16]

As propriedades de eventos personalizados aninhados também são suportadas na [entrega baseada em ação][19].

![Filtros de propriedades de eventos personalizados para um cartão abandonado. Um filtro é selecionado se algum item do carrinho tiver um preço superior a 100 dólares.][20]

#### Personalização de mensagens

Você também pode usar propriedades de eventos personalizados para personalização no modelo de envio de mensagens. Qualquer campanha que use [entrega baseada em ação][19] com um evento de gatilho pode usar propriedades de evento personalizado desse evento para personalização de envio de mensagens.

Por exemplo, se você tiver um app de jogos e quiser enviar uma mensagem aos usuários que concluíram um nível, poderá personalizar ainda mais sua mensagem com uma propriedade para o tempo que os usuários levaram para concluir esse nível. Nesse exemplo, a mensagem é personalizada para três segmentos diferentes usando a [lógica condicional][18]. A propriedade do evento personalizado chamada `time_spent` pode ser incluída na mensagem chamando ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Se o usuário não tiver uma conexão com a Internet, as mensagens no app disparadas com propriedades de eventos personalizados modelados (por exemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) falharão e não serão exibidas.
{% endalert %}

Para obter uma lista completa de Liquid tags que farão com que as mensagens no app sejam entregues como mensagens in-app modeladas, consulte [Perguntas frequentes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Considerações sobre os filtros

- **Chamadas de API:** Ao fazer chamadas de API e usar o filtro "is blank" (está em branco), uma propriedade de evento personalizado é considerada "em branco" se for excluída da chamada. Por exemplo, se você incluísse `"event_property": ""`, seus usuários seriam considerados "não em branco".
- **Inteiros:** Ao filtrar uma propriedade de evento personalizado de número e o número for muito grande, não use o filtro "exactly". Se um número for muito grande, ele poderá ser arredondado em um determinado comprimento, de modo que seu filtro não funcionará como esperado.

#### Segmentação

Use a segmentação de propriedades de eventos para direcionar os usuários com base em eventos personalizados realizados e nas propriedades associadas a esses eventos. Isso aumenta suas opções de filtragem ao segmentar por compra e eventos personalizados.

As propriedades de eventos personalizados são atualizadas em tempo real para qualquer segmento que as utilize. Você pode gerenciar as propriedades acessando **Configurações de dados** > **Eventos personalizados** e selecionando **Gerenciar propriedades** para o evento personalizado associado. As propriedades de eventos personalizados usadas em determinados filtros de segmento têm um histórico de análise máximo de 30 dias.

{% alert note %}
Se quiser criar segmentos com base na recência e na frequência da propriedade do evento, entre em contato com o gerente de sucesso do cliente para ativar a segmentação para propriedades específicas de eventos personalizados. Quando ativada, você pode acessar opções adicionais de filtragem ao segmentar.
{% endalert %}

Os filtros de segmentação de propriedades de eventos incluem:

- Realizou um evento personalizado com a propriedade A com o valor B, X vezes nos últimos Y dias.
- Fez compras com a propriedade A no valor B, X vezes nos últimos Y dias.
- Adiciona a capacidade de segmentar em 1, 3, 7, 14, 21 e 30 dias.

![Um grupo de filtros que "tem 'Abandono de carrinho' com a propriedade 'número de vezes' e valor '2' 'mais de' 1'1 vez nos últimos '30' dias corridos (720-744 horas)".][3]

Os dados só são registrados para uma determinada propriedade de evento depois que ela é ativada pelo gerente de sucesso do cliente, e as propriedades de evento só ficam disponíveis a partir dessa data.

##### Pontos de dados

Com relação ao uso da inscrição, as propriedades de eventos personalizados ativadas para segmentação com os seguintes filtros são todas contadas como pontos de dados separados, além do ponto de dados contado pelo próprio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriedades de entrada da tela e propriedades de evento

É possível usar `canvas_entry_properties` e `event_properties` em suas jornadas de usuário do Canva. Consulte as [propriedades de entrada do Canva e as propriedades de evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para obter mais informações e exemplos.

{% tabs local %}
{% tab Propriedades de entrada da tela %}

[As propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) são as propriedades que você mapeia para Canvas que são baseadas em ações ou disparadas por API. Note que o objeto `canvas_entry_properties` tem um limite máximo de tamanho de 50 KB.

{% alert note %}
Especificamente para os canais de envio de mensagens no app, o `canvas_entry_properties` só pode ser referenciado no Canvas Flow e no editor original do Canvas se as propriedades de entrada persistente estiverem ativadas no editor original como parte do acesso antecipado anterior.
{% endalert %}

Para o envio de mensagens do Canvas Flow, `canvas_entry_properties` pode ser usado em qualquer etapa do canva com este formato Liquid: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma. 

#### Caso de uso

{% raw %}
Digamos que uma loja de varejo, RetailApp, tenha a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. O RetailApp pode inserir o nome do produto (sapatos) em uma mensagem com o Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

O RetailApp também pode disparar o envio de mensagens específicas para diferentes propriedades do `product_name` em um Canva que direciona os usuários depois que eles acionam um evento de compra. Por exemplo, eles podem enviar mensagens diferentes para os usuários que compraram sapatos e para os usuários que compraram outra coisa, adicionando o seguinte Liquid em uma etapa de Mensagem.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expandir para o editor original do Canva %}

A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível apenas para referência.

Para os canvas criados com o editor original, o site `canvas_entry_properties` pode ser referenciado somente na primeira etapa completa de um canvas.

{% enddetails %}
{% endtab %}

{% tab Propriedades do evento %}

{% alert important %}
Não é possível usar `event_properties` na etapa de envio de mensagens. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes da** etapa de mensagem que inclui `event_properties`.
{% endalert %}

As propriedades de eventos referem-se às propriedades que você define para eventos e compras personalizados. Esses `event_properties` podem ser usados em campanhas com entrega baseada em ação e Canvas.

No Canvas Flow, as propriedades de eventos personalizados e de compra podem ser usadas no Liquid em qualquer etapa de mensagens que siga uma etapa de jornadas de ação. Use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} ao fazer referência a estes `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente Message.

Na primeira etapa de mensagem após uma jornada de ação, você pode usar `event_properties` relacionado ao evento referenciado nessa jornada de ação. Esses `event_properties` só podem ser usados se o usuário realmente realizou a ação (e não foi para o grupo Todos os outros). Você pode ter outras etapas (que não sejam outros caminhos de ação ou etapa de mensagem) entre esses caminhos de ação e a etapa de mensagem.

{% details Expandir para o editor original do Canva %}

A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível apenas para referência.

Para o editor de canva original, `event_properties` não pode ser usado em etapas completas agendadas. No entanto, você pode usar `event_properties` na primeira etapa completa de um Canva baseado em ação, mesmo que a etapa completa esteja programada.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objetos aninhados {#nested-objects}

Você pode usar objetos aninhados (objetos dentro de outro objeto) para enviar dados JSON aninhados como propriedades de eventos e compras personalizados. Esses dados aninhados podem ser usados para modelar informações personalizadas em mensagens, disparar envios de mensagens e segmentar usuários.

Para saber mais, consulte nossa página dedicada a [objetos aninhados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

## Armazenamento de propriedades de eventos personalizados

As propriedades de eventos personalizados são projetadas para ajudá-lo a aumentar a precisão do direcionamento e fazer com que as mensagens pareçam ainda mais personalizadas. As propriedades de eventos personalizados podem ser armazenadas no Braze a curto e longo prazo.

Você pode segmentar com base nos valores das propriedades do evento de duas maneiras:

1. **Dentro de 30 dias:** A equipe de suporte da Braze pode ativar a segmentação de propriedades de eventos com base na frequência e na recorrência de valores específicos de propriedades de eventos nos segmentos Braze. Se quiser aproveitar as propriedades do evento dentro dos segmentos, entre em contato com o executivo de contas do Braze ou com o gerente de sucesso do cliente. Essa opção afetará o uso de dados.<br><br>
2. **Dentro e além de 30 dias:** Para cobrir a segmentação de propriedades de eventos de curto e longo prazo, você pode usar [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Esse recurso segmenta os usuários com base em eventos personalizados e propriedades de eventos rastreados nos últimos dois anos. Essa opção não afetará o uso de dados.

Entre em contato com o gerente de sucesso do cliente Braze para obter recomendações sobre a melhor abordagem, dependendo de suas necessidades específicas.

[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engajamento_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
