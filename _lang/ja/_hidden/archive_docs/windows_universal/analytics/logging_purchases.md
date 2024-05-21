---
nav_title: 購入履歴
article_title: Windowsユニバーサルの購入履歴
platform: Windows Universal
page_order: 4
description: "この参考記事では、Windowsユニバーサルプラットフォームでの購入履歴の記録方法について説明します。"
hidden: true
---
 
# 購入履歴
{% multi_lang_include archive/windows_deprecation.md %}

アプリ内課金を記録することで、長期的な収益や収益源の違いを追跡したり、ユーザーのライフタイムバリューでセグメント化したりすることができます。

Brazeは複数通貨での購入に対応しています。米ドル以外の通貨で報告した購入品は、報告日の為替レートに基づいて米ドルでダッシュボードに表示されます。

実装する前に、カスタムイベント、カスタム属性、購入イベントによって提供されるセグメンテーションオプションの例を、[ベストプラクティスの][3]記事で確認してください。また、[イベントの命名規則を]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)よく理解されることをお勧めします。

この機能を使用するには、アプリで購入が成功した後にこのメソッド呼び出しを追加します：

購入履歴はIAppboyで公開されている`EventLogger` 。`EventLogger` への参照を得るには、`Appboy.SharedInstance.EventLogger` を呼び出す。

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## 注文レベルでのログ購入
商品レベルではなく、注文レベルで購入のログを取りたい場合、注文名または注文カテゴリーを`product_id` として使用することができます。詳しくは、[購入対象の仕様を]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)ご覧ください。 

## REST API

また、REST APIを使用して購入を記録することもできます。詳細については、[ユーザーAPIの][2]ドキュメントを参照のこと。

[2]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
