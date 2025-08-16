---
nav_title: 8月
page_order: 4
noindex: true
page_type: update
description: "この記事には2021年8月のリリースノートが含まれています。"
---

# 2021年8月

## Google オーディエンスの同期

Braze [オーディエンス同期をGoogleに]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/)統合により、ブランドはクロスチャネルの顧客ジャーニーの範囲をGoogle検索、Googleショッピング、Gmail、YouTube、およびGoogleディスプレイに拡張できます。ファーストパーティの顧客データを使用して、ダイナミックな行動トリガー、セグメンテーションなどに基づいて安全に広告を配信できます。通常、Braze キャンバスの一部としてメッセージ (プッシュ、メール、SMS など) をトリガーするために使用する基準は、Google のカスタマーマッチを介してそのユーザーに広告をトリガーするために使用できます。

## ベストプラクティスiOS SDK統合ガイド

このオプションの[iOS統合SDKガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk)は、iOS SDKとそのコアコンポーネントをアプリケーションに初めて統合する際のセットアップのベストプラクティスについて、ステップバイステップで案内します。このガイドは、`BrazeManager.swift` ヘルパーファイルを作成する際に役立ちます。このヘルパーファイルは、Braze iOS SDK への依存関係をプロダクションコードの残りの部分から切り離し、アプリケーション全体で 1 つの `import AppboyUI` を生成します。このアプローチでは、過剰な SDK インポートから発生する問題が制限されるため、コードの追跡、デバッグ、および変更が容易になります。 

## 予測購入

予測購入は、マーケティング担当者に購入の可能性に基づいてユーザーを特定し、メッセージングするための強力なツールを提供します。購入予測を作成すると、Brazeは[勾配ブースト決定木](https://en.wikipedia.org/wiki/Gradient_boosting)を使用して機械学習モデルをトレーニングし、過去の購入活動から学習し、将来の購入活動を予測します。[予測購入]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/)ドキュメントをご覧ください。 

## ドラッグアンドドロップエディタ

Braze メールでは、新しい[ドラッグ＆ドロップ編集エクスペリエンス]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/)を使用して、キャンペーンとキャンバスのいずれかで完全なカスタムメールメッセージおよびパーソナライズされたメールメッセージを作成できます。ユーザーはエディターブロックをメールにドラッグできるようになり、より直感的なカスタマイズが可能になりました。 

## ユーザーエイリアスインポート

`external_id`を持たないユーザーを対象にするには、[ユーザー別名を持つユーザーの一覧をインポートすることができます]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias)エイリアスは、代替の一意のユーザー識別子として機能します。これは、アプリにサインアップしていないか、アカウントを作成していない匿名ユーザーを対象とするマーケティングを行う場合に役立ちます。 

## iOS 15 アップグレード ガイド

この[iOS 15 アップグレードガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/)は、iOS 15（WWDC21）で導入された変更点と、Braze iOS SDK統合のために必要なアップグレード手順を概説しています。

## Android 12 アップグレード ガイド

この[Android 12 アップグレードガイド]({{site.baseurl}}/developer_guide/platforms/android/android_13/)は、Android 12（2021年）で導入された関連する変更点と、Braze Android SDK統合のために必要なアップグレード手順について説明しています。

## A2P 10DLC

A2P 10DLCとは、企業が標準的な10桁のロングコード（10DLC）電話番号を使ってアプリケーション・ツー・パーソン（A2P）タイプのメッセージングを送信できる米国のシステムを指す。10桁のロングコードは従来、個人間（P2P）トラフィック用に設計されてきたため、スループットの制限やフィルタリングの強化によってビジネスが制約を受ける原因となっていた。このサービスはこれらの問題を軽減し、全体的なメッセージの配信率を向上させ、ブランドがリンクやアクションを含むメッセージを大量に送信できるようにし、消費者を望まないメッセージからさらに保護するのに役立ちます。 

米国のロングコードを現在所有しているか、米国の顧客に送信するために使用しているすべてのお客様が、10DLC のロングコードを登録する必要があります。10DLCの詳細とその必要性について詳しくは、専用の[10DLC記事]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/)をご覧ください。

## 2要素認証のリセット

2 要素認証を使用してログインに問題が発生しているユーザーは、会社の管理者に連絡して[2 要素認証をリセット]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset)できます。

## 新しいBrazeのパートナーシップ

### Hightouch - ワークフローオートメーション

Brazeと[Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/)の統合により、データウェアハウスからの最新の顧客データを使用して、Brazeでより良いキャンペーンを構築できます。お客様に関連性があり、タイムリーなやり取りを提供したいと考えており、そのためにはBrazeアカウントのデータが正確で新鮮であることが非常に重要です。顧客データをデータウェアハウスから Braze に自動的に同期させることで、データの整合性を心配する必要がなくなり、世界レベルのカスタマーエクスペリエンスの構築に集中して取り組むことができます。

### Transcend - データプライバシーとコンプライアンス

Brazeと[Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/)のパートナーシップは、数十のデータシステムにわたるデータを調整することで、ユーザーがプライバシーリクエストを自動化するのに役立ちます。最終的に、これはチームが GDPR や CCPA などの規制に準拠するのに役立ち、個人が自分のデータに関して主導権を握ることができます。

### Tinyclues - コホートインポート

[Tinyclues]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/)は、カスタマーエクスペリエンスを損なうことなくキャンペーン数と収益を増加させる機能を提供するオーディエンス構築機能であり、オンラインおよびオフラインのCRMキャンペーンのパフォーマンスを追跡するための分析を提供します。一緒に、BrazeとTinycluesの統合はユーザーにより良いCRM計画と戦略へのパスを提供し、ユーザーがよりターゲティングされたキャンペーンを送信し、新しい製品機会を見つけ、非常にユーザーフレンドリーなUIを使用して収益を向上させることを可能にします。

### optilyz - ダイレクトメール

[optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/)は、より顧客中心で持続可能かつ収益性の高いダイレクトメールキャンペーンを実行できるダイレクトメールオートメーションプラットフォームです。optilyzはヨーロッパ中の何百もの企業で使用されており、手紙、はがき、セルフメーラーをクロスチャネルのマーケティングに統合し、キャンペーンを自動化してよりパーソナライズすることができます。optilyzとBrazeのWebhook統合を使用して、顧客にダイレクトメールを送信します。