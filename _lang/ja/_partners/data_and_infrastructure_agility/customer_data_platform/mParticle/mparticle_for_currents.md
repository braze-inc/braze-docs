---
nav_title: mParticle for Currents
article_title: mParticle for Currents
alias: /partners/mparticle_for_currents/
description:「この参考記事では、Braze CurrentsとmParticleのパートナーシップについて概説しています。mParticleは、情報を収集してマーケティングスタック内のソース間でルーティングする顧客データプラットフォームです。「
page_type: partner
tool:Currents
search_tag:Partner

---

# Currents 用mParticle

> [mParticleは](https://www.mparticle.com)、複数のソースから情報を収集してマーケティングスタックのさまざまな場所に転送する顧客データプラットフォームです。

Braze と mParticle の統合により、2 つのシステム間の情報の流れをシームレスにコントロールできます。Currents を使うと、データを mParticle に接続して、成長スタック全体でアクションを起こせるようにすることもできます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| mParticle アカウント | このパートナーシップを利用するには、[mParticleアカウントが必要です](https://app.mparticle.com/login)。 |
| Currents | データをmParticleにエクスポートし直すには、[アカウントにBraze Currentsを設定しておく必要があります]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)。 |
| mParticle サーバーからサーバーへのキー<br><br>mParticle サーバー間シークレット | これらは、mParticleダッシュボードに移動し、mParticleがiOS、Android、[およびWebプラットフォーム用のBrazeインタラクションデータを受信できるようにするために必要なフィードを作成することで取得できます](#step-1-create-feeds)。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:フィードの作成

mParticle 管理者アカウントから、\[**設定] > \[入力**] に移動します。mParticle **ディレクトリで** **Braze** を探し、フィードインテグレーションを追加します。

Braze フィードインテグレーションは、iOS、Android、Web、アンバウンドの 4 つのフィードをサポートしています。非バインドフィードは、プラットフォームに接続されていないメールなどのイベントに使用できます。メインプラットフォームフィードごとに入力を作成する必要があります。\[**フィード設定] タブの \[設定****] > \[入力**] から追加の入力を作成できます。

![][1]

各フィードの「**プラットフォームとして活用**」で、一覧から一致するプラットフォームを選択します。**アクトアズフィード**を選択するオプションが表示されない場合、データはバインドされていないものとして扱われますが、データウェアハウス出力に転送することはできます。

![最初の統合ダイアログ・ボックスでは、構成名の指定、フィード・ステータス決定、および動作するプラットフォームの選択を求められます。][2]{: style="max-width:40%;"} ![2 番目の統合ダイアログボックスには、サーバー間キーとサーバー間シークレットが表示されます。][3]{: style="max-width:37%;"}

各入力を作成すると、mParticleからキーとシークレットが提供されます。これらの認証情報をコピーし、認証情報の各ペアがどのフィード用であるかを必ず書き留めておきます。

### ステップ2:\[現在のものを作成]

Braze で、\[**電流] > \[+ Currents を作成] > \[mParticle エクスポートを作成**] に移動します。各プラットフォームインテグレーション名、連絡先メールアドレス、mParticle API キーと mParticle シークレットキーを指定します。次に、追跡するイベントを選択します。利用可能なイベントのリストが表示されます。最後に、「**現在のバージョンを起動**」をクリックします

![The mParticle Currents page in Braze. Here, you can find fields for integration name, contact email, API key, and secret key.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
認証情報が期限切れになると、コネクタはイベントの送信を停止します。's important to keep your mParticle API Key and mParticle Secret Key up to date; if your connector'この状態のまま **48 時間**を超えると、コネクターのイベントがドロップし、データが永久に喪失します。
{% endalert %}

mParticle に送信されるすべてのイベントには、`external_user_id``customerid`ユーザーのイベントがとして含まれます。現時点では、`external_user_id` Brazeはセットを持っていないユーザーにはイベントデータを送信しません。デフォルトではないmParticle内の別のIDにマッピングしたい場合は`customerid`、Braze カスタマーサクセスマネージャーにお問い合わせください。`external_user_id` 

## サポートされている Currents イベント

Braze は、Currents [[のユーザー行動およびメッセージエンゲージメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベント用語集に記載されている以下のデータを mParticle にエクスポートすることをサポートしています。

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
- アプリ内メッセージ (中止、クリック、インプレッション)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- プッシュ通知 (中止、バウンス、開封、送信)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


mParticle インテグレーションの詳細については、[こちらのドキュメントをご覧ください](http://docs.mparticle.com/integrations/braze/feed)。

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
