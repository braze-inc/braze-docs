---
nav_title: Shopify概要
article_title: "Shopify概要"
description: "このリファレンス記事では、BrazeとShopifyの提携について説明しています。Shopifyはグローバルなコマース企業であり、ShopifyストアをBrazeとシームレスに接続して、選択したShopifyのwebhookをBrazeに渡すことができます。Brazeクロスチャネルの戦略とキャンバスを活用して、顧客が購入を完了するよう促したり、以前の購入に基づいてユーザーをリターゲティングする。"
page_type: partner
search_tag: Partner
alias: "/shopify_overview/"
page_order: 0
---

# Shopify概要

> [Shopify](https://www.shopify.com/) は、あらゆる規模の小売 (店) ビジネスを開始、成長、マーケティング、および管理するための信頼できるツールを提供する、世界をリードするコマース企業です。Shopifyは、信頼性の高いプラットフォームとサービスを提供し、世界中の消費者により良いショッピング体験を提供することで、すべての人にとって商取引をより良くします。

ShopifyとBrazeの統合により、Shopifyストアを接続してShopifyデータをシームレスにBrazeに渡すことができます。Brazeでクロスチャネルの戦略とキャンバスを活用して、新しいリードを引き付けたり、新しい顧客にメッセージを送ったり、放棄されたチェックアウトメッセージングでユーザーをリターゲティングして購入を完了するよう促すことができます。

## サポートされている機能

- Braze Web SDKを介してオンサイトの行動と匿名ユーザーを追跡する
- Braze Web SDKを介してShopifyの顧客をBrazeに同期および照合するのを支援する
- Shopifyの顧客データを同期する
- ShopifyのメールおよびSMSサブスクライバーのオプトインサブスクリプション状態を収集する
- 過去のShopify購入データをバックフィルする 
- Shopifyカタログ同期 
- チャネルとしてアプリ内メッセージを使用する 

## サポートされているユースケース 

- パス-to-purchase campaigns and キャンバス ユーザー journeys, including: 
  - ブラウズ放棄 
  - 放棄カート 
  - 放棄されたチェックアウト 
- 購入後のキャンペーンとキャンバスユーザーの旅程を含む:
  - 注文確認 
  - 実現の更新 
  - 注文のキャンセル 
  - 注文の払い戻し
- 製品の推奨
- クロスセルとアップセル
- [再入荷]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## 要件

| 要件 | 説明 |
| --- | --- |
| Shopifyストア | アクティブな[Shopify](https://www.shopify.com/)ストアがあります。<br><br>ワークスペースごとに1つのShopifyストアを接続できます。複数のストアを1つのワークスペースに接続することに興味がある場合は、Shopifyの複数ストアベータ版に参加するために顧客成功マネージャーに連絡してください。 |
| Shopify ユーザー permissions | あなたは、Shopifyストアに対して次のいずれかの権限を持っています:{::nomarkdown}<ul><li>店主</li><li>スタッフ</li><li>すべての一般およびオンラインストアの設定に加え、次の追加の管理者権限を持つメンバー:<ul><li>注文</li><li><b>製品</b>の下にあるビュー</li><li>顧客</li><li>設定を管理する</li><li>スタッフや協力者が開発したアプリを表示</li><li>アプリとチャンネルの管理とインストール</li></ul></li></ul>{:/} |
| Braze Web SDK 実装 | オンサイトの行動と匿名ユーザーを追跡するには、デフォルトのShopify統合または手動でBraze Web SDKを実装する必要があります。<br><br>詳細な実装オプションについては、[ShopifyサイトでのWeb SDKの実装]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)を参照してください。 |
| イベントプロパティセグメンテーションが有効になりました | Shopifyイベントプロパティをセグメント化できることを確認するには、顧客成功マネージャーまたは[Brazeサポート]({{site.baseurl}}/braze_support/)と連携して、Brazeダッシュボードでイベントプロパティのセグメンテーションがオンになっていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 }

## 一般データ保護規則（GDPR）

Brazeのサービスに顧客またはその代理として提供された個人データに関して、Brazeはデータ処理者であり、当社の顧客はデータ管理者です。したがって、Brazeはそのような個人データを当社の顧客の指示に従ってのみ処理し、該当する場合には、データ主体からの要求を顧客に通知します。データ管理者として、私たちの顧客はデータ主体の要求に直接対応します。BrazeプラットフォームのShopify統合の一環として、Brazeは自動的に[ShopifyのGDPR webhook](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app)を受信します。ただし、Brazeの顧客は、[Braze SDKs]({{site.baseurl}}/developer_guide/home/)または[REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)を使用して、Shopifyの顧客からのデータ主体要求に応答する責任を最終的に負います。これは、当社の[GDPRコンプライアンス]({{site.baseurl}}/help/dp-technical-assistance/)ポリシーに従ったものです。
