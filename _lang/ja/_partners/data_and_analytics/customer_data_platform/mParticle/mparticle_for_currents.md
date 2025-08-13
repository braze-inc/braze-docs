---
nav_title: mParticle と Currents
article_title: mParticle と Currents
alias: /partners/mparticle_for_currents/
description: "この参考記事では、Braze Currentsと、マーケティング・スタック内のソース間で情報を収集し、ルーティングする顧客データ・プラットフォームであるmParticleとのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle と Currents

> [mParticle](https://www.mparticle.com) は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所に情報をルーティングする顧客データプラットフォームです。

BrazeとmParticleの統合により、2つのシステム間の情報の流れをシームレスに制御できる。[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) では、データを mParticle に接続し、グローススタック全体で実用的なデータにすることもできます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Currents | mParticle にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
| mParticle アカウント | このパートナーシップを利用するには、[mParticleアカウント](https://app.mparticle.com/login)が必要です。 |
| mParticle のサーバー間キーとシークレット | これらを取得するには、mParticle ダッシュボードに移動し、mParticle が iOS、Android、および Web プラットフォームの Braze インタラクションデータを受信できるようにするために[必要なフィード](#step-1-create-feeds)を作成します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## mParticle認証情報について

mParticleには、アプリレベルとワークスペースレベルの認証情報があり、イベントの送信方法に影響を与える。

- **アプリレベル：**mParticleは各アプリごとにイベントを分離するため、iOSアプリに与えるアプリレベルの認証情報は、iOS固有のイベントを送信するためにのみ使用できる。
- **ワークスペースレベル：**mParticle は、(アプリ固有**ではない**) すべてのイベントをグループ化します。つまり、アプリグループに与えるワークスペースレベルの認証情報は、アプリ固有ではないすべてのイベントの送信に使用されます。

これは、mParticle が個々のアプリに基づいて「フィード」を取り込んでいると考えることができます。例えば、iOS用、Android用、Web用のアプリを1つずつ用意すると、イベントがバラバラになってしまう。つまり、各アプリに同じ認証情報を提供すると、1つのmParticleフィードが、重複することなく、すべてのアプリのすべてのデータを受信するために使用される。

## 統合

### ステップ1:フィードを作成する

mParticle 管理者アカウントから、**[Setup] > [Inputs]** に移動します。mParticle**Directory** で **Braze** を見つけ、フィード統合を追加します。

Braze フィード統合は、iOS、Android、Web、Unbound の4つのフィードをサポートしています。バインドされていないフィードは、プラットフォームに接続されていない電子メールなどのイベントに使用できる。メインプラットフォームフィードごとに入力を作成する必要があります。[**Feed Configurations**] タブの **[Setup] > [Input]** から追加の入力を作成できます。

![]({% image_buster /assets/img/braze-feed-inputs.png %})

フィードごとに、[**Act as Platform**] で対応するプラットフォームをリストから選択します。**act-as**フィードを選択するオプションが表示されない場合、データは結合されていないものとして扱われるが、データウェアハウスの出力に転送することは可能である。

![設定名を入力し、フィードのステータスを決定し、act as platform を選択することを求める最初の統合ダイアログボックス。]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}![ サーバー間キーとサーバー間シークレットを示す 2 番目の統合ダイアログボックス。]{% image_buster /assets/img/braze-feed-act2.png %}{: style="max-width:37%;"}

各入力を作成すると、mParticleはキーとシークレットを提供する。これらの認証情報をコピーし、各認証情報のペアがどのフィードのものであるかをメモしておいてください。

### ステップ2:Current を作成する

Braze で **[Currents] > [+ Currents を作成] > [mParticle エクスポートを作成]** に移動します。統合名、連絡先メールアドレス、各プラットフォームの mParticle API キーと mParticle シークレットキーを入力します。次に、追跡したいイベントを選択する。利用可能なイベントのリストが提供される。最後に [**Currents を起動**] をクリックします。

![BrazeのmParticle Currentsページ。統合名、連絡先メール、API キー、シークレットキーのフィールドがある。]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
mParticle API キーと mParticle シークレットキーを最新の状態に維持することが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態のまま **48 時間**を超えると、コネクターのイベントがドロップし、データが永久に喪失します。
{% endalert %}

mParticleに送信されるすべてのイベントには、ユーザーの `external_user_id` が `customerid` として含まれます。現時点では、Brazeは、`external_user_id` を設定していないユーザーのイベントデータを送信しない。mParticle で、デフォルトの `customerid` ではない別の ID に `external_user_id` をマッピングする場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。 

## サポートされている Currents イベント

Brazeは、Currentsの[ユーザー行動]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメントイベントの]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)用語集に記載されている以下のデータをmParticleにエクスポートすることをサポートしている：

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
- アプリ内メッセージ（中止、クリック、インプレッション）
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- プッシュ通知 (中止、バウンス、開封、送信)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


mParticle 統合の詳細については、[こちらのドキュメント](http://docs.mparticle.com/integrations/braze/feed)を参照してください。

