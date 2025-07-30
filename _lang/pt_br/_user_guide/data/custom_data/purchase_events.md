---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 8
page_type: reference
description: "Este artigo de referência descreve eventos e propriedades de compra, seu uso, segmentação, onde visualizar a análise de dados relevante e mais."
search_rank: 3
---

# Eventos de compra

> Esta página aborda eventos e propriedades de compra, seu uso, segmentação, onde visualizar análises de dados relevantes e muito mais.

Os eventos de compra são ações de compra realizadas por seus usuários e são usados para registrar compras no app e estabelecer o valor do tempo de vida (LTV) para cada perfil de usuário. Esses eventos devem ser organizados pela sua equipe. Registrar eventos de compra permite adicionar propriedades como quantidade e tipo, ajudando a segmentar ainda mais seus usuários com base nessas propriedades.

## Registrando eventos de compra

Você pode registrar compras passando um [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) pelo [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

A seguir estão listados métodos em várias plataformas que são usados para registrar compras. Nessas páginas, você também encontrará documentação sobre como adicionar propriedades e quantidades ao seu evento de compra. Você pode segmentar ainda mais seus usuários com base nessas propriedades.

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

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

Para obter detalhes sobre cada filtro, consulte o glossário [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) e filtre por "Comportamento de compra".

![Filtragem de usuários que fizeram exatamente três compras]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Para segmentar o número de vezes que uma compra específica ocorreu, registre essa compra individualmente como um [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
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

Você também pode personalizar sua mensagem acionada com Liquid. No exemplo a seguir, `${purchase_product_name}` é um atributo personalizado que você substituiria pelo nome do atributo real que armazena o nome do produto comprado em sua configuração do Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Análise de dados

Além do rastreamento de métricas de compra para segmentação, a Braze também registra o número de compras de cada produto e a receita gerada ao longo do tempo. Isso pode ser útil para identificar os produtos mais populares ou medir o impacto de uma campanha promocional nas vendas.

Você pode encontrar esses dados na página [Relatório de receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

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

Ao usar eventos de compra para rastrear dados de compra, você deve rastrear reembolsos registrando um evento de compra do Braze com uma propriedade `price` negativa. Essa abordagem mantém um total preciso para a receita vitalícia.

No entanto, tenha em mente que o reembolso contará como um evento de compra adicional. Vamos considerar o seguinte exemplo. Sam faz sua primeira compra por $12, mas devolve parte da compra para um reembolso de $5. O perfil de Sam registraria:

- 1 compra com um preço de $12
- 1 compra com um preço de -$5
- Receita vitalícia de $7

Embora Sam tenha dois eventos de compra em seu perfil, na realidade, ele fez apenas uma compra. Isso é importante considerar se você tiver algum segmento ou caso de uso construído em torno do número de compras que um usuário fez. Reembolsos constantes irão inflar a contagem de compras no perfil do usuário.

## Propriedades do evento de compra {#purchase-properties}

Com as propriedades do evento de compra, você pode definir propriedades nas compras que podem ser usadas para qualificar ainda mais as condições de {disparar}, aumentar a personalização no {envio de mensagens} e gerar {análise de dados} mais sofisticadas por meio da exportação de dados brutos. Tipos de valor de propriedade (string, numérico, booleano, data) variam por plataforma e são frequentemente atribuídos como pares chave-valor.

Por exemplo, se você tiver um aplicativo de comércio eletrônico e quiser enviar mensagens a um usuário depois de fazer uma compra, poderá melhorar ainda mais seu público-alvo e permitir uma maior personalização da campanha adicionando uma propriedade de evento de compra de `brand_name`.

**Exemplo de acionamento com base nas propriedades do evento de compra:**

![Configurações de entrega baseada em ação para enviar uma campanha aos usuários que compram fones de ouvido com um nome de marca igual ao HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Consulte o objeto de [propriedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) para mais.

### Segmentação de propriedade de evento

A segmentação de propriedades de eventos permite o direcionamento de usuários com base não apenas em eventos personalizados realizados, mas também nas propriedades associadas a esses eventos. Este recurso adiciona opções adicionais de filtragem ao segmentar compras e eventos personalizados.

![]({% image_buster /assets/img/nested_object3.png %}){: style="max-width:80%;margin-left:15px;"}

Esses filtros de segmentação incluem:
- Realizou o evento personalizado com a propriedade Y com o valor V X vezes nos últimos Y dias
- Fez alguma compra com a propriedade Y com valor V X vezes nos últimos Y dias
- Adiciona segmentação de 1 a 30 dias em todas as compras, eventos e propriedades de compras e eventos

Ao contrário das [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), os segmentos usados são atualizados em tempo real, suportam uma quantidade ilimitada de segmentos, oferecem um histórico de até 30 dias e geram pontos de dados. Devido à cobrança adicional de ponto de dados, você deve entrar em contato com seu gerente de sucesso do cliente da Braze para ativar as propriedades de eventos para seus eventos personalizados.

Quando aprovadas, propriedades adicionais podem ser adicionadas no dashboard em **Configurações de dados** > **Eventos personalizados**, selecionando **Gerenciar propriedades**. Você pode então usar essas propriedades de evento na {etapa} alvo da campanha ou do construtor de {canva}.

### Propriedades de entrada da canva e propriedades de evento

{% multi_lang_include canvas_entry_event_properties.md %}

### Registre as compras no nível do pedido

Para registrar compras no nível do pedido em vez de no nível do produto, use o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Convenções de nomenclatura de ID de produto

Na Braze, oferecemos algumas convenções gerais de nomenclatura para o objeto de compra `product_id`. Ao escolher `product_id`, a Braze sugere o uso de nomes simplistas, como o nome do produto ou a categoria do produto (em vez de SKUs), com a intenção de agrupar todos os itens registrados por esse `product_id`.

Isso ajuda a tornar os produtos fáceis de identificar para segmentação e disparo. 

## Eventos de compra em lista de bloqueio

Você pode ocasionalmente identificar eventos de compra que consomem muitos pontos de dados, {2|não são mais úteis para sua estratégia de marketing, ou {3|foram registrados por engano. Para impedir que esses dados sejam enviados para a Braze, você pode colocar o objeto de dados personalizados na lista de bloqueio enquanto sua equipe de engenharia trabalha para removê-lo do backend do seu app ou site.

No dashboard da Braze, você pode gerenciar a lista de bloqueio em **Configurações de Dados** > **Produtos**. Confira [Gerenciamento de dados personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) para saber mais.

