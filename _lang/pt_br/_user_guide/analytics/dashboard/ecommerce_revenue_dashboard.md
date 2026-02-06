---
nav_title: Painel de receitas de comércio eletrônico
article_title: Painel de receitas de comércio eletrônico
alias: "/ecommerce_revenue_dashboard/"
page_order: 6
description: "Este artigo fornece uma visão geral do dashboard Receita de comércio eletrônico - Atribuição do último ponto de contato."
---

# Painel de receitas de comércio eletrônico

> O dashboard **Receita de comércio eletrônico - atribuição de último ponto de contato** rastreia a receita atribuída de último ponto de contato para campanhas e telas usando [eventos recomendados de comércio eletrônico]({{site.baseurl}}/ecommerce_events/). Use esse dashboard para entender quais mensagens geram receita e para monitorar o desempenho geral do comércio eletrônico ao longo do tempo.

{% alert note %}
Os eventos recomendados para comércio eletrônico estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente Braze se estiver interessado em participar desse acesso antecipado. <br><br>Se estiver usando o novo [conector do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), esses eventos recomendados estarão automaticamente disponíveis por meio da integração. Caso contrário, esses eventos devem ser implementados antes que os dados apareçam nesse dashboard.
{% endalert %}

Para visualizar seu painel de receita de comércio eletrônico, acesse **Análise de dados** > **Dashboard Builder** e selecione **Receita de comércio eletrônico - Atribuição do último ponto de contato**. Esse dashboard informa sobre a receita atribuída à última campanha ou à última tela com a qual um usuário interagiu antes de fazer um pedido, dentro da janela de conversão selecionada.

## Métricas disponíveis

| Métrico | Definição |
| --- | --- |
| Receita de e-commerce | Receita total atribuída ao último ponto de contato com base no intervalo de datas e na janela de conversão selecionados. |
| Pedidos diários feitos | O número médio de pedidos distintos feitos por dia. |
| Receita média diária de e-commerce | Receita média de atribuição por dia para o período de tempo selecionado. |
| Receita de e-commerce ao longo do tempo | Uma série temporal da receita atribuída no intervalo de datas selecionado. |
| Receita de e-commerce por campanha | Receita de atribuição discriminada por campanha. | 
| Receita de e-commerce por canva | Receita de atribuição dividida por Canva. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Modelo de atribuição

O dashboard **Receita de comércio eletrônico - Atribuição do último ponto de contato** usa a atribuição do último ponto de contato. Isso significa que a receita é atribuída à campanha mais recente do Braze ou ao Canva com o qual o usuário se engajou antes de fazer um pedido.

{% alert important %}
As interações de mensagens devem ter ocorrido dentro da janela de conversão selecionada. Os pedidos sem uma interação de mensagens elegível dentro da janela de conversão não são atribuídos.
{% endalert %}

## Dados incluídos

O dashboard **Receita de comércio eletrônico - Atribuição do último ponto de contato** extrai dados de eventos recomendados de comércio eletrônico:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

As contagens de receita e de pedidos usam cálculos padronizados da Braze.

| Métrico | Cálculo |
| --- | --- |
| Total de receitas | Soma dos valores dos pedidos feitos - Soma dos valores reembolsados |
| Total de pedidos | Ordens distintas colocadas - Ordens distintas canceladas |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

### Dados excluídos

As compras registradas usando o evento de compra antigo não estão incluídas. O dashboard **Receita de comércio eletrônico - Atribuição do último ponto de contato** atualmente não oferece suporte a recursos vinculados a eventos de compra herdados, como LTV ou relatórios de receita em campanhas ou Canvas. 


## Manuseio de moedas

Todas as receitas são exibidas em dólares americanos. Moedas que não sejam dólares americanos são convertidas em dólares americanos usando a taxa de câmbio na data em que o evento é relatado. Para evitar a conversão, codifique a moeda para `USD` ao enviar eventos.
