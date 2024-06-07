---
nav_title: 8月
page_order: 4
noindex: true
page_type: update
description: "この記事には2021年8月のリリースノートが含まれている。"
---

# 2021年8月

## Google Audience Sync

Braze[Audience Sync to Googleの]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)統合により、ブランドはGoogle検索、Googleショッピング、Gmail、YouTube、Googleディスプレイにクロスチャネルのカスタマージャーニーのリーチを拡大することができます。ファーストパーティの顧客データを使用することで、動的な行動トリガーやセグメンテーションなどに基づいた広告を安全に配信することができます。Brazeキャンバスの一部としてメッセージ（例えば、プッシュ、Eメール、SMSなど）をトリガーするために通常使用する基準はすべて、GoogleのCustomer Matchを介してそのユーザーに広告をトリガーするために使用することができます。

## ベストプラクティスiOS SDKインテグレーションガイド

このオプションの[iOS統合SDKガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewios_sdk_integration/)、iOS SDKとそのコアコンポーネントをアプリケーションに初めて統合する際のセットアップのベストプラクティスについて、ステップバイステップで説明します。`BrazeManager.swift` このガイドでは、Braze iOS SDKへの依存を本番コードの他の部分から切り離し、アプリケーション全体で`import AppboyUI` 。このアプローチは、過剰なSDKインポートから発生する問題を制限し、コードの追跡、デバッグ、変更を容易にする。 

## 予測購買

Predictive Purchasesは、マーケティング担当者が購入する可能性に基づいてユーザーを特定し、メッセージを送るための強力なツールを提供します。購買予測を作成すると、Brazeは[勾配ブースティング決定木を](https://en.wikipedia.org/wiki/Gradient_boosting)使用して機械学習モデルを訓練し、過去の購買活動から学習して将来の購買活動を予測します。詳しくは[予測購買を]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/)ご覧ください。 

## ドラッグ＆ドロップ・エディター

Braze Emailでは、新しい[ドラッグ＆ドロップ編集機能]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/)を使って、キャンペーンまたはキャンバスに、完全にカスタム化されたパーソナライズされたメールメッセージを作成することができます。エディタブロックをメールにドラッグできるようになり、より直感的なカスタマイズが可能になりました。 

## ユーザーエイリアスのインポート

`external_id` を持っていないユーザーをターゲットにするには、[ユーザーエイリアスを持つ ユーザーのリストをインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias)することができます。エイリアスは、代替の一意なユーザー識別子の役割を果たす。あなたのアプリにサインアップしていない、あるいはアカウントを作っていない匿名のユーザーに対してマーケティングを行おうとしている場合に役立つ。 

## iOS 15アップグレードガイド

この[iOS 15アップグレードガイドは]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/)、iOS 15 (WWDC21)で導入された変更点の概要と、Braze iOS SDKインテグレーションに必要なアップグレード手順を説明しています。

## アンドロイド12アップグレードガイド

この[Android 12アップグレードガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/)、Android 12 (2021)で導入された関連する変更点と、Braze Android SDKインテグレーションに必要なアップグレード手順について説明します。

## A2P 10DLC

A2P 10DLCとは、企業が標準的な10桁のロングコード（10DLC）電話番号を使ってアプリケーション・ツー・パーソン（A2P）タイプのメッセージングを送信できる米国のシステムを指す。10桁のロングコードは従来、個人間（P2P）トラフィック用に設計されてきたため、スループットの制限やフィルタリングの強化によってビジネスが制約を受ける原因となっていた。このサービスはこれらの問題を軽減し、全体的なメッセージの配信性を向上させ、ブランドはリンクや行動喚起を含む大規模なメッセージの送信を可能にし、さらに消費者を迷惑メッセージから保護するのに役立つ。 

現在、米国のロングコードをお持ちのお客様、または米国のお客様に送信するために米国のロングコードを使用しているお客様は、10DLCにロングコードを登録する必要があります。10DLCの詳細と、なぜ10DLCが必要なのかについては、[10DLCの]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/)専門[記事を]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/)ご覧ください。

## 二要素認証のリセット

二要素認証によるログインに問題があるユーザーは、会社の管理者に連絡して[二要素認証をリセット]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset)することができる。

## 新しいブレイズ・パートナーシップ

### ハイタッチ - ワークフローの自動化

Brazeと[Hightouchの]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/)統合により、貴社のデータウェアハウスから最新の顧客データを使用して、Braze上でより良いキャンペーンを構築することができます。お客様に適切でタイムリーなインタラクションを提供するためには、Brazeアカウントのデータが正確で新鮮であることが重要です。データウェアハウスからBrazeに顧客データを自動的に同期させることで、データの整合性を心配する必要がなくなり、ワールドクラスの顧客体験の構築に集中することができます。

### トランセンド - データプライバシーとコンプライアンス

Brazeと[Transcendの]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/)パートナーシップは、数十のデータシステムにわたるデータをオーケストレーションすることで、ユーザーがプライバシー要求を自動化できるよう支援します。最終的には、GDPRやCCPAのような規制への準拠を支援し、データに関しては個人を運転席に座らせる。

### ティニクル - コーホート・インポート

[Tinycluesは]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/)、顧客体験を損なうことなくキャンペーン数と収益を増加させる機能と、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンスを追跡する分析機能を提供するオーディエンス構築機能です。BrazeとTinycluesの統合は、より良いCRMプランニングと戦略への道筋をユーザーに提供し、ユーザーはよりターゲットを絞ったキャンペーンを送信し、新しい製品機会を見つけ、驚くほどユーザーフレンドリーなUIを使用して収益を向上させることができます。

### optilyz - ダイレクトメール

[optilyzは]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/)、より顧客中心の、持続可能で収益性の高いダイレクトメールキャンペーンの実施を可能にするダイレクトメール自動化プラットフォームです。optilyzはヨーロッパ中の何百もの企業で使用されており、手紙、はがき、セルフメーラーをクロスチャネルマーケティングに統合し、キャンペーンを自動化し、よりパーソナライズすることを可能にします。optilyzとBrazeのウェブフック統合を使用して、お客様にダイレクトメールを送信できます。