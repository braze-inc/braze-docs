---
nav_title: Shopify の概要
article_title:「Shopify の概要」
description:「この参考記事では、BrazeとShopifyとのパートナーシップについて概説しています。ShopifyストアとShopifyは、ShopifyストアをBrazeシームレスにに接続して、一部のShopifywebhook をBrazeに渡すことを可能にするグローバルコマース企業です。Brazeのクロスチャネルの戦略とCanvasを活用して、購入を完了するように顧客に働きかけたり、以前の購入に基づいてユーザーをリターゲティングするしたりします。「
page_type: partner
search_tag:Partner
alias: 「/shopify_overview/"
page_order:0
---

# Shopify の概要

> [Shopifyは](https://www.shopify.com/)、あらゆる規模の小売 (店) ビジネスを開始、成長、マーケティング、管理するための信頼できるツールを提供する大手グローバルコマース企業です。Shopifyは、信頼性を重視して設計されたプラットフォームとサービスにより、すべての人にとってより良い商取引を実現すると同時に、世界中の消費者により良いショッピング体験を提供します。

ShopifyとBrazeの統合により、Shopifyストアを接続して、ShopifyデータをBrazeにシームレスにに渡すことができます。クロスチャネルの戦略と Canvas in Braze を活用して、新しい見込み客を引き付けたり、新規顧客にメッセージを送ったり、チェックアウトを断念したメッセージングでユーザーをリターゲティングするして購入を完了するように誘導したりできます。

## サポートされている機能

- Braze Web SDKを使用してオンサイトの行動と匿名ユーザーを追跡します
- Braze Web SDK を使用して Braze での Shopify のお客様との同期と照合を支援します
- Shopifyの顧客データ同期する
- ShopifyのメールとSMSサブスクライバーオプトインサブスクリプション状態を収集
- 過去のShopify購入データをバックフィルする 
- Shopify カタログ同期 
- アプリ内メッセージをチャネルとして使用 

## サポート対象のユースケース 

- 以下を含む購入経路キャンペーンとCanvasユーザーージャーニー 
  - ブラウズ放棄 
  - 放棄されたカート 
  - チェックアウト放棄 
- 以下を含む購入後のキャンペーンとCanvasユーザーージャーニー
  - 注文確認 
  - フルフィルメントの更新 
  - 注文キャンセル 
  - 注文の返金
- おすすめ商品
- クロスセルとアップセル
- [再入荷 (早期アクセス]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)) 

## 要件

| 必要条件 | 説明 |
| --- | --- |
| Shopify ストア | [アクティブなShopifyストアがあります](https://www.shopify.com/)。<br><br>ワークスペースごとに1つのShopifyストアを接続できます。複数のストアを1つのワークスペースに接続することに関心がある場合は、顧客サクセスマネージャーに連絡して、Shopify Multiple Storesベータ版に参加してください。 |
| Shopifyのユーザー権限 | Shopifyストアに対する以下の権限のいずれかを持っています。{::nomarkdown}<ul><li>ストアオーナー</li><li>スタッフ</li><li>すべての一般設定とオンラインストア設定、および次の追加の管理者権限を持つメンバー:<ul><li>注文</li><li>表示 (「<b>製品</b>」の下にあります)</li><li>顧客</li><li>\[設定を管理]</li><li>スタッフや共同作業者が開発したアプリを見る</li><li>アプリとチャンネルの管理とインストール</li></ul></li></ul>{:/} |
| Braze Web SDK の実装 | オンサイトの行動と匿名ユーザーを追跡するには、デフォルト Shopify統合または手動でBraze Web SDKを実装する必要があります。<br><br>実装オプションの詳細については、「[ShopifyサイトへのWeb SDKの実装]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)」を参照してください。 |
| イベントプロパティのセグメンテーションが有効 | ShopifyのイベントプロパティをSegment 化できることを確認するには、顧客[サクセスマネージャーまたはBraze Supportと協力して、Braze管理ダッシュボード]({{site.baseurl}}/braze_support/)でイベントプロパティのセグメンテーションが有効になっていることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 }

## 一般データ保護規則 (GDPR)

お客様によって、またはお客様に代わってBrazeサービスに送信された個人データについては、Brazeがデータ処理者であり、当社の顧客がデータ管理者です。したがって、Brazeはお客様の指示がある場合にのみそのような個人データを処理し、該当する場合、データ主体の要求についてお客様に通知します。データ管理者として、お客様はデータ主体の要求に直接対応します。[BrazeプラットフォームのShopify統合の一環として、BrazeはShopifyのGDPRwebhook を自動的に受信します。](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app)[ただし、Brazeのお客様は、GDPRコンプライアンスポリシーに従い、[Braze SDKまたはREST]({{site.baseurl}}/developer_guide/home/) [APIを使用してShopifyのお客様からのデータ主体の要求に対応する責任を最終的に負うものとします]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)。]({{site.baseurl}}/help/dp-technical-assistance/)
