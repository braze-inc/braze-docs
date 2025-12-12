---
nav_title: Eventos recomendados
article_title: Eventos recomendados
alias: /recommended_events/
page_type: reference
description: "Este artigo de referência descreve os eventos recomendados, que são recomendações fornecidas pelo Braze para eventos de comércio eletrônico."
---

# Eventos recomendados

> Os eventos recomendados são mapeados para os casos de uso mais comuns de comércio eletrônico. Ao usar os eventos recomendados, você pode desbloquear modelos pré-construídos do Canvas, painéis de relatórios que mapeiam o ciclo de vida do cliente e muito mais.

Por exemplo, você pode ter um evento personalizado chamado “cart_updated” ou “update_to_cart” para capturar quando um usuário adiciona, remove ou atualiza os produtos em seu carrinho. Para eventos recomendados, o Braze fornecerá o modelo de evento, que inclui um nome definido e propriedades relevantes para esse evento.

{% alert important %}
Os eventos recomendados estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente Braze se estiver interessado em participar desse acesso antecipado. <br><br>Se você estiver aproveitando o novo [conector da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), esses eventos recomendados estarão automaticamente disponíveis por meio da integração.
{% endalert %}

## Como funciona

O Braze aplica uma validação especial a todos os eventos recomendados, e alguns eventos recomendados têm ações especiais de pós-processamento. Para determinados eventos recomendados pelo setor, o Braze pode oferecer suporte a um tratamento especial, como novos acionadores baseados em ações para campanhas e Canvases.

Os eventos recomendados funcionam de forma semelhante aos [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events). Você pode exportar eventos recomendados do Currents, colocá-los em listas de bloqueio e usá-los em relatórios. Você também pode enviar dados para o Braze para rastrear esses eventos usando o [SDK do Braze]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) ou o [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Eventos recomendados para comércio eletrônico

[Os eventos recomendados para comércio eletrônico]({{site.baseurl}}/ecommerce_events/) são baseados em eventos recomendados. Esses eventos recomendados para comércio eletrônico rastreiam as ações realizadas pelos clientes, como visualizar um produto, atualizar o carrinho ou iniciar o processo de checkout. 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### Modelos do eCommerce Canvas

Confira nossos [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) dedicados [ao comércio eletrônico]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) para obter mais ideias sobre como usar os modelos pré-construídos do Braze Canvas para implementar estratégias essenciais.

## Perguntas frequentes

### Os eventos recomendados são iguais aos eventos personalizados?

Não. O Braze definirá esquemas de dados opinativos para eventos recomendados. Isso incluirá propriedades de evento obrigatórias e opcionais que passarão por um processo de validação no Braze. [Eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) são ações específicas realizadas por seus usuários ou atualizações sobre eles em seu aplicativo ou site que você deseja rastrear. Você pode personalizar o nome do evento e o que ele rastreia.

### Posso personalizar o nome dos eventos recomendados?

Não. Os eventos recomendados têm nomes e propriedades de eventos padronizados. Essas padronizações ajudam a criar consistência em seus dados.

### Ainda posso usar eventos de compra para registrar compras?

Com o lançamento dos eventos recomendados para comércio eletrônico, o Braze eliminará gradualmente o evento de compra legado no futuro. Se estiver usando atualmente o evento de compra, você receberá um aviso prévio sobre os planos de depreciação. Enquanto isso, você pode continuar a usar os eventos de compra até a data oficial de descontinuação.