---
nav_title: 購入のロギング
article_title: Unityの購入履歴
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "この参考記事では、Unityプラットフォームでの購入履歴の記録方法について説明します。"

---
 
# 購入のロギング

> アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装前に、[ベストプラクティス][5]記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。

この機能を使用するには、アプリで購入が成功した後に以下のメソッド呼び出しを追加します：

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

この方法では、数量1の購入が記録される。別の数量を渡したい場合は、以下のメソッドを呼び出すことができる：

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

数量は100以下でなければならない。Brazeは、`Dictionary` の購入プロパティを渡すことで、購入に関するメタデータを追加することもサポートしています：

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## 注文レベルで購入を記録する
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## 通貨コード

以下のコードがサポートされている通貨記号です。これ以外の通貨コードを指定すると警告が記録され、SDK でその他のアクションは実行されません。

- USD、AED、AFN、ALL、AMD、ANG、AOA、ARS、AUD、AWG、AZN、BAM、BBD、BDT、BGN、BHD、BIF、BMD、BND、BOB、BRL、BSD、btc, btn, bwp, byr, bzd, cad, cdf, chf, clf, clp, cny, cop, crc, cuc, cup, cve, czk, djf, dkk, dop, dzd、eek, egp, ern, etb, eur, fjd, fkp, gbp, gel, ggp, ghs, gip, gmd, gnf, gtq, gyd, hkd, hnl, hrk, htg, huf, idr、ils、imp、inr、iqd、irr、isk、jep、jmd、jod、jpy、kes、kgs、khr、kmf、kpw、krw、kwd、kyd、kzt、lak、lbp、lkr, lrd, lsl, ltl, lvl, lyd, mad, mdl, mga, mkd, mmk, mnt, mop, mro, mtl, mur, mvr, mwk, mxn, myr, mzn, nad、ngn, nio, nok, npr, nzd, omr, pab, pen, pgk, php, pkr, pln, pyg, qar, ron, rsd, rub, rwf, sar, sbd, scr、sdg, sek, sgd, shp, sll, sos, srd, std, svc, syp, szl, thb, tjs, tmt, tnd, top, try, ttd, twd, tzs, uah、UGX、UYU、UZS、VEF、VND、VUV、WST、XAF、XAG、XAU、XCD、XDR、XOF、XPD、XPF、XPT、YER、ZAR、ZMK、ZMW、ZWL。

## サンプルコード

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## REST API

REST API を使用して購入を記録することもできます。詳細については、[ユーザー API][4] のドキュメントを参照してください。

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
