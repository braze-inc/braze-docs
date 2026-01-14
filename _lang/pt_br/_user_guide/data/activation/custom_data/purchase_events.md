---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 8
page_type: reference
description: "Este artigo de referência descreve eventos e propriedades de compra, seu uso, segmentação, onde visualizar análises relevantes e muito mais."
search_rank: 3
---

# Eventos de compra

> Esta página aborda eventos e propriedades de compra, seu uso, segmentação, onde visualizar análises relevantes e muito mais.

Os eventos de compra são ações de compra realizadas pelos usuários e são usados para registrar as compras no aplicativo e estabelecer o Lifetime Value (LTV) para cada perfil de usuário. Esses eventos devem ser organizados pela sua equipe. O registro de eventos de compra permite adicionar propriedades como quantidade e tipo, o que ajuda a segmentar ainda mais seus usuários com base nessas propriedades.

## Registro de eventos de compra

É possível registrar compras passando um [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) pelo [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou usando uma de nossas bibliotecas SDK listadas abaixo.

A seguir, listamos os métodos usados em várias plataformas para registrar compras. Nessas páginas, você também encontrará documentação sobre como adicionar propriedades e quantidades ao seu evento de compra. Você pode segmentar ainda mais seus usuários com base nessas propriedades.

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unidade]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## Visualização de dados de compra

Depois de configurar e começar a registrar os eventos de compra, você poderá visualizar esses dados de compra no perfil de um usuário na [guia Overview (Visão geral]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab)).

## Uso de dados de compra

Há várias maneiras de usar dados de compra no Braze:

- **[Segmentação](#purchase-event-segmentation):** Use dados de compra para criar segmentos de usuários com base em seu comportamento de compra.
- **[Personalização](#personalization):** Use dados de compra para personalizar mensagens para os usuários.
- **[Mensagens de acionamento](#trigger-messages):** Configure mensagens para serem acionadas com base em eventos de compra.
- **[Análises](#analytics):** Analise seus dados de compra para obter insights sobre o comportamento do usuário e a eficácia de suas campanhas de marketing.

### Segmentação {#purchase-event-segmentation}

É possível acionar qualquer número ou tipo de campanhas de acompanhamento com base em eventos de compra registrados. Por exemplo, você pode criar um segmento de usuários que fizeram uma compra nos últimos 30 dias ou um segmento de usuários que gastaram mais de um determinado valor.

Os seguintes filtros de segmentação estão disponíveis ao segmentar usuários:

- Primeira compra realizada
- Primeira compra do aplicativo
- Último produto comprado
- Dinheiro gasto
- Produto adquirido
- Número total de compras
- X dinheiro gasto em Y dias
- X Produto comprado em Y dias
- X Compra de propriedade em Y dias
- X compras nos últimos Y dias

Para obter detalhes sobre cada filtro, consulte o glossário [de filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) e filtre por "Comportamento de compra".

\![Filtragem de usuários que fizeram exatamente três compras]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Para segmentar o número de vezes que uma compra específica ocorreu, registre essa compra individualmente como um [atributo personalizado de incremento]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalização

Como qualquer outro tipo de dados coletados de seus usuários, você pode usar os dados de compra para personalizar suas mensagens por meio do Liquid. Por exemplo, você pode enviar um e-mail personalizado a um usuário recomendando produtos semelhantes aos que ele acabou de comprar.

Digamos que você tenha uma propriedade de evento de compra chamada `last_purchased_product` que armazena o nome do último produto que um usuário comprou. Você pode usar essa propriedade para personalizar uma mensagem de e-mail como esta:

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

Neste exemplo, a mensagem é personalizada com base na propriedade `last_purchased_product`. Se o último produto que o usuário comprou foi "Tênis de corrida", ele receberá uma mensagem recomendando shorts de corrida e garrafas de água. Se o último produto foi um "tapete de ioga", eles receberão uma mensagem recomendando blocos e tiras de ioga. Se o endereço `last_purchased_product` for outro, eles receberão uma mensagem genérica de agradecimento.

### Mensagens de acionamento

Um caso de uso comum é o envio automático de uma mensagem, como um e-mail, quando um usuário faz uma compra. Por exemplo, você pode enviar uma mensagem de agradecimento ou um código de desconto para uma compra futura.

Para isso, crie uma campanha baseada em ação ou um Canvas e, em seguida, defina a ação de acionamento como **Make Purchase (Fazer compra)**. Você também pode especificar condições adicionais para o acionador, como o produto comprado ou o valor da compra.

Você também pode personalizar sua mensagem acionada com o Liquid. No exemplo a seguir, `${purchase_product_name}` é um atributo personalizado que você substituiria pelo nome do atributo real que armazena o nome do produto comprado em sua configuração do Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Análises

Além de acompanhar as métricas de compra para segmentação, a Braze também registra o número de compras de cada produto e a receita gerada ao longo do tempo. Isso pode ser útil para identificar os produtos mais populares ou medir o impacto de uma campanha promocional nas vendas.

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
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Receita vitalícia</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor vitalício por usuário</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Receita média diária</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Compras diárias</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Receita diária por usuário</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Cálculo da receita vitalícia

A Braze usa eventos de compra para calcular a receita vitalícia (também chamada de valor vitalício ou LTV) de um usuário, que é uma previsão do lucro líquido atribuído a todo o relacionamento futuro com um cliente. Isso pode ajudá-lo a tomar decisões informadas sobre estratégias de aquisição e retenção de clientes.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Há dois locais principais no Braze que você pode consultar para entender o LTV dos seus usuários:

- Para obter métricas gerais, como a *receita vitalícia* e o *valor vitalício por usuário* para cada aplicativo e site, consulte o [Relatório de receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Para entender a receita vitalícia de um usuário específico, consulte seu [perfil de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impacto dos reembolsos na receita vitalícia

Ao usar eventos de compra para rastrear dados de compra, você deve rastrear reembolsos registrando um evento de compra do Braze com uma propriedade negativa `price`. Essa abordagem mantém um total preciso para a receita vitalícia.

No entanto, lembre-se de que o reembolso será contabilizado como um evento de compra adicional. Vamos considerar o seguinte exemplo. Sam faz sua primeira compra por US$ 12, mas devolve parte da compra para receber um reembolso de US$ 5. O perfil de Sam seria registrado:

- 1 compra com um preço de US$ 12
- 1 compra com um preço de -$5
- Receita vitalícia de US$ 7

Embora Sam tenha dois eventos de compra em seu perfil, na realidade, ele fez apenas uma compra. É importante considerar isso se você tiver algum segmento ou caso de uso criado em torno do número de compras que um usuário fez. Os reembolsos constantes aumentarão a contagem de compras no perfil do usuário.

## Propriedades do evento de compra {#purchase-properties}

Com as propriedades de eventos de compra, você pode definir propriedades sobre compras que podem ser usadas para qualificar ainda mais as condições de acionamento, aumentar a personalização das mensagens e gerar análises mais sofisticadas por meio da exportação de dados brutos. Os tipos de valores de propriedade (string, numérico, booleano, data) variam de acordo com a plataforma e geralmente são atribuídos como pares de valores-chave.

Por exemplo, se você tiver um aplicativo de comércio eletrônico e quiser enviar uma mensagem a um usuário depois de fazer uma compra, poderá melhorar ainda mais seu público-alvo e permitir uma maior personalização da campanha adicionando uma propriedade de evento de compra de `brand_name`.

**Exemplo de acionamento com base nas propriedades do evento de compra:**

Configurações de entrega baseadas em ação para enviar uma campanha aos usuários que comprarem fones de ouvido com um nome de marca igual a HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Consulte o [objeto de propriedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) para obter mais informações.

### Segmentação de propriedades de eventos

A segmentação de propriedades de eventos permite segmentar usuários com base não apenas em eventos personalizados realizados, mas também nas propriedades associadas a esses eventos. Esse recurso acrescenta opções adicionais de filtragem ao segmentar eventos de compra e personalizados.

\![]({% image_buster /assets/img/nested_object3.png %}){: style="max-width:80%;margin-left:15px;"}

Esses filtros de segmentação incluem:
- Realizou o evento personalizado com a propriedade Y com o valor V X vezes nos últimos Y dias
- Fez compras com a propriedade Y com valor V X vezes nos últimos Y dias
- Adiciona segmentação de 1 a 30 dias em todas as compras, eventos e propriedades dentro de compras e eventos

Diferentemente das [Extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), os segmentos usados são atualizados em tempo real, suportam uma quantidade ilimitada de segmentos, oferecem um histórico de no máximo 30 dias e incorrem em pontos de dados. Devido à cobrança de ponto de dados adicional, você deve entrar em contato com o gerente de sucesso do cliente Braze para ativar as propriedades do evento para seus eventos personalizados.

Quando aprovadas, propriedades adicionais podem ser adicionadas no painel em **Configurações de dados** > **Eventos personalizados**, selecionando **Gerenciar propriedades**. Em seguida, você pode usar essas propriedades de evento na etapa de destino da campanha ou do construtor do Canvas.

### Propriedades de entrada de tela e propriedades de evento

{% multi_lang_include canvas_entry_event_properties.md %}

### Registrar compras no nível do pedido

Para registrar compras no nível do pedido em vez de no nível do produto, use o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Convenções de nomenclatura de ID de produto

Na Braze, oferecemos algumas convenções gerais de nomenclatura para o objeto de compra `product_id`. Ao escolher `product_id`, a Braze sugere o uso de nomes simplistas, como o nome do produto ou a categoria do produto (em vez de SKUs), com a intenção de agrupar todos os itens registrados por esse `product_id`.

Isso ajuda a tornar os produtos fáceis de identificar para segmentação e acionamento. 

## Eventos de compra com lista de bloqueio

Ocasionalmente, você pode identificar eventos de compra que registram muitos pontos de dados, que não são mais úteis para a sua estratégia de marketing ou que foram registrados por engano. Para impedir que esses dados sejam enviados ao Braze, você pode colocar o objeto de dados personalizados em uma lista de bloqueio enquanto sua equipe de engenharia trabalha para removê-lo do backend do seu aplicativo ou site.

No painel do Braze, você pode gerenciar a lista de bloqueio em **Data Settings** > **Products**. Consulte [Gerenciar dados personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) para saber mais.

