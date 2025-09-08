---
nav_title: キャンペーンのアラート
article_title: キャンペーンのアラート
page_order: 6

page_type: reference
description: "この記事では、キャンペーンアラートの概要、その利点、および安心感を得られる設定方法について説明します。"
tool: Campaigns
channel:
- email
- webhooks

---

# キャンペーンのアラート

> 弊社のゴールは、予想に反する事態が起きた場合には警告を発し、すべてがスムーズに運んでいるという安心感を提供することです。キャンペーンのしきい値アラートによって、安心感を得ることができます。重要なキャンペーンが、送信されるメッセージが予想よりも多かったり、少なすぎる場合には、これをいち早く知ることができます。

キャンペーンのアラートは、以下のキャンペーンで使用できます。

- 定期的なスケジュールされたキャンペーン
- アクションベースのキャンペーン
- API トリガーキャンペーン

## キャンペーンアラートの設定

アラートの設定を開始するには、キャンペーンの分析ページに移動します。[**アラートを設定**] を選択すると、アラートの上限と下限のしきい値、およびアラートの受信者とチャネルを指定できます。

![「キャンペーンモニタリング」ダイアログボックスにある 2 つのボタン: [キャンセル] と [保存]。]({% image_buster /assets/img_archive/campaign_alerts.png %})

スケジュールされた定期的なキャンペーンでは、キャンペーンが送信するたびに送られるメッセージの上限と下限のしきい値を設定できます。トリガーキャンペーンでは、毎時および毎日送信されるメッセージ数の上限と下限を設定できます。

メールアラート、Webhook アラート、またはその両方を設定できます。Webhook アラートは、Slack チャネルにアラートを送信できるため、非常に便利です。キャンペーンアラートと Slack の統合の詳細については、弊社の[ドキュメント]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration)を参照してください。

{% alert note %}
今後のキャンペーンのキャンペーンアラートを設定する場合、キャンペーンの開始前と終了後に更新を受信することがあります。これは、キャンペーンアラートは、キャンペーンが手動で停止されるまで送信され続けるためです。
{% endalert %}

## キャンペーンアラートの Webhook ペイロード

以下は、キャンペーンアラート Webhook の本文のペイロードの例です。この例では、特定のキャンペーン送信で送られたメッセージが 500 件を下回った場合に送信するように設定されたアラートを使用します。

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

