---
nav_title: 10月
page_order: 2
noindex: true
page_type: update
description: "この記事には、2021年10月のリリースノートが含まれている。"
---
 
# 2021年10月

## データポイント使用量ダッシュボード

**合計データポイント使用量**ダッシュボードを使用して、契約割り当てに関連するデータポイント使用量のペースを追跡する。このダッシュボードでは、契約、現在の請求サイクル、会社の請求データ、ワークスペースの請求データに関する情報を提供する。詳細については、「[請求]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard)」を参照のこと。

## セグメントエクステンション再生への変更

2022年2月1日以降、未使用の[セグメントエクステンションについては]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)、毎日エクステンションを再生成する設定が自動的にオフになる。Braze では、未使用のエクステンションを次の基準を満たすものと定義しています。

- アクティブなキャンペーン、キャンバス、セグメントで使用されていない
- 非アクティブな (下書きの、停止された、アーカイブされた) キャンペーン、キャンバス、またはセグメントで使用されていない
- 7日以上変更されていない

この設定をオフにすると、Braze は会社の連絡先とエクステンションの作成者に通知します。エクステンションを毎日再生成するオプションはいつでも有効にできます。

## Android アドバンスド実装ガイド

### コンテンツカードによって促進された

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)、コンテンツカードのコードに関する考慮事項、私たちのチームによって構築された3つのカスタムユースケース、付随するコードスニペット、インプレッション、クリック、および却下のログに関するガイダンスについて説明する。

### アプリ内メッセージング

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/)、アプリ内メッセージコードの考慮事項、私たちのチームによって構築された3つのカスタムユースケース、および付随するコードスニペットについて説明する。

### プッシュ通知

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/)、カスタム`FirebaseMessagingService` サブクラスを活用してプッシュ・メッセージを最大限に活用する方法について説明する。Braze チームが作成したカスタムのユースケース、付属のコードスニペット、ロギング分析に関するガイダンスも含まれています。

## 新しいBrazeパートナーシップ

### アドビ - 顧客データプラットフォーム

Adobe Experience Platform上に構築されたアドビのリアルタイム顧客データプラットフォーム（リアルタイムCDP）は、企業が複数の企業ソースから既知および匿名のデータを収集し、顧客プロファイルを作成するのを支援する。

Brazeと[Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/)CDPの統合により、ブランドはAdobeデータ（カスタム属性とセグメンテーション）をリアルタイムでBrazeに接続し、マッピングすることができる。そして、ブランドはこのデータに基づいて行動し、パーソナライズされたターゲット体験をユーザーに提供することができる。 

### Shopify - コマース

[Shopifyは]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/)、あらゆる規模の小売(店)ビジネスを開始、成長、マーケター、管理するための信頼できるツールを提供する世界的なコマースのリーディングカンパニーである。BrazeとShopifyの統合により、ブランドはShopifyストアをシームレスにBrazeに接続し、選択したShopifyのWebhookをBrazeに渡すことができる。Brazeのクロスチャネルストラテジーとキャンバスを活用することで、ユーザーを再ターゲティングしてチェックアウト放棄メッセージングを表示し、顧客の購入完了を促したり、過去の購入履歴に基づいてユーザーをリターゲティングすることができます。