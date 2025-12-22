---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "このリファレンス記事では、Braze と Mixpanel のパートナーシップについて説明します。Mixpanel はビジネス分析プラットフォームであり、Mixpanel コホートを Braze にインポートして Braze セグメントを作成できます。作成したセグメントは、今後の Braze キャンペーンやキャンバスでユーザーをターゲットにするために使用できます。"
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"} Mixpanel

> [Mixpanel](https://mixpanel.com/) はビジネス分析プラットフォームであり、Mixpanel から他のプラットフォームにイベントをエクスポートして、より深い解析を実行できます。収集されたデータは、カスタムレポートの作成やユーザーエンゲージメントとリテンションの測定に使用できます。

Braze と Mixpanel の統合により、[Mixpanel コホートを Brazeにインポートして]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) Braze セグメントを作成できます。このセグメントは、今後の Braze キャンペーンやキャンバスでユーザーをターゲットにするために使用できます。Braze Currents を利用して [Braze イベントを Mixpanel にエクスポート](#data-export-integration)し、コンバージョン、リテンション、製品使用率に関する詳細な分析を促進することもできます。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Mixpanelアカウント | このパートナーシップを活用するには、[Mixpanel アカウント](https://mixpanel.com/)が必要です。 |
| Currents | Mixpanel にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## データ・エクスポートの統合

Braze から Mixpanel にエクスポートできるすべてのイベントを以下に示します。Mixpanel に送信されるすべてのイベントには、ユーザーの`external_user_id` が Mixpanel Distict ID として含まれます。現時点では、Brazeは、`external_user_id` を設定していないユーザーのイベントデータを送信しない。

Mixpanel にエクスポートできるイベントは2種類あります。[メッセージエンゲージメントイベント](#supported-currents-events) (メッセージ送信に直接関連する Braze イベントで構成される) と、[顧客行動イベント](#supported-currents-events) (セッション、カスタムイベント、プラットフォーム経由で追跡された購入などのその他のアプリまたは Web サイトアクティビティを含む) です。すべてのカスタムイベントには、接頭辞として `[Braze Custom Event]` が付いています。カスタムイベントプロパティの接頭辞は `[Custom event property]`、購入イベントプロパティの接頭辞は `[Purchase property]` です。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。

### ステップ1:Mixpanel 認証情報を取得する

Mixpanel ダッシュボードで、新規または既存のプロジェクトの [**Project Settings**] をクリックします。ここにMixpanel API シークレットとMixpanel トークンがあります。これらの認証情報は、次のステップで Currents 接続を作成するために使用します。 

### ステップ2:Braze Current を作成する

Braze で \*\*[Currents] > [**\+ Currents を作成**] > [**Mixpanel エクスポートを作成**] に移動します。表示されているフィールドに、統合名、連絡先メール、Mixpanel API シークレット、Mixpanel トークンを入力します。次に、追跡したいイベントを選択する。利用可能なイベントのリストが提供される。最後に [**Currents を起動**] をクリックします。

![Braze Mixpanel Currents ページ。このページには、インテグレーションの名前、連絡先メール、APIシークレット、およびMixpanelエクスポートトークンのフィールドが含まれます。Currentsページの下半分には、送信可能なCurrentsイベントがリストされている。]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
詳細については、Mixpanel の[統合に関するドキュメント](https://help.mixpanel.com/hc/en-us/articles/360001243663)を参照してください。
{% endtab %}

## サポートされている Currents イベント

Braze では、Currents の[ユーザーの行動]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)イベント用語集にある次のデータを Mixpanel にエクスポートすることがサポートされています。

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
  
