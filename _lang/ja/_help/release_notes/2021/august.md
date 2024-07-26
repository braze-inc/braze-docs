---
nav_title: 8月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2021年8月のリリースノートが含まれている。"
---

# 2021年8月

## Google オーディエンス・シンク

Braze[Audience Sync to Googleの]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)統合により、ブランドはクロスチャネルのカスタマージャーニーをGoogle検索、Googleショッピング、Gmail、YouTube、Googleディスプレイに拡大することができる。ファーストパーティの顧客データを利用し、ダイナミックな行動トリガーやセグメンテーションなどに基づいた広告を安全に配信することができる。Brazeキャンバスの一部としてメッセージ（例えば、プッシュ、メール、SMSなど）をトリガーするために通常使用する基準はすべて、Googleのカスタマーマッチ経由でそのユーザーに広告をトリガーするために使用することができる。

## ベストプラクティスiOS SDK統合ガイド

このオプションの[iOS統合SDKガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewios_sdk_integration/)、iOS SDKとそのコアコンポーネントをアプリケーションに初めて統合する際のセットアップのベストプラクティスについて、ステップバイステップで説明する。このガイドは、`BrazeManager.swift` ヘルパーファイルを作成する際に役立ちます。このヘルパーファイルは、Braze iOS SDK への依存関係をプロダクションコードの残りの部分から切り離し、アプリケーション全体で 1 つの `import AppboyUI` を生成します。このアプローチでは、過剰な SDK インポートから発生する問題が制限されるため、コードの追跡、デバッグ、および変更が容易になります。 

## 購入予測

購入予測は、マーケターがユーザーを識別し、購入する可能性に基づいてメッセージングするための強力なツールを提供する。購入予測を作成すると、Brazeは[勾配ブースティング決定木を](https://en.wikipedia.org/wiki/Gradient_boosting)使用した機械学習モデルをトレーニングし、過去の購入活動から学習し、将来の購入活動を予測する。詳しくは[購入予測]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/)ドキュメントをご覧いただきたい。 

## ドラッグ＆ドロップ・エディター

Braze Emailでは、[ドラッグ＆ドロップの]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/)新しい[編集機能を使って]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/)、キャンペーンでもキャンバスでも、完全にカスタマイズされたパーソナライズされたメールメッセージを作成することができます。ユーザーはエディターブロックをメールにドラッグできるようになり、より直感的なカスタマイズが可能になった。 

## ユーザーエイリアスのインポート

`external_id` を持っていないユーザーをターゲットにするには、[ユーザーエイリアスを持つ ユーザーのリストをインポートする]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias)ことができる。エイリアスは、代替のユニークなユーザー識別子として機能する。アプリにサインアップしていない、あるいはアカウントを作っていない匿名ユーザーにマーケターを行おうとしている場合に役立つ。 

## iOS 15アップグレードガイド

この[iOS 15アップグレードガイドは]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/)、iOS 15 (WWDC21)で導入された変更の概要と、Braze iOS SDKインテグレーションに必要なアップグレードのステップを説明している。

## Android 12アップグレードガイド

この[Android 12アップグレードガイドでは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/)、Android 12 (2021)で導入された関連する変更点と、お客様のBraze Android SDK統合に必要なアップグレードステップについて説明しています。

## A2P 10DLC

A2P 10DLCとは、企業が標準的な10桁のロングコード（10DLC）の電話番号を使ってアプリケーション・ツー・パーソン（A2P）タイプのメッセージングを送信できる米国のシステムを指す。10桁のロングコードは従来、パーソナライズされた個人間（P2P）トラフィック用に設計されていたため、スループットの制限やフィルターの強化によってビジネスが制約を受ける原因となっていた。このサービスはこれらの問題を軽減し、全体的なメッセージング配信性を向上させ、ブランドはリンクやアクションへの呼びかけを含む大規模なメッセージングを送信することができ、さらに消費者を迷惑メッセージから保護するのに役立つ。 

現在、米国のロングコードを持っている、または米国の顧客に送信するために米国のロングコードを使っている顧客は、すべて10DLCにロングコードを登録しなければならない。10DLCの詳細と、なぜ10DLCが必要なのかについては、[10DLCの]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/)専門[記事を]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/)参照されたい。

## 2 要素認証のリセット

2 要素認証によるログインに問題があるユーザーは、会社の管理者に連絡して、[2 要素認証をリセット]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset)することができる。

## 新しいBrazeパートナーシップ

### ハイタッチ - ワークフローオートメーション

Brazeと[Hightouchの]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/)統合により、データウェアハウスからの最新の顧客データを使用して、Braze上でより良いキャンペーンを構築することができる。顧客に適切でタイムリーなインタラクションを提供したいが、そのためにはBrazeアカウントのデータが正確で新鮮であることが重要である。データウェアハウスから顧客データを自動的にBrazeに同期させることで、データの整合性を心配する必要がなくなり、ワールドクラスのカスタマーエクスペリエンスの構築に集中することができる。

### トランセンド - データプライバシーとコンプライアンス

Brazeと[Transcendの]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/)パートナーシップは、数十のデータシステムにまたがるデータをオーケストレーションすることで、ユーザーによるプライバシー要求の自動化を支援する。最終的に、これはチームがGDPRやCCPAのような規制を遵守するのに役立ち、自分のデータに関しては個人が運転席に座ることになる。

### ティニクル -コホート・インポート

[Tinycluesは]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/)オーディエンス構築機能で、カスタマーエクスペリエンスを損なうことなくキャンペーン数と収益を増加させる機能と、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンスを追跡する分析機能を提供する。BrazeとTinycluesの統合は、ユーザーにより良いCRMプランニングと戦略へのパスを提供し、驚くほどユーザーフレンドリーなUIを使って、よりターゲットを絞ったキャンペーンを送り、新しい製品機会を見つけ、収益を上げることを可能にする。

### optilyz - ダイレクトメール

[optilyzは]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/)、顧客中心、持続可能、収益性の高いダイレクトメールキャンペーンを可能にするダイレクトメールオートメーションプラットフォームです。optilyzはヨーロッパ中の何百もの企業で使用されており、レター、ポストカード、セルフメーラーをクロスチャネルマーケティングに統合し、キャンペーンの自動化とパーソナライズ化を実現します。optilyzとBrazeのWebhook統合を使用して、顧客にダイレクトメールを送信する。