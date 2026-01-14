 
# 購入のロギング

> アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。このリファレンス記事では、Android または FireOS アプリケーションでアプリ内購入と収益をトラッキングし、購入プロパティを割り当てる方法を説明します。

Braze は複数の通貨での購入に対応しています。ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいてドルでダッシュボードに表示されます。

実装する前に、[分析の概要]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)でカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。

## 購入と売上のトラッキング

この機能を使用するには、アプリで正常な購入後に[`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html)を呼び出します。製品 ID が空の場合、購入は Braze に記録されません。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
金額`10 USD`と数量`3`を渡すと、10ドルの購入3件、合計30ドルとしてユーザーのプロファイルに記録されます。数量は100以下でなければなりません。購入額がマイナスになることもあります。
{% endalert %}

### プロパティの追加

購入に関するメタデータを追加するには、[イベントプロパティ配列]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects)、または購入情報を含む [Braze プロパティ](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html)オブジェクトを渡します。

#### Braze プロパティオブジェクトの書式設定

プロパティはキーと値のペアとして定義されています。キーは `String` オブジェクトで、値は `String`、`int`、`float`、`boolean`、または [`Date`](http://developer.android.com/reference/java/util/Date.html) オブジェクトになります。

{% tabs %}
{% tab JAVA %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endtab %}
{% endtabs %}

詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) を参照してください。

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

