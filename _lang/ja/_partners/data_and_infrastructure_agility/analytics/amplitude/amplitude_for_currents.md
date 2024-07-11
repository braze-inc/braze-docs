---
nav_title: Amplitude for Currents
article_title:電流の振幅
page_order:0
description:「この参考記事では、Braze Currents と製品分析およびビジネス インテリジェンス プラットフォームである Amplitude とのパートナーシップについて概説します。」
page_type: partner
tool:Currents
search_tag:Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}電流の振幅

> [Amplitude は](https://amplitude.com/) 、製品分析およびビジネス インテリジェンス プラットフォームです。

Braze と Amplitude の双方向統合により [、Amplitude コホート、ユーザー特性、イベントを Braze に同期できる]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)ほか、Braze Currents を活用して [Braze イベントを Amplitude にエクスポートし、](#data-export-integration) 製品やマーケティング データのより詳細な分析を実行できます。

## 前提条件

| 要件 | 説明 |
|---|---|
| アンプリチュードアカウント | このパートナーシップを活用するには、[Amplitude アカウント](https://amplitude.com/) が必要です。 |
| Currents | データを Amplitude にエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2} 

## データエクスポート統合

Braze から Amplitude にエクスポートできるイベントとイベント プロパティの完全なリストについては、次のセクションを参照してください。Amplitudeに送信されるすべてのイベントには、ユーザーの `external_user_id` Amplitude ユーザー ID として。Braze固有のイベントプロパティは、 `event_properties`Amplitude に送信されたデータを入力します。

{% alert important %}
この機能を使用するには、Amplitude ユーザー ID が Braze 外部 ID と一致している必要があります。
{% endalert %}

Brazeは、イベントデータを、 `external_user_id` 設定されたユーザーまたは匿名のユーザーが `device_id` セット。匿名ユーザーの場合は、SDK で Amplitude デバイス ID を Braze デバイス ID と同期する必要があります。以下に例を示します。
```java
amplitude.setDeviceId(Apppboy.getInstance(context).getDeviceId();)
```

Amplitude には 2 種類のイベントをエクスポートできます。[メッセージエンゲージメントイベントは](#supported-currents-events) 、メッセージ送信に直接関連する Braze イベントと、プラットフォームを通じて追跡されるセッション、カスタムイベント、購入などの他のアプリまたは Web サイトのアクティビティを含む [顧客行動イベント](#supported-currents-events)で構成されます。すべての定期イベントには、 `[Appboy]`、すべてのカスタムイベントにはプレフィックスが付きます `[Appboy] [Custom Event]`。カスタムイベントと購入イベントのプロパティには、 `[Custom event property]` そして `[Purchase property]`、 それぞれ。

Brazeに名前が付けられインポートされたすべてのコホートには、 `[Amplitude]` そして、それらの `cohort_id`。これは、「TEST_COHORT" とともに `cohort_id` 「abcd1234」のタイトルは `[Amplitude] TEST_COHORT: abcd1234` Braze フィルターで。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット][support]を開いてください。

### ステップ1:Brazeで振幅統合を構成する 

Amplitude で、Amplitude エクスポート API キーを見つけます。

{% alert warning %}
Amplitude API キーを最新の状態に保ってください。コネクタの資格情報の有効期限が切れると、コネクタはイベントの送信を停止します。この状態が **48 時間**以上続くと、コネクタのイベントがドロップされ、データは永久に失われます。
{% endalert %}

### ステップ2:ろう付け電流を作成する

Braze で、**「Currents」>「+ Create Current」>「Create Amplitude Export」**に移動します。リストされたフィールドに、統合名、連絡先メール、Amplitude エクスポート API キー、および Amplitude リージョンを入力します。次に、追跡するイベントを選択します。利用可能なイベントのリストが表示されます。最後に、**「現在の起動」を**クリックします

{% alert note %}
Braze Currents から Amplitude に送信されたイベントは、Amplitude イベント ボリューム クォータにカウントされます。
{% endalert %}

![The Braze Amplitude Currents page. This page includes fields for integration name, contact email, API key, and US region. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
詳細については、Amplitude の [統合ドキュメント](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) をご覧ください。
{% endtab %}

## レート制限

CurrentsはAmplitudeのHTTP APIに接続しますが、 [レート制限](https://developers.amplitude.com/docs/http-api-v2#upload-limit) は30イベントです。/second per device and an undocumented limit of 500K events/day per device. If these thresholds are exceeded, Amplitude will throttle events logged through Currents. If a device in your integration exceeds this rate limit, you may experience a delay in when events from all devices will appear in Amplitude.

デバイスは30件を超えるイベントを報告してはならない/second or 500K events/day under normal circumstances, and this event pattern should only occur due to a misconfigured integration. To avoid this type of delay, ensure that your SDK integration reports events at a normal rate as specified in our SDK integration instructions and refrain from running automated tests that generate many events for a single device.

## サポートされている Currents イベント

Braze は、Currents の [ユーザー行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) と [メッセージ エンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) イベント用語集に記載されている次のデータを Amplitude にエクスポートすることをサポートしています。

### 行動
- カスタムイベント: `users.behaviors.CustomEvent`
- インストール属性: `users.behaviors.InstallAttribution`
- Location: `users.behaviors.Location`
- Purchase: `users.behaviors.Purchase`
- Uninstall: `users.behaviors.Uninstall`
- アプリ（最初のセッション、セッションの終了、セッションの開始）
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- サブスクリプション（グローバル状態の変更）: `users.behaviors.subscription.GlobalStateChange`
- サブスクリプション グループ (状態の変更): `users.behaviors.subscriptiongroup.StateChange`
  
### キャンペーン
- Abort: `users_campaigns_abort`
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### キャンバス
- Abort: `users_canvas_abort`
- Conversion: `users.canvas.Conversion`
- Entry: `users.canvas.Entry`
- 終了（一致したオーディエンス、実行されたイベント）
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 実験ステップ（コンバージョン、分割エントリ）
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### メッセージ
- コンテンツ カード (中止、クリック、却下、表示、送信)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- 電子メール (中止、バウンス、クリック、配信、スパムとしてマーク、開く、送信、ソフトバウンス、登録解除)
- アプリ内メッセージ（中止、クリック、インプレッション）
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- プッシュ通知（中止、バウンス、iOSフォアグラウンド、開く、送信）
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (中止、キャリア送信、配信、配信失敗、着信受信、拒否、送信、短縮リンクのクリック)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (中止、送信)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (中止、配信、失敗、受信、読み取り、送信)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  
[support]: {{site.baseurl}}/braze_support/
