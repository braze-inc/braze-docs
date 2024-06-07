---
nav_title: 購入のロギング
article_title: Web での購入のログ記録
platform: Web
page_order: 4
page_type: reference
description: "この記事では、Web で購入を記録し、それらの購入にプロパティを追加する方法について説明します。"

---
 
# 購入のロギング

> アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。 

Braze は複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装前に、[ベストプラクティス][3]記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。

この機能を使用するには、アプリで購入が成功した後に呼び出しを追加します [`logPurchase()`][8] 。は `quantity` 100 以下でなければならないことに注意してください。

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## プロパティの追加

購入に関する [メタデータ][8] を追加するには、 [イベントプロパティ配列]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) を渡すか、購入情報を含むキーと値のペアのオブジェクトを渡します。 

#### オブジェクトの書式設定

キーは `string` オブジェクトで、値は `string`、`numeric`、`boolean`、`Date`、または  オブジェクトになります。

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### 注文レベルで購入を記録する
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API][1] のドキュメントを参照してください。

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[8]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase
