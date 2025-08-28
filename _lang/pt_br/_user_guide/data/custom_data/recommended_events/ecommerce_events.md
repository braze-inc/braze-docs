---
nav_title: Eventos recomendados para e-commerce
article_title: Eventos recomendados para e-commerce
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artigo de referência descreve eventos e propriedades recomendados para eCommerce, seu uso, segmentação, onde visualizar análises relevantes e mais."
---

# eventos recomendados para eCommerce

> Esta página cobre eventos e propriedades recomendados para eCommerce. Esses eventos são criados para capturar comportamentos de compra chave que os profissionais de marketing precisam para disparar mensagens eficazes, como direcionamento de carrinhos abandonados.

A Braze reconhece que o planejamento de dados leva tempo. Incentivamos nossos clientes a familiarizarem suas equipes de desenvolvimento e começarem a enviar esses eventos agora. Embora alguns recursos possam não estar disponíveis imediatamente com os eventos recomendados para eCommerce, você pode aguardar a introdução de novos produtos ao longo de 2025 que aprimorarão suas capacidades de eCommerce.

{% alert important %}
Os eventos recomendados para eCommerce estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se você estiver interessado em participar deste acesso antecipado. <br><br>Se você estiver utilizando o novo [conector Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), esses eventos recomendados estarão automaticamente disponíveis através da integração.
{% endalert %}


## Tipos de eventos recomendados para eCommerce

{% tabs %}
{% tab ecommerce.produto_visualizado %}

Você pode usar o evento de produto visualizado para disparar quando um cliente visualiza uma página de detalhes do produto.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. <br> Para clientes que não são do Shopify, este será o valor que você definir para IDs de itens de catálogo como SKUs. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. | 
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL para a página do produto para mais detalhes. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `currency` | Sim | String | A moeda na qual o preço do produto está listado (como "USD" ou "EUR") no [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto | |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplo de objeto

```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
            "sku": "sku"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.carrinho_atualizado %}

Você pode usar o evento de carrinho atualizado para rastrear quando produtos são adicionados, removidos ou atualizados no carrinho. O evento `ecommerce.cart_updated` verifica as seguintes informações antes de ser acionado:

- O horário do evento é maior que o horário `updated_at` para o carrinho específico do usuário.
- O carrinho não prosseguiu para o processo de checkout.
- O array `products` não está vazio.

#### Objeto de mapeamento de carrinhos

O evento `ecommerce.cart_updated` tem um objeto de mapeamento de carrinhos. Este objeto é criado para o perfil do usuário que contém um mapeamento de carrinhos, que contêm todos os produtos no carrinho do comprador. Você pode acessar os produtos no carrinho de compras através da tag Liquid: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Se um carrinho não foi atualizado e progrediu para um evento de pedido realizado em 10 dias, iremos deletar o carrinho e os produtos associados.

{% alert note %}
Produtos por carrinho não são limitados no Braze. No entanto, o limite do Shopify é 500.
{% endalert %}

#### Comportamento do carrinho ao mesclar perfis de usuário

Se houver dois carrinhos, adicione ambos ao usuário mesclado. Reenfileire o canva se for o mesmo ou um carrinho diferente para enviar uma mensagem com as informações mais recentes do carrinho. O evento `ecommerce.cart_updated` conterá o ID do carrinho mais recente e os produtos mais recentes no carrinho.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `cart_id` | Sim | String | Identificador único para o carrinho. Se nenhum valor for passado, determinaremos um valor padrão (compartilhado entre eventos de carrinho, checkout e pedido) para o mapeamento do carrinho do usuário. |
| `total_value` | Sim | Float | Valor monetário total do carrinho. | 
| `currency` | Sim | String | A moeda na qual o preço do produto está listado (como "USD" ou "EUR") no [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Sim | Vetor |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. <br> Esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL para a página do produto para mais detalhes. |
| `quantity` | Sim | Inteiro | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplo de objeto

```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endtab %}
{% tab ecommerce.checkout_iniciado %}

Você pode usar o evento de checkout iniciado para redirecionar clientes que iniciaram o processo de checkout, mas não fizeram um pedido.

Semelhante ao evento `ecommerce.cart_updated`, este evento permite que você aproveite a tag Liquid do carrinho de compras para acessar todos os produtos dentro do carrinho para mensagens de checkout abandonado:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `checkout_id` | Sim | String | Identificador único para o checkout. |
| `cart_id` | Não | String | Identificador único para o carrinho. Se nenhum valor for passado, determinaremos um valor padrão (compartilhado entre eventos de carrinho, checkout e pedido) para o mapeamento do carrinho do usuário. | 
| `total_value` | Sim | Float | Valor monetário total do carrinho. |
| `currency` | Sim | String | Moeda na qual o carrinho é avaliado. |
| `products` | Sim | Vetor de objetos |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. Por exemplo, esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado.  |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL para a página do produto para mais detalhes. |
| `quantity` | Sim | Inteiro | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto |  |
| `checkout_url` | Não | String | URL para a página de checkout. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplo de objeto

```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.pedido_realizado %}

Você pode usar o evento de pedido realizado para disparar quando um cliente completa com sucesso o processo de checkout e faz um pedido.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `order_id` | Sim | String | Identificador único para o pedido realizado. |
| `cart_id` | Não | String | Identificador único para o carrinho. Se nenhum valor for passado, determinaremos um valor padrão (compartilhado entre eventos de carrinho, checkout e pedido) para o mapeamento do carrinho do usuário. |
| `total_value` | Sim | Float | Valor monetário total do carrinho. | 
| `currency` | Sim | String | Moeda na qual o carrinho é avaliado. |
| `total_discounts` | Não | Float | Valor total dos descontos aplicados ao pedido. | 
| `discounts`| Não | Vetor de objetos | Lista detalhada dos descontos aplicados ao pedido. |
| `products` | Sim | Vetor de objetos |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL para a página do produto para mais detalhes. |
| `quantity` | Sim | Inteiro | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto |  |
| `order_status_url` | Não | String | URL para visualizar o status do pedido. |
| `order_number` | Não | String | (Apenas Shopify) Número de pedido único para o pedido realizado. |
| `tags` | Não | Vetor | (Apenas Shopify) Etiquetas do pedido
| `referring_site` | Não | String | (Apenas Shopify) O site de onde o pedido se originou (como Meta). |
| `payment_gateway_names` | Não | Vetor | (Apenas Shopify) Fonte do sistema de pagamento (como ponto de venda ou móvel). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplo de objeto

```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.pedido_reembolsado %}

Você pode usar o evento de pedido reembolsado para disparar quando um pedido é parcialmente ou totalmente reembolsado.

#### Propriedades

| Nome da propriedade       | Obrigatória | Tipo de dados | Descrição   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sim      | String    | Identificador único para o pedido realizado.        |
| `total_value`         | Sim      | Float     | Valor monetário total do carrinho.    |
| `currency`            | Sim      | String    | Moeda na qual o carrinho é avaliado.    |
| `total_discounts`     | Não       | Float     | Valor total dos descontos aplicados ao pedido.   |
| `discounts`           | Não       | Vetor de objetos     | Lista detalhada dos descontos aplicados ao pedido. |
| `products`            | Sim      | Vetor de objetos     |  |
| `product_id`       | Sim      | String    | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto, SKU ou similar. <br>Se um reembolso parcial for emitido e não houver `product_id` atribuído ao reembolso (por exemplo, um reembolso em nível de pedido), forneça um `product_id` generalizado.             |
| `product_name`     | Sim      | String    | O nome do produto que foi visualizado.                                                                      |
| `variant_id`       | Sim      | String    | Um identificador único para a variante do produto (como `shirt_medium_blue`).                                         |
| `image_url`        | Não       | String    | URL da imagem do produto.     |
| `product_url`      | Não       | String    | URL para a página do produto para mais detalhes.  |
| `quantity`         | Sim      | Inteiro   | Número de unidades do produto no carrinho.   |
| `price`            | Sim      | Float     | O preço unitário da variante do produto no momento da visualização.  |
| `metadata`         | Não       | Objeto    | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos SKU. Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku`            | Não       | String    | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo.  |
| `source`              | Sim      | String    | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine).    |
| `metadata`            | Não       | Objeto    |                |
| `order_status_url`  | Não       | String    | URL para visualizar o status do pedido.     |
| `order_note`       | Não       | String    | (Apenas Shopify) Nota anexada ao pedido pelo comerciante.    |
| `order_number`     | Não       | String    | (Apenas Shopify) Número de pedido único para o pedido realizado.   |
| `tags`             | Não       | Vetor     | (Apenas Shopify) Etiquetas do pedido.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplo de objeto

```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
			"order_note": "item was broken",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.pedido_cancelado %}

Você pode usar o evento de pedido cancelado para disparar quando um cliente cancela um pedido.

#### Propriedades

| Nome da propriedade      | Obrigatória | Tipo de dados | Descrição       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sim      | String    | Identificador único para o pedido realizado.              |
| `cancel_reason`       | Sim      | String    | Motivo pelo qual o pedido foi cancelado.           |
| `total_value`         | Sim      | Float     | Valor monetário total do carrinho.         |
| `currency`            | Sim      | String    | Moeda na qual o carrinho é avaliado.           |
| `total_discounts`     | Não       | Float     | Valor total dos descontos aplicados ao pedido.     |
| `discounts`           | Não       | Vetor de objetos     | Lista detalhada dos descontos aplicados ao pedido.             |
| `products`            | Sim      | Vetor de objetos     |         |
| `product_id`          | Sim      | String    | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto, SKU ou similar.             |
| `product_name`        | Sim      | String    | O nome do produto que foi visualizado.          |
| `variant_id`          | Sim      | String    | Um identificador único para a variante do produto (como `shirt_medium_blue`).        |
| `image_url`           | Não       | String    | URL da imagem do produto.           |
| `product_url`         | Não       | String    | URL para a página do produto para mais detalhes.                                                                     |
| `quantity`            | Sim      | Inteiro   | Número de unidades do produto no carrinho.        |
| `price`               | Sim      | Float     | O preço unitário da variante do produto no momento da visualização.     |
| `metadata`            | Não       | Objeto    | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos SKU. Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku`                 | Não       | String    | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo.        |
| `source`              | Sim      | String    | Fonte da qual o evento é derivado. (Para Shopify, isso é vitrine).    |
| `metadata`            | Não       | Objeto    |       |
| `order_status_url`    | Não       | String    | URL para visualizar o status do pedido.                                                                          |
| `order_number`        | Não       | String    | (Apenas Shopify) Número de pedido único para o pedido realizado.  |
| `tags`                | Não       | Vetor     | (Apenas Shopify) Tags do pedido.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplo de objeto

```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## Modelos de Canvas de eCommerce

A Braze criou modelos de Canvas pré-construídos que são alimentados por eventos recomendados de eCommerce, como direcionar clientes que iniciaram o processo de checkout, mas saíram antes de finalizar o pedido. Você pode usar esses eventos para tomar decisões informadas para aprimorar a jornada do usuário, personalizando o envio de mensagens e direcionando públicos específicos.

Confira nossos casos de uso dedicados [eCommerce use cases]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) para mais maneiras de como você pode usar esses eventos com modelos de Canvas.

## Campos calculados pelo usuário

Usamos cálculos de campos de usuário padronizados para os seguintes campos: 

- **Receita Total** = soma do valor total dos pedidos realizados - soma do valor total dos pedidos reembolsados
- **Contagem Total de Pedidos** = contagem de eventos distintos de pedidos realizados - contagem de eventos distintos de cancelamentos de pedidos
- **Valor Total de Reembolso** = soma do valor total dos pedidos reembolsados 

Esses cálculos de campos de usuário também estão incluídos na aba **Transações** dos perfis de usuário.

![A aba "Transações" com campos calculados pelo usuário.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}

{% alert important %}
Os planos para descontinuar o evento de compra serão anunciados no final de 2025. A longo prazo, o evento de compra será substituído por novos [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/), que virão com recursos aprimorados para segmentação, relatórios, análise de dados e mais. No entanto, os novos eventos de eCommerce não suportarão recursos existentes relacionados ao evento de compra, como Valor do Tempo de Vida (LTV) ou relatórios de receita em Canvases ou campanhas. Para uma lista completa de recursos relacionados a eventos de compra, consulte a seção sobre [Registro de eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}
