---
nav_title: Logging purchases
article_title: Logging purchases through the Braze SDK
page_order: 3.2
description: "Learn how to log purchases through the Braze SDK."

---

# Logging purchases

> Learn how to log in-app purchases through the Braze SDK, so you can determine your revenue over-time and across sources. This will let you segment users [based on their lifetime value]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking) using custom events, custom attributes, and purchase events.

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android or Swift method instead.
{% endalert %}

Any non-USD currency reported will display in Braze in USD based on the exchange rate on the date it was reported. To prevent currency conversion, hardcode the currency to USD.

## Logging purchases and revenue

To log purchases and revenue, call `logPurchase()` after a successful purchase in your app. If the product Identifier is empty, the purchase will not be logged to Braze.

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
For a standard Web SDK implementation, you can use the following method:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

If you'd like to use Google Tag Manager instead, you can use the **Purchase** tag type to call the [`logPurchase` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Use this tag to track purchases to Braze, optionally including purchase properties. To do so:

1. The **Product ID** and **Price** fields are required.
2. Use the **Add Row** button to add purchase properties.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type", "external ID", "price", "currency code", "quantity", and "purchase properties".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
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

{% tab unreal engine %}

```cpp
UBraze->LogPurchase(TEXT("product_id"), TEXT("USD"), price, quantity);
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` can only have a maximum of 255 characters. Additionally, if the product identifier is empty, the purchase will not be logged to Braze.
{% endalert %}

### Adding properties

You can add metadata about purchases by passing a Dictionary populated with `Int`, `Double`, `String`, `Bool`, or `Date` values.

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
For a standard Web SDK implementation, you can use the following method:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

If your site logs purchases using the standard [eCommerce event](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) data layer item to Google Tag Manager, then you can use the **E-commerce Purchase** tag type. This action type will log a separate "purchase" in Braze for each item sent in the list of `items`.

You can also specify additional property names you want to include as purchase properties by specifying their keys in the Purchase properties list. Note that Braze will look within the individual `item` that is being logged for any purchase properties you add to the list.

For example, given the following eCommerce payload:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

If you only want `item_brand` and `item_name` to be passed as purchase properties, then just add those two fields to the purchase properties table. If you don't supply any properties, then no purchase properties will be sent in the [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) call to Braze.
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

{% tab unreal engine %}

```cpp
TMap<FString, FString> PurchaseProperties;
PurchaseProperties.Add(TEXT("key"), TEXT("value"));

UBraze->LogPurchaseWithProperties(TEXT("product_id"), TEXT("USD"), price, quantity, PurchaseProperties);
```

{% endtab %}
{% endtabs %}

### Adding quantity

By default, `quantity` is set to `1`. However, you can add a quantity to your purchases if customers make the same purchase multiple times in a single checkout. To add a quantity, pass an `Int` value to `quantity`.

### Using the REST API

You can also use our REST API to record purchases. For more information, refer to [User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Logging orders

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

## Reserved keys

The following keys are reserved and cannot be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Supported currencies

These are the supported currency symbols. Any other currency symbol you provide will log a warning and the purchase will not be logged to Braze.

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
