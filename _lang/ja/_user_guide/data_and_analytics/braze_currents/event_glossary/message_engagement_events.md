---
nav_title: メッセージエンゲージメントイベント
layout: message_engagement_events_glossary
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "この用語集には、Braze が追跡し、選択されたデータウェアハウスに Currents を使用して送信できるさまざまなメッセージエンゲージメントイベントをリストしています。"
tool: Currents
search_rank: 6
---

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。必要な情報がこの記事に見つからない場合は、 [顧客行動イベント ライブラリ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/)または [Currents サンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご覧ください。

{% details Explanation of message engagement event structure and platform values %}

### イベントの構造

このイベントの内訳は、メッセージエンゲージメントイベントに一般的に含まれる情報のタイプを示します。開発者とビジネスインテリジェンス戦略チームは、情報の構成要素をしっかり理解したうえで、受信した Currents イベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。

![Breakdown of a message engagement event showing an email unsubscribe event with the listed properties grouped by user-specific properties, campaign or Canvas tracking properties, and event-specific properties]({% image_buster /assets/img/message_engagement_event.png %})

メッセージエンゲージメントイベントは、**ユーザー固有**のプロパティ、**キャンペーン / キャンバス追跡**プロパティ、 および**イベント固有**のプロパティで構成されます。

### プラットフォームの値

特定のイベントは、ユーザーのデバイスのプラットフォームを示す `platform` 値を返します。
<br>次の表に、返される可能性のある値の詳細を示します。

| ユーザーデバイス | プラットフォームの値 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2}

{% enddetails %}

{% alert important %}
以下に示すスキーマは、データウェアハウスパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルのイベントデータにのみ適用されます。他のパートナーに適用されるスキーマについては、 [利用可能なパートナー]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。<br><br>さらに、Currents は 900 KB 超の過度に大きいペイロードを持つイベントをドロップすることに注意してください。
{% endalert %}

{% alert update %}
キャンバスフローに関連して、判読可能なオブジェクト名が近日中に Currents に導入されます。それまで、ID をグループ化に使用し、[キャンバスの詳細エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)を介して判読可能な名前に変換できます。
{% endalert %}

{% api %}

## WhatsApp 既読イベント

{% apitags %}
WhatsApp、既読
{% endapitags %}

このイベントは、WhatsApp メッセージがエンドユーザーによって既読になったときに発生します。

\`\`\`json
// WhatsApp 既読: users.messages.whatsapp.Read

{
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"company_id": (optional, string) ID of the sending Company,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"from_phone_number": (optional, string) phone number used to send,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"subscription_group_id": (optional, string) ID of the sending subscription group,
"time": (optional, int) 10-digit UTC time of the event in seconds since the epoch,
"to_phone_number": (optional, string) phone number of User receiving the message,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`

{% endapi %}
{% api %}

## WhatsApp 配信イベント

{% apitags %}
WhatsApp、配信
{% endapitags %}

このイベントは、送信された WhatsApp メッセージがエンドユーザーデバイスに正常に着信したときに発生します。

\`\`\`json
// WhatsApp 配信: users.messages.whatsapp.Delivery

{
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"company_id": (optional, string) ID of the sending Company,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"from_phone_number": (optional, string) phone number used to send,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"subscription_group_id": (optional, string) ID of the sending subscription group,
"time": (optional, int) 10-digit UTC time of the event in seconds since the epoch,
"to_phone_number": (optional, string) phone number of User receiving the message,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`

{% endapi %}

{% api %}

## WhatsApp 失敗イベント

{% apitags %}
WhatsApp、失敗
{% endapitags %}

このイベントは、WhatsApp がユーザーにメッセージを配信できないときに発生します。ハードバウンスは、配信到達性の永続的なエラーを意味します。

\`\`\`json
// WhatsApp 配信失敗: users.messages.whatsapp.Failure

{
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"company_id": (optional, string) ID of the sending Company,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"from_phone_number": (optional, string) phone number used to send,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"provider_error_code": (optional, string) Error Code from WhatsApp,
"provider_error_title": (optional, string) Description of failure from WhatsApp,
"subscription_group_id": (optional, string) ID of the sending subscription group,
"time": (optional, int) 10-digit UTC time of the event in seconds since the epoch,
"to_phone_number": (optional, string) phone number of User receiving the message,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}
  {% api %}

## WhatsApp 送信イベント

{% apitags %}
WhatsApp、送信
{% endapitags %}

このイベントは、Braze と WhatsApp の間で送信リクエストが正常に通信されたときに発生します。ただし、これはメッセージがエンドユーザーによって受信されたことを意味しません。

\`\`\`json
// WhatsApp 送信: users.messages.whatsapp.Send

{
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"company_id": (optional, string) ID of the sending Company,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"from_phone_number": (optional, string) phone number used to send,
"message_extras": (optional, string) Liquid tags related fields,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"subscription_group_id": (optional, string) ID of the sending subscription group,
"time": (optional, int) 10-digit UTC time of the event in seconds since the epoch,
"to_phone_number": (optional, string) phone number of User receiving the message,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}

{% api %}

## WhatsApp メッセージ中止イベント

{% apitags %}
WhatsApp、中止
{% endapitags %}

このイベントは、WhatsApp メッセージが Liquid の中止、サイレント時間などに基づいて中止された場合に発生します。

\`\`\`json
// WhatsApp 中止: users.messages.whatsapp.Abort

{
"abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
"abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
"action": (optional, string) action taken in response to this message (for example, Subscribed, Unsubscribed, or None),
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) id of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) id of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) id of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"company_id": (optional, string) id of the sending Company,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"send_id": (optional, string) message send ID this message belongs to,
"subscription_group_id": (optional, string) ID of the sending subscription group,
"time": (optional, int) 10-digit UTC time of the event in seconds since the epoch,
"user_id": (required, string) Braze ID of the user that performed this event
```
{% endapi %}
  {% api %}

## WhatsApp インバウンド受信イベント

{% apitags %}
WhatsApp、インバウンド受信
{% endapitags %}

このイベントは、ユーザーの 1 人が Braze WhatsApp サブスクリプショングループのいずれかの電話番号に WhatsApp メッセージを送信したときに発生します。 

\`\`\`json
// WhatsApp インバウンド受信: users.messages.whatsapp.InboundReceive

{
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"company_id": (optional, string) ID of the sending Company,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"inbound_phone_number": (optional, string)the inbound number that the message was sent to,
"medial_urls": (optional, string[]) media urls from the user,
"message_body": (optional, string) typed response from the user,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"quick_reply_text": (optional, string) test of button pressed by the user,
"subscription_group_id": (optional, string) ID of the sending subscription group,
"time": (optional, int) 10-digit UTC time of the event in seconds since the epoch,
"user_phone_number": (optional, string) the user’s phone number from which the message was received,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}

{% api %}

## コンテンツカードのメッセージ中止イベント

{% apitags %}
Abort, Content Cards
{% endapitags %}

このイベントは、コンテンツカードのメッセージが Liquid の中止、サイレント時間などに基づいて中止された場合に発生します。

\`\`\`json
// コンテンツカードの中止: users.messages.contentcard.Abort

{
"abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
"abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"device_id": (optional, string) ID of the device on which the event occurred,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"id": (required, string) globally unique ID of this event,
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"send_id": (optional, string) message send ID this message belongs to,
"time": (required, int) unix timestamp at which the event happened,
"timezone": (optional, string) timezone of the user,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}

{% api %}

## メールメッセージ中止イベント

{% apitags %}
Abort, Email
{% endapitags %}

このイベントは、メールメッセージが Liquid の中止、サイレント時間などに基づいて中止された場合に発生します。

\`\`\`json
// メール中止: users.messages.email.Abort

{
"abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
"abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
"app_group_id": (optional, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
"device_id": (optional, string) ID of the device on which the event occurred,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"email_address": (required, string) email address of the user,
"external_user_id": (optional, string) External user ID of the user,
"id": (required, string) globally unique ID of this event,
"ip_pool": (optional, string) IP Pool from which the email send was made
"message_variation_id": (optional, string) message variation ID of the variation this user received,
"message_variation_name": (optional, string) name of the message variation this user received,
"send_id": (optional, string) message send ID this message belongs to,
"time": (required, int) unix timestamp at which the event happened,
"timezone": (optional, string) timezone of the user,
"user_id": (required, string) Braze ID of the user that performed this event,
}
  \`\`\`
  {% endapi %}

{% api %}

## プッシュ通知中止イベント

{% apitags %}
Abort, Push
{% endapitags %}

このイベントは、プッシュ通知メッセージが Liquid の中止、サイレント時間などに基づいて中止された場合に発生します。

\`\`\`json
// プッシュ通知中止: users.messages.pushnotification.Abort

{
"abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
"abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"app_id": (required, string) Braze ID of the app this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received
"canvas_step_name": (optional, string) API ID of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) ID of the Canvas variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"device_id": (optional, string), ID of the device on which the event occurred,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"id": (required, string) unique ID of this event,
"message_variation_id": (optional, string) ID of the message variation this user received,
"message_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"platform": (required, string) platform of the device,
"send_id": (optional, string) message send ID this message belongs to,
"time": (required, int) unix timestamp at which the event happened,
"timezone": (optional, string) IANA time zone of the user at the time of the event,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}

{% api %}

## SMS メッセージ中止イベント

{% apitags %}
中止、SMS
{% endapitags %}

このイベントは、SMS メッセージが Liquid の中止、サイレント時間などに基づいて中止された場合に発生します。

\`\`\`json
// SMS 中止: users.messages.sms.Abort

{
"abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
"abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received
"canvas_step_name": (optional, string) API ID of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) ID of the Canvas variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"external_user_id": (optional, string) External user ID of the user,
"id": (required, string) globally unique ID of this event,
"message_variation_id": (optional, string) ID of the message variation this user received,
"message_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"subscription_group_id": (optional, string) ID of the subscription group targeted for this SMS message,
"time": (required, int) unix timestamp at which the event happened,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}

{% api %}

## Webhook メッセージ中止イベント

{% apitags %}
Abort,  Webhooks
{% endapitags %}

このイベントは、Webhook メッセージが Liquid の中止、サイレント時間などに基づいて中止された場合に発生します。

\`\`\`json
// Webhook 中止: users.messages.webhook.Abort

{
"abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
"abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
"campaign_name": (optional, string) name of the campaign,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_message_variation_id": (optional, string) ID of the Canvas step message variation this user received
"canvas_step_name": (optional, string) API ID of the Canvas step this event belongs to,
"canvas_variation_id": (optional, string) ID of the Canvas variation this event belongs to,
"canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"device_id": (optional, string) ID of the device on which the event occurred,
"dispatch_id": (optional, string) ID of the dispatch this message belongs to,
"external_user_id": (optional, string) External user ID of the user,
"id": (required, string) globally unique ID of this event,
"message_variation_id": (optional, string) ID of the message variation this user received,
"message_variation_name": (optional, string) name of the message variation the user is in if from a Canvas,
"send_id": (optional, string) message send ID this message belongs to,
"time": (required, int) unix timestamp at which the event happened,
"timezone": (optional, string) IANA time zone of the user at the time of the event,
"user_id": (required, string) Braze ID of the user that performed this event
}
  \`\`\`
  {% endapi %}


{% api %}

## イベント実行によるキャンバス離脱イベント

{% apitags %}
Exit, Canvas
{% endapitags %}

このイベントは、ユーザーがイベントを実行してキャンバスを離脱したときに発生します。

\`\`\`json
// キャンバス離脱実行イベント: users.canvas.exit.PerformedEvent

{
"id": (required, string) globally unique ID of this event,
"user_id": (required, string) Braze user ID of the user,
"external_user_id": (optional, string) External user ID of the user,
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"app_group_api_id": (optional, string) API ID of the workspace this user belongs to,
"time": (required, int) unix timestamp at which the event happened,
"canvas_id": (required, string) ID of the Canvas if from a Canvas,
"canvas_variation_id": (required, string) ID of the Canvas variation the user is in if from a Canvas,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_api_id": (optional, string) Braze ID of the experiment step this event belongs to,
"canvas_variation_api_id": (optional, string) API ID of the Canvas variation this event belongs to,
"canvas_step_api_id": (optional, string) API ID of the Canvas step this event belongs to
}
  \`\`\`
  {% endapi %}

{% api %}

## オーディエンス照合によるキャンバス離脱イベント

{% apitags %}
Exit, Canvas
{% endapitags %}

このイベントは、ユーザーがオーディエンスを照合してキャンバスを離脱したときに発生します。

\`\`\`json
// キャンバス離脱のオーディエンス照合: users.canvas.exit.MatchedAudience

{
"id": (required, string) globally unique ID of this event,
"user_id": (required, string) Braze user ID of the user,
"external_user_id": (optional, string) External user ID of the user,
"app_group_id": (required, string) Braze ID of the workspace this user belongs to,
"app_group_api_id": (optional, string) API ID of the workspace this user belongs to,
"time": (required, int) unix timestamp at which the event happened,
"canvas_id": (required, string) ID of the Canvas if from a Canvas,
"canvas_variation_id": (required, string) ID of the Canvas variation the user is in if from a Canvas,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"canvas_api_id": (optional, string) Braze ID of the experiment step this event belongs to,
"canvas_variation_api_id": (optional, string) API ID of the Canvas variation this event belongs to,
"canvas_step_api_id": (optional, string) API ID of the Canvas step this event belongs to
}
  \`\`\`
  {% endapi %}
  {% api %}
## 実験分割エントリイベント

{% apitags %}
Experiment Step, Canvas
{% endapitags %}

このイベントは、ユーザーがキャンバスの実験ステップパスに入ったときに発生します。

\`\`\`json
// 実験ステップの分岐パス侵入: users.canvas.experimentstep.SplitEntry

{
"id": (required, string) globally unique ID of this event,
"user_id": (required, string) Braze user ID of the user,
"external_user_id": (optional, string) External user ID of the user,
"time": (required, int) unix timestamp at which the event happened,
"canvas_id": (optional, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
"canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"experiment_step_id": (required, string) Braze ID of the experiment step this event belongs to,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"experiment_split_id": (optional, string) Braze ID of the experiment split the user enrolled in,
"experiment_split_name": (optional, string) name of the experiment split the user enrolled in,
"in_control_group": (required, boolean) whether the user was enrolled in the control group
}
  \`\`\`

{% endapi %}

{% api %}

## 実験コンバージョンイベント

{% apitags %}
Experiment Step, Canvas
{% endapitags %}

このイベントは、キャンバスの実験ステップでユーザーのコンバージョンが起きたときに発生します。

\`\`\`json
// 実験ステップでのコンバージョン: users.canvas.experimentstep.Conversion

{
"id": (required, string) globally unique ID of this event,
"user_id": (required, string) Braze user ID of the user,
"external_user_id": (optional, string) External user ID of the user,
"app_id": (optional, string) Braze ID of the app this user belongs to,
"time": (required, int) unix timestamp at which the event happened,
"canvas_id": (required, string) ID of the Canvas if from a Canvas,
"canvas_name": (optional, string) name of the Canvas,
"canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
"canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
"canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
"canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
"experiment_step_id": (optional, string) Braze ID of the experiment step this event belongs to,
"experiment_split_id": (required, string) Braze ID of the experiment split variation this user received,
"experiment_split_name": (optional, string) name of the experiment split the user enrolled in,
"conversion_behavior_index": (optional, int) index of the conversion behavior,
"conversion_behavior": (optional, string) conversion behavior
}
  \`\`\`
  {% endapi %}
  {% api %}

## プッシュ送信イベント

{% apitags %}
プッシュ、送信
{% endapitags %}

このイベントは、Braze がユーザー宛てのプッシュメッセージを処理し、Apple Push Notification Service または Fire Cloud Messaging に伝達したときに発生します。これは、プッシュがデバイスに配信されたという意味ではなく、単にメッセージが送信されたことを意味します。

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,  
  "platform": (required, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) name of the message variation the user is in if from a Canvas,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,  
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) ID of the device that we made a delivery attempt to,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device,
  "message_extras": (optional, string) key-value pairs sent with this event
}
```

#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}
{% api %}

## プッシュオープンイベント

{% apitags %}
Push, Opens
{% endapitags %}

このイベントは、ユーザーがプッシュ通知を直接クリックしてアプリケーションを開いたときに発生します。現在、プッシュオープンイベントは、厳密に言うと「オープン数の合計」ではなく「直接オープン数」を指します。キャンペーンレベルの「誘発された開封数」に表示される統計情報は、ユーザーレベルで寄与していないため、これに含まれません。

```json
// Push Notification Open: users.messages.pushnotification.Open
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "canvas_step_message_variation_id": (optional, string) API ID of the Canvas step message variation this user received,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) ID of the device that we made a delivery attempt to,
  "button_action_type": (optional, string) Action type of the push notification,
  button. One of [URI, DEEP_LINK, NONE, CLOSE]. null if not
  from a button click,
  "button_string": (optional, string) identifier (button_string) of the push notification button clicked. null if not from a button click,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}
{% api %}

## iOS フォアグラウンドのプッシュ通知イベント

{% apitags %}
プッシュ、iOS、送信
{% endapitags %}

このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、 [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨になりました。

```json
// Push Notification iOS Foreground: users.messages.pushnotification.IosForeground
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "platform": (required, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) ID of the device that we made a delivery attempt to,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}
{% api %}

## プッシュ通知のバウンス

{% apitags %}
プッシュ、送信、バウンス
{% endapitags %}

このイベントは、Apple Push Notification Service または Fire Cloud Messaging からエラーを受信した場合に発生します。これは、プッシュメッセージがバウンスされたため、ユーザーのデバイスに配信されなかったことを意味します。

```json
// Push Notification Bounce: users.messages.pushnotification.Bounce
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the bounce occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) ID of the device that we made a delivery attempt to,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}
{% api %}

## メール送信イベント

{% apitags %}
メール、送信
{% endapitags %}

このイベントは、Braze と SendGrid の間でメール送信リクエストが正常に通信されたときに発生します。ただし、これは、メールがエンドユーザーの受信トレイに受信されたことを意味しません。

```json
// Email Send: users.messages.email.Send
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "ip_pool": (optional, string) IP pool used for message sending, 
  "message_extras": (optional, string) key-value pairs sent with this event
}
```

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}


{% api %}

## メール配信イベント

{% apitags %}
Email, Delivery
{% endapitags %}

このイベントは、送信されたメールがエンドユーザーの受信トレイで正常に受信された場合に発生します。

```json
// Email Delivery: users.messages.email.Delivery
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,  
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "sending_ip": (optional, string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (optional, string) IP pool used for message sending,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email
}
```

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}

## メール開封イベント

{% apitags %}
Email, Opens
{% endapitags %}

このイベントは、ユーザーがメールを開封したときに発生します。ユーザーが複数回メールを開封すると、同じキャンペーンについて複数のイベントが生成される場合があります。

```json
// Email Open: users.messages.email.Open
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),  
  "user_agent": (optional, string) description of the user's system and browser for the event,
  "ip_pool": (optional, string) IP pool used for message sending,
  "machine_open": (optional, string) Indicator of whether the email was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (for example, "Apple" or "Google" to indicate which process made the fetch) may be added in the future.,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email,
  "is_amp": (optional, boolean) indicates that this is an AMP event,
  "device_class": (optional, string) type of device used, such as 'mobile', 'desktop', 'tablet', 'other',
  "device_os": (optional, string) the operating system used, such as 'os x', 'android', 'iOS',
  "browser": (optional, string) browser used, such as 'chrome', 'edge', 'safari',
  "device_model": (optional, string) model of device used, such as 'iPhone',
  "mailbox_provider": (optional, string) the mailbox provider
}
```

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}

## メールクリックイベント

{% apitags %}
Email, Clicks
{% endapitags %}

このイベントは、ユーザーがメールをクリックしたときに発生します。ユーザーがメールを複数回クリックしたり、メール内の異なるリンクをクリックしたりすると、同じキャンペーンについて複数のイベントが生成される場合があります。

```json
// Email Click: users.messages.email.Click
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Only included when campaign_id is present. Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "url": (optional, string) the URL that was clicked,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "user_agent": (optional, string) description of the user's system and browser for the event,
  "ip_pool": (optional, string) IP pool used for message sending,
  "link_id": (optional, string) unique value generated by Braze for the URL - null unless link aliasing is enabled,
  "link_alias": (optional, string) alias name set when the message was sent - null unless link aliasing is enabled,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email,
  "is_amp": (optional, boolean) indicates that this is an AMP event,
  "device_class": (optional, string) type of device used, such as 'mobile', 'desktop', 'tablet', 'other',
  "device_os": (optional, string) the operating system used, such as 'os x', 'android', 'iOS',
  "browser": (optional, string) browser used, such as 'chrome', 'edge', 'safari',
  "device_model": (optional, string) model of device used, such as 'iPhone',
  "mailbox_provider": (optional, string) the mailbox provider
}
```

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}

## メールバウンスイベント

{% apitags %}
Email, Bounce
{% endapitags %}

このイベントは、インターネットサービスプロバイダーがハードバウンスを返したときに発生します。ハードバウンスは、配信到達性の永続的なエラーを意味します。

```json
// Email Bounce: users.messages.email.Bounce
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "sending_ip": (optional, string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (optional, string) IP pool used for message sending (for certain bounce cases, IP pool will not be provided) ,
  "bounce_reason": (optional, string) reason for bounce provided by server,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email,
  "is_drop": (optional, boolean) indicates that this event counts as a drop event
}
```

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}

## メールソフトバウンスイベント

{% apitags %}
Email, Bounce
{% endapitags %}

このイベントは、インターネットサービスプロバイダーがソフトバウンスを返したときに発生します。ソフトバウンスは、一時的な配信到達性のエラーによりメールを配信できなかったことを意味します。

```json
// Email Soft Bounce: users.messages.email.SoftBounce
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "sending_ip": (optional, string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (optional, string) IP pool used for message sending(for certain bounce cases, IP pool will not be provided),
  "bounce_reason": (optional, string) reason for bounce provided by server,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email
}
```

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}

## メールスパムイベント

{% apitags %}
Email, Spam
{% endapitags %}

このイベントは、エンドユーザーがメールの [スパム] ボタンを押したときに発生します。Braze はこれを追跡しないため、このイベントはメールがスパムフォルダーに入れられた事実を表すものではないことに注意してください。

```json
// Email Mark As Spam: users.messages.email.MarkAsSpam
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "user_agent": (optional, string) This field is no longer used in any destination for this event and will always be empty,
  "ip_pool": (optional, string) IP pool used for message sending,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email
}
```

#### プロパティの詳細

`dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}


{% api %}

## メール配信停止イベント

{% apitags %}
Email, Subscription
{% endapitags %}

このイベントは、エンドユーザーがメールの [配信停止] をクリックしたときに発生します。

{% alert important %}
`Unsubscribe` イベントは実質的に特殊なクリックイベントであり、ユーザーが配信停止状態に変更したときではなく、ユーザーがメール内の配信停止リンク (メールの本文またはフッターにある通常の配信停止リンク、または [list-unsubscribe ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)を使用したもの) をクリックしたときに発生します。サブスクリプションの状態変更が API を介して送信された場合、Currents でイベントはトリガーされません。
{% endalert %}

```json
// Email Unsubscribe: users.messages.email.Unsubscribe
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "ip_pool": (optional, string) IP pool used for message sending
}
```
#### プロパティの詳細

`dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}

## アプリ内メッセージのインプレッションイベント

{% apitags %}
In-App Messages, Impressions
{% endapitags %}

このイベントは、ユーザーがアプリ内メッセージを表示したときに発生します。

```json
// In-App Message Impression: users.messages.inappmessage.Impression
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "card_id": (optional, string) ID of the card that was viewed,  
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "device_id": (optional, string) ID of the device on which the event occurred,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device,
  "message_extras": (optional, string) a JSON string of the tagged key-value pairs during Liquid rendering
}
```

{% alert note %}
`message_extras` フィールドは、2024 年 4 月 4 日にアクティブになります。
{% endalert %}

#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}

## アプリ内メッセージのクリックイベント

{% apitags %}
In-App Messages, Clicks
{% endapitags %}

このイベントは、ユーザーがアプリ内メッセージをクリックしたときに発生します。

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "card_id": (optional, string) ID of the card that was viewed,  
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "button_id": (optional, string) index of the button clicked if it was a button that was clicked, tracking ID of the click if the event came from an appboyBridge.logClick or brazeBridge.logClick invocation, or choice_id if the in app-message type is a simple survey,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "device_id": (optional, string) ID of the device on which the event occurred,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}


{% api %}

## Webhook 送信イベント

{% apitags %}
Webhook、送信
{% endapitags %}

このイベントは、Webhook が処理され、その Webhook に指定されたサードパーティに送信されたときに発生します。これは、リクエストが受信されたかどうかを示していないことに注意してください。

```json
// Webhook Send: users.messages.webhook.Send
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types)
  "message_extras": (optional, string) key-value pairs sent with this event
}
```
#### プロパティの詳細

- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。

{% endapi %}

{% api %}
## コンテンツカード送信イベント

{% apitags %}
コンテンツカード、送信
{% endapitags %}

このイベントは、コンテンツカードがユーザーに送信されたときに発生します。

```json
// Content Card Send: users.messages.contentcard.Send
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) ID of the content card that was sent,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "message_extras": (optional, string) key-value pairs sent with this event
}
```
#### プロパティの詳細

- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}

{% api %}
## コンテンツカードのインプレッションイベント

{% apitags %}
Content Cards, Impressions
{% endapitags %}

このイベントは、ユーザーがコンテンツカードを表示したときに発生します。

```json
// Content Card Impression: users.messages.contentcard.Impression
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) ID of the content card that was viewed/clicked/dismissed,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## コンテンツカードのクリックイベント

{% apitags %}
Content Cards, Clicks
{% endapitags %}

このイベントは、ユーザーがコンテンツカードをクリックしたときに発生します。

```json
// Content Card Click: users.messages.contentcard.Click
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) ID of the content card that was viewed/clicked/dismissed,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}


{% api %}
## コンテンツカード却下イベント

{% apitags %}
Content Cards, Dismissal
{% endapitags %}

このイベントは、ユーザーがコンテンツカードを却下したときに発生します。

```json
// Content Card Dismiss: users.messages.contentcard.Dismiss
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) ID of the content card that was viewed/clicked/dismissed,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,  
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。`iOS`ad_id` と `Android`ad_id_type` 向けのこの設定については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}


{% api %}

## SMS クリックイベント

{% apitags %}
SMS, Clicks
{% endapitags %}

このイベントは、ユーザーが SMS の短縮リンクをクリックしたときに発生します。

```json
// SMS Send: users.messages.sms.ShortLinkClick
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user targeted by short_url,
  "external_user_id": (optional, string) External ID of the user, null if short_url,
  "app_group_id": (required, string) API ID of the workspace associated with the inbound phone number,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA timezone of the user at the time of the event, null if short_url did not use user click tracking,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign if from a campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation a user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "url": (required, string) original URL contained in message that was shortened for click tracking,
  "short_url": (required, string) shortened URL that is sent to user for click tracking,
  "user_agent": (optional, string) User-Agent header of the device performing the click event,
  "user_phone_number": (optional, string) Phone number of the user that short_url was sent to
}
```
{% endapi %}
{% api %}
## SMS 送信イベント

{% apitags %}
SMS、送信
{% endapitags %}

このイベントは、ユーザーが SMS を送信したときに発生します。

```json
// SMS Send: users.messages.sms.Send
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "subscription_group_id": (optional, string) ID of the subscription group targeted for this SMS message,
  "to_phone_number": (optional, string) the number the message was sent to,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) message send ID this message belongs to,
  "category": (optional, string) If the SMS was sent as a result of auto-response to one of your global SMS keywords, the Category will be reflected here (e.g Opt-In, Opt-Out, Help)
  "message_extras": (optional, string) key-value pairs sent with this event
}
```
#### プロパティの詳細
- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。

{% endapi %}

{% api %}

## SMS から通信事業者への送信イベント

{% apitags %}
SMS, Delivery
{% endapitags %}

{% alert important %}
`CarrierSend` は、レガシーインフラストラクチャのユーザーに対してのみサポートされます。
{% endalert %}

このイベントは、SMS が通信事業者に送信されたときに発生します。

```json
// SMS Delivery: users.messages.sms.CarrierSend
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) ID of the subscription group targeted for this SMS message,
  "from_phone_number": (optional, string) the from phone number of the message (Delivered and Undelivered only),
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) message send ID this message belongs to
}
```
{% endapi %}

{% api %}

## SMS 配信イベント

{% apitags %}
SMS, Delivery
{% endapitags %}

このイベントは、SMS がユーザーの携帯電話に正常に配信されたときに発生します。

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) ID of the subscription group targeted for this SMS message,
  "from_phone_number": (optional, string) the from phone number of the message (Delivered and Undelivered only),
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) message send ID this message belongs to
}
```
{% endapi %}

{% api %}

## SMS 拒否イベント

{% apitags %}
SMS, Rejection
{% endapitags %}

このイベントは、SMS 送信が通信事業者によって拒否された場合に発生し、いくつかの理由で発生する可能性があります。このイベントと提供されたエラーコードを使用すると、SMS 配信に関する問題のトラブルシューティングに役立ちます。

```json
// SMS Rejection: users.messages.sms.Rejection
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) ID of the subscription group targeted for this SMS message,
  "from_phone_number": (optional, string) the from phone number of the message (Delivered and Undelivered only),
  "error": (optional, string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (optional, string) the provider's reason code as to why the message was not sent (Rejection and Delivery Failure events only),
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```
{% endapi %}


{% api %}

## SMS 配信失敗イベント

{% apitags %}
SMS, Delivery
{% endapitags %}

このイベントは、SMS で配信エラーが発生したときに発生します。このイベントと提供されたエラーコードを使用すると、SMS 配信に関する問題のトラブルシューティングに役立ちます。

```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "dispatch_id": (optional, string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,  
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) ID of the subscription group targeted for this SMS message,
  "error": (optional, string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (optional, string) the provider's reason code as to why the message was not sent (Rejection and Delivery Failure events only),
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) message send ID this message belongs to
}
```
{% endapi %}
{% api %}

## SMS インバウンド受信イベント

{% apitags %}
SMS, InboundReceived
{% endapitags %}

このイベントは、ユーザーの 1 人が Braze SMS サブスクリプショングループの 1 つの電話番号に SMS を送信したときに発生します。 

Braze がインバウンド SMS を受信すると、そのインバウンドメッセージがその電話番号を共有するすべてのユーザーに起因するとみなします。その結果、Braze インスタンス内の複数のユーザーが同じ電話番号を共有している場合、インバウンドメッセージごとに複数のイベントを受信する可能性があります。特定のユーザーに送信された以前のメッセージに基づいてそのユーザー ID のアトリビューションが必要な場合は、SMS 配信イベントを使用して、Braze の番号から最後にメッセージを受信したユーザー ID がインバウンド受信イベントに寄与したと見なすことができます。

このインバウンドメッセージが Braze から送信されたアウトバウンドのキャンペーンまたはキャンバスコンポーネントへの返信であることが検出された場合は、キャンペーンまたはキャンバスのメタデータもイベントに含まれます。Braze での返信とは、アウトバウンドメッセージから 4 時間以内に送信されるインバウンドメッセージとして定義されます。ただし、最後に受信したアウトバウンド SMS のアトリビューションされたキャンペーン情報には 1 分間のキャッシュがあります。

```json
// SMS Inbound Received: users.messages.sms.InboundReceive
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_group_id": (required, string) API ID of the workspace associated with the inbound phone number,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "user_phone_number": (required, string) the phone number of the user who sent the message to your Braze number,
  "subscription_group_id": (optional, string) ID of the subscription group which the phone number the user messaged belongs to,
  "inbound_phone_number": (required, string) the phone number the message was sent to,
  "action": (required, string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),
  "message_body": (required, string) the body of the message sent by the user,
  "media_urls": (optional, array of string) the media URLs sent by the user,
  "campaign_id": (optional, string) ID of the campaign if Braze identifies this inbound message is a reply to a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "message_variation_name": (optional, string) the name of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to
}
```
{% endapi %}


{% api %}

## キャンペーンのコンバージョンイベント

{% apitags %}
Campaign, Conversion
{% endapitags %}

このイベントは、キャンペーンにコンバージョンイベントとして設定されたアクションをユーザーが実行したときに発生します。

{% alert important %}
コンバージョンイベントは `conversion_behavior` フィールドにエンコードされ、コンバージョンイベントのタイプ、ウィンドウ (期間)、およびコンバージョンイベントのタイプに応じた追加情報が含まれます。`conversion_behavior_index` フィールドは、0 = A、1 = B、2 = C、3 = D のように、どのコンバージョンイベントかを表します。
{% endalert %}

```json
// Campaign Conversion Event: users.campaigns.Conversion
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (required, string) ID of the campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (required, string) ID of the message variation,
  "message_variation_name": (optional, string) the name of the message variation,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types)
  "conversion_behavior_index": (optional, int) index of the conversion behavior,
  "conversion_behavior": (optional, string) JSON-encoded string describing the conversion behavior
}
```
{% endapi %}


{% api %}

## キャンバスコンバージョンイベント

{% apitags %}
Canvas, Conversion
{% endapitags %}

このイベントは、キャンバスにコンバージョンイベントとして設定されたアクションをユーザーが実行したときに発生します。

{% alert important %}
コンバージョンイベントは `conversion_behavior` フィールドにエンコードされ、コンバージョンイベントのタイプ、ウィンドウ (期間)、およびコンバージョンイベントのタイプに応じた追加情報が含まれます。`conversion_behavior_index` フィールドは、0 = A、1 = B、2 = C、3 = D のように、どのコンバージョンイベントかを表します。
{% endalert %}

```json
// Canvas Conversion Event: users.canvas.Conversion
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "canvas_id": (required, string) ID of the Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (required, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (required, string) ID of the last step the user was sent before the conversion,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "conversion_behavior_index": (optional, int) index of the conversion behavior,
  "conversion_behavior": (optional, string) JSON-encoded string describing the conversion behavior
}
```
{% endapi %}


{% api %}

## キャンバスエントリイベント

{% apitags %}
Canvas, Entry
{% endapitags %}

このイベントは、ユーザーがキャンバスに入ったときに発生します。このイベントは、ユーザーがどのバリアントに入ったかを示します。

```json
// Canvas Entry Event: users.canvas.Entry
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "canvas_id": (required, string) ID of the Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (required, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "in_control_group": (required, boolean) whether the user was enrolled in the control group for a Canvas
}
```

{% endapi %}

{% api %}
## キャンペーンコントロールグループ登録イベント

{% apitags %}
Campaign, Entry
{% endapitags %}

このイベントは、複数のバリアントを持つキャンペーンに設定されたコントロールバリアントに、ユーザーが登録したときに発生します。このイベントは、このユーザーのチャネル送信イベントがないために生成されます。

```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) ID of the campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation,
  "message_variation_name": (optional, string) the name of the message variation,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

{% endapi %}

{% api %}

## サブスクリプションイベント

{% apitags %}
Subscription
{% endapitags %}

このイベントは、サブスクリプショングループ内のユーザーのサブスクリプション状態が変化したときに発生します。

{% alert important %}
現在、サブスクリプショングループは、メール、SMS、WhatsApp チャネルでのみ使用できます。
{% endalert %}

```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "email_address": (optional, string) email address for this user,
  "phone_number": (optional, string) phone number of the user (presented in e.164 format),
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "campaign_id": (optional, string) ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "subscription_group_id": (required, string) ID of the subscription group,
  "subscription_status": (required, string) status of the subscription after the change: 'Subscribed', 'Unsubscribed', or 'Pending Double Opt-In',
  "channel": (optional, string) either 'sms', 'email', or 'whats_app',
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "send_id": (optional, string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "state_change_source": (optional, string) Source of the state change, e.g: REST, SDK, Dashboard, Preference Center etc.
}
```

#### プロパティの詳細

`state_change_source` は、完全なソース名文字列を返します。例えば、ソース CSV のインポートでは、文字列 `CSV Import` が返されます。利用可能なソースを以下に示します。

| ソース |説明 |
| --- | --- |
| SDK | SDK エンドポイント |
| ダッシュボード | ユーザーのサブスクリプション状態がダッシュボードの [ユーザープロファイル] ページから更新されたとき |
| [サブスクリプション] ページ | ユーザーがユーザー設定センターではないメールリンクから配信停止したとき |
| REST API | REST API エンドポイント |
| CSV インポート | CSV ユーザーインポート |
| ユーザー設定センター |ユーザーがユーザー設定センターから更新されたとき |
| インバウンドメッセージ | SMS などのチャネル経由でエンドユーザーからのインバウンドメッセージによってユーザーが更新されたとき |
| 移行 | ユーザーが内部移行またはメンテナンススクリプトによって更新されたとき |
| ユーザーのマージ | ユーザーマージプロセスによってユーザーが更新されたとき |
| キャンバスユーザー更新ステップ | キャンバスユーザー更新ステップによってユーザーが更新されたとき |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

{% api %}

## グローバル状態変更イベント

{% apitags %}
Subscription
{% endapitags %}

このイベントは、ユーザーのグローバルサブスクリプション状態が変更されたときに発生します。

```json
// Global State Change: users.behaviors.subscription.GlobalStateChange
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze ID of the user with this global subscription state change,
  "external_user_id": (optional, string) External ID of the user,
  "email_address": (optional, string) User email address,
  "state_change_source": (optional, string) Source of the state change, for example, REST, SDK, Dashboard, Preference Center, etc.,
  "subscription_status": (required, string) Global subscription status: Subscribed, Unsubscribed and Opt-In,
  "channel": (optional, string) Channel: only email for now,
  "time": (required, int) 10-digit UTC time of the state change event in seconds since the epoch,
  "timezone": (optional, string) IANA timezone of the user at the time of the event,
  "app_group_id": (required, string) Braze ID of the workspace this user belongs to,
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "campaign_id": (optional, string) Braze ID of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) ID of the message variation if from a campaign,
  "canvas_id": (optional, string) Braze ID of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) ID of the Canvas step this event belongs to,
  "canvas_step_name": (optional, string) name of the Canvas step this event belongs to,
  "send_id": (optional, string) Message send ID this subscription state change action originated from
}
```

#### プロパティの詳細

`state_change_source` は、完全なソース名文字列を返します。例えば、ソース CSV のインポートでは、文字列 `CSV Import` が返されます。利用可能なソースを以下に示します。

| ソース |説明 |
| --- | --- |
| SDK | SDK エンドポイント |
| ダッシュボード | ユーザーのサブスクリプション状態がダッシュボードの [**ユーザープロファイル** ] ページから更新されたとき |
| [サブスクリプション] ページ | ユーザーがユーザー設定センターではないメールリンクから配信停止したとき |
| REST API | REST API エンドポイント |
| CSV インポート | CSV ユーザーインポート |
| ユーザー設定センター |ユーザーがユーザー設定センターから更新されたとき |
| インバウンドメッセージ | SMS などのチャネル経由でエンドユーザーからのインバウンドメッセージによってユーザーが更新されたとき |
| 移行 | ユーザーが内部移行またはメンテナンススクリプトによって更新されたとき |
| ユーザーのマージ | ユーザーのマージプロセスによってユーザーが更新されたとき |
| キャンバスユーザー更新ステップ | キャンバスユーザー更新ステップによってユーザーが更新されたとき |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
{% api %}
## アンインストールイベント

{% apitags %}
Uninstall
{% endapitags %}

このイベントは、ユーザーがアプリをアンインストールしたときに発生します。このデータを使用して、ユーザーがアプリをアンインストールしたタイミングを追跡します。これは現在、メッセージエンゲージメントイベントですが、将来はユーザー行動イベントに変更される予定です。

{% alert important %}
このイベントは、ユーザーが実際にアプリをアンインストールしたときには発生しません。その時点を正確に追跡することが不可能だからです。Braze は、アプリがユーザーのデバイスにまだ存在するかどうかを判断するために、毎日サイレントプッシュを送信します。そのサイレントプッシュのエラーが返された場合に、アプリがアンインストールされたと見なします。
{% endalert %}

```json
// Uninstall Event: users.behaviors.Uninstall
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "device_id": (optional, string) ID of the device on which the session occurred,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch
}
```

{% endapi %}
