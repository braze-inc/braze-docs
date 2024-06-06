---
nav_title: 通知設定
article_title: 通知設定
page_order: 1
page_type: reference
description: "このリファレンス記事では、会社アカウントでのメッセージングとアクティビティの監視に使用できるオプションについて説明します。"

---

# 通知設定

> 会社アカウントのメッセージングとアクティビティを監視する場合は、特定の通知を設定してその宛先を選択できます。

[**通知設定**] ページでは、会社に関する通知を受信するユーザー (存在する場合) を設定できます。キャンペーンの配信や技術的なエラーに関する通知を受信するユーザーを設定できます。週次分析レポートの受信者も指定できます。ほとんどの通知について、Braze はメールと Webhook チャネルをサポートしています。

![Braze ダッシュボードの [通知設定]ページ][61]

このページにアクセスするには、[**設定**] > [**管理者設定**] > [**通知設定**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントのドロップダウンを選択し、［**会社の設定**］ > ［**通知設定**］ に移動します。
{% endalert %}

## 利用可能な通知

次の表は、利用可能な通知の一覧です。

| 通知 | 説明 |利用可能な通知チャネル |
|--------------|-------------|-----------------|
| AWS 認証エラー | データをエクスポートするために Braze が Amazon Web サービスの認証情報を使用しようとしてエラーを受信したときに、受信者に通知します。 | メール、Webhook |
| キャンペーンの自動停止 | Braze がキャンペーンを停止したときに受信者に通知します。 | メール |
| キャンペーンインタラクションの有効期限 | キャンペーンインタラクションデータの有効期限が迫っているキャンペーンについて受信者に通知します。過去 30 日間にリターゲティングフィルターでそれを参照し、メッセージを送信するために使用されたセグメント、キャンペーン、キャンバスに関する情報もともに通知します。 | メール |
| キャンペーン/Canvas Updated | Notifies recipients when an active campaign/canvas is updated or deactivated, as well as when an inactive campaign/canvas is reactivated or when drafts are launched. | Email |
| キャンバスのインタラクションの有効期限 | キャンバスのインタラクションデータの有効期限が迫っているキャンバスについて受信者に通知します。リターゲティングフィルターでそれを参照し、過去 30 日間にメッセージを送信するために使用されたセグメント、キャンペーン、キャンバスに関する情報もともに通知します。 | メール |
| ニュースフィードカードを公開 /Live | Notifies recipients when News Feed cards are scheduled or published. | Email, Webhook |
| Push Credential Errors | Notifies recipients when an app's push credentials are invalid and when an app's push credentials are expiring soon. | Email, Webhook |
| Scheduled Campaign Sent/Not Sent | Notifies recipients when scheduled campaigns begin sending or when scheduled campaigns attempted to send but had no eligible users to send to. | Email, Webhook |
| スケジュールされたキャンペーンの上限到達 | スケジュールされた定期キャンペーンが上限に達したときに受信者に通知します。 | メール、Webhook |
| スケジュールされたキャンペーンの送信完了 | スケジュールされたキャンペーンの送信が完了したときに受信者に通知します。|メール、Webhook |
| 週次分析レポート | 毎週月曜日に、前週のワークスペースアクティビティの概要を受信者に送信します。受信者は、所属するワークスペースごとに概要を受け取ります。 | メール |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 週次分析レポート

Braze はオプションで、毎週月曜日の午前 5 時 (東部標準時) に、指定した社内の個人に週次レポートをメールで送信します。週次レポートに含めるカスタムイベントは、[**データ設定**] > [**カスタムイベント**] から選択できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは [**設定の管理**] > [**カスタムイベント**] にあります。
{% endalert %}

週次レポートに含めるイベントを 5 つまで選択できます。

![分析レポートに含めるイベントの選択][22]

## Slack の受信 Webhook 連携

Slack には外部ソースから Slack にメッセージを投稿できる[受信 Webhook アプリ][67]があります。始めるには、受信 Webhook アプリを開きます。

1. 通知の送信先の Slack チャネルを選択し、［**受信 Webhook 連携の追加**］ をクリックします。<br><br>
    ![Slack の受信 webhook 連携の追加][63]<br><br>
  Slack により URL が生成されます。受信しようとする通知について、この URL を Braze に入力する必要があります。<br><br>
2. **Webhook の URL** をコピーします。<br><br>
    ![Webhook の URL をコピー][64]<br><br>
3. [**会社の設定**] > [**通知設定**] タブに移動します。<br><br>
4. Slack で有効にする通知を選択します。この Slack チャネルに送信する通知が複数ある場合は、［**一括追加**］ を使用して複数の通知に Webhook を追加します。<br><br>
    ![有効にする Slack 通知を選択][65]{: style="max-width:60%;"}<br><br>
5. Slack により生成された URL を入力します。

操作完了です。この Slack チャネルに会社に関する通知が届くようになるはずです。このトピックについて、Slack のヘルプ記事 [Sending messages using Incoming Webhooks][62] も参照できます。


[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks