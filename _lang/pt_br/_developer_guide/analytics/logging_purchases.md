---
nav_title: Registro de compras
article_title: Registro de compras por meio do SDK do Braze
page_order: 3.2
description: "Saiba como registrar compras por meio do Braze SDK."

---

# Registro de compras

> Saiba como registrar as compras no aplicativo por meio do Braze SDK, para que possa determinar sua receita ao longo do tempo e entre as fontes. Isso permitirá segmentar os usuários [com base no valor do tempo de vida deles]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking) usando eventos personalizados, atributos personalizados e eventos de compra.

{% alert note %}
Para SDKs de wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Registro de compras e receitas

Para registrar compras e receitas, ligue para `logPurchase()` após uma compra bem-sucedida no seu app. Se o identificador do produto estiver vazio, a compra não será registrada no Braze.

{% tabs %}
{% tab Android %}
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

{% tab web %}
Para uma implementação padrão do Web SDK, você pode usar o seguinte método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Se, em vez disso, você quiser usar o Google Tag Manager, poderá usar o tipo de tag **Purchase** para chamar o [método`logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Use essa tag para rastrear as compras no Braze, incluindo opcionalmente as propriedades de compra. Para isso:

1. Os campos **ID do produto** e **Preço** são obrigatórios.
2. Use o botão **Adicionar linha** para adicionar propriedades de compra.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (tipo de tag), "external ID" (ID externa), "price" (preço), "currency code" (código de moeda), "quantity" (quantidade) e "purchase properties" (propriedades de compra).]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab Cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab vibração %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab React Native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab Unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}

{% tab Unreal Engine %}

```cpp
UBraze->LogPurchase(TEXT("product_id"), TEXT("USD"), price, quantity);
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` só pode ter um máximo de 255 caracteres. Além disso, se o identificador do produto estiver vazio, a compra não será registrada no Braze.
{% endalert %}

### Adição de propriedades

Você pode adicionar metadados sobre compras passando um Dicionário preenchido com os valores `Int`, `Double`, `String`, `Bool`, ou `Date`.

{% tabs %}
{% tab Android %}
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

{% tab web %}
Para uma implementação padrão do Web SDK, você pode usar o seguinte método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Se o seu site registra compras usando o item padrão da camada de dados de [eventos de comércio eletrônico](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) para o Google Tag Manager, é possível usar o tipo de tag **E-commerce Purchase**. Esse tipo de ação registrará uma "compra" separada no Braze para cada item enviado na lista de `items`.

Você também pode especificar nomes de propriedades adicionais que deseja incluir como propriedades de compra, especificando suas chaves na lista Propriedades de compra. Note que o Braze procurará no site `item` individual que está sendo registrado todas as propriedades de compra que você adicionar à lista.

Por exemplo, dada a seguinte carga útil de comércio eletrônico:

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

{% tab Cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab vibração %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab React Native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab Unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}

{% tab Unreal Engine %}

```cpp
TMap<FString, FString> PurchaseProperties;
PurchaseProperties.Add(TEXT("key"), TEXT("value"));

UBraze->LogPurchaseWithProperties(TEXT("product_id"), TEXT("USD"), price, quantity, PurchaseProperties);
```

{% endtab %}
{% endtabs %}

### Adição de quantidade

Por padrão, `quantity` é definido como `1`. No entanto, você pode adicionar uma quantidade às suas compras se os clientes fizerem a mesma compra várias vezes em um único checkout. Para adicionar uma quantidade, passe um valor `Int` para `quantity`.

### Usando a API REST

Também é possível usar nossa API REST para registrar compras. Para saber mais, consulte [Pontos de extremidade de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Registro de pedidos

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

Esses são os símbolos de moeda compatíveis. Qualquer outro símbolo de moeda que você fornecer registrará um aviso e a compra não será registrada no Braze.

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
