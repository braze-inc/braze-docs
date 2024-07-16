---
nav_title: Amplitude for Currents
article_title:Amplitude for Currents
page_order:0
description:「この参考記事では、Braze Currentsと製品分析およびビジネスインテリジェンスプラットフォームであるAmplitude とのパートナーシップについて概説しています。「
page_type: partner
tool:Currents
search_tag:Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents for Amplitude

> [Amplitude](https://amplitude.com/) は、製品分析およびビジネスインテリジェンスプラットフォームです。

BrazeとAmplitude の双方向統合により、[Amplitude コホート、ユーザー特性、イベントをBrazeに同期できるだけでなく]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)、Braze Currentsを利用してBrazeイベントをAmplitude [にエクスポートし、製品やマーケティングデータのより深い分析を行うことができます](#data-export-integration)。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Amplitude 勘定 | このパートナーシップを利用するには、[Amplitude アカウントが必要です](https://amplitude.com/)。 |
| Currents | データをAmplitude にエクスポートし直すには、[アカウントにBraze Currentsを設定しておく必要があります]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)。 |
{: .reset-td-br-1 .reset-td-br-2} 

## データエクスポート統合

Braze から Amplitude にエクスポートできるイベントとイベントプロパティの完全なリストは、以下のセクションにあります。Amplitude に送信されるすべてのイベントには、AAmplitude ユーザー `external_user_id` ID としてユーザーのイベントが含まれます。

{% alert important %}
この機能を使用するには、Amplitude のユーザー ID がBrazeの外部IDと一致している必要があります。
{% endalert %}

Brazeは、`external_user_id`セットを持っているユーザーまたはセットを持っている匿名ユーザーにのみイベントデータを送信します。`device_id`匿名ユーザーの場合は、Amplitude デバイスIDをSDK BrazeデバイスIDと同期する必要があります。以下に例を示します。
```java
amplitude.setDeviceId(Apppboy.getInstance(context).getDeviceId();)
```

Amplitude には次の 2 種類のイベントをエクスポートできます。[メッセージエンゲージメントイベントは](#supported-currents-events)、メッセージ送信に直接関連するBrazeイベントと、プラットフォームを通じて追跡されるセッション、[カスタムイベント、購入などの他のアプリまたはWeb サイトアクティビティを含む顧客行動イベントで構成されます](#supported-currents-events)。通常のイベントにはすべてプレフィックスが付き`[Appboy]`、カスタムイベントにはすべてプレフィックスが付きます。`[Appboy] [Custom Event]`カスタムイベントプロパティと購入イベントプロパティには`[Purchase property]`、`[Custom event property]`それぞれプレフィックスとが付きます。

Brazeに名前を付けてインポートしたすべてのコホートには、プレフィックスとサフィックスに「the」`[Amplitude]` が付きます。`cohort_id`つまり、「TEST_COHORT」という名前のコホートと `cohort_id`「abcd1234」の付いたコホートには、Braze フィルターでタイトルが付けられます。`[Amplitude] TEST_COHORT: abcd1234`

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット][support]を開いてください。

### ステップ1:Braze でのAmplitude 積分の設定 

Amplitude で、Amplitude エクスポート API キーを探します。

{% alert warning %}
Amplitude API キーを最新の状態に保ってください。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。**これが48時間以上続くと**、コネクタのイベントはドロップされ、データは完全に失われます。
{% endalert %}

### ステップ2:Braze カレントを作成

Braze で、\[**電流] > \[+ Currents を作成] > \[Amplitude エクスポートを作成**] に移動します。リストされたフィールドに、インテグレーション名、連絡先メールアドレス、Amplitude エクスポート API キー、Amplitude リージョンを入力します。次に、追跡するイベントを選択します。利用可能なイベントのリストが表示されます。最後に、「**現在のバージョンを起動**」をクリックします

{% alert note %}
Braze CurrentsからAmplitude に送信されたイベントは、Amplitude イベントのボリュームクォータにカウントされます。
{% endalert %}

![The Braze Amplitude Currents page. This page includes fields for integration name, contact email, API key, and US region. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
詳細については、[Amplitudeの統合ドキュメントをご覧ください](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)。
{% endtab %}

## レート制限

Currents AmplitudeのHTTP APIに接続しますが、[このAPIのレート制限は30イベントです](https://developers.amplitude.com/docs/http-api-v2#upload-limit)/second per device and an undocumented limit of 500K events/day per device. If these thresholds are exceeded, Amplitude will throttle events logged through Currents. If a device in your integration exceeds this rate limit, you may experience a delay in when events from all devices will appear in Amplitude.

デバイスは30件を超えるイベントレポートしてはいけません/second or 500K events/day under normal circumstances, and this event pattern should only occur due to a misconfigured integration. To avoid this type of delay, ensure that your SDK integration reports events at a normal rate as specified in our SDK integration instructions and refrain from running automated tests that generate many events for a single device.

## サポートされている Currents イベント

Braze は、Currents [[のユーザー行動とメッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベントの用語集に記載されている以下のデータを Amplitude にエクスポートすることをサポートしています。

### 行動
- カスタムイベント: `users.behaviors.CustomEvent`
- インストールアトリビューション: `users.behaviors.InstallAttribution`
- Location: `users.behaviors.Location`
- Purchase: `users.behaviors.Purchase`
- Uninstall: `users.behaviors.Uninstall`
- アプリ (最初のセッション、セッション終了、セッション開始)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
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
  
[support]: {{site.baseurl}}/braze_support/
