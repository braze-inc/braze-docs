---
nav_title: 10月
page_order: 2
noindex: true
page_type: update
description: "この記事には、2021年10月のリリースノートが含まれている。"
---
 
# 2021年10月

## データポイント利用ダッシュボード

**合計データポイント使用量**ダッシュボードを使用して、契約割り当てに関連するデータポイントの使用ペースを追跡する。このダッシュボードには、契約内容、現在の請求サイクル、会社の請求データ、ワークスペースの請求データに関する情報が表示される。詳細については、「[請求]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard)」を参照してください。

## セグメントエクステンションの再生成の変更

2022年2月1日以降、未使用の[セグメント・エクステンションについては]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)、毎日エクステンションを再生成する設定が自動的にオフになる。Braze では、未使用のエクステンションを次の基準を満たすものと定義しています。

- アクティブなキャンペーン、キャンバス、セグメントで使用されていない
- 非アクティブな (下書きの、停止された、アーカイブされた) キャンペーン、キャンバス、またはセグメントで使用されていない
- 7日以上変更されていない

この設定をオフにすると、Braze は会社の連絡先とエクステンションの作成者に通知します。エクステンションを毎日再生成するオプションはいつでも有効にできます。

## Androidアドバンスド実装ガイド

### コンテンツカードによって促進された

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)、Content Cardコードの検討事項、当社チームが構築した3つのカスタムユースケース、付随するコードスニペット、インプレッション、クリック、および却下のログに関するガイダンスについて説明する。

### アプリ内メッセージング

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/)、アプリ内メッセージコードの考慮事項、我々のチームによって構築された3つのカスタムユースケース、付随するコードスニペットについて説明する。

### プッシュ通知

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/)、カスタム`FirebaseMessagingService` サブクラスを活用してプッシュ・メッセージを最大限に活用する方法について説明する。Braze チームが作成したカスタムのユースケース、付属のコードスニペット、ロギング分析に関するガイダンスも含まれています。

## Braze の新しいパートナーシップ

### アドビ - 顧客データプラットフォーム

Adobe Experience Platform 上に構築された Adob​​e のリアルタイム顧客データプラットフォーム (リアルタイム CDP) は、企業が複数のエンタープライズソースからの既知のデータと匿名データを統合し、すべてのチャネルとデバイスでパーソナライズされた顧客体験をリアルタイムで提供するために使用できる顧客プロファイルを作成するのに役立ちます。

Brazeと[Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/)CDPの統合により、ブランドはAdobeデータ（カスタム属性とセグメント）をリアルタイムでBrazeに接続し、マッピングすることができる。ブランドはこのデータに基づいて行動し、パーソナライズされ、ターゲットに応じた体験をユーザーに提供できます。 

### Shopify - Eコマース

[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/)は、あらゆる規模の小売 (店)事業を始め、成長し、販売し、管理するための信頼できる道具を提供する世界的な大手商業企業です。Braze と Shopify の統合により、ブランドは Shopify ストアを Braze とシームレスに接続し、選択した Shopify Webhook を Braze に渡すことができます。Braze のクロスチャネル戦略とキャンバスを活用して、購入手続き放棄のメッセージングでユーザーをリターゲティングし、顧客に購入を完了するよう促したり、以前の購入に基づいてユーザーをリターゲティングしたりできます。