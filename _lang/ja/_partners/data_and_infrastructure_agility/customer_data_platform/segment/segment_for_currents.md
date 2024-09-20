---
nav_title: Currents事業
article_title: Currents事業
page_order: 2
alias: /partners/segment_for_currents/
description: "このリファレンス記事では、Braze Currentsとセグメント間の連携について概説します。この顧客データプラットフォームは、マーケティングスタック内の送信元間で情報を収集し、ルーティングします。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Currents事業  

> [Segment](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。本参考文献では、Braze Currentsとセグメントの関係を概観し、適切な実施と使用のための要求事項と手順を説明する。

Brazeとセグメントインテグレーションを使用すると、Brazeの行動をセグメントにエクスポートするBraze Currentsを活用して、より深い分析をコンバージョンs、リテンション、および商品の使用状況に組み込むことができます。 

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| セグメント勘定 | この提携の前倒しタグを行うには、[セグメントアカウント](https://app.segment.com/login)が必要です。 |
| Braze 送信先 | セグメントインテグレーションでは、すでに[Brazeを送信先]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)として設定しておく必要があります。<br><br>これには、[接続設定s]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)に正しいBrazeデータセンターとREST API キーを提供することも含まれます。 |
| Currents | データをセグメントにエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:セグメント書き込みキーの取得

セグメントダッシュボードで、セグメントソースを選択します。次に、**Settings > API キー s** に移動します。ここには、**Segment Write Key** があります。

{% alert warning %}
セグメント書き込みキーを最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を中止します。これが **48 時間** 以上続く場合、コネクタのイベントはドロップされ、データは永続的に失われます。
{% endalert %}

### ステップ2:新しいCurrentsコネクターを作成する

1. Braze で、**Partner Integrations** > **データエクスポート** に移動します。
2. **\+ Create New Current** > **Segment Data Export**をクリックします。
3. 次に、インテグレーションの名前、連絡先メール、セグメント書き込みキー、およびセグメント領域を指定します。

![BrazeのセグメントCurrentsページです。ここには、インテグレーションの名前、連絡先メール、Segmentリージョン、およびAPI キーのフィールドs があります。][3]

### ステップ3:メールエンゲージメントをエクスポートする

次に、エクスポートしたいエンゲージメントを選択します。リストされている次のエクスポートイベントおよびプロパティテーブルを参照してください。セグメントに送信されるすべてのイベントには、ユーザーの`external_user_id` が`userId` として含まれます。このとき、Braze は`external_user_id` が設定されていないユーザーs に対してイベントデータを送信しません。

![BrazeのセグメントCurrentsページで使用可能なすべてのメッセージエンゲージメントイベントのリスト。][2]

最後に、**Launch Current**を選択します。

{% alert warning %}
同じCurrentsコネクターを複数作成する場合(たとえば、2 つのメッセージエンゲージメントイベントコネクター)、それらは別々のワークスペースにする必要があります。Braze セグメントCurrentsインテグレーションでは、1 つのワークスペース内のさまざまなアプリs によってイベントを分離できないため、これを実行しないと、不必要なデータのデデューピングとデータの損失が発生します。
{% endalert %}

詳細については、セグメント [ドキュメント](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) を参照してください。

## 最新の情報を更新する

{% multi_lang_include updating_currents.md %}

## 対応Currents

Braze は、Currents [ユーザー動作]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) および [メッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) イベント用語集にリストされている以下のデータのセグメントへのエクスポートをサポートしています。
 
### 行動
- アンインストール: `users.behaviors.Uninstall`
- サブスクリプション(グローバル状態の変更): `users.behaviors.subscription.GlobalStateChange`
- サブスクリプショングループ(状態の変更): `users.behaviors.subscriptiongroup.StateChange`
  
### キャンペーン
- 中止: `users_campaigns_abort`
- 変換: `users.campaigns.Conversion`
- 登録制御: `users.campaigns.EnrollInControl`
  
### キャンバス
- 中止: `users_canvas_abort`
- 変換: `users.canvas.Conversion`
- 入力: `users.canvas.Entry`
- 終了(一致したオーディエンス、実行されたイベント)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 試験手順(コンバージョン、分割エントリ)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### メッセージ
- コンテンツカード(中止、クリック、削除、インプレッション、送信)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- メール(中止、バウンス、クリック、配信、マークスパム、開封、送信、ソフトバウンス、配信停止)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- アプリ中(中止、押下、インプレッション)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- プッシュ通知(中止、跳ね返り、iOS フォアグラウンド、開封、送信)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS(アボート、キャリア送信、配信、配信失敗、インバウンド受信、拒否、送信、ショートリンククリック)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webフック(中止、送信)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp(アボート、配信、障害、受信、読み取り、送信)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}
