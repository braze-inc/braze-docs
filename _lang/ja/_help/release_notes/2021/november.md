---
nav_title: 11月
page_order: 1
noindex: true
page_type: update
description: "この記事には、2021 年 11 月のリリースノートが含まれています。"
---
# 2021 年 11 月

## クリック・トゥ・オープン率レポート指標
[Brazeは、レポートビルダーで利用できる新しいメール指標「クリック開封率」を追加しました。]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)この指標は、開封されたメールのうち、クリックされた割合を表します。

## マシンオープンレポート指標

メールの [キャンバス] ページと [キャンペーン分析] ページに、新しいメール指標「[マシンオープン数]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens)」が追加されました。この指標は、開封総数のサブセットとして表示される、人間以外の開封数（Appleのサーバーで開封されたものなど）を識別します。

## ランダムバケット数液体変数
`random_bucket_number`[メッセージをパーソナライズするためのサポートされている Liquid 変数のリストに]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)、変数が追加されました。 

## iOS 15 リッチプッシュ通知ガイドライン
[通知の状態やテキスト切り捨て変数の内訳に関する情報を含む、新しいiOSプッシュ通知ガイドラインがiOSのリッチドキュメントに追加されました]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)。

## ウェブフックとコネクテッドコンテンツ用にEUでホワイトリストに登録するIP
[ウェブフックとコネクテッドコンテンツについて EU でホワイトリストに登録する追加の IP が、[ウェブフックとコネクテッドコンテンツの記事に追加されました]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)。]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)これらの新しい IP には`18.157.135.97`、、`3.123.166.46`、`3.64.27.36`、`3.65.88.25``3.68.144.188`、が含まれます`3.70.107.88`。

## 購入エンドポイントのエクスポート
Braze [`/purchases/product_list`に新しいエンドポイントが追加されました]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)。このエンドポイントは、ページ分割された製品 ID のリストを返します。

## Braze の新しいパートナーシップ

### Adobe-顧客データプラットフォーム
[BrazeとAdobeの統合により]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe)、ブランドはアドビのデータ（カスタム属性とセグメント）をBrazeにリアルタイムで接続してマッピングできます。その後、ブランドはこのデータに基づいて行動を起こし、パーソナライズされたターゲットを絞ったエクスペリエンスをそれらのユーザーに提供できます。 

### BlueConic-顧客データプラットフォーム
[Blueconicを使用すると]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic)、Brazeユーザーはデータを永続的な個別のプロファイルに統合し、顧客とのタッチポイントやシステム間で同期して、顧客ライフサイクルの調整、モデリングと分析、デジタル製品とエクスペリエンス、オーディエンスベースの収益化など、成長に焦点を当てた幅広い取り組みをサポートできます。

### 価値がある-ダイナミックコンテンツ
[BrazeとWorthyの統合により]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy)、Worthyのドラッグアンドドロップの動的コンテンツエディターを使用して、パーソナライズされたリッチなアプリ内エクスペリエンスを簡単に作成し、Brazeを通じて配信できます。

### 柔道-ダイナミックコンテンツ
[JudoとBrazeの統合により]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo)、キャンペーンのコンポーネントを上書きして、Judoエクスペリエンスに置き換えることができます。Brazeのデータは、柔道体験におけるパーソナライズされたコンテンツをサポートするために使用される場合があります。ユーザーイベントやエクスペリエンスからのデータを Braze にフィードバックして、アトリビューションやターゲティングに役立てることができます。

### 回線-メッセージング
[Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) [と Braze の統合により、Braze ウェブフック、高度なセグメンテーション、パーソナライズ、トリガー機能を活用して、Line Messaging API を通じて Line でユーザーにメッセージを送ることができます。](https://developers.line.biz/en/docs/messaging-api/overview/)

### 収益CAT-支払い
[RevenueCatとBrazeの統合により]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat)、顧客の購入およびサブスクリプションのライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客へのエンゲージメントや、請求の問題がある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクル段階に対応するキャンペーンを構築できます。

### パンチ-ロイヤリティ
[PunchhはBrazeと提携して]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh)、ギフトやロイヤルティの目的で2つのプラットフォーム間でデータを同期しています。Brazeで公開されたデータはセグメンテーションに使用でき、Brazeで設定されたWebhookテンプレートを使用してユーザーデータをPunchhに同期できます。  