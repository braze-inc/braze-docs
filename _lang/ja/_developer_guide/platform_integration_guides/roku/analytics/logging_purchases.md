---
nav_title: 購入のロギング
article_title: Roku の購入のロギング
platform: Roku
page_order: 3
page_type: reference
description: "このページでは、Braze SDK を介して Roku の購入イベントをロギングする方法について説明します。"

---
 
# 購入のロギング

> アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいてドルでダッシュボードに表示されます。

実装前に、[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

## 購入と売上のトラッキング

この機能を使用するには、アプリ内購入が正常に完了した後でこのメソッド呼び出しを追加します。

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### プロパティの追加

購入に関するメタデータを追加するには、購入情報とともにプロパティディクショナリを渡します。

プロパティはキーと値のペアとして定義されています。 キーは `String` オブジェクトで、値は `String` または `Integer` になります。

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### 注文レベルでの購入記録
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

### REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) のドキュメントを参照してください。

