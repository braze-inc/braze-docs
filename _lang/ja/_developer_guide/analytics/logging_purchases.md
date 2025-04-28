---
nav_title: 購入のロギング
article_title: Braze SDK を使用した購入の記録
page_order: 3.2
description: "Braze SDK を使用して購入を記録する方法について説明します。"

---

# 購入のロギング

> Braze SDK を使用してアプリの購入をログインする方法を学習することで、経時的およびソース間で収益を判断できます。これにより、ユーザのライフタイム値 に基づいて、カスタムイベント、カスタム属性、および購入イベントを使用して、ユーザをセグメント化できます[。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。
{% endalert %}

## 仕入および収益の記録

購入と収益を記録するには、アプリでの正常な購入後に`logPurchase()` を呼び出します。製品 ID が空の場合、購入は Braze に記録されません。

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

{% tab ウェブ %}
標準のWeb SDK 実装では、以下の方法を使用できます。

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

代わりにGoogleタグマネージャを使用したい場合は、**Purchase**タグタイプを使用して、[`logPurchase`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)を呼び出すことができます。このタグを使用して、Brazeへの購入を追跡します。オプションで、購入プロパティを含めます。そのためには:

1. **商品ID**と**価格**フィールドsが必要です。
2. 購入プロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ構成設定を示すダイアログボックス。含まれる設定は、「タグタイプ」、「外部ID」、「価格」、「通貨コード」、「数量」、「購入プロパティ」である。]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab コルドバ %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab フラッタ %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab 天然に反応する %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab 六 %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab Unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}

{% tab 非現実的なエンジン %}

```cpp
UBraze->LogPurchase(TEXT("product_id"), TEXT("USD"), price, quantity);
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` 最大255 文字まで指定できます。さらに、製品識別子が空の場合、購入はブレーズに記録されません。
{% endalert %}

### プロパティの追加

`Int`、`Double`、`String`、`Bool`、または `Date` の値が入力されたディクショナリを渡すことで、購入に関するメタデータを追加できます。

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

{% tab ウェブ %}
標準のWeb SDK 実装では、以下の方法を使用できます。

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

サイトが標準の[eCommerceイベント](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)データレイヤーアイテムを使用して購入をGoogleタグマネージャーに記録する場合、**E-commerce Purchase**タグタイプを使用できます。このアクションタイプでは、`items` のリストで送信されたアイテムごとに個別の「購入」を Braze に記録します。

購入プロパティリストでキーを指定することで、購入プロパティとして含める追加のプロパティの名前を指定することもできます。Brazeは、一覧に追加した購入プロパティーのログに記録されている個々の`item` 内を検索します。

たとえば、次のeCommerce ペイロードがあるとします。

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

`item_brand` と `item_name` だけを購入プロパティとして渡す場合は、これら2つのフィールドを購入プロパティテーブルに追加するだけです。プロパティを指定しない場合、[[`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)] Braze の呼び出しで購入プロパティは送信されません。
{% endtab %}

{% tab コルドバ %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab フラッタ %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab 天然に反応する %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab 六 %}

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

{% tab 非現実的なエンジン %}

```cpp
TMap<FString, FString> PurchaseProperties;
PurchaseProperties.Add(TEXT("key"), TEXT("value"));

UBraze->LogPurchaseWithProperties(TEXT("product_id"), TEXT("USD"), price, quantity, PurchaseProperties);
```

{% endtab %}
{% endtabs %}

### 数量の追加

デフォルトでは、`quantity` は`1` に設定されます。ただし、顧客が1回のチェックアウトで同じ購入を複数回行う場合は、購入に数量を追加できます。数量を追加するには、`Int` 値を`quantity` に渡します。これは`[0, 100]` の範囲内です。

### REST API の使用

REST API を使用して購入を記録することもできます。詳細については、[User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ログ受注

商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## 予約済みのキー

以下のキーは予約されているため、購入プロパティとして使用できません。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## 対応通貨

サポートされている通貨記号です。他の通貨記号を入力すると、警告がログに記録され、購入はブレーズに記録されません。

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
