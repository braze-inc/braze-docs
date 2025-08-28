---
nav_title: Käufe protokollieren
article_title: Protokollierung von Einkäufen über das Braze SDK
page_order: 3.2
description: "Erfahren Sie, wie Sie Einkäufe über das Braze SDK protokollieren können."

---

# Einkäufe protokollieren

> Erfahren Sie, wie Sie In-App-Käufe über das Braze SDK protokollieren können, damit Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Quellen hinweg bestimmen können. Damit können Sie Nutzer:innen [anhand ihres Lifetime-Value]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking) mit angepassten Events, angepassten Attributen und Kauf-Events segmentieren.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Käufe und Einnahmen protokollieren

Um Käufe und Umsätze zu protokollieren, rufen Sie `logPurchase()` nach einem erfolgreichen Kauf in Ihrer App auf. Wenn der Bezeichner des Produkts leer ist, wird der Kauf nicht in Braze protokolliert.

{% tabs %}
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

{% tab schnell %}
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

{% tab Internet %}
Für eine Standard Internet SDK-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Wenn Sie stattdessen Google Tag Manager verwenden möchten, können Sie den Tag-Typ **Purchase** verwenden, um die [Methode`logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) aufzurufen. Verwenden Sie dieses Tag, um Käufe zu tracken, und schließen Sie optional Kauf-Eigenschaften ein. Um dies zu tun:

1. Die Felder **Produkt-ID** und **Preis** sind erforderlich.
2. Verwenden Sie den Button **Zeile hinzufügen**, um Kauf-Eigenschaften hinzuzufügen.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Zu den Einstellungen gehören "Tag-Typ", "Externe ID", "Preis", "Währungscode", "Menge" und "Kauf-Eigenschaften".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flattern %}

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
`productID` kann nur maximal 255 Zeichen lang sein. Wenn der Bezeichner des Produkts leer ist, wird der Kauf außerdem nicht in Braze protokolliert.
{% endalert %}

### Hinzufügen von Eigenschaften

Sie können Metadaten über Käufe hinzufügen, indem Sie ein Wörterbuch mit den Werten `Int`, `Double`, `String`, `Bool` oder `Date` übergeben.

{% tabs %}
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

{% tab schnell %}
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

{% tab Internet %}
Für eine Standard Internet SDK-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Wenn Ihre Website Einkäufe unter Verwendung des [Standard-Event-Daten-Layer-Artikels](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) in Google Tag Manager protokolliert, können Sie den Tag-Typ **E-Commerce Purchase** verwenden. Dieser Aktionstyp protokolliert in Braze einen separaten "Kauf" für jeden Artikel in der Liste `items`.

Sie können auch weitere Eigenschaftsnamen angeben, die Sie als Kauf-Eigenschaften einbeziehen möchten, indem Sie deren Schlüssel in der Liste der Kauf-Eigenschaften angeben. Beachten Sie, dass Braze in einem individuellen `item`, der protokolliert wird, nach Kauf-Eigenschaften sucht, die Sie der Liste hinzufügen.

Nehmen wir zum Beispiel die folgende E-Commerce-Nutzlast:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Wenn Sie nur `item_brand` und `item_name` als Kaufeigenschaften übergeben möchten, fügen Sie einfach diese beiden Felder zur Tabelle der Kaufeigenschaften hinzu. Wenn Sie keine Eigenschaften angeben, werden auch keine Kauf-Eigenschaften im Aufruf [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) an Braze gesendet.
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flattern %}

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

### Menge hinzufügen

Standardmäßig ist `quantity` auf `1` eingestellt. Sie können jedoch eine Menge zu Ihren Einkäufen hinzufügen, wenn Kund:innen denselben Einkauf mehrmals in einer einzigen Kasse tätigen. Um eine Menge hinzuzufügen, übergeben Sie einen `Int` Wert an `quantity`.

### Verwendung der REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data):in.

## Aufträge protokollieren

Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als Kaufeigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Unterstützte Währungen

Dies sind die unterstützten Währungssymbole. Jedes andere Währungssymbol, das Sie angeben, führt zu einer Warnung und der Kauf wird nicht in Braze gespeichert.

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
