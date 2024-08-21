---
nav_title: Amplitude for Currents
article_title: Amplitude for Currents
page_order: 0
description: "この参考記事では、Braze Currentsと、製品分析およびビジネス・インテリジェンス・プラットフォームであるAmplitudeのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze Learning course]](https://learning.braze.com/amplitude-integration-with-braze)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}電流に対する振幅

> [Amplitudeは](https://amplitude.com/)製品分析とビジネスインテリジェンスのプラットフォームである。

BrazeとAmplitudeの双方向統合により、[AmplitudeのCohorts]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)、ユーザー特性、イベントをBrazeに[同期させる]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)ことができる。また、Braze Currentsを活用して[BrazeのイベントをAmplitudeにエクスポート](#data-export-integration)し、製品やマーケティングデータの詳細な分析を行うこともできる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 振幅アカウント | このパートナーシップを利用するには、[Amplitudeアカウントが](https://amplitude.com/)必要である。 |
| Currents | データをAmplitudeにエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2} 

## データ・エクスポートの統合

BrazeからAmplitudeにエクスポートできるイベントとイベントプロパティの完全なリストは、以下のセクションにある。Amplitudeに送信されるすべてのイベントには、AmplitudeのユーザーIDとしてユーザーの`external_user_id` 。ブレーズ特有のイベント・プロパティは、Amplitudeに送られるデータの`event_properties` ・キーの下に送られる。

{% alert important %}
この機能を使うには、AmplitudeのユーザーIDとBrazeの外部IDが一致していなければならない。
{% endalert %}

Brazeがイベントデータを送信するのは、`external_user_id` を設定したユーザーか、`device_id` を設定した匿名ユーザーのみである。匿名ユーザーの場合は、SDKでAmplitudeのデバイスIDとBrazeのデバイスIDを同期させる必要がある。以下に例を示します。

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitudeには2種類のイベントをエクスポートできる：[メッセージ](#supported-currents-events)送信に直接関連するBrazeイベント、およびプラットフォームを通じて追跡されるセッション、カスタムイベント、購入などのその他のアプリまたはウェブサイトのアクティビティを含む[顧客行動イベントから](#supported-currents-events)構成される[メッセージエンゲージメントイベント](#supported-currents-events)。すべてのレギュラー・イベントのプレフィックスは`[Appboy]` で、すべてのカスタム・イベントのプレフィックスは`[Appboy] [Custom Event]` である。カスタム・イベントと購入イベントのプロパティには、それぞれ`[Custom event property]` と`[Purchase property]` というプレフィックスが付く。

名前が付けられBrazeにインポートされたすべてのコホートには、`[Amplitude]` が先頭に、`cohort_id` が末尾に付けられる。つまり、`cohort_id` "abcd1234 "を持つ "TEST_COHORT "という名前のコホートは、Brazeフィルターでは`[Amplitude] TEST_COHORT: abcd1234` というタイトルになる。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット][support]を開いてください。

### ステップ1:Brazeで振幅統合を設定する 

Amplitudeで、AmplitudeエクスポートAPIキーを探す。

{% alert warning %}
Amplitude API Keyを最新の状態に保つ。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止する。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

### ステップ2:ブレイズ電流を作る

Brazeで、**Current > + Create Current > Create Amplitude Exportに**移動する。リストにあるフィールドに、統合名、連絡先のEメール、AmplitudeエクスポートAPIキー、およびAmplitudeリージョンを入力する。次に、追跡したいイベントを選択する。利用可能なイベントのリストが提供される。最後に、**Launch Currentを**クリックする。

{% alert note %}
Braze CurrentsからAmplitudeに送信されたイベントは、Amplitudeのイベントボリュームクォータにカウントされる。
{% endalert %}

![ブレイズ振幅電流のページ。このページには、インテグレーション名、コンタクトEメール、APIキー、米国地域のフィールドがある。Currentsページの下半分には、送信可能なCurrentsイベントがリストアップされている。]({% image_buster /assets/img/amplitude4.png %})

{% tab 備考 %}
詳しくはAmplitudeの[統合ドキュメントを](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)チェックしてほしい。
{% endtab %}

## レート制限

電流はAmplitudeのHTTP APIに接続するが、このAPIには[、](https://developers.amplitude.com/docs/http-api-v2#upload-limit)1デバイスあたり30イベント/秒という[レート制限と](https://developers.amplitude.com/docs/http-api-v2#upload-limit)、1デバイスあたり500Kイベント/日という文書化されていない制限がある。これらのしきい値を超えた場合、AmplitudeはCurrentsを通じて記録されたイベントをスロットルする。インテグレーション内のデバイスがこのレート制限を超えると、すべてのデバイスからのイベントがAmplitudeに表示されるタイミングが遅れることがある。

デバイスは、通常であれば、30イベント/秒または500Kイベント/日を超えて報告すべきではなく、このようなイベントパターンは、誤設定された統合によってのみ発生するはずである。このような遅延を回避するには、SDKインテグレーションが、SDKインテグレーション・インストラクションで指定されているように、通常の速度でイベントをレポートすることを確認し、1つのデバイスに対して多くのイベントを生成する自動テストの実行を控えること。

## 百花繚乱イベントをサポート

Brazeは、Currentsの[ユーザー行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメントイベントの]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)用語集に記載されている以下のデータをAmplitudeにエクスポートすることをサポートしている：

### 行動
- カスタムイベントだ： `users.behaviors.CustomEvent`
- 帰属をインストールする： `users.behaviors.InstallAttribution`
- 場所はここだ： `users.behaviors.Location`
- 購入する： `users.behaviors.Purchase`
- アンインストールする： `users.behaviors.Uninstall`
- アプリ（初回セッション、セッション終了、セッション開始）
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- サブスクリプション（グローバルな状態変更）： `users.behaviors.subscription.GlobalStateChange`
- サブスクリプション・グループ（状態変更）： `users.behaviors.subscriptiongroup.StateChange`
  
### キャンペーン
- 中止する： `users_campaigns_abort`
- コンバージョンだ： `users.campaigns.Conversion`
- エンローリンコントロール `users.campaigns.EnrollInControl`
  
### キャンバス
- 中止する： `users_canvas_abort`
- コンバージョンだ： `users.canvas.Conversion`
- エントリーする： `users.canvas.Entry`
- 退場（マッチした観客、行われたイベント）
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 実験ステップ（コンバージョン、スプリット・エントリー）
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### メッセージ
- コンテンツカード（中止、クリック、却下、インプレッション、送信）
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- 電子メール（中止、バウンス、クリック、配信、マークアスパム、開封、送信、ソフトバウンス、購読解除）
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
