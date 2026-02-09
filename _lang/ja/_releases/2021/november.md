---
nav_title: 11月
page_order: 1
noindex: true
page_type: update
description: "この記事には、2021年11月のリリースノートが含まれている。"
---
# 2021年11月

## クリック開封率レポートメトリック
Brazeは、[レポートビルダーで]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)利用可能な新しいメール指標「クリック・ツー・オープン率」を追加した。このメトリックは、クリックされた開封メールの割合を表します。

## マシン開封レポートメトリック

キャンバスとキャンペーンアナリティクスのEメールページで、新しいEメール指標「[マシンオープンズ]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens)」が利用できるようになった。この指標は、（Appleのサーバーによって開封されたような）人為的ではないメール開封を特定するもので、開封総数のサブセットとして表示される。

## random_bucket_number 液体変数
メッセージパーソナライゼーションの[サポートされている Liquid 変数]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)のリストに、変数 `random_bucket_number` が追加されました。 

## iOS 15のリッチプッシュ通知ガイドライン
新しい[iOSプッシュ通知ガイドラインが]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)iOSリッチドキュメントに追加され、通知状態に関する情報とテキスト切り捨て変数の内訳が含まれる。

## EUでウェブフックとコネクテッド・コンテンツのホワイトリストに登録するIP
EUでウェブフックとコネクテッド・コンテンツのホワイトリストに追加するIPが、[ウェブフックと]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) [コネクテッド・コンテンツの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)記事に追加された。これらの新しい IP には `18.157.135.97`、`3.123.166.46`、`3.64.27.36`、`3.65.88.25`、`3.68.144.188`、`3.70.107.88` が含まれます。

## 購入エンドポイントをエクスポートする
Brazeに新しい[エンドポイント（`/purchases/product_list` ）が]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)追加された。このエンドポイントは、製品IDのページ分割されたリストを返す。

## 新しいBrazeのパートナーシップ

### アドビ - 顧客データプラットフォーム
Braze と [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) の統合により、ブランドはリアルタイムで Braze に接続し、Adobe データ (カスタム属性とセグメント) を Braze にマッピングできます。そうすれば、ブランドはこの情報に基づいて行動し、パーソナライズされたなターゲットを絞った体験をユーザーに提供することができる。 

### BlueConic - 顧客データプラットフォーム
[Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic) を使用すると、Braze ユーザーはデータを永続的な個別のプロファイルに統合し、顧客タッチポイントやシステムを横断して同期して、カスタマーライフサイクルオーケストレーション、モデリングと分析、デジタル製品とエクスペリエンス、オーディエンスベースの収益化など、成長に重点を置いた幅広いイニシアチブをサポートできます。

### 価値がある - ダイナミックなコンテンツ
Braze と [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) の統合により、Worthy のドラッグ＆ドロップダイナミックコンテンツエディターを使用して、パーソナライズされたリッチなアプリ内エクスペリエンスを簡単に作成し、Braze を通じて提供できるようになります。

### 柔道 - ダイナミックコンテンツ
[Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo)とBrazeインテグレーションを使用すると、Judoのエクスペリエンスでキャンペーンのコンポーネントを上書きして置き換えることができます。Braze のデータは、Judo エクスペリエンスでパーソナライズされたコンテンツをサポートするために使用できます。ユーザーイベントとエクスペリエンスからのデータは、アトリビューションとターゲティングのためにBrazeにフィードバックできる。

### ライン - メッセージング
[LINE]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) と Braze の統合により、[Line メッセージング API](https://developers.line.biz/en/docs/messaging-api/overview/) を介し、Braze の Webhook、高度なセグメンテーション、パーソナライゼーション、およびトリガー機能を利用して、Line のユーザーにメッセージを送信できます。

### RevenueCat - 決済
[RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat)とBrazeインテグレーションを使用すると、顧客の購買およびサブスクリプションライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客への働きかけや、請求で問題のある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクルステージに対応するキャンペーンを作成できます。

### Punchh - ロイヤルティ
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh)はBrazeと提携し、プレゼントやロイヤルティのために2つのプラットフォーム間でデータを同期しました。Brazeで公開されたデータはセグメンテーションに利用でき、Brazeで設定されたWebhookテンプレートを介してPunchhにユーザーデータを同期することができる。  