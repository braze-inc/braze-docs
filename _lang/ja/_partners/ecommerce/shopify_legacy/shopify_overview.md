---
nav_title: Shopifyの概要（レガシー）
article_title: "Shopifyの概要（レガシー）"
description: "このリファレンス記事では、Braze と Shopify のパートナーシップについて説明します。Shopify はグローバルなコマース企業であり、Shopify ストアを Brazeとシームレスに接続して、選択した Shopify Webhook を Braze に渡すことができます。Braze クロスチャネル戦略とキャンバスを活用して、顧客が購入を完了するように促し、購入履歴に基づいてユーザーをリターゲティングできます。"
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# Shopify の概要（レガシー）

> [Shopify](https://www.shopify.com/) は、あらゆる規模の小売 (店) ビジネスの開始、拡大、マーケティング、および管理のための信頼できるツールを提供する、世界をリードするコマース企業です。Shopifyは、信頼性の高いプラットフォームとサービスを提供し、世界中の消費者により良いショッピング体験を提供することで、すべての人にとって商取引をより良くします。

ShopifyとBrazeの統合により、Shopifyストアを接続してShopifyデータをシームレスにBrazeに渡すことができます。Brazeでクロスチャネルの戦略とキャンバスを活用して、新しいリードの獲得、新しい顧客へのメッセージの送信、ユーザーに購入の完了を促す購入手続き放棄対応メッセージによるユーザーのリターゲティングを行うことができます。

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## サポートされている機能

- Braze Web SDKを介してオンサイトの行動と匿名ユーザーを追跡する
- Braze Web SDK を使用して Braze で Shopify 顧客の同期と照合を支援する
- Shopifyの顧客データを同期する
- ShopifyのメールおよびSMSサブスクライバーのオプトインサブスクリプション状態を収集する
- 過去のShopify購入データをバックフィルする 
- Shopifyカタログ同期 
- チャネルとしてアプリ内メッセージを使用する 

## サポートされているユースケース 

- 次を含む購入経路キャンペーンとキャンバスユーザージャーニー: 
  - ブラウズ放棄 
  - カート放棄 
  - 購入手続き放棄 
- 次を含む購入後のキャンペーンとキャンバスユーザージャーニー:
  - 注文確認 
  - フルフィルメントの更新 
  - 注文のキャンセル 
  - 注文の払い戻し
- 製品の推奨
- クロスセルとアップセル
- [再入荷]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## 要件

| 要件 | 説明 |
| --- | --- |
| Shopify ストア | アクティブな[Shopify](https://www.shopify.com/)ストアがあります。<br><br>ワークスペースごとに1つのShopifyストアを接続できます。複数のストアを1つのワークスペースに接続することに興味がある場合は、Shopify Multiple Stores ベータ版への参加についてカスタマーサクセスマネージャーにご連絡ください。 |
| Shopify のユーザー権限 | Shopify ストアに対して次のいずれかの権限を持ちます。{::nomarkdown}<ul><li>店主</li><li>スタッフ</li><li>すべての一般設定およびオンラインストア設定と、次の管理者権限を持つメンバー:<ul><li>Orders</li><li><b>製品</b>の下にあるビュー</li><li>顧客</li><li>設定を管理する</li><li>スタッフや協力者が開発したアプリを表示</li><li>アプリとチャンネルの管理とインストール</li></ul></li></ul>{:/} |
| Braze Web SDK 実装 | オンサイトの行動と匿名ユーザーを追跡するには、デフォルトのShopify統合または手動でBraze Web SDKを実装する必要があります。<br><br>詳細な実装オプションについては、[ShopifyサイトでのWeb SDKの実装]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify)を参照してください。 |
| イベントプロパティセグメンテーションが有効になりました | Shopifyイベントプロパティをセグメント化できることを確認するには、顧客成功マネージャーまたは[Brazeサポート]({{site.baseurl}}/braze_support/)と連携して、Brazeダッシュボードでイベントプロパティのセグメンテーションがオンになっていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 }

## 一般データ保護規則 (GDPR)

Braze のサービスにお客様またはお客様の代理により提供される個人データに関して、Braze はデータ処理者であり、Braze のお客様はデータ管理者です。したがって、Braze はそのような個人データを当社のお客様の指示のみに従って処理し、該当する場合には、データ主体の要求をお客様に通知します。当社のお客様はデータ管理者としてデータ主体の要求に直接対応します。BrazeプラットフォームのShopify統合の一環として、Brazeは自動的に[ShopifyのGDPR webhook](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app)を受信します。ただし、Brazeの顧客は、[Braze SDKs]({{site.baseurl}}/developer_guide/home/)または[REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)を使用して、Shopifyの顧客からのデータ主体要求に応答する責任を最終的に負います。これは、当社の[GDPRコンプライアンス]({{site.baseurl}}/dp-technical-assistance/)ポリシーに従ったものです。
