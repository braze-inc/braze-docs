---
nav_title: Registro de compras
article_title: Registro de compras para iOS
platform: Swift
page_order: 4
description: "Este artigo de referência mostra como rastrear compras e receitas no app e atribuir propriedades de compra para o Swift SDK."

---

# Registro de compras

Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita e segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [práticas recomendadas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Rastreamento de compras e receitas

Para usar esse recurso, adicione essa chamada de método após uma compra bem-sucedida em seu app:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endtab %}
{% endtabs %}

- Os símbolos de moeda compatíveis incluem: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK e muito mais.
  - Qualquer outro símbolo de moeda fornecido resultará em um aviso registrado e nenhuma outra ação será realizada pelo SDK.
- A ID do produto pode ter no máximo 255 caracteres
- Note que se o identificador do produto estiver vazio, a compra não será registrada na Braze.

### Adição de propriedades {#properties-purchases}
Você pode adicionar metadados sobre compras passando um Dicionário preenchido com os valores `Int`, `Double`, `String`, `Bool`, ou `Date`.

Consulte a [documentação da classe iOS e a ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "documentação do registro de compra") para obter mais detalhes.

### Adição de quantidade
Você pode adicionar uma quantidade às suas compras se os clientes fizerem a mesma compra várias vezes em um único checkout. Você pode fazer isso passando um `Int` para a quantidade.

* Uma entrada de quantidade precisa estar no intervalo de [0, 100] para que o SDK registre uma compra.
* Os métodos sem uma entrada de quantidade terão um valor de quantidade padrão de 1.

Consulte a [documentação da classe iOS e a ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "documentação do registro de compra") para obter mais detalhes.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logPurchase(productId: "product_id", currency: "USD", price: price, quantity: quantity, properties: ["key1":"value1"])
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze logPurchase:productId
                      currency:@"USD"
                         price:price
                      quantity:quantity
                    properties:@{@"checkout_id" : self.checkoutId}];
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Se você passar um valor de 10 dólares e uma quantidade de 3, isso será registrado no perfil do usuário como três compras de 10 dólares, totalizando 30 dólares.
{% endalert %}

### Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Chaves reservadas

As seguintes chaves são reservadas e não podem ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

Também é possível usar nossa API REST para registrar compras. Consulte a [documentação da API do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

