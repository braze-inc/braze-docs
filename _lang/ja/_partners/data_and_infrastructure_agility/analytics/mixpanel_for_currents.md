---
nav_title: Mixpanel
article_title:Mixpanel
alias: /partners/mixpanel_for_currents/
description:「この参考記事では、Brazeとビジネス分析プラットフォームであるMixpanelのパートナーシップについて概説しています。これにより、MixpanelコホートをBrazeにインポートして、将来のBrazeキャンペーンやCanvasesでユーザーをターゲットにするために使用できるBrazeセグメントを作成できます。「
page_type: partner
search_tag:Partner
tool:Currents

---
 
# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}ミックスパネル

> [Mixpanelは](https://mixpanel.com/)、Mixpanelから他のプラットフォームにイベントをエクスポートしてより詳細な分析を行うことができるビジネス分析プラットフォームです。収集されたデータを使用して、カスタムレポートを作成し、ユーザーエンゲージメントとリリテンションを測定できます。

BrazeとMixpanelの統合により、[MixpanelコホートをBrazeにインポートして、今後のBrazeキャンペーンやキャンバスでユーザーをターゲットにするために使用できるBrazeセグメントを作成できます]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/mixpanel/)。また、Braze [Currentsを活用してBrazeイベントをMixpanelにエクスポートし](#data-export-integration)、コンバージョン、リテンション、製品の使用状況をより深く分析することもできます。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ミックスパネルアカウント | このパートナーシップを利用するには、[Mixpanelアカウントが必要です](https://mixpanel.com/)。 |
| Currents | データをMixpanelにエクスポートし直すには、[アカウントにBraze Currentsを設定しておく必要があります]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)。 |
{: .reset-td-br-1 .reset-td-br-2} 

## データエクスポート統合

Braze から Mixpanel にエクスポートできるイベントの完全なリストは以下にあります。Mixpanelに送信されるすべてのイベントには、`external_user_id`ユーザーのイベントがMixpanelの個別IDとして含まれます。現時点では、`external_user_id` Brazeはセットを持っていないユーザーにはイベントデータを送信しません。

Mixpanelには2種類のイベントをエクスポートできます。[メッセージエンゲージメントイベントは](#supported-currents-events)、メッセージ送信に直接関連するBrazeイベントと、プラットフォームを通じて追跡されるセッション、[カスタムイベント、購入などの他のアプリまたはWeb サイトアクティビティを含む顧客行動イベントで構成されます](#supported-currents-events)。すべてのカスタムイベントにはというプレフィックスが付きます`[Braze Custom Event]`。カスタムイベントプロパティと購入イベントプロパティには`[Purchase property]`、`[Custom event property]`それぞれプレフィックスとが付きます。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット][support]を開いてください。

### ステップ1:Mixpanelの認証情報を取得

Mixpanelダッシュボードで、**新規または既存のプロジェクトのプロジェクト設定をクリックします**。ここには Mixpanel API シークレットとミックスパネルトークンが表示されます。これらの認証情報は、ステップで Currents 接続を作成するときに使用されます。 

### ステップ2:Braze カレントを作成

Braze で、\*\*Currents > **\+ カレントを作成 > **Mixpanelエクスポートの作成に移動します****。インテグレーション名、連絡先メールアドレス、Mixpanel APIシークレット、Mixpanelトークン一覧のフィールドに入力します。次に、追跡するイベントを選択します。利用可能なイベントのリストが表示されます。最後に、「**現在起動**」をクリックします。

![The Braze Mixpanel Currents page. This page includes fields for integration name, contact email, API secret, and mixpanel export token. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
詳細については、[Mixpanelの統合ドキュメントをご覧ください](https://help.mixpanel.com/hc/en-us/articles/360001243663)。
{% endtab %}

## サポートされている Currents イベント

Brazeは、[[Currentsのユーザー行動とメッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベントの用語集に記載されている以下のデータをMixpanelにエクスポートすることをサポートしています。

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
  
[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
