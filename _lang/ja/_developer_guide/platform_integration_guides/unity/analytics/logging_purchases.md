---
nav_title: 購入のロギング
article_title: Unity の購入のロギング
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "この参考記事では、Unity プラットフォームで購入を記録する方法について説明します。"

---
 
# 購入のロギング

> アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいてドルでダッシュボードに表示されます。

実施にあたっては、まずカスタムイベントs、カスタム属性s、購買イベントが提供するセグメンテーション選択肢の事例を[ベストプラクティス][5]で検討すること。

この機能を使用するには、アプリ内購入が正常に完了した後で次のメソッド呼び出しを追加します。

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

このメソッドは、数量が1の購入を記録します。別の数量を渡す場合は、以下のメソッドを呼び出すことができます。

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

数量は100以下である必要があります。Braze では、購入プロパティの `Dictionary` を渡すことによる、購入に関するメタデータの追加もサポートしています。

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## 注文レベルでの購入記録
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## 為替コードs

以下のコードs は、サポートされている通貨記号です。これ以外の通貨コードを指定すると警告が記録され、SDK でその他のアクションは実行されません。

- USD、AED、AFN、ALL、AMD、ANG、AOA、ARS、AUD、AWG、AZN、BAM、BBD、BDT、BGN、BHD、BIF、BMD、BND、BOB、BRL、BSD、BTC、BTN、BWP、BYR、BZD、CAD、CDF、CHF、CLF、CLP、CNY、COP、CRC、CUC、CUP、CVE、CZK、DJF、DKK、DOP、DZD、EEK、EGP、ERN、ETB、EUR、FJD、FKP、GBP、GEL、GGP、GHS、GIP、GMD、GNF、GTQ、GYD、HKD、HNL、HRK、HTG、HUF、IDR、ILS、IMP、INR、IQD、IRR、ISK、JEP、JMD、JOD、JPY、KES、KGS、KHR、KMF、KPW、KRW、KWD、KYD、KZT、LAK、LBP、LKR、LRD、LSL、LTL、LVL、LYD、MAD、MDL、MGA、MKD、MMK、MNT、MOP、MRO、MTL、MUR、MVR、MWK、MXN、MYR、MZN、NAD、NGN、NIO、NOK、NPR、NZD、OMR、PAB、PEN、PGK、PHP、PKR、PLN、PYG、QAR、RON、RSD、RUB、RWF、SAR、SBD、SCR、SDG、SEK、SGD、SHP、SLL、SOS、SRD、STD、SVC、SYP、SZL、THB、TJS、TMT、TND、TOP、TRY、TTD、TWD、TZS、UAH、UGX、UYU、UZS、VEF、VND、VUV、WST、XAF、XAG、XAU、XCD、XDR、XOF、XPD、XPF、XPT、YER、ZAR、ZMK、ZMW、およびZWL。

## サンプルコード

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API][4] のドキュメントを参照してください。

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
