---
nav_title: 顧客行動イベントとユーザーイベント
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集には、Braze が Currents を使用して追跡し、選択したデータウェアハウスに送信できるさまざまな顧客行動とユーザーイベントがリストされています。"
tool: Currents
search_rank: 7
---

その他のイベントの種類にアクセスする必要がある場合は、Braze の担当者に問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。必要な情報がこの記事に見つからない場合は、[メッセージエンゲージメントイベントライブラリ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/)または [Currents のサンプルデータ例](https://github.com/Appboy/currents-examples/tree/master/sample-data)を参照してください。

{% details 顧客行動とユーザーイベント構造およびプラットフォームの価値の説明 %}

### イベントの構造

この顧客行動とユーザーイベントの内訳は、一般的に顧客行動やユーザーイベントに含まれる情報のタイプを示します。開発者とビジネスインテリジェンス戦略チームは、情報の構成要素をしっかり理解したうえで、受信した Currents イベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。

![ユーザーイベントの内訳で、ユーザー固有のプロパティ、行動固有のプロパティ、およびデバイス固有のプロパティでグループ化されたリストされたプロパティを持つ購入イベントを示しています]({% image_buster /assets/img/customer_engagement_event.png %})

顧客行動およびユーザーイベントは、**ユーザー固有**のプロパティ、**行動固有**のプロパティ、および**デバイス固有**のプロパティで構成されます。

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
ストレージスキーマは、データウェアハウスのストレージパートナー（Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storageなど）に送信するフラットファイルのイベントデータに適用される。ここにリストされているいくつかのイベントと宛先の組み合わせは、まだ一般的には利用できません。さまざまなパートナーがサポートするイベントの情報については、[利用可能なパートナー]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。<br><br>さらに、Currents は 900 KB 超の過度に大きいペイロードを持つイベントをドロップすることに注意してください。
{% endalert %}
{% api %}

## カスタムイベント

{% apitags %}
カスタムイベント
{% endapitags %}

このイベントは、特定のカスタムイベントがトリガーされたときに発生します。これを使用して、ユーザーがアプリケーションでカスタムイベントを実行したタイミングを追跡します。

{% tabs %}
{% tab Mixpanel %}
```json
// [Braze Custom Event] custom event name: users.behaviors.CustomEvent

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// [Braze Custom Event] custom event name: users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "name" : "(required, string) Name of the custom event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// [Braze Custom Event] custom event name: users.behaviors.CustomEvent

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) の詳細については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。

{% endapi %}
{% api %}

## 購入イベント

{% apitags %}
購入
{% endapitags %}

このイベントは、ユーザーが購入を行ったときに発生します。このデータを使用して、ユーザーがアプリケーションで何かを購入したタイミングを追跡します。

{% alert tip %}
購入は特別なカスタムイベントであり、カスタムイベントと同様に、カスタムイベントプロパティの JSON エンコード文字列が付属しています。
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// Purchase: users.behaviors.Purchase

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// Purchase: users.behaviors.Purchase

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "price" : "(required, float) Price of the purchase",
  "product_id" : "(required, string) ID of the product purchased",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Purchase: users.behaviors.Purchase

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) の詳細については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}


{% api %}

## 初回セッションイベント

{% apitags %}
セッション
{% endapitags %}

このイベントは、ユーザーがアプリケーション内で最初のセッションを開始したときに発生します。このデータを使用して、ユーザーがいつセッションを開始したかを追跡します。

{% alert tip %}
ユーザーが最初のセッションを開始すると、`FirstSession` イベントと `SessionStart` イベントの両方がトリガーされます。
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// First Session: users.behaviors.app.FirstSession

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// First Session: users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "gender" : "(optional, string) Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) Language of the user",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// First Session: users.behaviors.app.FirstSession

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## セッション開始イベント

{% apitags %}
セッション
{% endapitags %}

このイベントは、ユーザーがセッションを開始したときに発生します。このデータを使用して、ユーザーがいつセッションを開始したかを追跡します。

{% alert tip %}
ユーザーが最初のセッションを開始すると、`FirstSession` イベントと `SessionStart` イベントの両方がトリガーされます。
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// Session Start: users.behaviors.app.SessionStart

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// Session Start: users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session Start: users.behaviors.app.SessionStart

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## セッション終了イベント

{% apitags %}
セッション
{% endapitags %}

これは、ユーザーがアプリケーションを離脱したとき、つまり現在のセッションを終了したときに発生します。このデータを使用して、セッションの終了時点をを追跡し、対応するセッション開始イベントとあわせてセッション時間の長さを計算します。

{% alert tip %}
ユーザーが最初のセッションを開始すると、`FirstSession` イベントと `SessionStart` イベントの両方がトリガーされます。
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// Session End: users.behaviors.app.SessionEnd

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// Session End: users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session End: users.behaviors.app.SessionEnd

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## ロケーションイベント

{% apitags %}
ロケーション
{% endapitags %}

このイベントは、ユーザーが特定のロケーションに移動したときにトリガーされます。これを使用して、アプリ内でロケーションイベントをトリガーするユーザーを追跡します。

{% tabs %}
{% tab Mixpanel %}
```json
// Location: users.behaviors.Location

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) Altitude of recorded location",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// Location: users.behaviors.Location

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Location: users.behaviors.Location

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) Altitude of recorded location",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細
- `ad_id`、`ad_id_type`、および `ad_tracking_enabled` については、ネイティブ SDK を通じて、iOS IDFA と Android Google 広告 ID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) の詳細については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}

{% api %}

## アトリビューションイベント

{% apitags %}
アトリビューション
{% endapitags %}

このイベントは、アプリのインストールがソースに起因する場合に発生します。これを使用して、アプリのインストール元を追跡します。

{% tabs %}
{% tab Mixpanel %}
```json
// Install Attribution: users.behaviors.InstallAttribution

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab クラウド・ストレージ %}
```json
// Install Attribution: users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Install Attribution: users.behaviors.InstallAttribution

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## ランダムバケット番号イベント

{% apitags %}
ランダムバケット番号
{% endapitags %}

このユーザーイベントは、ワークスペース内で新規ユーザーが作成されるたびに発生します。このイベントの間、新規ユーザーのそれぞれにランダムなバケット番号が割り当てられます。このバケット番号を使用して、ランダムなユーザーの一様分布セグメントを作成できます。これを使用して、ランダムバケット番号値の範囲をグループ化し、キャンペーンとキャンペーンバリアント間でパフォーマンスを比較します。

{% tabs %}
{% tab クラウド・ストレージ %}
```json
// Random Bucket Number Update: users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
この Currents イベントは「すべてのイベントコネクター」を購入した場合にのみ利用でき、ストレージイベントコネクター (i.e Amazon S3、Microsoft Azure、Google Cloud Storage) についてのみ利用できることに注意してください。
<br><br>このイベントを有効にして、ワークスペース内の既存ユーザーのランダムバケット番号の埋め戻しをスケジュールする方法については、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% endapi %}
