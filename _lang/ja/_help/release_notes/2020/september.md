---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2020年9月のリリースノートが含まれています。"
---

# 9月

## ファンネルレポート

ファネルレポートは、[キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) または[キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports) を受信した後に、顧客が実行するジャーニーを分析できる視覚的なレポートを提供します。

## iOS 14アップグレードガイド

Apple の新しい iOS 14で発表された変更に伴い、Braze iOS SDK の統合に必要な Braze 関連の変更とアクション項目がいくつかあります。詳細については、この[アップグレードガイド]({{site.baseurl}}/ios_14/)を参照してください。

## iOS 14の IDFA および IDFV の変更

iOS 14では、ユーザーがアプリにアクセスしたときに広告トラッキングをオプトインして、アプリと広告ネットワークに IDFA の読み取りを許可するかどうかを決定する必要があります。それに応じた Braze の戦略として、代わりに「ベンダーの識別子」 (IDFV など) を使用して、異なるデバイス間でユーザーを継続的に追跡できるようにします。詳しくは、[iOS 14 アップグレードガイド]({{site.baseurl}}/ios_14/)をご覧ください。

## メール検証

この新しいメールシンタックス検証プロセスは、Brazeの既存のものへのアップグレードです。これは、Brazeに更新またはインポートされたメールが正しいことを確認するための検査です。詳細については、[これらのガイドラインと注記]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation)を参照してください。

## Currentsにおけるランダムバケットユーザー事象

ランダムバケット番号 (RBNなど) は、ワークスペース内で新しいユーザーが作成されるたびに生成されます。このイベントの間、新規ユーザーのそれぞれにランダムなバケット番号が割り当てられます。このバケット番号を使用して、ランダムなユーザーの一様分布セグメントを作成できます。これを使用して、ランダムバケット番号値の範囲をグループ化し、キャンペーンとキャンペーンバリアント間でパフォーマンスを比較します。このイベントが使用可能かどうかを確認するには、Currents [顧客行動イベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)を参照してください。

## キャンバスコンポーネント - 近日提供開始

Braze は、キャンバスの柔軟性と機能性を向上させるために、4つの新しいキャンバスコンポーネントを追加しました。これらの新しいコンポーネントには[条件分岐ステップ]({{site.baseurl}}/decision_split/)、[遅延ステップ]({{site.baseurl}}/delay_step/)、[メッセージングステップ]({{site.baseurl}}/message_step/)、[FaceBook へのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)が含まれます。
- **キャンバスの条件分岐、遅延、およびメッセージングステップ**<br>条件分岐を使用して、ユーザーが定義済みのクエリと一致するかどうかに基づいてキャンバス Branch を作成できます。遅延ステップでは、対応するメッセージを必要とせずに、キャンバスにスタンドアロン遅延を追加できます。メッセージステップでは、キャンバスフロー内の目的の場所にスタンドアロンメッセージを追加できます。
- **Facebook へのオーディエンス同期**<br>Braze Facebook へのオーディエンス同期を使用すると、ブランドは独自の Braze 統合からのユーザーデータを Facebook のカスタムオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze キャンバスでメッセージをトリガーするために通常使用する基準 (プッシュ、メール、SMS、Webhook など) を、カスタムオーディエンスを介して Facebook 内の該当ユーザーに対して広告をトリガーするために使用できるようになりました。

## SMS インバウンド受信イベント

新しいメッセージングエンゲージメントが Currents に追加されました。このイベントは、ユーザーの 1 人が Braze SMS サブスクリプショングループの 1 つの電話番号に SMS を送信したときに発生します。詳細については、Currents [ メッセージングおよびエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) を参照してください。
