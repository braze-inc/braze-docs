---
nav_title: 購入のロギング
article_title: iOS の購入のロギング
platform: Swift
page_order: 4
description: "このリファレンス記事では、アプリ内購入と売上をトラッキングし、Swift SDK の購入プロパティを割り当てる方法を説明します。"

---

# 購入のロギング

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze では、複数の通貨での購入がサポートされています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装前に、[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)のメモを必ず確認しておいてください。

## 購入と売上のトラッキング

この機能を使用するには、アプリ内購入が正常に完了した後でこのメソッド呼び出しを追加します。

{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endtab %}
{% endtabs %}

- サポートされている通貨コードは USD、CAD、EUR、GBP、JPY、AUD、CHF、NOK、MXN、NZD、CNY、RUB、TRY、INR、IDR、ILS、SAR、ZAR、AED、SEK、HKD、SPD、DKK などです。
  - これ以外の通貨コードを指定すると警告が記録され、SDK でその他のアクションは実行されません。
- 商品 ID は最大 255 文字です。
- 製品 ID が空の場合、購入は Braze に記録されないことに注意してください。

### プロパティ {#properties-purchases} の追加
`Int`、`Double`、`String`、`Bool`、または `Date` の値が入力されたディクショナリを渡すことで、購入に関するメタデータを追加できます。

詳細については、[iOS クラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "logpurchase documentation")を参照してください。

### 数量の追加
顧客が 1 回のチェックアウト手続きで同じ購入を複数回行う場合は、購入に数量を追加できます。これを行うには、数量として `Int` を渡します。

* SDK で購入を記録するには、数量入力が [0, 100] の範囲内である必要があります。
* 数量入力のないメソッドは、デフォルトの数量の値が 1 になります。

詳細については、[iOS クラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "logpurchase documentation")を参照してください。

{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.logPurchase(productId: "product_id", currency: "USD", price: price, quantity: quantity, properties: ["key1":"value1"])
```

{% endtab %}
{% tab OBJECTIVE-C %}

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
10 米ドルという値と数量 3 を渡すと、10 ドルの購入 3 件、合計 30 ドルとしてユーザープロファイルに記録されます。
{% endalert %}

### 注文レベルで購入を記録する
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

### 予約済みのキー

以下のキーは予約されているため、購入プロパティとして使用できません。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API のドキュメント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

