---
nav_title: 10月
page_order: 2
noindex: true
page_type: update
description: "この記事には2021年10月のリリースノートが含まれている。"
---
 
# 2021年10月

## データポイント利用ダッシュボード

**合計データポイント使用量**ダッシュボードを使用して、契約割り当てに関連するデータポイント使用ペースを追跡します。このダッシュボードでは、お客様の契約、現在の請求サイクル、会社の請求データ、ワークスペースの請求データに関する情報を提供します。詳細については、「[請求]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard)」を参照してください。

## セグメント延長再生への変更

2022年2月1日より、未使用の[セグメント・エクステンションについては]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)、毎日エクステンションを再生成する設定が自動的にオフになります。Brazeでは、以下の条件を満たすものを未使用の拡張子と定義しています：

- アクティブなキャンペーン、キャンバス、セグメントで使用されていない
- 非アクティブな (下書きの、停止された、アーカイブされた) キャンペーン、キャンバス、またはセグメントで使用されていない
- 7日以上変更されていない

この設定をオフにすると、Braze は会社の連絡先とエクステンションの作成者に通知します。エクステンションを毎日再生するオプションは、いつでも再度オンにすることができます。

## Androidアドバンスド実装ガイド

### コンテンツカード

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)、Content Cardのコードに関する考慮事項、私たちのチームによって構築された3つのカスタムユースケース、付随するコードスニペット、インプレッション、クリック、および却下のログに関するガイダンスについて説明します。

### アプリ内メッセージング

このオプショナルで高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/)、アプリ内メッセージコードの考慮事項、当社チームが構築した3つのカスタム使用例、および付随するコードスニペットについて説明します。

### プッシュ通知

このオプションの高度な[実装ガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/)、カスタム`FirebaseMessagingService` サブクラスを活用してプッシュメッセージを最大限に活用する方法を説明します。私たちのチームによって構築されたカスタムユースケース、付随するコードスニペット、分析のロギングに関するガイダンスが含まれています。

## 新しいブレイズ・パートナーシップ

### アドビ - 顧客データプラットフォーム

Adobe Experience Platform上に構築されたアドビのリアルタイム顧客データプラットフォーム（リアルタイムCDP）は、企業が複数の企業ソースから既知および匿名のデータを収集し、顧客プロファイルを作成するのに役立ちます。

Brazeと[Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/)CDPの統合により、ブランドはAdobeデータ（カスタム属性とセグメント）をリアルタイムでBrazeに接続し、マッピングすることができます。ブランドはこのデータに基づいて行動し、パーソナライズされたターゲット体験をユーザーに提供することができる。 

### Shopify - Eコマース

[Shopifyは]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/)、あらゆる規模の小売ビジネスを開始し、成長させ、マーケティングし、管理するための信頼できるツールを提供する世界的なコマースのリーディングカンパニーです。BrazeとShopifyの統合により、ブランドはShopifyストアをBrazeとシームレスに接続し、選択したShopifyのウェブフックをBrazeに渡すことができます。Brazeのクロスチャネル戦略とCanvasを活用して、放棄されたチェックアウトメッセージでユーザーを再ターゲティングし、購入を完了するよう誘導したり、過去の購入履歴に基づいてユーザーを再ターゲティングしたりすることができます。