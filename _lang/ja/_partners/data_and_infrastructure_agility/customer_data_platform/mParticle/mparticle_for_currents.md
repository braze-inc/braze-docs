---
nav_title: 電流用m粒子
article_title: 電流用m粒子
alias: /partners/mparticle_for_currents/
description: "この参考記事では、Braze Currentsと、マーケティング・スタック内のソース間で情報を収集し、ルーティングする顧客データ・プラットフォームであるmParticleとのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# 電流用m粒子

> [mParticleは](https://www.mparticle.com)、複数のソースから情報を収集し、マーケティング・スタックの他のさまざまな場所にルーティングする顧客データ・プラットフォームである。

BrazeとmParticleの統合により、2つのシステム間の情報の流れをシームレスに制御できる。Currentsを使えば、データをmParticleに接続し、成長スタック全体で実行可能にすることもできる。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| mパーティクルアカウント | このパートナーシップを利用するには、[mParticleのアカウントが](https://app.mparticle.com/login)必要である。 |
| Currents | データをmParticleにエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
| mParticleサーバーからサーバーへのキー<br><br>mParticleサーバー間の秘密 | これらは、mParticleのダッシュボードに移動し、mParticleがiOS、Android、およびWebプラットフォーム用のBraze相互作用データを受信できるようにするために[必要なフィードを](#step-1-create-feeds)作成することで取得できる。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:フィードを作成する

mParticleの管理者アカウントから、**「設定」>「入力**」に移動する。mParticle**ディレクトリで** **Brazeを**見つけ、フィード統合を追加する。

Brazeのフィード統合は、iOS、Android、Web、Unboundの4つのフィードに対応している。バインドされていないフィードは、プラットフォームに接続されていない電子メールなどのイベントに使用できる。各メイン・プラットフォーム・フィードの入力を作成する必要がある。**Setup > Inputsの** **Feed Configurations**タブで追加入力を作成できる。

![][1]

各フィードについて、**「Act as Platform**」で、一致するプラットフォームをリストから選択する。**act-as**フィードを選択するオプションが表示されない場合、データは結合されていないものとして扱われるが、データウェアハウスの出力に転送することは可能である。

![最初の統合ダイアログボックスが表示され、設定名を入力し、フィードのステータスを決定し、動作するプラットフォームを選択するよう促される。][2]{: style="max-width:40%;"} ![サーバー間キーとサーバー間シークレットを示す2つ目の統合ダイアログボックス。][3]{: style="max-width:37%;"}

各入力を作成すると、mParticleはキーとシークレットを提供する。これらのクレデンシャルをコピーし、各クレデンシャルのペアがどのフィードのものであるかをメモしておくこと。

### ステップ2:電流を作る

Brazeで、**Current > + Create Current > Create mParticle Exportに**移動する。統合名、連絡先メールアドレス、各プラットフォームのmParticle APIキーとmParticleシークレットキーを入力する。次に、追跡したいイベントを選択する。利用可能なイベントのリストが提供される。最後に、**Launch Currentを**クリックする。

![BrazeのmParticle Currentsページ。] （{% image_buster /assets/img_archive/currents-mparticle-edit.png %} ）。

{% alert important %}
mParticle API KeyとmParticle Secret Keyを最新の状態に保つことが重要で、コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止する。この状態のまま **48 時間**を超えると、コネクターのイベントがドロップし、データが永久に喪失します。
{% endalert %}

mParticleに送信されるすべてのイベントには、`customerid` としてユーザーの`external_user_id` が含まれる。現時点では、Brazeは、`external_user_id` を設定していないユーザーのイベントデータを送信しない。mParticleの`external_user_id` 、デフォルトの`customerid` 以外のIDにマッピングしたい場合は、Braze CSMに連絡すること。 

## 百花繚乱イベントをサポート

Brazeは、Currentsの[ユーザー行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメントイベントの]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)用語集に記載されている以下のデータをmParticleにエクスポートすることをサポートしている：

### 行動
- アンインストールする： `users.behaviors.Uninstall`
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
- プッシュ通知（中止、バウンス、開封、送信）
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


mParticleの統合についての詳細は、[こちらの](http://docs.mparticle.com/integrations/braze/feed)ドキュメントを参照されたい。

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
