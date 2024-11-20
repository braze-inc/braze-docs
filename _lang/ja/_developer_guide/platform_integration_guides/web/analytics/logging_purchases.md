---
nav_title: 購入のロギング
article_title: Web の購入のロギング
platform: Web
page_order: 4
page_type: reference
description: "この記事では、Web に関して、購入を記録し、それらの購入にプロパティを追加する方法について説明します。"

---
 
# 購入のロギング

> アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。 

Braze は複数の通貨での購入に対応しています。ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいてドルでダッシュボードに表示されます。

実施にあたっては、まずカスタムイベントs、カスタム属性s、購買イベントが提供するセグメンテーション選択肢の事例を[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)で検討すること。

この機能を使用するには、アプリでの購入が成功した後に[`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)呼び出しを追加します。`quantity` は100以下でなければなりません。

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## プロパティの追加

購入に関する[メタデータ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)を追加するには、[イベントプロパティ配列]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects)を渡すか、購入情報を含むキーと値のペアのオブジェクトを渡します。 

#### オブジェクトのフォーマット

キーは `string` オブジェクトであり、値は `string`、`numeric`、`boolean`、または `Date` オブジェクトになります。

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### 注文レベルでの購入記録
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) のドキュメントを参照してください。

