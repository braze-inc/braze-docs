---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel_for_currents/
description: "このリファレンス記事では、Braze と業務分析 プラットフォームであるMixpanel との提携の概要を説明します。これにより、Mixpanel コホートをBraze に読み込んで、将来のBraze キャンペーンs またはキャンバスでユーザーs をターゲットにするために使用できるBraze Segments を作成できます。"
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/) は、Mixpanel から他のプラットフォームs にイベントをエクスポートして、より深い解析を実行できるビジネス分析 プラットフォームです。収集されたデータは、カスタムレポートs を構築し、ユーザー エンゲージメントとリテンションを測定するために使用できます。

Braze とMixpanel を統合すると、[Mixpanel コホートをBraze]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/mixpanel/) にインポートして、将来のBraze キャンペーンs またはキャンバスでユーザーs をターゲットにするために使用できるBraze Segments を作成できます。また、[ へのBraze Currentsを活用して、Brazeの行動をMixpanel](#data-export-integration) にエクスポートし、コンバージョンのs、リテンション、および商品の使用状況をより深く分析することもできます。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Mixpanelアカウント | この提携の前倒しタグを行うには、[Mixpanelアカウント](https://mixpanel.com/)が必要です。 |
| Currents | データをMixpanel に書き戻すには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2} 

## データエクスポート統合

Braze からミックスパネルにエクスポートできるイベントの一覧は、以下のとおりです。Mixpanel に送信されるすべてのイベントには、ユーザーの`external_user_id` がMixpanel の識別ID として含まれます。このとき、Braze は`external_user_id` が設定されていないユーザーs のイベントデータを送信しません。

ミックスパネルには2 種類のイベントを書き出すことができます。[メッセージエンゲージメントイベント](#supported-currents-events) メッセージ送信に直接的に関連するBrazeイベント、および[カスタマービヘイビアイベント](#supported-currents-events) には、セッション s、カスタムイベント、およびプラットフォーム経由で追跡された購買などの他のアプリやWeb サイトアクティビティが含まれます。すべてのカスタムイベントs には、`[Braze Custom Event]` が接頭辞として付加されます。カスタムイベントプロパティと購入イベントプロパティのプレフィックスは、それぞれ`[Custom event property]` と`[Purchase property]` です。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット][support]を開いてください。

### ステップ1:ミックスパネル認証情報を取得

ミックスパネルダッシュボードで、新規または既存のプロジェクトの**プロジェクト設定**を選択します。ここにMixpanel API シークレットとMixpanel トークンがあります。これらの認証情報は、次回のステップでCurrentsコネクションを作成するために使用されます。 

### ステップ2:Braze電流の作成

Braze で、\*\*Currents > **\+ Create Current** > **Create Mixpanel Export** に移動します。一覧表示されているフィールドで、インテグレーションの名前、連絡先メール、Mixpanel API シークレット、およびMixpanel トークンを指定します。次に、追跡するイベントを選択します。使用可能なイベントのリストが表示されます。最後に、**Launch Current**をクリックします。

![BrazeミックスパネルのCurrents画面。このページには、インテグレーションの名前、連絡先メール、APIシークレット、およびMixpanelエクスポートトークンのフィールドが含まれます。Currents画面の下半分には、送信可能なCurrentsが表示されます。]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab 注 %}
詳細については、Mixpanel の[integration docs](https://help.mixpanel.com/hc/en-us/articles/360001243663) を参照してください。
{% endtab %}

## 対応Currents

Braze は、Currents [ ユーザーの動作]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) および [ メッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) イベント用語集の Mixpanel へのエクスポートをサポートしています。

### 行動
- カスタムイベント: `users.behaviors.CustomEvent`
- インストール属性: `users.behaviors.InstallAttribution`
- 場所: `users.behaviors.Location`
- 購入: `users.behaviors.Purchase`
- アンインストール: `users.behaviors.Uninstall`
- アプリ(最初のセッション、セッションエンド、セッションスタート)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- サブスクリプション(グローバル状態の変更): `users.behaviors.subscription.GlobalStateChange`
- サブスクリプショングループ(状態変更): `users.behaviors.subscriptiongroup.StateChange`
  
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
  
[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
