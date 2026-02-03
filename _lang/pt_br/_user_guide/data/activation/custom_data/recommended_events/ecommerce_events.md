---
nav_title: eventos recomendados de eCommerce
article_title: Eventos recomendados para e-commerce
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artigo de referência descreve eventos e propriedades recomendados de eCommerce, seu uso, segmentação, onde visualizar análises relevantes e mais."
---

# eventos recomendados de eCommerce

> Esta página cobre eventos e propriedades recomendados de eCommerce. Esses eventos são criados para capturar comportamentos de compra chave que os profissionais de marketing precisam para disparar mensagens eficazes, como direcionar carrinhos abandonados.

{% alert important %}
Os eventos recomendados de eCommerce estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se estiver interessado em participar deste acesso antecipado. <br><br>Se você estiver usando o novo [conector Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), esses eventos recomendados estarão automaticamente disponíveis através da integração.
{% endalert %}

A Braze reconhece que o planejamento de dados leva tempo. Incentivamos nossos clientes a familiarizarem suas equipes de desenvolvimento e começarem a enviar esses eventos agora. Embora alguns recursos possam não estar disponíveis imediatamente com os eventos recomendados de eCommerce, você pode aguardar a introdução de novos produtos ao longo de 2025 que aprimorarão suas capacidades de eCommerce.

## Tipos de eventos recomendados de eCommerce

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Qualquer moeda que não seja USD relatada será exibida na Braze em USD com base na taxa de câmbio na data em que foi relatada. Para evitar conversão de moeda, defina a moeda como USD.

{% tabs %}
{% tab ecommerce.product_viewed %}

Você pode usar o evento de produto visualizado para disparar quando um cliente visualiza uma página de detalhes do produto.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. <br> Para clientes que não são Shopify, este será o valor que você definir para IDs de itens de catálogo como SKUs. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. | 
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL para a página do produto para mais detalhes. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `currency` | Sim | String | A moeda na qual o preço do produto está listado (como "USD" ou "EUR") no [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto | |
| `type` | Não | Objeto | Funciona com [notificações de volta ao estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) e [notificações de queda de preço]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de exemplo

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        }
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

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
Produtos por carrinho não têm limite no Braze. No entanto, o limite do Shopify é 500.
{% endalert %}

#### Comportamento do carrinho ao mesclar perfis de usuário

Se houver dois carrinhos, adicione ambos ao usuário mesclado. Reenfileire o canva se for o mesmo ou diferente carrinho para enviar uma mensagem com as informações mais recentes do carrinho. O evento `ecommerce.cart_updated` conterá o ID do carrinho mais recente e os produtos mais recentes no carrinho.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `cart_id` | Sim | String | Se você não estiver usando uma plataforma de terceiros que forneça um `cart_id`, pode usar o [Braze session ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
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
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de exemplo

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

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
| `cart_id` | Não | String | Se você não estiver usando uma plataforma de terceiros que forneça um `cart_id`, pode usar o [Braze session ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). | 
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
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `metadata` | Não | Objeto |  |
| `checkout_url` | Não | String | URL para a página de checkout. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de exemplo

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

Você pode usar o evento de pedido realizado para disparar quando um cliente completa com sucesso o processo de checkout e faz um pedido.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dados | Descrição | 
|---|---|---|---|
| `order_id` | Sim | String | Identificador único para o pedido realizado. |
| `cart_id` | Não | String | Se você não estiver usando uma plataforma de terceiros que forneça um `cart_id`, pode usar o [Braze session ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Sim | Float | Valor monetário total do carrinho. | 
| `currency` | Sim | String | Moeda na qual o carrinho é avaliado. |
| `total_discounts` | Não | Float | Valor total dos descontos aplicados ao pedido. | 
| `discounts`| Não | Vetor de objetos | Lista detalhada de descontos aplicados ao pedido. |
| `products` | Sim | Vetor de objetos |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL para a página do produto para mais detalhes. |
| `quantity` | Sim | Inteiro | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Objeto | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku` | Não | String | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine). |
| `order_status_url` | Não | String | URL para visualizar o status do pedido. |
| `order_number` | Não | String | (Apenas Shopify) Número de pedido único para o pedido realizado. |
| `tags` | Não | Vetor | (Apenas Shopify) Etiquetas do pedido
| `referring_site` | Não | String | (Apenas Shopify) O site de onde o pedido se originou (como Meta). |
| `payment_gateway_names` | Não | Vetor | (Apenas Shopify) Fonte do sistema de pagamento (como ponto de venda ou móvel). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de exemplo

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

Você pode usar o evento de pedido reembolsado para disparar quando um pedido é parcialmente ou totalmente reembolsado.

#### Propriedades

| Nome da propriedade       | Obrigatória | Tipo de dados | Descrição   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sim      | String    | Identificador único para o pedido realizado.        |
| `total_value`         | Sim      | Float     | Valor monetário total do carrinho.    |
| `currency`            | Sim      | String    | Moeda na qual o carrinho é avaliado.    |
| `total_discounts`     | Não       | Float     | Valor total dos descontos aplicados ao pedido.   |
| `discounts`           | Não       | Vetor de objetos     | Lista detalhada de descontos aplicados ao pedido. |
| `products`            | Sim      | Vetor de objetos     |  |
| `product_id`       | Sim      | String    | Um identificador único para o produto que foi visualizado. Este valor pode ser o ID do produto, SKU ou similar. <br>Se um reembolso parcial for emitido e não houver `product_id` atribuído ao reembolso (por exemplo, um reembolso em nível de pedido), forneça um `product_id` generalizado.             |
| `product_name`     | Sim      | String    | O nome do produto que foi visualizado.                                                                      |
| `variant_id`       | Sim      | String    | Um identificador único para a variante do produto (como `shirt_medium_blue`).                                         |
| `image_url`        | Não       | String    | URL da imagem do produto.     |
| `product_url`      | Não       | String    | URL para a página do produto para mais detalhes.  |
| `quantity`         | Sim      | Inteiro   | Número de unidades do produto no carrinho.   |
| `price`            | Sim      | Float     | O preço unitário da variante do produto no momento da visualização.  |
| `metadata`         | Não       | Objeto    | Campo de metadados adicional sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. Isso terá um limite baseado em nosso limite geral de propriedades de eventos de 50kb. |
| `sku`            | Não       | String    | (Apenas Shopify) SKU do Shopify. Isso pode ser configurado como o campo de ID do catálogo.  |
| `source`              | Sim      | String    | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine).    |
| `metadata`            | Não       | Objeto    |                |
| `order_status_url`  | Não       | String    | URL para visualizar o status do pedido.     |
| `order_note`       | Não       | String    | (Apenas Shopify) Nota anexada ao pedido pelo comerciante.    |
| `order_number`     | Não       | String    | (Apenas Shopify) Número de pedido único para o pedido realizado.   |
| `tags`             | Não       | Vetor     | (Apenas Shopify) Etiquetas do pedido.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de exemplo

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

Você pode usar o evento de pedido cancelado para disparar quando um cliente cancela um pedido.

#### Propriedades

| Nome da propriedade      | Obrigatória | Tipo de dados | Descrição       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sim      | String    | Identificador único para o pedido realizado.              |
| `cancel_reason`       | Sim      | String    | Motivo pelo qual o pedido foi cancelado.           |
| `total_value`         | Sim      | Float     | Valor monetário total do carrinho.         |
| `currency`            | Sim      | String    | Moeda na qual o carrinho é avaliado.           |
| `total_discounts`     | Não       | Float     | Total de descontos aplicados ao pedido.     |
| `discounts`           | Não       | Vetor de objetos     | Lista detalhada de descontos aplicados ao pedido.             |
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
| `source`              | Sim      | String    | Fonte da qual o evento é derivado. (Para Shopify, isso é a vitrine).    |
| `metadata`            | Não       | Objeto    |       |
| `order_status_url`    | Não       | String    | URL para visualizar o status do pedido.                                                                          |
| `order_number`        | Não       | String    | (Apenas Shopify) Número de pedido único para o pedido realizado.  |
| `tags`                | Não       | Vetor     | (Apenas Shopify) Etiquetas de pedido.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de exemplo

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Modelos de Canvas de eCommerce

A Braze criou modelos de Canvas pré-construídos que são alimentados por eventos recomendados de eCommerce, como direcionar clientes que iniciaram o processo de checkout, mas saíram antes de finalizar o pedido. Você pode usar esses eventos para tomar decisões informadas para melhorar a jornada do usuário, personalizando o envio de mensagens e direcionando públicos específicos.

Confira nossos [casos de uso de eCommerce]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) dedicados para mais maneiras de como você pode usar esses eventos com modelos de Canvas.

## Campos calculados pelo usuário

Usamos cálculos de campos de usuário padronizados para os seguintes campos: 

- **Receita Total** = soma do valor total dos pedidos realizados - soma do valor total dos pedidos reembolsados
- **Contagem Total de Pedidos** = contagem de eventos de pedidos distintos realizados - contagem de eventos de cancelamentos de pedidos distintos
- **Valor Total de Reembolso** = soma do valor total dos pedidos reembolsados 

Esses cálculos de campos de usuário também estão incluídos na aba **Transações** dos perfis de usuário.

![A aba "Transações" com campos calculados pelo usuário.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}
