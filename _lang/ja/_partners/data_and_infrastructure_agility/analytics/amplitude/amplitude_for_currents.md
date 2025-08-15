---
nav_title: Amplitude for Currents
article_title: Amplitude for Currents
page_order: 0
description: "この参考記事では、Braze Currentsと、製品分析およびビジネス・インテリジェンス・プラットフォームであるAmplitudeのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude for Currents

> [Amplitude](https://amplitude.com/) は製品分析およびビジネスインテリジェンスプラットフォームです。

Braze と Amplitude の双方向統合により、[ Amplitude コホート]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)、ユーザー特性、およびイベントを Braze に同期し、また Braze Currents を使用して [Amplitude に Braze イベントをエクスポートして](#data-export-integration)、製品データとマーケティングデータのより深い分析を実行できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Amplitude アカウント | このパートナーシップを活用するには、[Amplitude アカウント](https://amplitude.com/)が必要です。 |
| Currents | Amplitude にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## データ・エクスポートの統合

BrazeからAmplitudeにエクスポートできるイベントとイベントプロパティの完全なリストは、以下のセクションにある。Amplitude に送信されるすべてのイベントには、ユーザーの`external_user_id` が Amplitude ユーザー ID として含まれます。Braze 固有のイベントプロパティは、Amplitude に送信されるデータの`event_properties` キーで送信されます。

{% alert important %}
この機能を使用するには、Amplitude のユーザー IDが Braze の external ID に一致している必要があります。
{% endalert %}

Brazeがイベントデータを送信するのは、`external_user_id` を設定したユーザーか、`device_id` を設定した匿名ユーザーのみである。匿名ユーザーの場合は、SDKでAmplitudeのデバイスIDとBrazeのデバイスIDを同期させる必要がある。以下に例を示します。

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitudeには2種類のイベントをエクスポートできる：[メッセージエンゲージメントイベント](#supported-currents-events) (メッセージ送信に直接関連する Braze イベントで構成される) と、[顧客行動イベント](#supported-currents-events) (セッション、カスタムイベント、プラットフォーム経由で追跡された購入などのその他のアプリまたは Web サイトアクティビティを含む) です。すべての標準的なイベントには `[Appboy]` が接頭辞として付加され、すべてのカスタムイベントには `[Appboy] [Custom Event]` が付加されます。カスタムイベントプロパティの接頭辞は `[Custom event property]`、購入イベントプロパティの接頭辞は `[Purchase property]` です。

名前が付けられ Braze にインポートされるすべてのコホートには、接頭辞として `[Amplitude]` が、接尾辞として`cohort_id` が付加されます。これは、`cohort_id` が「abcd1234」で名前が「TEST_COHORT」のコホートが、Braze フィルターでは `[Amplitude] TEST_COHORT: abcd1234` というタイトルになることを意味します。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット][support]を開いてください。

### ステップ1:Braze で Amplitude 統合を設定する 

Amplitudeで、AmplitudeエクスポートAPIキーを探す。

{% alert warning %}
Amplitude API Keyを最新の状態に保つ。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

### ステップ2:Braze Current を作成する

Braze で **[Currents] > [+ Currents を作成] > [Amplitude エクスポートを作成]** に移動します。統合名、連絡先メール、Amplitude エクスポート API キー、および Amplitude リージョンを、リストされているフィールドに入力します。次に、追跡したいイベントを選択する。利用可能なイベントのリストが提供される。最後に [**Currents を起動**] をクリックします。

{% alert note %}
Braze Currents から Amplitude に送信されたイベントは、Amplitude イベントボリューム割り当ての対象となります。
{% endalert %}

![Braze Amplitude Currents ページ。このページには、統合名、連絡先メール、APIキー、US リージョンのフィールドがある。Currents ページの下半分には、送信可能なCurrents イベントが表示されている。]({% image_buster /assets/img/amplitude4.png %})

{% tab 注 %}
詳細については、Amplitude の[統合に関するドキュメント](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)を参照してください。
{% endtab %}

## レート制限

電流はAmplitudeのHTTP APIに接続するが、このAPIには、1デバイスあたり30イベント/秒という[レート制限と](https://developers.amplitude.com/docs/http-api-v2#upload-limit)、1デバイスあたり500Kイベント/日という文書化されていない制限がある。これらのしきい値を超えた場合、Amplitude はCurrents を通じて記録されるイベントを調整します。インテグレーション内のデバイスがこのレート制限を超えると、すべてのデバイスからのイベントがAmplitudeに表示されるタイミングが遅れることがある。

通常の状況では、デバイスが報告するレポートの数は、30イベント/秒または50万イベント/日を超えてはなりません。このようなイベントパターンは、設定の誤りがある場合にのみ発生します。このような遅延を回避するには、SDKインテグレーションが、SDKインテグレーション・インストラクションで指定されているように、通常の速度でイベントをレポートすることを確認し、1つのデバイスに対して多くのイベントを生成する自動テストの実行を控えること。

## サポートされている Currents イベント

Braze では、Currents の[ユーザーの行動]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)イベント用語集にある次のデータを Amplitude にエクスポートすることがサポートされています。

### 行動
- カスタムイベント: `users.behaviors.CustomEvent`
- インストールアトリビューション: `users.behaviors.InstallAttribution`
- 場所はここだ： `users.behaviors.Location`
- 購入: `users.behaviors.Purchase`
- アンインストール: `users.behaviors.Uninstall`
- アプリ（初回セッション、セッション終了、セッション開始）
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- サブスクリプション（グローバルな状態変更）： `users.behaviors.subscription.GlobalStateChange`
- サブスクリプション・グループ（状態変更）： `users.behaviors.subscriptiongroup.StateChange`
  
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
- アプリ内メッセージ（中止、クリック、インプレッション）
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
  
[support]: {{site.baseurl}}/braze_support/
