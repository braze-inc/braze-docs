---
nav_title: 11月
page_order: 1
noindex: true
page_type: update
description: "この記事には2021年11月のリリースノートが含まれています。"
---
# 2021年11月

## クリック率報告指標
Brazeは新しいメール指標であるクリック率を[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)で利用できるようにしました。この指標は、クリックされた開封メールの割合を表しています。

## マシン開封報告メトリック

新しいメールの指標である[機械開封]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens)が、キャンバスおよびキャンペーンの分析ページで利用可能です。この指標は、非人間によるメールの開封（Appleのサーバーによって開封されたものなど）を特定し、総開封数のサブセットとして表示します。

## random_bucket_number Liquid variable
変数 `random_bucket_number` がメッセージのパーソナライゼーションのための[サポートされている Liquid 変数]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)のリストに追加されました。 

## iOS 15 リッチプッシュ通知ガイドライン
新しい[iOSプッシュ通知ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)がiOSリッチドキュメントに追加され、通知状態に関する情報やテキスト切り捨て変数の内訳が含まれています。

## webhookおよびコネクテッドコンテンツのためにEUでホワイトリストに登録するIP
webhooksおよびコネクテッドコンテンツのためにEUでホワイトリストに追加する追加のIPが、私たちの[Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)および[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)の記事に追加されました。これらの新しいIPには`18.157.135.97`、`3.123.166.46`、`3.64.27.36`、`3.65.88.25`、`3.68.144.188`、および`3.70.107.88`が含まれます。

## 購入エクスポートエンドポイント
新しい[`/purchases/product_list`エンドポイント]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)がBrazeに追加されました。このエンドポイントは、製品IDのページネーションされたリストを返します。

## 新しいBrazeのパートナーシップ

### アドビ - 顧客データプラットフォーム
Brazeと[Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe)の統合により、ブランドはAdobeのデータ（カスタム属性とセグメント）をリアルタイムでBrazeに接続およびマッピングできます。ブランドはこのデータを活用し、パーソナライズされたターゲット体験をユーザーに提供できます。 

### BlueConic - 顧客データプラットフォーム
[Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic)を使用すると、Brazeユーザーはデータを永続的な個別プロファイルに統合し、顧客の接点やシステム全体で同期させることができます。これにより、カスタマーライフサイクルのオーケストレーション、モデリングと分析、デジタル製品と体験、オーディエンスベースの収益化など、成長に焦点を当てた幅広い取り組みをサポートします。

### 価値のある - ダイナミックなコンテンツ
Brazeと[Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy)の統合により、Worthyのドラッグアンドドロップダイナミックコンテンツエディタを使用して、パーソナライズされたリッチなアプリ内体験を簡単に作成し、それらをBrazeを通じて配信できます。

### Judo - ダイナミックな content
[Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo)とBrazeの統合により、キャンペーンのコンポーネントを上書きしてJudoのエクスペリエンスに置き換えることができます。Brazeのデータは、Judoの体験においてパーソナライズされたコンテンツをサポートするために使用される場合があります。ユーザーイベントと体験からのデータは、アトリビューションとターゲティングのためにフィードバックとしてBrazeに戻すことができます。

### ライン - メッセージング
LineとBrazeの統合により、Brazeのwebhook、高度なセグメンテーション、パーソナライゼーション、およびトリガー機能を活用して、Lineの[Line Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/)を通じてユーザーにメッセージを送信できます。

### RevenueCat - 支払い
[RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat)とBrazeの統合により、プラットフォーム間で顧客の購入およびサブスクリプションライフサイクルイベントを自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客とエンゲージメントを取ったり、請求に問題がある顧客にリマインダーを送信したりするなど、顧客のサブスクリプションライフサイクルステージに反応するキャンペーンを構築できます。

### Punchh - ロイヤルティ
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh)はBrazeと提携して、ギフティングとロイヤルティの目的で2つのプラットフォーム間のデータを同期させました。Brazeに公開されたデータはセグメンテーションに利用でき、Brazeで設定されたWebhookテンプレートを介してユーザーデータをPunchhに同期できます。  