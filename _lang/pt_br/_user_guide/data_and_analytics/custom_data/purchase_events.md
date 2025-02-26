---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 8
page_type: reference
description: "Este artigo de referência descreve eventos e propriedades de compra, seu uso, segmentação, onde visualizar a análise de dados relevante e mais."
search_rank: 3
---

# Eventos de compra

> Saiba mais sobre eventos e propriedades de compra, seu uso, segmentação, onde visualizar a análise de dados relevante e mais.

Eventos de compra são ações de compra realizadas pelos seus usuários. Esses eventos são usados para registrar compras no app e estabelecer o valor do tempo de vida (LTV) para cada perfil de usuário. Esses eventos de compra devem ser configurados pela sua equipe. Registrar eventos de compra permite adicionar propriedades como quantidade e tipo, ajudando a segmentar ainda mais seus usuários com base nessas propriedades.

## Registrando eventos de compra

Você pode registrar compras passando um [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) pelo [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

A seguir estão listados métodos em várias plataformas que são usados para registrar compras. Dentro destas páginas, você também encontrará documentação sobre como adicionar propriedades e quantidades ao seu evento de compra. Você pode segmentar ainda mais seus usuários com base nessas propriedades.

- [Android e FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Visualizando dados de compra

Depois de configurar e começar a registrar eventos de compra, você pode visualizar esses dados de compra no perfil do usuário na [guia Visão Geral]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Usando dados de compra

Existem várias maneiras de usar os dados de compra no Braze:

- **[Segmentação](#purchase-event-segmentation):** Use os dados de compra para criar segmentos de usuários com base em seu comportamento de compra.
- **[Personalização](#personalization):** Use dados de compra para personalizar mensagens para os usuários.
- **[Disparar mensagens](#trigger-messages):** Configure mensagens para disparar com base em eventos de compra.
- **[Análise de dados](#analytics):** Analise seus dados de compra para obter insights sobre o comportamento do usuário e a eficácia de suas campanhas de marketing.

### Segmentação {#purchase-event-segmentation}

Você pode disparar qualquer número ou tipo de campanhas de acompanhamento com base em eventos de compra registrados. Por exemplo, você pode criar um segmento de usuários que fizeram uma compra nos últimos 30 dias, ou um segmento de usuários que gastaram mais de um certo valor.

Os seguintes filtros de segmentação estão disponíveis ao direcionar usuários:

- Primeira compra feita
- Primeira Compra Para App
- Última compra de produto
- Dinheiro gasto
- Produto comprado
- Total de compras
- X Dinheiro Gasto em Y Dias
- Produto X comprado em Y dias
- X Comprar Propriedade em Y Dias
- X compras nos últimos Y dias

Para obter detalhes sobre cada filtro, consulte o glossário [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) e filtre por "Comportamento de compra".

![Filtrando para usuários que fizeram exatamente três compras][1]{: style="max-width:80%;"}

{% alert tip %}
Se você gostaria de segmentar pelo número de vezes que uma compra específica ocorreu, você deve registrar essa compra individualmente como um [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalização

Como qualquer outro tipo de dado que você coleta de seus usuários, você pode usar dados de compra para personalizar seu envio de mensagens através do Liquid. Por exemplo, você pode enviar um e-mail personalizado para um usuário recomendando produtos semelhantes aos que ele acabou de comprar.

Digamos que você tenha uma propriedade de evento de compra chamada `last_purchased_product` que armazena o nome do último produto que um usuário comprou. Você pode usar esta propriedade para personalizar uma mensagem de e-mail assim:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

Neste exemplo, a mensagem é personalizada com base na propriedade `last_purchased_product`. Se o último produto que o usuário comprou foi "Tênis de Corrida", ele recebe uma mensagem recomendando shorts de corrida e garrafas de água. Se o último produto foi um "Tapete de Yoga", eles recebem uma mensagem recomendando blocos e tiras de yoga. Se o `last_purchased_product` for qualquer outra coisa, eles recebem uma mensagem genérica de agradecimento.

### Disparar mensagens

Um caso de uso comum é enviar automaticamente uma mensagem, como um e-mail, quando um usuário faz uma compra. Por exemplo, você pode enviar uma mensagem de agradecimento ou um código de desconto para uma compra futura.

Para fazer isso, crie uma campanha baseada em ação ou canva, depois defina a ação-gatilho para **Fazer Compra**. Você também pode especificar condições adicionais para o disparo, como o produto comprado ou o valor da compra.

Você também pode personalizar sua mensagem acionada com Liquid.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

Neste exemplo, `${purchase_product_name}` é um atributo personalizado que você substituiria pelo nome real do atributo que armazena o nome do produto comprado na sua configuração do Braze.

### Análise de dados

Além do rastreamento de métricas de compra para segmentação, a Braze também registra o número de compras de cada produto e a receita gerada ao longo do tempo. Isso pode ser útil para ver quais produtos são mais populares ou medir o impacto de uma campanha promocional nas vendas.

Você pode visualizar esses dados na página do [Relatório de Receitas]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

### Compreensão dos cálculos de receita

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Receitas por tempo de vida</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de tempo de vida por usuário</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Receita média diária</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Compras diárias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Receitas diárias por usuário</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Cálculo de receita vitalícia

Braze usa eventos de compra para calcular a receita vitalícia (também chamada de valor do tempo de vida ou LTV) de um usuário, que é uma previsão do lucro líquido atribuído a todo o relacionamento futuro com um cliente. Isso pode ajudá-lo a tomar decisões informadas sobre estratégias de aquisição e retenção de clientes.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Existem dois lugares principais no Braze que você pode consultar para entender o LTV dos seus usuários:

- Para métricas gerais como *Receita do tempo de vida* e o *valor do tempo de vida por usuário* para cada app e site, consulte seu [Relatório de Receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Para entender a receita vitalícia de um usuário específico, consulte seu [perfil de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impacto dos reembolsos na receita vitalícia

Ao usar eventos de compra para rastrear dados de compra, você deve rastrear reembolsos registrando um evento de compra do Braze com uma propriedade `price` negativa. Esta abordagem manterá um total preciso para a receita vitalícia.

No entanto, tenha em mente que o reembolso contará como um evento de compra adicional. Vamos considerar o seguinte exemplo. Sam faz sua primeira compra por $12, mas devolve parte da compra para um reembolso de $5. O perfil de Sam registraria:

- 1 compra com um preço de $12
- 1 compra com um preço de -$5
- Receita vitalícia de $7

Embora Sam tenha dois eventos de compra em seu perfil, na realidade, ele fez apenas uma compra. Isso é importante considerar se você tiver algum segmento ou caso de uso construído em torno do número de compras que um usuário fez. Reembolsos constantes irão inflar a contagem de compras no perfil do usuário.

## Propriedades do evento de compra {#purchase-properties}

Com as propriedades do evento de compra, você pode definir propriedades nas compras que podem ser usadas para qualificar ainda mais as condições de {disparar}, aumentar a personalização no {envio de mensagens} e gerar {análise de dados} mais sofisticadas por meio da exportação de dados brutos. Tipos de valor de propriedade (string, numérico, booleano, data) variam por plataforma e são frequentemente atribuídos como pares chave-valor.

Por exemplo, se um aplicativo de comércio eletrônico quisesse enviar uma mensagem a um usuário após fazer uma compra, ele poderia melhorar adicionalmente seu público-alvo e permitir uma personalização de campanha aumentada adicionando uma propriedade de evento de compra de `brand_name`.

**Exemplo de acionamento com base nas propriedades do evento de compra:**

![Configurações de entrega baseada em ação para enviar uma campanha para usuários que compram fones de ouvido com uma marca igual a HeadphoneMart][2]{: style="max-width:80%;margin-left:15px;"}

Consulte o objeto de [propriedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) para mais.

### Segmentação de propriedade de evento

A segmentação de propriedades de eventos permite que você direcione os usuários com base não apenas nos eventos personalizados realizados, mas também nas propriedades associadas a esses eventos. Este recurso adiciona opções adicionais de filtragem ao segmentar compras e eventos personalizados.

![][6]{: style="max-width:80%;margin-left:15px;"}

Estes filtros de segmentação incluem:
- Realizou o evento personalizado com a propriedade Y com valor V X vezes nos últimos Y dias.
- Fez alguma compra com a propriedade Y com valor V X vezes nos últimos Y dias.
- Adiciona a capacidade de segmentar dentro de 1, 3, 7, 14, 21 e 30 dias.

Ao contrário das [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), os segmentos usados são atualizados em tempo real, suportam uma quantidade ilimitada de segmentos, oferecem um histórico de até 30 dias e geram pontos de dados. Devido à cobrança adicional de ponto de dados, você deve entrar em contato com seu gerente de sucesso do cliente da Braze para ativar as propriedades de eventos para seus eventos personalizados.

Quando aprovado, propriedades adicionais podem ser adicionadas no dashboard em **Configurações de Dados** > **Eventos Personalizados** clicando em **Gerenciar Propriedades**. Você pode então usar essas propriedades de evento na {etapa} alvo da campanha ou do construtor de {canva}.

### Propriedades de entrada da canva e propriedades de evento

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível para referência ao usar `canvas_entry_properties` e `event_properties` para o fluxo de trabalho original do canva.
{% endalert %}

Você pode aproveitar `canvas_entry_properties` e `event_properties` em suas jornadas de usuário na canva. Confira as propriedades de entrada e propriedades de evento da [canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para saber mais e exemplos.

{% alert important %}
Não é possível usar `event_properties` na etapa de envio de mensagens. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes da** etapa de mensagem que inclui `event_properties`.
{% endalert %}

{% tabs local %}
{% tab Propriedades de entrada da tela %}

[As propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) são as propriedades que você mapeia para Canvas que são baseadas em ações ou disparadas por API. Note que o objeto `canvas_entry_properties` tem um limite máximo de tamanho de 50 KB.

{% alert important %}
Especificamente para os canais de envio de mensagens no app, o `canvas_entry_properties` só pode ser referenciado no Canvas Flow e no editor original do Canvas se as propriedades de entrada persistente estiverem ativadas no editor original como parte do acesso antecipado anterior.
{% endalert %}

Para o envio de mensagens do Canvas Flow, o `canvas_entry_properties` pode ser usado no Liquid em qualquer etapa do canva. Use este Liquid ao fazer referência a essas propriedades: ``{% raw %} canvas_entry_properties${property_name} {% endraw %}``. Nota que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma. 

{% raw %}
Por exemplo, considere a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Você poderia adicionar a palavra "sapatos" a uma mensagem com o Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Para os canvas construídos com o editor original, `canvas_entry_properties` só pode ser referenciado na primeira etapa completa de um canva.

{% endtab %}

{% tab Propriedades do Evento %}
As propriedades do evento referem-se às propriedades que você define para eventos personalizados e compras. Esses `event_properties` podem ser usados em campanhas com entrega baseada em ação e Canvas.

No Canvas Flow, as propriedades de evento personalizado e evento de compra podem ser usadas no Liquid em qualquer etapa de Mensagem que siga uma etapa de jornadas de ação. Para o Canvas Flow, use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} se estiver fazendo referência a estes `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente de Mensagem.

Para o editor de canva original, `event_properties` não pode ser usado em etapas completas agendadas. No entanto, você pode usar `event_properties` na primeira etapa completa de um canva baseado em ação, mesmo que a etapa completa esteja agendada.

Na primeira etapa da Mensagem após uma jornada de ação, você pode usar `event_properties` relacionado ao evento referenciado nessa jornada de ação. Esses `event_properties` só podem ser usados se o usuário realmente realizou a ação (não foi para o grupo Todos os outros). Você pode ter outras etapas (que não são outras jornadas de ação ou etapa de mensagem) entre estas jornadas de ação e a etapa de mensagem.

{% endtab %}
{% endtabs %}

### Registre as compras no nível do pedido
Se você quiser registrar compras no nível do pedido em vez do nível do produto, pode usar o nome do pedido ou a categoria do pedido como o `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

## Eventos de compra em lista de bloqueio

Você pode ocasionalmente identificar eventos de compra que consomem muitos pontos de dados, {2|não são mais úteis para sua estratégia de marketing, ou {3|foram registrados por engano. Para impedir que esses dados sejam enviados para a Braze, você pode colocar o objeto de dados personalizados na lista de bloqueio enquanto sua equipe de engenharia trabalha para removê-lo do backend do seu app ou site.

No dashboard da Braze, você pode gerenciar a lista de bloqueio em **Configurações de Dados** > **Produtos**. Confira [Gerenciamento de dados personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data/) para saber mais.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar **Produtos** em **Gerenciar Configurações**.
{% endalert %}

[1]: {% image_buster /assets/img/purchase_filter_example.gif %}
[2]: {% image_buster /assets/img/purchase2.png %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
