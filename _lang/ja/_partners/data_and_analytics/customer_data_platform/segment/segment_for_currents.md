---
nav_title: Segment と Currents
article_title: Segment と Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "このリファレンス記事では、Braze Currentsとセグメント間の連携について概説します。この顧客データプラットフォームは、マーケティングスタック内の送信元間で情報を収集し、ルーティングします。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment と Currents  

> [Segment](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。本参考文献では、Braze Currentsとセグメントの関係を概観し、適切な実施と使用のための要求事項と手順を説明する。

Braze と Segments の統合により、Braze Currents を利用して Braze イベントを Segment にエクスポートし、コンバージョン、リテンション、製品使用率に関する詳細な分析を促進することもできます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Segment アカウント | このパートナーシップを活用するには、[Segment アカウント](https://app.segment.com/login)が必要です。 |
| Braze 宛先 | セグメントインテグレーションでは、すでに[Brazeを送信先]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)として設定しておく必要があります。<br><br>これには、[接続設定s]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)に正しいBrazeデータセンターとREST API キーを提供することも含まれます。 |
| Currents | Segment にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:セグメント書き込みキーの取得

Segment ダッシュボードで、Segment ソースを選択します。** [設定] > [API キー]** に移動します。ここで **Segment Write Key** を確認します。

{% alert warning %}
Segment Write Key を最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。これが**5 日** 以上続く場合、コネクタのイベントはドロップされ、データは永続的に失われます。
{% endalert %}

### ステップ2:新しいCurrentsコネクターを作成する

1. Braze で、**Partner Integrations** > **データエクスポート** に移動します。
2. [**\+ 新しい Currents を作成**] > [**セグメントデータのエクスポート**] をクリックします。
3. 次に、統合名、連絡先メール、Segment Write Key、および Segment リージョンを指定します。

![Braze の Segment Currents ページ。統合名、連絡先メール、Segment リージョン、API キーのフィールドがある。]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### ステップ3:メールエンゲージメントをエクスポートする

次に、エクスポートするメッセージエンゲージメントイベントを選択します。リストされている次のエクスポートイベントおよびプロパティテーブルを参照してください。Segment に送信されるイベントはすべて、ユーザーの `external_user_id` を `userId` に、ユーザーの `braze_id` を `anonymousId` に組み入れます。

Braze は、[**匿名ユーザーからのイベントを含める**] にチェックが入れられている場合にのみ、`external_user_id` がないユーザーのイベントデータを送信するため、注意が必要です。

{% alert important %}
現在、匿名ユーザーのエクスポートは早期アクセスの対象です。早期アクセスへの参加をご希望の場合は、Braze のアカウントマネージャーにご連絡ください。
{% endalert %}

![Braze の Segment Currents ページの利用可能なすべてのメッセージエンゲージイベントのリスト。]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

最後に [**Currents を起動**] を選択します。

{% alert warning %}
同じCurrentsコネクターを複数作成する場合(たとえば、2 つのメッセージエンゲージメントイベントコネクター)、それらは別々のワークスペースにする必要があります。Braze Segment Currents の統合では、1つのワークスペース内で異なるアプリケーションごとにイベントを分離することはできないため、そのようにできない場合、不必要なデータの重複排除やデータの損失が発生します。
{% endalert %}

詳細については、セグメント [ドキュメント](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) を参照してください。

## 最新の情報を更新する

{% multi_lang_include updating_currents.md %}

## サポートされている Currents イベント

Braze は、Currents [ユーザー動作]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) および [メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) イベント用語集にリストされている以下のデータのセグメントへのエクスポートをサポートしています。
 
### 行動
- アンインストール: `users.behaviors.Uninstall`
- サブスクリプション(グローバル状態の変更): `users.behaviors.subscription.GlobalStateChange`
- サブスクリプショングループ(状態の変更): `users.behaviors.subscriptiongroup.StateChange`
  
### キャンペーン
- 中止: `users_campaigns_abort`
- コンバージョン: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### キャンバス
- 中止: `users_canvas_abort`
- コンバージョン: `users.canvas.Conversion`
- エントリ:: `users.canvas.Entry`
- 離脱 (オーディエンス照合、実行済みのイベント)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 実験ステップ (コンバージョン、分割エントリ)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### メッセージ
- コンテンツカード（中止、クリック、却下、インプレッション、送信）
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- メール (中止、バウンス、クリック、配信、スパムとしてマーク、開封、送信、ソフトバウンス、配信停止)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- アプリ内メッセージ (中止、クリック、インプレッション)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- プッシュ通知（アボート、バウンス、iOSforeground、オープン、送信）
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS（中止、キャリア送信、配信、配信失敗、受信、拒否、送信、ショートリンククリック）
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- ウェブフック（中止、送信）
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (中止、配信、失敗、受信、読み取り、送信)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`

