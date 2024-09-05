---
nav_title: 11月
page_order: 1
noindex: true
page_type: update
description: "この記事には、2021年11月のリリースノートが含まれている。"
---
# 2021年11月

## クリック・ツー・オープン率報告指標
Brazeは、[レポートビルダーで]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)利用可能な新しいメール指標「クリック・ツー・オープン率」を追加した。この指標は、開封されたメールのうち、クリックされたメールの割合を表している。

## マシン・オープン レポート指標

キャンバスとキャンペーンアナリティクスのEメールページで、新しいEメール指標「[マシンオープンズ]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens)」が利用できるようになった。この指標は、（Appleのサーバーによって開封されたような）人為的ではないメール開封を特定するもので、開封総数のサブセットとして表示される。

## random_bucket_number Liquid variable
メッセージのパーソナライズ用に[サポートされているリキッド変数の]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)リストに、変数`random_bucket_number` が追加された。 

## iOS 15のリッチプッシュ通知ガイドライン
新しい[iOSプッシュ通知ガイドラインが]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)iOSリッチドキュメントに追加され、通知状態に関する情報とテキスト切り捨て変数の内訳が含まれる。

## EUでウェブフックとコネクテッド・コンテンツのホワイトリストに登録するIP
EUでウェブフックとコネクテッド・コンテンツのホワイトリストに追加するIPが、[ウェブフックと]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) [コネクテッド・コンテンツの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)記事に追加された。これらの新規IPには、`18.157.135.97` 、`3.123.166.46` 、`3.64.27.36` 、`3.65.88.25` 、`3.68.144.188` 、`3.70.107.88` が含まれる。

## 輸出購入エンドポイント
Brazeに新しい[エンドポイント（`/purchases/product_list` ）が]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)追加された。このエンドポイントは、製品IDのページ分割されたリストを返す。

## 新しいブレイズ・パートナーシップ

### アドビ - 顧客データプラットフォーム
Brazeと[Adobeの]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe)統合により、ブランドはAdobeデータ（カスタム属性とセグメント）をリアルタイムでBrazeに接続し、マッピングすることができる。そして、ブランドはこのデータに基づいて行動し、ユーザーにパーソナライズされたターゲット体験を提供することができる。 

### BlueConic - 顧客データプラットフォーム
[Blueconicにより]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic)、Brazeのユーザーは、データを永続的な個別プロファイルに統合し、顧客ライフサイクルのオーケストレーション、モデリングと分析、デジタル製品と体験、オーディエンスベースの収益化など、成長に焦点を当てた幅広いイニシアチブをサポートするために、顧客接点とシステム間で同期させることができる。

### 価値がある - ダイナミックなコンテンツ
Brazeと[Worthyの]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy)統合により、Worthyのドラッグアンドドロップ・ダイナミック・コンテンツ・エディタを使って、パーソナライズされたリッチなアプリ内体験を簡単に作成し、Brazeを通じて配信することができる。

### 柔道 - ダイナミックコンテンツ
[Judoと]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo)Brazeの統合により、キャンペーンのコンポーネントを上書きし、Judoのエクスペリエンスに置き換えることができる。Brazeのデータは、柔道体験においてパーソナライズされたコンテンツをサポートするために使用されることがある。ユーザーイベントとエクスペリエンスからのデータは、アトリビューションとターゲティングのためにBrazeにフィードバックできる。

### ライン - メッセージング
[LINEと]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line)Brazeの統合により、Brazeのウェブフック、高度なセグメンテーション、パーソナライゼーション、トリガー機能を活用し、[LINE Messaging APIを通じて](https://developers.line.biz/en/docs/messaging-api/overview/)LINEのユーザーにメッセージを送ることができる。

### RevenueCat - ペイメント
[RevenueCatと]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat)Brazeの統合により、顧客の購入と購読のライフサイクルイベントをプラットフォーム間で自動的に同期することができる。これにより、無料トライアル中にオプトアウトした顧客にエンゲージしたり、課金に問題がある顧客にリマインダーを送信するなど、顧客の購読ライフサイクルのステージに反応するキャンペーンを構築することができる。

### パンチ - 忠誠心
[Punchhは]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh)Brazeと提携し、2つのプラットフォーム間でデータを同期させ、ギフトとロイヤリティを目的としている。Brazeで公開されたデータはセグメンテーションに利用でき、Brazeで設定されたWebhookテンプレートを介してPunchhにユーザーデータを同期することができる。  