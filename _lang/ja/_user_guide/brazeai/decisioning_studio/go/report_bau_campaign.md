---
nav_title: BAUキャンペーンのレポート
article_title: BAUキャンペーンのレポート
page_order: 10
description: "この記事では、BAU（Business as Usual）キャンペーンのレポートについて、BrazeAI Decisioning Studio Goポータルでよくある質問にお答えする。"
---

# ビジネス・アズ・ユージュアル キャンペーンのレポート

> この記事では、BAU（Business as Usual）キャンペーンのレポートについて、BrazeAI Decisioning Studio™ Goポータルでよくある質問にお答えする。

## BAUキャンペーンのレポートについて

デフォルトでは、BrazeAI Decisioning Studio™ Goポータルレポートは、BrazeAI Decisioning Studio™ Goとランダムコントロールグループを比較する。この2つのグループを比較するだけでなく、BAU(Business as Usual)グループとBrazeAI Decisioning Studio™ Goのパフォーマンスを比較することもできる。BAUレポートを設定することで、BrazeAI Decisioning Studio™ Goポータルで、3つのグループすべてのパフォーマンスを一箇所で見ることができる。

BAUレポートを設定する主な利点は、BrazeAI Decisioning Studio™ Goの無効クリックフィルターを適用することである。このフィルターを3つの実験グループすべてに適用すると、機械のクリックや配信停止リンクへのクリックが疑われる追加ノイズを除去することで、最も正確で公平な（または「apples to apples」）クリックパフォーマンス比較が可能になる。

## 要件

BAUレポートを設定する前に、まず、BAU治療グループ、BrazeAI Decisioning Studio™ Go、およびランダムコントロールグループの間に、同等比較があることを確認する。これには、以下のチェックが含まれる：

- 受信者は（実験期間中）複数のグループに所属することはできない。
- 受信者は無作為にグループ分けされ、グループ分けに偏りはない。
- BAUグループで利用可能なオプション（クリエイティブ、頻度、時間、インセンティブ、オファー）はすべて、BrazeAI Decisioning Studio™ Goとランダムコントロールグループで利用可能である。

リンゴ対リンゴ」の実験デザインがなければ、BAUレポートは混乱したり誤解を招いたりする可能性がある。

実験デザインを検証した後、BAUレポートを設定するには以下の詳細が必要である：
- 統合アクティベーションプラットフォーム（Braze、Salesforce Marketing Cloud、Klaviyo）のキャンペーンID（1つまたは複数）。
    - Brazeでは、キャンペーンとキャンバスを受け付けている。
    - Salesforce Marketing Cloudでは、ジャーニーのみを受け付ける
    - Klaviyoの場合、Flowsのみが受け入れられる
- 統合されたアクティベーションプラットフォームから、毎日BAUオーディエンスの受信者をトラッキングするオーディエンスIDを1つ取得する。
    - Brazeでは、セグメンテーションのみ受け付ける。
    - Salesforce Marketing Cloudでは、データ拡張機能のみが使用可能である。
    - Klaviyoでは、セグメンテーションのみ受け付ける。

BAUオーディエンスをトラッキング追跡する既存のオーディエンスがない場合は、作成する必要がある。

{% alert note %}
**Braze顧客のみ：**Braze CurrentsからBrazeAI Decisioning Studio™ Goへのエクスポートに、BAUキャンペーンのデータが含まれていることを確認する。
{% endalert %}

## 考慮事項

より一般的にはBrazeAI Decisioning Studio™ Goと同様に、BAUレポートはクリックKPIのみをカバーし、コンバージョンKPIはカバーしない。

現時点では、特定のキャンバスステップIDへのフィルターはサポートしていない。すべてのキャンバスステップからのイベントは、BAUデータに含まれる。特定のキャンバスステップのみを含めるべき場合、BAUとの比較が無効になる可能性があることに留意されたい。

## BAUキャンペーンの設定 

BrazeAI Decisioning Studio™ Goポータルの指示に従う。1つ以上の[キャンペーンIDとオーディエンスIDが](#what-are-the-requirements-to-use-in-portal-bau-reporting)必要である。