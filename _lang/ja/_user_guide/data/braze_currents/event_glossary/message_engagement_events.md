---
nav_title: メッセージエンゲージメントイベント
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "この用語集には、Braze が追跡し、選択されたデータウェアハウスに Currents を使用して送信できるさまざまなメッセージエンゲージメントイベントをリストしています。"
tool: Currents
search_rank: 6
---

ストレージスキーマは、データウェアハウスストレージパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルイベントデータに適用されます。他のパートナーに適用されるスキーマについては、 [利用可能なパートナー]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。必要な情報がこの記事に見つからない場合は、 [顧客行動イベント ライブラリ]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)または [Currents サンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご覧ください。

{% details メッセージエンゲージメントイベントの構造とプラットフォームの値の説明 %}

### イベントの構造

このイベントの内訳は、メッセージエンゲージメントイベントに一般的に含まれる情報のタイプを示します。開発者とビジネスインテリジェンス戦略チームは、情報の構成要素をしっかり理解したうえで、受信した Currents イベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。

![メールの購読解除イベントを示すメッセージエンゲージメントの内訳。ユーザー固有のプロパティ、キャンペーンまたはキャンバスの追跡プロパティ、およびイベント固有のプロパティで、プロパティをグループ化してリストしています]({% image_buster /assets/img/message_engagement_event.png %})

メッセージエンゲージメントイベントは、**ユーザー固有**のプロパティ、**キャンペーン / キャンバス追跡**プロパティ、 および**イベント固有**のプロパティで構成されます。

### ユーザー ID スキーマ

ユーザーIDの命名規則に注意すること。

| Brazeスキーマ | カレントスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されたユーザーのプロファイルの一意の識別子。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### プラットフォームの値

特定のイベントは、ユーザーのデバイスのプラットフォームを示す `platform` 値を返します。
<br>次の表に、返される可能性のある値の詳細を示します。

| ユーザー デバイス | プラットフォーム値 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents は、900 KB を超える過度に大きなペイロードを持つイベントをドロップします。
{% endalert %}

{% alert note %}
キャンバスフローに関連するオブジェクトの ID は、グループ化に使用でき、[「キャンバスの詳細をエクスポートする」エンドポイントによ]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)って人間が読める名前に変換されます。
{% endalert %}

{% alert note %}
キャンペーンやキャンバスの更新後、特定のフィールドが最新の状態を表示するのに時間がかかる場合がある。これらのフィールドは以下の通りである：
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
完全な一貫性が必要な場合は、これらのフィールドの最終更新から1時間待ってからユーザーにメッセージングを送信することを推奨する。
{% endalert %}
{% api %}
## アンインストールイベント

{% apitags %}
アンインストール
{% endapitags %}

このイベントは、ユーザーがアプリをアンインストールしたときに発生します。このデータを使用して、ユーザーがアプリをアンインストールしたタイミングを追跡します。これは現在、メッセージエンゲージメントイベントですが、将来はユーザー行動イベントに変更される予定です。

{% alert important %}
このイベントは、ユーザーが実際にアプリをアンインストールしたときには発生しません。その時点を正確に追跡することが不可能だからです。Braze は、アプリがユーザーのデバイスにまだ存在するかどうかを判断するために、毎日サイレントプッシュを送信します。そのサイレントプッシュのエラーが返された場合に、アプリがアンインストールされたと見なします。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Application Uninstalls (users.behaviors.Uninstall)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Application Uninstalled (users.behaviors.Uninstall)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.behaviors.Uninstall

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## グローバルサブスクリプション状態変更イベント

{% apitags %}
Subscription
{% endapitags %}

このイベントは、Brazeが、リクエストがユーザーの現行のサブスクリプションステートを変更しない場合でも、ユーザーのグローバルサブスクリプションステートを更新するリクエストを受信したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Global Subscription State Changes (users.behaviors.subscription.GlobalStateChange)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Global Subscription State Changed (users.behaviors.subscription.GlobalStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.behaviors.subscription.GlobalStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `state_change_source` は、完全なソース名文字列を返します。例えば、ソース CSV のインポートでは、文字列 `CSV Import` が返されます。利用可能なソースを以下に示します。

| ソース | 説明 |
| --- | --- |
| SDK | SDKエンドポイントs |
| ダッシュボード | ユーザーの購読状態がダッシュボードの [**ユーザープロファイル**] ページから更新された場合 |
| サブスクリプションページ | ユーザー設定センター以外のメールを介してユーザー 配信停止が発生した場合 |
| REST API | REST APIエンドポイント |
| CSV インポート | CSVユーザーインポート |
| 環境設定センター | ユーザー設定センターからユーザーを更新した場合 |
| 受信メッセージ | SMS などのチャネルを経由するエンドユーザーからのインバウンドメッセージによってユーザが更新された場合 |
| 移行 | ユーザーが内部移行または保守スクリプトによって更新されている場合 |
| ユーザーマージ | ユーザーのマージプロセスによってユーザーが更新された場合 |
| Canvas ユーザー更新ステップ | キャンバスユーザー更新ステップによってユーザーが更新された場合 |
| プッシュトークン登録 | トークン登録プロセスによってユーザが更新された場合 |
| リスト購読解除 | ユーザーが Braze の宛先またはワンクリックリスト - 購読解除ヘッダーを使用して購読解除した場合 |
| その他 | デモまたはプロバイダの同期ジョブ、SMS およびWhatsapp イベントコールバックなど、その他のソースが含まれます |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## サブスクリプショングループの状態変更イベント

{% apitags %}
Subscription
{% endapitags %}

このイベントは、サブスクリプショングループ内のユーザーのサブスクリプション状態が変化したときに発生します。

{% alert important %}
現在、サブスクリプショングループは、メール、SMS、WhatsApp チャネルでのみ使用できます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Subscription Group State Changes (users.behaviors.subscriptiongroup.StateChange)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_group_id" : "(required, string) Subscription group API ID",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Subscription Group State Changed (users.behaviors.subscriptiongroup.StateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.behaviors.subscriptiongroup.StateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format (for example +14155552671)",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_group_id" : "(required, string) Subscription group API ID",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `state_change_source` は、完全なソース名文字列を返します。例えば、ソース CSV のインポートでは、文字列 `CSV Import` が返されます。利用可能なソースを以下に示します。

| ソース | 説明 |
| --- | --- |
| SDK | SDKエンドポイントs |
| ダッシュボード | ダッシュボードのユーザープロファイルのページからユーザーのサブスクリプションの状態が更新された場合 |
| サブスクリプションページ | ユーザー設定センター以外のメールを介してユーザー 配信停止が発生した場合 |
| REST API | REST APIエンドポイント |
| CSV インポート | CSVユーザーインポート |
| 環境設定センター | ユーザー設定センターからユーザーを更新した場合 |
| 受信メッセージ | ユーザーが更新の場合、エンドユーザーsからSMSなどのチャネルsを経由した着信メッセージ |
| 移行 | ユーザーが内部移行または保守スクリプトによって更新されている場合 |
| ユーザーマージ | ユーザー結合処理で更新した場合 |
| Canvas ユーザー更新ステップ | キャンバスユーザー更新ステップによってユーザーが更新された場合 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## キャンペーンコンバージョンイベント

{% apitags %}
キャンペーン、コンバージョン
{% endapitags %}

このイベントは、キャンペーンにコンバージョンイベントとして設定されたアクションをユーザーが実行したときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% alert important %}
コンバージョンイベントは `conversion_behavior` フィールドにエンコードされ、コンバージョンイベントのタイプ、ウィンドウ (期間)、およびコンバージョンイベントのタイプに応じた追加情報が含まれます。`conversion_behavior_index` フィールドは、0 = A、1 = B、2 = C、3 = D のように、どのコンバージョンイベントかを表します。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Conversions (users.campaigns.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Converted (users.campaigns.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.campaigns.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## キャンペーンコントロールグループ登録イベント

{% apitags %}
キャンペーン、エントリー
{% endapitags %}

このイベントは、複数のバリアントを持つキャンペーンに設定されたコントロールバリアントに、ユーザーが登録したときに発生します。このイベントは、このユーザーのチャネル送信イベントがないために生成されます。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Control Group Enrollments (users.campaigns.EnrollInControl)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Control Group Entered (users.campaigns.EnrollInControl)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.campaigns.EnrollInControl

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## キャンバス変換イベント

{% apitags %}
キャンバス、変換
{% endapitags %}

このイベントは、キャンバスにコンバージョンイベントとして設定されたアクションをユーザーが実行したときに発生します。

{% alert important %}
コンバージョンイベントは `conversion_behavior` フィールドにエンコードされ、コンバージョンイベントのタイプ、ウィンドウ (期間)、およびコンバージョンイベントのタイプに応じた追加情報が含まれます。`conversion_behavior_index` フィールドは、0 = A、1 = B、2 = C、3 = D のように、どのコンバージョンイベントかを表します。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Conversions (users.canvas.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Converted (users.canvas.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvas.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## キャンバスエントリイベント

{% apitags %}
キャンバス、エントリ
{% endapitags %}

このイベントは、ユーザーがキャンバスに入ったときに発生します。このイベントは、ユーザーがどのバリアントに入ったかを示します。

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Entries (users.canvas.Entry)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Entered (users.canvas.Entry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvas.Entry

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## マッチオーディエンスイベントの終了

{% apitags %}
出口、キャンバス
{% endapitags %}

このイベントは、ユーザーがオーディエンスを照合してキャンバスを離脱したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Matched Audiences (users.canvas.exit.MatchedAudience)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Matched Audience (users.canvas.exit.MatchedAudience)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvas.exit.MatchedAudience

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## プラットフォーム離脱イベントのイベント

{% apitags %}
出口、キャンバス
{% endapitags %}

このイベントは、ユーザーがイベントを実行してキャンバスを離脱したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Performed Events (users.canvas.exit.PerformedEvent)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Performed Event (users.canvas.exit.PerformedEvent)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvas.exit.PerformedEvent

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 実験ステップコンバージョンイベント

{% apitags %}
実験ステップ、キャンバス
{% endapitags %}

このイベントは、キャンバスの実験ステップでユーザーのコンバージョンが起きたときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Step Conversions (users.canvas.experimentstep.Conversion)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Step Converted (users.canvas.experimentstep.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvas.experimentstep.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 実験分割エントリイベント

{% apitags %}
実験ステップ、キャンバス
{% endapitags %}

このイベントは、ユーザーがキャンバスの実験ステップパスに入ったときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event_properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Split Entries (users.canvas.experimentstep.SplitEntry)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Split Entered (users.canvas.experimentstep.SplitEntry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvas.experimentstep.SplitEntry

{
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## キャンバスのStep Progression イベント

{% apitags %}
キャンバスステップ、進行
{% endapitags %}

このイベントは、ユーザーがキャンバスのステップを進み、何らかの結果を得たときに発生する。このイベントは、ステップの開始または終了時には発生しないことに注意してください。現在、分岐ステップ (オーディエンスパス、条件分岐、アクションパス、実験) と（オーディエンスパス、条件分岐、アクションパス、エクスペリメント）と Advance の結果のみがステップの進行イベントを生成します。

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Step Progressions (users.canvasstep.Progression)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
          "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
          "next_step_id" : "(optional, string) API ID of the next step in the canvas",
          "progression_type" : "(required, string) What type of step progression event this is",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.canvasstep.Progression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
  "next_step_id" : "(optional, string) API ID of the next step in the canvas",
  "progression_type" : "(required, string) What type of step progression event this is",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## バナー中止イベント

{% apitags %}
Banner, Abort
{% endapitags %}

このイベントは、予定されていたバナーメッセージが何らかの理由で中断された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Aborts (users.messages.banner.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Aborted (users.messages.banner.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.banner.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## バナークリックイベント

{% apitags %}
Banner, Click
{% endapitags %}

このイベントは、ユーザーがバナーをクリックしたときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Banner Click (users.messages.banner.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Click (users.messages.banner.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Clicks (users.messages.banner.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Clicked (users.messages.banner.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.banner.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## バナーインプレッションイベント

{% apitags %}
Banner, Impressions
{% endapitags %}

このイベントは、ユーザーがバナーを表示したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Impressions (users.messages.banner.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Viewed (users.messages.banner.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.banner.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## コンテンツカードアボートイベント

{% apitags %}
Abort, Content Cards
{% endapitags %}

このイベントは、コンテンツカードのメッセージが Liquid の中止などに基づいて中止された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Aborts (users.messages.contentcard.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Aborted (users.messages.contentcard.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.contentcard.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## コンテンツカードのクリックイベント

{% apitags %}
コンテンツカード、クリック
{% endapitags %}

このイベントは、ユーザーがコンテンツカードをクリックしたときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Clicks (users.messages.contentcard.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Clicked (users.messages.contentcard.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.contentcard.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## コンテンツカード却下イベント

{% apitags %}
コンテンツカード、解雇
{% endapitags %}

このイベントは、ユーザーがコンテンツカードを却下したときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Dismisses (users.messages.contentcard.Dismiss)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Dismissed (users.messages.contentcard.Dismiss)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.contentcard.Dismiss

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## コンテンツカードインプレッションイベント

{% apitags %}
コンテンツカード、インプレッション
{% endapitags %}

このイベントは、ユーザーがコンテンツカードを表示したときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Impressions (users.messages.contentcard.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Viewed (users.messages.contentcard.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.contentcard.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## コンテンツカード送信イベント

{% apitags %}
コンテンツカード、送信
{% endapitags %}

このイベントは、コンテンツカードがユーザーに送信されたときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Sends (users.messages.contentcard.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Sent (users.messages.contentcard.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.contentcard.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、または国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}

{% api %}
## メールアボートイベント

{% apitags %}
Abort, Email
{% endapitags %}

このイベントは、メールメッセージが Liquid の中止などに基づいて中止された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Email Abort (users.messages.email.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Abort (users.messages.email.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Aborts (users.messages.email.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Aborted (users.messages.email.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## メールバウンスイベント

{% apitags %}
メール、バウンス
{% endapitags %}

このイベントは、インターネットサービスプロバイダーがハードバウンスを返したときに発生します。ハードバウンスとは、永続的な配信の失敗です。

{% tabs %}
{% tab Amplitude %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Bounces (users.messages.email.Bounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Bounced (users.messages.email.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Bounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## Eメールクリックイベント

{% apitags %}
電子メール、クリック
{% endapitags %}

このイベントは、ユーザーがメールをクリックしたときに発生します。ユーザーがメールを複数回クリックしたり、メール内の異なるリンクをクリックしたりすると、同じキャンペーンについて複数のイベントが生成される場合があります。

{% tabs %}
{% tab Amplitude %}
```json
// Email Click (users.messages.email.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Click (users.messages.email.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Clicks (users.messages.email.Click)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
          "link_alias" : "(optional, string) Alias associated with this link ID",
          "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Link Clicked (users.messages.email.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_url" : "(optional, string) URL that the user clicked on",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
  "link_alias" : "(optional, string) Alias associated with this link ID",
  "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(optional, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## メール延期イベント

{% apitags %}
電子メール、延期
{% endapitags %}

このイベントは、インターネットサービスプロバイダがEメールをハードバウンスされていないEメールアドレスにすぐに配信せず、BrazeがEメールを最大72時間再試行した場合に発生します。遅延の典型的な理由には、受信トレイプロバイダーからのレピュテーションベースのメールボリュームレート制限、一時的な接続の問題、受信者のメールボックスがいっぱいになった、またはDNS エラーなどがあります。

{% tabs %}
{% tab Amplitude %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deferrals (users.messages.email.Deferral)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "attempt_count" : "(optional, int) Number of attempts made to send the message",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "recipient_domain" : "(optional, string) Receipient's email domain",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Deferred (users.messages.email.Deferral)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Deferral

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "attempt_count" : "(optional, int) Number of attempts made to send the message",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "recipient_domain" : "(optional, string) Receipient's email domain",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## メール配信イベント

{% apitags %}
電子メール、配信
{% endapitags %}

このイベントは、送信されたメールがエンドユーザーの受信トレイで正常に受信された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deliveries (users.messages.email.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Delivered (users.messages.email.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## スパムメールとしてマークするイベント

{% apitags %}
電子メール、スパム
{% endapitags %}

このイベントは、エンドユーザーがメールの [スパム] ボタンを押したときに発生します。Braze はこれを追跡しないため、このイベントはメールがスパムフォルダーに入れられた事実を表すものではないことに注意してください。

{% tabs %}
{% tab Amplitude %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Marks As Spam (users.messages.email.MarkAsSpam)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Marked as Spam (users.messages.email.MarkAsSpam)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.MarkAsSpam

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## メールオープンイベント

{% apitags %}
メール、オープン
{% endapitags %}

このイベントは、ユーザーがメールを開封したときに発生します。ユーザーが複数回メールを開封すると、同じキャンペーンについて複数のイベントが生成される場合があります。

{% alert important %}
メール開封イベントのフィールド `device_model` と`mailbox_provider` が空であることは、既知の動作です。現時点ではこれは無視できます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Open (users.messages.email.Open)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Open (users.messages.email.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Opens (users.messages.email.Open)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Opened (users.messages.email.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Open

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## メール送信イベント

{% apitags %}
メール、送信
{% endapitags %}

このイベントは、Braze と SendGrid の間でメール送信リクエストが正常に通信されたときに発生します。ただし、これは、メールがエンドユーザーの受信トレイに受信されたことを意味しません。

{% tabs %}
{% tab Amplitude %}
```json
// Email Send (users.messages.email.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Send (users.messages.email.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Sends (users.messages.email.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Sent (users.messages.email.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}

{% api %}
## メールソフトバウンスイベント

{% apitags %}
メール、バウンス
{% endapitags %}

このイベントは、インターネットサービスプロバイダーがソフトバウンスを返したときに発生します。ソフトバウンスは、一時的な配信到達性のエラーによりメールを配信できなかったことを意味します。

{% tabs %}
{% tab Amplitude %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Soft Bounces (users.messages.email.SoftBounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Soft Bounced (users.messages.email.SoftBounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.SoftBounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## メール配信停止イベント

{% apitags %}
メール、サブスクリプション
{% endapitags %}

このイベントは、エンドユーザーがメールの [配信停止] をクリックしたときに発生します。

{% alert important %}
`Unsubscribe` イベントは実質的に特殊なクリックイベントであり、ユーザーが配信停止状態に変更したときではなく、ユーザーがメール内の配信停止リンク (メールの本文またはフッターにある通常の配信停止リンク、または [list-unsubscribe ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)を使用したもの) をクリックしたときに発生します。サブスクリプションの状態の変更が API またはカスタム (Braze 以外) サブスクリプション解除リンク経由で送信された場合、Currents ではイベントはトリガーされません。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Unsubscribes (users.messages.email.Unsubscribe)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Unsubscribed (users.messages.email.Unsubscribe)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.email.Unsubscribe

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。
{% endapi %}

{% api %}
## フィーチャーフラグ実験のインプレッションイベント

{% apitags %}
FeatureFlags, インプレッション
{% endapitags %}

ユーザーが機能を操作する機会があった場合、または機能が無効になっているとき (AB テストのコントロールグループの場合) にユーザーが操作した可能性がある場合には、常にこのイベントが発生します。

フィーチャーフラグのインプレッションは、1セッションにつき1回のみ記録されます。


{% tabs %}
{% tab Amplitude %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Feature Flag Experiment Impressions (users.messages.featureflag.Impression)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Feature Flag Experiment Impressed (users.messages.featureflag.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.featureflag.Impression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## アプリ内メッセージの中止イベント

{% apitags %}
In-App Messages, Abort
{% endapitags %}

このイベントは、最初にスケジュールされたアプリ内メッセージが中止されたときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Aborts (users.messages.inappmessage.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Aborted (users.messages.inappmessage.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.inappmessage.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "carrier" : "(optional, string) Carrier of the device",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "version" : "(required, string) Which version of in-app message, legacy or triggered"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## アプリ内メッセージクリックイベント

{% apitags %}
アプリ内メッセージ、クリック
{% endapitags %}

このイベントは、ユーザーがアプリ内メッセージをクリックしたときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Clicks (users.messages.inappmessage.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Clicked (users.messages.inappmessage.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.inappmessage.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## アプリ内メッセージのインプレッションイベント

{% apitags %}
アプリ内メッセージ、印象
{% endapitags %}

このイベントは、ユーザーがアプリ内メッセージを表示したときに発生します。

{% alert note %}
`dispatch_id` は非推奨であり、次の Currents リリースでは削除されます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Impressions (users.messages.inappmessage.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Viewed (users.messages.inappmessage.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.inappmessage.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## ライブアクティビティの結果イベント

{% apitags %}
ライブアクティビティ、結果
{% endapitags %}

このイベントは、Braze がサードパーティプロバイダから応答を受信したときに発生します(e.g)。APN) ライブアクティビティ送信後

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Outcomes (users.messages.liveactivity.Outcome)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.liveactivity.Outcome

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## ライブアクティビティ送信イベント

{% apitags %}
ライブアクティビティ、センド
{% endapitags %}

このイベントは、Braze バックエンドがライブアクティビティに関するリクエストをプロバイダーに対して行ったときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Sends (users.messages.liveactivity.Send)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Sent (users.messages.liveactivity.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.liveactivity.Send

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## プッシュ通知アボートイベント

{% apitags %}
Abort, Push
{% endapitags %}

このイベントは、プッシュ通知メッセージが Liquid の中止などに基づいて中止された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Aborts (users.messages.pushnotification.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Aborted (users.messages.pushnotification.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.pushnotification.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## プッシュ通知バウンスイベント

{% apitags %}
プッシュ、送信、バウンス
{% endapitags %}

このイベントは、Apple Push Notification Service または Fire Cloud Messaging からエラーを受信した場合に発生します。これは、プッシュメッセージがバウンスされたため、ユーザーのデバイスに配信されなかったことを意味します。

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Bounces (users.messages.pushnotification.Bounce)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Bounced (users.messages.pushnotification.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.pushnotification.Bounce

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}

{% api %}
## プッシュ通知iOS フォアグラウンドオープンイベント

{% apitags %}
プッシュ、iOS、送信
{% endapitags %}

このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、 [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨になりました。

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Ios Foreground Push Opened (users.messages.pushnotification.IosForeground)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.pushnotification.IosForeground

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## プッシュ通知オープンイベント

{% apitags %}
プッシュ、オープン
{% endapitags %}

このイベントは、ユーザーがプッシュ通知を直接クリックしてアプリケーションを開いたときに発生します。現在、プッシュオープンイベントは、厳密に言うと「オープン数の合計」ではなく「直接オープン数」を指します。キャンペーンレベルの「誘発された開封数」に表示される統計情報は、ユーザーレベルで寄与していないため、これに含まれません。

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Opens (users.messages.pushnotification.Open)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Tapped (users.messages.pushnotification.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.pushnotification.Open

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_action_type" : "(optional, string) Action type of the push notification button, null if not from a button click. One of ['uri', 'deep_link', 'none', 'close']",
  "button_string" : "(optional, string) Identifier (button_string) of the push notification button clicked. null if not from a button click",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
{% endapi %}

{% api %}
## プッシュ通知送信イベント

{% apitags %}
プッシュ、送信
{% endapitags %}

このイベントは、Braze がユーザー宛てのプッシュメッセージを処理し、Apple Push Notification Service または Fire Cloud Messaging に伝達したときに発生します。これは、プッシュがデバイスに配信されたという意味ではなく、単にメッセージが送信されたことを意味します。

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Sends (users.messages.pushnotification.Send)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Sent (users.messages.pushnotification.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.pushnotification.Send

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) および[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の設定について詳しく説明します。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込んでいる場合は、カスタマーサクセスマネージャーに連絡して、`ad_id` の送信を有効にしてください。
- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}

{% api %}
## SMSアボートイベント

{% apitags %}
中止、SMS
{% endapitags %}

このイベントは、SMS メッセージが Liquid の中止などに基づいて中止された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Aborts (users.messages.sms.Abort)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Aborted (users.messages.sms.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMSキャリア送信イベント

{% apitags %}
SMS、送信
{% endapitags %}

このイベントは、SMS が通信事業者に送信されたときに発生します。

{% alert important %}
`CarrierSend` は、レガシーインフラストラクチャのユーザーに対してのみサポートされます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Carrier Sends (users.messages.sms.CarrierSend)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Sent to Carrier (users.messages.sms.CarrierSend)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.CarrierSend

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS 配信イベント

{% apitags %}
SMS、配信
{% endapitags %}

このイベントは、SMSがユーザーの携帯電話に正常に配信されたときに発生する。

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Deliveries (users.messages.sms.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivered (users.messages.sms.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS 配信失敗イベント

{% apitags %}
SMS、配信
{% endapitags %}

このイベントは、SMS で配信エラーが発生したときに発生します。このイベントと提供されたエラーコードを使用すると、SMS 配信に関する問題のトラブルシューティングに役立ちます。

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Delivery Failures (users.messages.sms.DeliveryFailure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivery Failed (users.messages.sms.DeliveryFailure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.DeliveryFailure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS インバウンド受信イベント

{% apitags %}
SMS、受信済み
{% endapitags %}

このイベントは、ユーザーの 1 人が Braze SMS サブスクリプショングループの 1 つの電話番号に SMS を送信したときに発生します。

Braze がインバウンド SMS を受信すると、そのインバウンドメッセージがその電話番号を共有するすべてのユーザーに起因するとみなします。その結果、Braze インスタンス内の複数のユーザーが同じ電話番号を共有している場合、インバウンドメッセージごとに複数のイベントを受信する可能性があります。特定のユーザーに送信された以前のメッセージに基づいてそのユーザー ID のアトリビューションが必要な場合は、SMS 配信イベントを使用して、Braze の番号から最後にメッセージを受信したユーザー ID がインバウンド受信イベントに寄与したと見なすことができます。

このインバウンドメッセージが Braze から送信されたアウトバウンドのキャンペーンまたはキャンバスコンポーネントへの返信であることが検出された場合は、キャンペーンまたはキャンバスのメタデータもイベントに含まれます。Braze での返信とは、アウトバウンドメッセージから 4 時間以内に送信されるインバウンドメッセージとして定義されます。ただし、最後に受信したアウトバウンド SMS のアトリビューションされたキャンペーン情報には 1 分間のキャッシュがあります。


{% tabs %}
{% tab Amplitude %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS拒否イベント

{% apitags %}
SMS、拒否
{% endapitags %}

このイベントは、SMS 送信が通信事業者によって拒否された場合に発生し、いくつかの理由で発生する可能性があります。このイベントと提供されたエラーコードを使用すると、SMS 配信に関する問題のトラブルシューティングに役立ちます。

{% tabs %}
{% tab Amplitude %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Rejections (users.messages.sms.Rejection)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Rejected (users.messages.sms.Rejection)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.Rejection

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS 送信イベント

{% apitags %}
SMS、送信
{% endapitags %}

このイベントは、ユーザーが SMS を送信したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// SMS Send (users.messages.sms.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Send (users.messages.sms.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Sends (users.messages.sms.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Sent (users.messages.sms.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}

{% api %}
## SMS ショートリンククリックイベント

{% apitags %}
SMS、クリック
{% endapitags %}

このイベントは、ユーザーが SMS の短縮リンクをクリックしたときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Short Link Clicks (users.messages.sms.ShortLinkClick)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Short Link Clicked (users.messages.sms.ShortLinkClick)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.sms.ShortLinkClick

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook 中止イベント

{% apitags %}
中止、Webhook
{% endapitags %}

このイベントは、Webhook メッセージが Liquid の中止などに基づいて中止された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Aborts (users.messages.webhook.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Aborted (users.messages.webhook.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.webhook.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook 失敗イベント

{% apitags %}
Failure, Webhooks
{% endapitags %}

このイベントは、Webhook メッセージが配信されたが、エンドポイントからのエラー応答で失敗した場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Failures (users.messages.webhook.Failure)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "content_length" : "(optional, int) Content length of the response",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
          "host" : "(optional, string) The host of the webhook URL that returned a failure response",
          "http_status_code" : "(optional, int) HTTP status code of the response",
          "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "raw_response" : "(optional, string) Truncated raw response from endpoint",
          "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
          "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
          "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Failed (users.messages.webhook.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.webhook.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_length" : "(optional, int) Content length of the response",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "host" : "(optional, string) The host of the webhook URL that returned a failure response",
  "http_status_code" : "(optional, int) HTTP status code of the response",
  "id" : "(required, string) Globally unique ID for this event",
  "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "raw_response" : "(optional, string) Truncated raw response from endpoint",
  "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
  "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook 送信イベント

{% apitags %}
Webhook、送信
{% endapitags %}

このイベントは、Webhook が処理され、その Webhook に指定されたサードパーティに送信されたときに発生します。これは、リクエストが受信されたかどうかを示していないことに注意してください。

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Sends (users.messages.webhook.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Sent (users.messages.webhook.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.webhook.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `message_extras` を使用すると、Connected Content からのダイナミックなデータ、カスタム属性 (言語、または国など)、およびキャンバスエントリのプロパティを使用して、送信イベントに注釈を付けることができます。詳細については、[Message extras]({{site.baseurl}}/message_extras_tag/) を参照してください。
{% endapi %}

{% api %}
## WhatsApp 中止イベント

{% apitags %}
WhatsApp、中止
{% endapitags %}

このイベントは、WhatsApp メッセージが Liquid の中止などに基づいて中止された場合に発生します。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Aborts (users.messages.whatsapp.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Aborted (users.messages.whatsapp.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp 追跡リンククリックイベント

{% apitags %}
WhatsApp, Click
{% endapitags %}

このイベントは、ユーザがリンクのドメインがクリック追跡ドメインに一致するWhatsAppメッセージのリンクまたはボタンをクリックしたときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "timezone" : "(optional, string) Time zone of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Tracked Link Clicks (users.messages.whatsapp.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Tracked Link Clicked (users.messages.whatsapp.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp 配信イベント

{% apitags %}
WhatsApp、配信
{% endapitags %}

このイベントは、送信された WhatsApp メッセージがエンドユーザーデバイスに正常に着信したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Deliveries (users.messages.whatsapp.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Delivered (users.messages.whatsapp.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp 障害イベント

{% apitags %}
WhatsApp、失敗
{% endapitags %}

このイベントは、WhatsApp がユーザーにメッセージを配信できないときに発生します。ハードバウンスとは、永続的な配信の失敗です。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Failures (users.messages.whatsapp.Failure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(required, string) Error code from WhatsApp",
          "provider_error_title" : "(required, string) Description of error from WhatsApp",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Failed (users.messages.whatsapp.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(required, string) Error code from WhatsApp",
  "provider_error_title" : "(required, string) Description of error from WhatsApp",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp 受信イベント

{% apitags %}
WhatsApp、インバウンド受信
{% endapitags %}

このイベントは、ユーザーの 1 人が Braze WhatsApp サブスクリプショングループのいずれかの電話番号に WhatsApp メッセージを送信したときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "quick_reply_text" : "(optional, string) Text of button pressed by the user",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(optional, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "quick_reply_text" : "(optional, string) Text of button pressed by the user",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp 読み取りイベント

{% apitags %}
WhatsApp、既読
{% endapitags %}

このイベントは、WhatsApp メッセージがエンドユーザーによって既読になったときに発生します。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Reads (users.messages.whatsapp.Read)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.Read

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp 送信イベント

{% apitags %}
WhatsApp、送信
{% endapitags %}

このイベントは、Braze と WhatsApp の間で送信リクエストが正常に通信されたときに発生します。ただし、これはメッセージがエンドユーザーによって受信されたことを意味しません。

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Sends (users.messages.whatsapp.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Sent (users.messages.whatsapp.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// users.messages.whatsapp.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
