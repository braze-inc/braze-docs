---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2020年9月のリリースノートが含まれている。"
---

# 9月

## ファネルレポート

Funnel Reportingは、[キャンペーンや]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) [キャンバスを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports)受け取った後のカスタマージャーニーを分析できるビジュアルレポートを提供する。

## iOS 14アップグレードガイド

Appleの新しいiOS 14で発表された変更に伴い、Braze iOS SDK統合に必要なBraze関連の変更とアクション項目がいくつかある。詳しくは[アップグレードガイドを]({{site.baseurl}}/ios_14/)ご覧いただきたい。

## iOS 14におけるIDFAとIDFVの変更点

iOS 14では、ユーザーは広告トラッキングにオプトインし、アプリや広告ネットワークがアプリにアクセスした際に自分のIDFAを読み取るようにするかどうかを決めなければならない。その結果、Brazeの戦略では、代わりに（IDFVのような）「ベンダーの識別子」を使用することで、異なるデバイス間でユーザーをトラッキングし続けることができる。詳しくは[iOS 14アップグレードガイドを]({{site.baseurl}}/ios_14/)ご覧いただきたい。

## メール認証

この新しいメール構文検証プロセスは、Brazeの既存のものをアップグレードしたものである。これは、Brazeに更新またはインポートされたメールが正しいかどうかを確認するためのチェックである。詳しくは、[こちらのガイドラインと注意]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation)事項をご覧いただきたい。

## Currentsのランダム・バケツ・ユーザー・イベント

ランダムバケット番号（RBNなど）は、ワークスペース内で新しいユーザーが作成されるたびに発生する。このイベントの間、新規ユーザーのそれぞれにランダムなバケット番号が割り当てられます。このバケット番号を使用して、ランダムなユーザーの一様分布セグメントを作成できます。これを使用して、ランダムバケット番号値の範囲をグループ化し、キャンペーンとキャンペーンバリアント間でパフォーマンスを比較します。このイベントが利用可能かどうかは、Currents[顧客行動イベント用語集を]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)参照のこと。

## キャンバス・コンポーネント - 近日公開予定！

Brazeは、キャンバスの柔軟性と機能性を高める4つの新しいキャンバスコンポーネントを追加した。これらの新コンポーネントには以下が含まれる：[条件分岐ステップ]({{site.baseurl}}/decision_split/)、[ディレイステップ]({{site.baseurl}}/delay_step/)、[メッセージングステップ]({{site.baseurl}}/message_step/)、[Facebookへのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)。
- **キャンバスの条件分岐、ディレイ、メッセージングのステップ**<br>条件分岐は、ユーザーが定義されたクエリにマッチするかどうかに応じてキャンバス分岐を作成するために使用できる。ディレイ・ステップは、メッセージを必要とせず、キャンバスに独立したディレイを追加することができる。メッセージングステップを使えば、キャンバスフローの好きな場所に単体のメッセージを追加できる。
- **オーディエンスがFacebookに同期する**<br>Braze Audience Sync to Facebookを使用することで、ブランドは自社のBrazeインテグレーションからユーザーデータをFacebookカスタムオーディエンスに追加し、行動トリガーやセグメンテーションなどに基づいた広告配信を選択することができる。顧客データに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準をすべて、カスタムオーディエンスを使ってFacebookでそのユーザーに広告をトリガーできるようになりました。

## SMS インバウンド受信イベント

Currentsに新しいメッセージング・エンゲージメント・イベントが追加された。このイベントは、ユーザーの 1 人が Braze SMS サブスクリプショングループの 1 つの電話番号に SMS を送信したときに発生します。詳しくは、Currents[メッセージングとエンゲージメント・イベントの用語集を]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)ご覧いただきたい。
