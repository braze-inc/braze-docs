---
nav_title: 8月
page_order: 4
noindex: true
page_type: update
description: "この記事には2021年8月のリリースノートが含まれています。"
---

# 2021年8月

## Google オーディエンス Sync

Braze [オーディエンス同期をGoogleに]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)統合により、ブランドはクロスチャネルの顧客ジャーニーの範囲をGoogle検索、Googleショッピング、Gmail、YouTube、およびGoogleディスプレイに拡張できます。ファーストパーティの顧客データを使用して、ダイナミックな行動トリガー、セグメンテーションなどに基づいて安全に広告を配信できます。Braze キャンバスの一部としてメッセージをトリガーするために通常使用する任意の基準（例えば、プッシュ、メール、SMSなど）を使用して、Googleの顧客マッチを介してそのユーザーに広告をトリガーすることができます。

## ベストプラクティスiOS SDK統合ガイド

このオプションの[iOS統合SDKガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewios_sdk_integration/)は、iOS SDKとそのコアコンポーネントをアプリケーションに初めて統合する際のセットアップのベストプラクティスについて、ステップバイステップで案内します。このガイドは、`BrazeManager.swift` ヘルパーファイルを作成する際に役立ちます。このヘルパーファイルは、Braze iOS SDK への依存関係をプロダクションコードの残りの部分から切り離し、アプリケーション全体で 1 つの `import AppboyUI` を生成します。このアプローチでは、過剰な SDK インポートから発生する問題が制限されるため、コードの追跡、デバッグ、および変更が容易になります。 

## 予測購入

予測購入は、マーケティング担当者に購入の可能性に基づいてユーザーを特定し、メッセージングするための強力なツールを提供します。購入予測を作成すると、Brazeは[勾配ブースト決定木](https://en.wikipedia.org/wiki/Gradient_boosting)を使用して機械学習モデルをトレーニングし、過去の購入活動から学習し、将来の購入活動を予測します。[予測購入]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/)ドキュメントをご覧ください。 

## ドラッグアンドドロップエディタ

Brazeメールを使用すると、新しい[ドラッグアンドドロップ編集体験]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/)を使用して、キャンペーンやキャンバスのいずれかで完全にカスタムおよびパーソナライズされたメールメッセージを作成できます。ユーザーはエディターブロックをメールにドラッグできるようになり、より直感的なカスタマイズが可能になりました。 

## ユーザーエイリアスインポート

`external_id`を持っていないユーザーをターゲットにするには、[ユーザーのエイリアスを持つユーザーのリストをインポートする]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias)ことができます。エイリアスは、代替の一意のユーザー識別子として機能します。匿名ユーザーにマーケティングしようとしている場合、アカウントを作成していないユーザーに役立ちます。 

## iOS 15 アップグレード ガイド

この[iOS 15 アップグレードガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/)は、iOS 15（WWDC21）で導入された変更点と、Braze iOS SDK統合のために必要なアップグレード手順を概説しています。

## Android 12 アップグレード ガイド

この[Android 12 アップグレードガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/)は、Android 12（2021年）で導入された関連する変更点と、Braze Android SDK統合のために必要なアップグレード手順について説明しています。

## A2P 10DLC

A2P 10DLCは、企業が標準的な10桁の長いコード（10DLC）電話番号を介してアプリケーションから人（A2P）タイプのメッセージングを送信できる米国のシステムを指します。10 桁の長いコードは、従来、個人間（P2P）トラフィック用に設計されていたため、企業はスループットの制限とフィルタリングの強化に悩まされていました。このサービスはこれらの問題を軽減し、全体的なメッセージの配信率を向上させ、ブランドがリンクやアクションを含むメッセージを大量に送信できるようにし、消費者を望まないメッセージからさらに保護するのに役立ちます。 

現在、米国のロングコードを持っているお客様、または米国のお客様に送信するために米国のロングコードを使用しているお客様は、10DLCのためにロングコードを登録する必要があります。10DLCの詳細とその必要性について詳しくは、専用の[10DLC記事]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/)をご覧ください。

## 2 要素認証リセット

2 要素認証を使用してログインに問題が発生しているユーザーは、会社の管理者に連絡して[2 要素認証をリセット]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset)できます。

## 新しいBrazeのパートナーシップ

### Hightouch - ワークフローオートメーション

Brazeと[Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/)の統合により、データウェアハウスからの最新の顧客データを使用して、Brazeでより良いキャンペーンを構築できます。お客様に関連性があり、タイムリーなやり取りを提供したいと考えており、そのためにはBrazeアカウントのデータが正確で新鮮であることが非常に重要です。データウェアハウスからBrazeに顧客データを自動的に同期することで、データの一貫性を心配する必要がなくなり、世界クラスの顧客体験の構築に集中できます。

### Transcend - データプライバシーとコンプライアンス

Brazeと[Transcend]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/)のパートナーシップは、数十のデータシステムにわたるデータを調整することで、ユーザーがプライバシーリクエストを自動化するのに役立ちます。最終的に、これはチームがGDPRやCCPAのような規制に準拠するのを助け、個人が自分のデータに関して主導権を握ることができます。

### Tinyclues - コホート Import

[Tinyclues]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/)は、カスタマーエクスペリエンスを損なうことなくキャンペーン数と収益を増加させる機能を提供するオーディエンス構築機能であり、オンラインおよびオフラインのCRMキャンペーンのパフォーマンスを追跡するための分析を提供します。一緒に、BrazeとTinycluesの統合はユーザーにより良いCRM計画と戦略へのパスを提供し、ユーザーがよりターゲティングされたキャンペーンを送信し、新しい製品機会を見つけ、非常にユーザーフレンドリーなUIを使用して収益を向上させることを可能にします。

### optilyz - ダイレクトメール

[optilyz]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/)は、より顧客中心で持続可能かつ収益性の高いダイレクトメールキャンペーンを実行できるダイレクトメールオートメーションプラットフォームです。optilyzはヨーロッパ中の何百もの企業で使用されており、手紙、はがき、セルフメーラーをクロスチャネルのマーケティングに統合し、キャンペーンを自動化してよりパーソナライズすることができます。optilyzとBrazeのWebhook統合を使用して、顧客にダイレクトメールを送信します。