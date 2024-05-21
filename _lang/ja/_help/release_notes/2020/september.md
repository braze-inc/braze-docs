---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2020 年 9 月のリリース ノートが含まれています。"
---

# 9月

## ファネルレポート

ファネル レポートでは、 [キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) や [キャンバスを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports)受け取った後の顧客の行動を分析できる視覚的なレポートが提供されます。

## iOS 14 アップグレードガイド

Apple の新しい iOS 14 で発表された変更に従って、Braze iOS SDK の統合に必要な Braze 関連の変更とアクション項目がいくつかあります。詳細については、この [アップグレード ガイド]({{site.baseurl}}/ios_14/)をご覧ください。

## iOS 14 の IDFA と IDFV の変更

iOS 14 では、ユーザーはアプリにアクセスしたときに広告トラッキングをオプトインして、アプリと広告ネットワークに IDFA の読み取りを許可するかどうかを決定する必要があります。その結果、Braze の戦略は、代わりに「ベンダーの識別子」(IDFV など) を使用して、さまざまなデバイス間でユーザーを継続的に追跡できるようにすることです。詳細については、[iOS 14 アップグレード ガイド]({{site.baseurl}}/ios_14/)をご覧ください。

## メール検証

この新しい電子メール構文検証プロセスは、Braze の既存のプロセスのアップグレードです。これは、Braze に更新またはインポートされた電子メールが正しいことを確認するためのチェックです。詳細については、 [こちらのガイドラインと注意事項]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation)をご覧ください。

## Currents のランダム バケット ユーザー イベント

ランダム バケット番号 (RBN など) は、ワークスペース内に新しいユーザーが作成されるたびに発生します。このイベント中、各新規ユーザーにはランダムなバケット番号が割り当てられ、それを使用して、ランダムなユーザーの均一に分散されたセグメントを作成できます。これを使用して、ランダムなバケット番号値の範囲をグループ化し、キャンペーンとキャンペーン バリアント全体のパフォーマンスを比較します。このイベントを利用できるかどうかを確認するには、Currents の [顧客行動イベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)をご覧ください。

## キャンバス コンポーネント - 近日公開予定!

Braze は、キャンバスの柔軟性と機能性を向上させるために、4 つの新しいキャンバス コンポーネントを追加しました。これらの新しいコンポーネントには次のものが含まれます。[決定分割ステップ]({{site.baseurl}}/decision_split/)、 [遅延ステップ]({{site.baseurl}}/delay_step/)、 [メッセージングステップ]({{site.baseurl}}/message_step/)、および [Facebook へのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)。
- **キャンバスの意思決定の分割、遅延、およびメッセージングの手順**<br>決定分割を使用すると、ユーザーが定義済みのクエリに一致するかどうかに応じて Canvas ブランチを作成できます。遅延ステップを使用すると、対応するメッセージを必要とせずに、キャンバスにスタンドアロンの遅延を追加できます。メッセージング ステップを使用すると、Canvas フローの任意の場所にスタンドアロン メッセージを追加できます。
-**Facebookへのオーディエンス同期**<br>Braze Audience Sync to Facebook を使用すると、ブランドは独自の Braze 統合から独自のユーザー データを Facebook カスタム オーディエンスに追加して、行動トリガー、セグメンテーションなどに基づいて広告を配信することを選択できます。ユーザー データに基づいて Braze Canvas でメッセージをトリガーするために通常使用する基準 (プッシュ、メール、SMS、Webhook など) は、カスタム オーディエンスを介して Facebook でそのユーザーに広告をトリガーするために使用できるようになりました。

## SMS 受信イベント

Currents に新しいメッセージング エンゲージメント イベントが追加されました。このイベントは、ユーザーの 1 人が Braze SMS サブスクリプション グループの 1 つにある電話番号に SMS を送信したときに発生します。詳細については、Currents の [メッセージングとエンゲージメント イベントの用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)をご覧ください。
