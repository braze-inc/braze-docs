---
nav_title: Segment for Currents
article_title:Currents 用セグメント
page_order:2
alias: /partners/segment_for_currents/
description:「この参考記事では、Braze CurrentsとSegmentのパートナーシップについて概説しています。Segmentは、情報を収集してマーケティングスタック内のソース間でルーティングする顧客データプラットフォームです。「
page_type: partner
tool:Currents
search_tag:Partner

---

# Currents 用セグメント  

> [Segmentは](https://segment.com)、顧客データ収集、整理、有効化に役立つ顧客データプラットフォームです。この参考記事では、Braze CurrentsとSegmentの関係の概要を説明し、適切な実装と使用のための要件とプロセスについて説明します。

Braze と Segment の統合により、Braze Currents を活用して Braze イベントをセグメントにエクスポートし、コンバージョン、リテンション、製品の使用状況をより深く分析できます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメント勘定科目 | このパートナーシップを利用するには、[セグメントアカウントが必要です](https://app.segment.com/login)。 |
| Braze 送信先 | [セグメント統合の送信先として Braze を既に設定しておく必要があります]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)。<br><br>これには、[接続設定に正しい]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings) Braze データセンターと REST API キーを指定することが含まれます。 |
| Currents | データをセグメントにエクスポートし直すには、[アカウントにBraze Currentsを設定する必要があります]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:セグメント書き込みキーを取得

セグメントダッシュボードで、セグメントソースを選択します。次に、**\[設定] > \[API キー]** に移動します。**ここにセグメント書き込みキーがあります**。

{% alert warning %}
認証情報が期限切れになると、コネクタはイベントの送信を停止します。's important to keep your Segment write key up to date. If your connector'**これが48時間以上続くと**、コネクタのイベントはドロップされ、データは完全に失われます。
{% endalert %}

### ステップ2:Currents コネクタを新規作成

1. Braze で、\[**パートナー統合**] > \[**データエクスポート**] に移動します。
2. \[**\+ 新規作成] \[**現在のセグメントデータエクスポート****] をクリックします。
3. 次に、インテグレーション名、連絡先メールアドレス、セグメント書き込みキー、セグメントリージョンを入力します。

![Braze のセグメントカCurrents ページここには、インテグレーション名、連絡先メールアドレス、Segment リージョン、API キーフィールドがあります。][3]

### ステップ3:メッセージエンゲージメントイベントをエクスポートする

次に、エクスポートするメッセージエンゲージメントイベントを選択します。次のエクスポートイベントとプロパティの表を参照してください。Segment に送信されるすべてのイベントには、`external_user_id``userId`ユーザーのイベントがとして含まれます。現時点では、`external_user_id` Brazeはセットを持っていないユーザーにはイベントデータを送信しません。

![Braze のセグメントCurrents ページで利用可能なすべてのメッセージエンゲージメントイベントのリスト。][2]

最後に、「**現在起動**」を選択します。

{% alert warning %}
同じ Currents コネクタを複数作成する場合 (たとえば、2 つのメッセージエンゲージメントイベントコネクタ) は、それぞれ異なるワークスペースに配置する必要があります。Braze Segment Currents統合では、1つのワークスペース内のさまざまなアプリによるイベントを分離できないため、これを行わないと、不要なデータ重複排除やデータの損失につながります。
{% endalert %}

詳しくは、[セグメントのドキュメントをご覧ください](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/)。

## 現在のデータを更新する

{% multi_lang_include updating_currents.md %}

## サポートされている Currents イベント

Brazeは、[[Currentsのユーザー行動とメッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベントの用語集に記載されている以下のデータをSegmentにエクスポートすることをサポートしています。
 
### 行動
- Uninstall: `users.behaviors.Uninstall`
- サブスクリプション (グローバル状態変更): `users.behaviors.subscription.GlobalStateChange`
- サブスクリプショングループ (状態変更): `users.behaviors.subscriptiongroup.StateChange`
  
### キャンペーン
- Abort: `users_campaigns_abort`
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### キャンバス
- Abort: `users_canvas_abort`
- Conversion: `users.canvas.Conversion`
- Entry: `users.canvas.Entry`
- 終了 (オーディエンスマッチング、イベントの実施)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 実験工程 (コンバージョン、分割エントリ)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### メッセージ
- コンテンツカード (中止、クリック、却下、インプレッション、送信)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- 電子メール (中止、バウンス、クリック、配信、迷惑メールとして登録、開封、送信、ソフトバウンス、配信停止)
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
- プッシュ通知 (中止、バウンス、iOS フォアグラウンド、開封、送信)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (中止、キャリア送信、配送、配信失敗、インバウンド受信、拒否、送信、ショートリンククリック)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- ウェブフック (中止、送信)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (中止、配信、失敗、受信受信、読み取り、送信)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}
