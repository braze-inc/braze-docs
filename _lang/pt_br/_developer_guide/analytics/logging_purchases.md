---
nav_title: Registrar compras
article_title: Registrar compras através do SDK Braze
page_order: 3.2
description: "Aprenda como registrar compras através do SDK Braze."

---

# Registrar compras

> Aprenda como registrar compras dentro do aplicativo através do SDK Braze, para que você possa determinar sua receita ao longo do tempo e entre fontes. Isso permitirá que você segmente usuários [com base em seu valor do tempo de vida]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking) usando eventos personalizados, atributos personalizados e eventos de compra.

{% alert note %}
Para SDKs wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

Qualquer moeda que não seja USD reportada será exibida no Braze em USD com base na taxa de câmbio na data em que foi reportada. Para evitar conversão de moeda, defina a moeda como USD.

## Registrando compras e receita

Para registrar compras e receita, chame `logPurchase()` após uma compra bem-sucedida em seu aplicativo. Se o identificador do produto estiver vazio, a compra não será registrada no Braze.

{% tabs %}
{% tab web %}
Para uma implementação padrão do SDK Web, você pode usar o seguinte método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Se você preferir usar o Google Tag Manager, pode usar o tipo de tag **Compra** para chamar o método [`logPurchase` método](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Use essa tag para rastrear as compras no Braze, incluindo opcionalmente as propriedades de compra. Para fazer isso:

1. Os campos **ID do produto** e **Preço** são obrigatórios.
2. Use o botão **Adicionar linha** para adicionar propriedades de compra.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tipo de tag", "ID externo", "preço", "código da moeda", "quantidade" e "propriedades de compra".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` pode ter no máximo 255 caracteres. Além disso, se o identificador do produto estiver vazio, a compra não será registrada no Braze.
{% endalert %}

### Adição de propriedades

Você pode adicionar metadados sobre compras passando um Dicionário preenchido com os valores `Int`, `Double`, `String`, `Bool`, ou `Date`.

{% tabs %}
{% tab web %}
Para uma implementação padrão do SDK Web, você pode usar o seguinte método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Se seu site registrar compras usando o item de camada de dados padrão [evento de eCommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) para o Google Tag Manager, então você pode usar o tipo de tag **Compra de E-commerce**. Esse tipo de ação registrará uma "compra" separada no Braze para cada item enviado na lista de `items`.

Você também pode especificar nomes de propriedades adicionais que deseja incluir como propriedades de compra, especificando suas chaves na lista Propriedades de compra. Note que o Braze procurará no site `item` individual que está sendo registrado todas as propriedades de compra que você adicionar à lista.

Por exemplo, dado o seguinte payload de eCommerce:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Se você quiser que apenas `item_brand` e `item_name` sejam passados como propriedades de compra, basta adicionar esses dois campos à tabela de propriedades de compra. Se você não fornecer nenhuma propriedade, nenhuma propriedade de compra será enviada na [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) chamada para o Braze.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
                      currency:@"USD"
                         price:price
                   properties:purchaseProperties];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}
{% endtabs %}

### Adição de quantidade

Por padrão, `quantity` é definido como `1`. No entanto, você pode adicionar uma quantidade às suas compras se os clientes fizerem a mesma compra várias vezes em um único checkout. Para adicionar uma quantidade, passe um valor `Int` para `quantity`.

### Usando a API REST

Também é possível usar nossa API REST para registrar compras. Para saber mais, consulte [Dados de Usuários Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Registrando pedidos

Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

## Chaves reservadas

As seguintes chaves são reservadas e não podem ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Moedas suportadas

Estes são os símbolos de moeda suportados. Qualquer outro símbolo de moeda que você fornecer registrará um aviso e a compra não será registrada no Braze.

- `USD`
- `CAD`
- `EUR`
- `GBP`
- `JPY`
- `AUD`
- `CHF`
- `NOK`
- `MXN`
- `NZD`
- `CNY`
- `RUB`
- `TRY`
- `INR`
- `IDR`
- `ILS`
- `SAR`
- `ZAR`
- `AED`
- `SEK`
- `HKD`
- `SPD`
- `DKK`
