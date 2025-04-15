---
nav_title: Registro de compras
article_title: Registro de compras para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência mostra como rastrear compras e receitas no app e atribuir propriedades de compra em seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Registro de compras para iOS

Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita e segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [práticas recomendadas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Rastreamento de compras e receitas

Para usar esse recurso, adicione essa chamada de método após uma compra bem-sucedida em seu app:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- Os símbolos de moeda compatíveis incluem: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK e muito mais.
  - Qualquer outro símbolo de moeda fornecido resultará em um aviso registrado e nenhuma outra ação será realizada pelo SDK.
- A ID do produto pode ter no máximo 255 caracteres
- Note que se o identificador do produto estiver vazio, a compra não será registrada na Braze.

### Adição de propriedades {#properties-purchases}

Você pode adicionar metadados sobre as compras transmitindo uma [matriz de propriedades de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) ou transmitindo um `NSDictionary` preenchido com os valores `NSNumber`, `NSString` ou `NSDate`.

Consulte a [documentação da classe iOS logpurchase](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc "c/ documentação da classe propriedades") para obter mais detalhes.

### Adição de quantidade
Você pode adicionar uma quantidade às suas compras se os clientes fizerem a mesma compra várias vezes em um único checkout. Você pode fazer isso passando um `NSUInteger` para a quantidade.

* Uma entrada de quantidade precisa estar no intervalo de [0, 100] para que o SDK registre uma compra.
* Os métodos sem uma entrada de quantidade terão um valor de quantidade padrão de 1.
* Os métodos com uma entrada de quantidade não têm valor padrão e **devem** receber uma entrada de quantidade para que o SDK registre uma compra.

Consulte a [documentação da classe iOS logpurchase](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa "c/ documentação da classe quantidade") para obter mais detalhes.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
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

