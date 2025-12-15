---
nav_title: 購入のロギング
article_title: Windowsユニバーサルの購入履歴を記録する
platform: Windows Universal
page_order: 4
description: "この参考記事では、Windowsユニバーサルプラットフォームでの購入履歴の記録方法について説明する。"
hidden: true
---
 
# 購入のロギング
{% multi_lang_include archive/windows_deprecation.md %}

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装する前に、カスタムイベント、カスタム属性、購入イベントによって提供されるセグメンテーションオプションの例を、[ベストプラクティスの]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)記事で確認してほしい。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

この機能を使用するには、アプリ内購入が正常に完了した後でこのメソッド呼び出しを追加します。

購入は、`EventLogger` を使用してログに記録されます。これは、IAppboy で公開されているプロパティです。`EventLogger` への参照を取得するには、`Appboy.SharedInstance.EventLogger` を呼び出します。

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## 注文レベルでの購入記録
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) のドキュメントを参照してください。

