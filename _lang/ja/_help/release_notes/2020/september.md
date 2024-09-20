---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事は、2020年9月のリリースノートを含んでいます。"
---

# 9月

## ファンネルレポート

ファネルレポートは、[キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) または[キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports) を受信した後に、顧客が実行するジャーニーを分析できる視覚的なレポートを提供します。

## iOS 14 アップグレード

アップルの新しいiOS 14で発表された変更に伴い、Braze関連の変更やアクションの項目が、iOS SDKの統合に必要なものがいくつかあります。詳細については、この[アップグレードガイド]({{site.baseurl}}/ios_14/)を参照してください。

## iOS 用IDFA およびIDFV の変更14

iOS 14 では、ユーザー s は"トラッキング をアドインするかどうかを決定し、アプリを訪問するときに、s およびアドネットワークにIDFA を読み取らせる必要があります。そのため、Braze の戦略では、代わりに" 識別子をベンダー" (IDFV など) に使用することで、さまざまな機器間でユーザーを追跡し続けることができます。詳しくは、[iOS 14 アップグレードガイド]({{site.baseurl}}/ios_14/)をご覧ください。

## メール検証

この新しいメールシンタックス検証プロセスは、Brazeの既存のものへのアップグレードです。これは、Brazeに更新またはインポートされたメールが正しいことを確認するための検査です。詳細については、[これらのガイドラインと注記]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation)を参照してください。

## Currentsにおけるランダムバケットユーザー事象

ランダムバケット番号(RBNなど)は、新しいユーザーがワークスペース内に作成されるたびに発生します。このイベントの間、新規ユーザーのそれぞれにランダムなバケット番号が割り当てられます。このバケット番号を使用して、ランダムなユーザーの一様分布セグメントを作成できます。これを使用して、ランダムバケット番号値の範囲をグループ化し、キャンペーンとキャンペーンバリアント間でパフォーマンスを比較します。このイベントが使用可能かどうかを確認するには、Currents[ 顧客行動 イベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) を参照してください。

## キャンバスコンポーネント - まもなく登場します!

Braze では、キャンバスの柔軟性と機能性を高めるために、4 つの新しいキャンバスコンポーネントが追加されました。これらの新しいコンポーネントは次のとおりです。[分割ステップ]({{site.baseurl}}/decision_split/)、[遅延ステップ]({{site.baseurl}}/delay_step/)、[メッセージングステップ]({{site.baseurl}}/message_step/)、および[Fac eBook]({{site.baseurl}}/audience_sync_facebook/)へのオーディエンス同期。
- **キャンバスのディシジョンの分割、遅延、およびメッセージングの手順**<br>ディシジョンスプリットは、ユーザーが定義済みクエリーと一致するかどうかに応じてキャンバスブランチを作成するために使用できます。遅延ステップでは、対応するメッセージを必要とせずに、キャンバスにスタンドアロン遅延を追加できます。メッセージステップでは、キャンバスフロー内の目的の場所にスタンドアロンメッセージを追加できます。
- **オーディエンスがファクトeBookに同期する**<br>Braze Audience Sync to Fac eBookを使用すると、ブランドは独自のBrazeインテグレーションからFac eBook カスタムオーディエンスに独自のユーザーのデータを追加して、行動トリガーやセグメンテーションなどに基づいた広告を配信できます。通常、メッセージをトリガーするために使用する基準(プッシュ、メール、SMS、Webフックなど)を、ユーザーデータに基づいてBrazeキャンバスで使用できるようになりました。これにより、カスタムオーディエンスを介してFac eBookでそのユーザーに広告をトリガーすることができます。

## SMS インバウンド受信イベント

新しいメッセージング エンゲージメントがCurrentsに追加されました。このイベントは、ユーザーの 1 人が Braze SMS サブスクリプショングループの 1 つの電話番号に SMS を送信したときに発生します。詳細については、Currents [ メッセージングおよびエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) を参照してください。
