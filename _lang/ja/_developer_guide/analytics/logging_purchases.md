---
nav_title: 購入のロギング
article_title: Braze SDK を使用した購入のロギング
page_order: 3.2
description: "Braze SDK を使用して購入を記録する方法について説明します。"

---

# 購入のロギング

> Braze SDK を使用してアプリ内購入をログに記録する方法について説明します。これにより、時間の経過やさまざまなソースにわたる収益を把握できるようになります。これにより、カスタムイベント、カスタム属性、および購入イベントを使用して、[生涯価値に基づいて]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking)ユーザーをセグメント化できます。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。
{% endalert %}

USD以外の通貨がレポートされた場合、Brazeではレポートされた日の為替レートに基づいてUSDで表示される。通貨コンバージョンを防ぐため、通貨をUSDにハードコードする。

## 購入と売上のロギング

購入と収益を記録するには、アプリでの正常な購入後に`logPurchase()` を呼び出します。製品 ID が空の場合、購入は Braze に記録されません。

{% tabs %}
{% tab web %}
標準のWeb SDK 実装では、以下の方法を使用できます。

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

代わりにGoogleタグマネージャを使用したい場合は、**Purchase**タグタイプを使用して、[`logPurchase`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)を呼び出すことができます。このタグを使用して、Brazeへの購入を追跡します。オプションで、購入プロパティを含めます。そのために必要なこと:

1. **商品ID**と**価格**フィールドsが必要です。
2. 購入プロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ構成設定を示すダイアログボックス。含まれる設定は、「タグタイプ」、「外部ID」、「価格」、「通貨コード」、「数量」、「購入プロパティ」である。]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
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
`productID` の最大文字数は 255 文字です。さらに、製品 ID が空の場合、購入は Braze に記録されないことに注意してください。
{% endalert %}

### プロパティの追加

`Int`、`Double`、`String`、`Bool`、または `Date` の値が入力されたディクショナリを渡すことで、購入に関するメタデータを追加できます。

{% tabs %}
{% tab web %}
標準のWeb SDK 実装では、以下の方法を使用できます。

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

サイトで標準の [[e コマースイベント](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)] データ層アイテムを使用して購入を Google Tag Manager に記録する場合は、**e コマース購入**タグタイプを使用できます。このアクションタイプでは、`items` のリストで送信されたアイテムごとに個別の「購入」を Braze に記録します。

購入プロパティリストでキーを指定することで、購入プロパティとして含める追加のプロパティの名前を指定することもできます。Brazeは、一覧に追加した購入プロパティーのログに記録されている個々の`item` 内を検索します。

たとえば、次の e コマースペイロードがあるとします。

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

### 数量の追加

デフォルトでは、`quantity` は`1` に設定されます。ただし、顧客が1回のチェックアウトで同じ購入を複数回行う場合は、購入に数量を追加できます。数量を追加するには、`Int` 値を`quantity` に渡します。

### REST API の使用

REST API を使用して購入を記録することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## 注文のロギング

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

サポートされている通貨記号です。他の通貨記号を指定すると警告が記録され、購入は Braze に記録されません。

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
