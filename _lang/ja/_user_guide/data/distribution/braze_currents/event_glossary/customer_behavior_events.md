---
nav_title: 顧客行動とユーザーイベント
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集には、Braze が Currents を使用して追跡し、選択したデータウェアハウスに送信できるさまざまな顧客行動とユーザーイベントがリストされています。"
tool: Currents
search_rank: 7
---

その他のイベントの種類にアクセスする必要がある場合は、Braze の担当者に問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。このページで必要なものが見つからない場合は、[メッセージ・エンゲージメント・イベント・ライブラリーや]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) [Currentsのサンプルデータ例を](https://github.com/Appboy/currents-examples/tree/master/sample-data)ご覧いただきたい。

{% details Explanation of customer behavior and user event structure and platform values %}

### イベントの構造

この顧客行動とユーザーイベントの内訳は、一般的に顧客行動やユーザーイベントに含まれる情報のタイプを示します。開発者とビジネスインテリジェンス戦略チームは、情報の構成要素をしっかり理解したうえで、受信した Currents イベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。

![ユーザーイベントの内訳は、ユーザー固有のプロパティ、行動固有のプロパティ、およびデバイス固有のプロパティによってグループ化されたリストアップされたプロパティを持つ購入イベントを示す。]({% image_buster /assets/img/customer_engagement_event.png %})

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
ストレージスキーマは、データウェアハウスのストレージパートナー（Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storageなど）に送信するフラットファイルのイベントデータに適用される。ここにリストされているいくつかのイベントと宛先の組み合わせは、まだ一般的には利用できません。さまざまなパートナーがサポートするイベントの情報については、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。<br><br>さらに、Currents は 900 KB 超の過度に大きいペイロードを持つイベントをドロップすることに注意してください。
{% endalert %}

{% api %}
## ランダムバケット番号更新イベント {#random-bucket-number-update-events}

{% apitags %}
ランダムバケット番号
{% endapitags %}

このユーザーイベントは、ワークスペース内で新規ユーザーが作成されるたびに発生します。このイベントでは、各新規ユーザーにランダムバケット番号が割り当てられ、これを使用してランダムユーザーの均一に分散されたセグメントを作成できます。これを使用して、ランダムバケット番号の値の範囲をグループ化し、キャンペーンとキャンペーンバリアント間でパフォーマンスを比較します。

{% alert important %}
この Currents イベントは「すべてのイベントコネクター」を購入した場合にのみ利用でき、ストレージイベントコネクター (Amazon S3、Microsoft Azure、Google Cloud Storage など) についてのみ利用できます。
<br><br>このイベントを有効にして、ワークスペース内の既存ユーザーのランダムバケット番号の埋め戻しをスケジュールする方法については、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## カスタムイベント {#custom-events}

{% apitags %}
カスタムイベント
{% endapitags %}

このイベントは、特定のカスタムイベントがトリガーされたときに発生します。これを使用して、ユーザーがアプリケーションでカスタムイベントを実行したタイミングを追跡します。

{% tabs %}
{% tab Amplitude %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
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
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// users.behaviors.CustomEvent

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "name" : "(required, string) Name of the custom event"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
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
{% endtabs %}

#### プロパティの詳細

- カスタムイベントの場合、ペイロードには、イベントに関連付けられている任意の[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/custom_data/custom_events#custom-event-properties) も入力されます。
- `ad_id`、`ad_id_type`、および`ad_tracking_enabled` の場合、ネイティブSDK を介してiOS IDFA およびAndroid Google アドID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の詳細については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}

{% api %}
## インストール アトリビューション イベント {#install-attribution-events}

{% apitags %}
アトリビューション
{% endapitags %}

このイベントは、アプリのインストールがソースに起因する場合に発生します。これを使用して、アプリのインストール元を追跡します。

{% tabs %}
{% tab Amplitude %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

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
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "source" : "(required, string) The source of the attribution"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## ロケーション・イベント {#location-events}

{% apitags %}
ロケーション
{% endapitags %}

このイベントは、ユーザーが特定のロケーションに移動したときにトリガーされます。これを使用して、アプリ内でロケーションイベントをトリガーするユーザーを追跡します。

{% tabs %}
{% tab Amplitude %}
```json
// Location (users.behaviors.Location)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
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
// Location (users.behaviors.Location)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Location (users.behaviors.Location)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.Location

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) [PII] Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) [PII] Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) [PII] Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `ad_id`、`ad_id_type`、および`ad_tracking_enabled` の場合、ネイティブSDK を介してiOS IDFA およびAndroid Google アドID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の詳細については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}

{% api %}
## イベント購入 {#purchase-events}

{% apitags %}
購入
{% endapitags %}

このイベントは、ユーザーが購入を行ったときに発生します。このデータを使用して、ユーザーがアプリケーションで何かを購入したタイミングを追跡します。

{% alert tip %}
購入は特別なカスタムイベントであり、カスタムイベントと同様に、カスタムイベントプロパティの JSON エンコード文字列が付属しています。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Purchase (users.behaviors.Purchase)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Purchase (users.behaviors.Purchase)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
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

{% tab Segment %}
```json
// Purchased (users.behaviors.Purchase)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.Purchase

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
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
{% endtabs %}

#### プロパティの詳細

- 購入イベントの場合、ペイロードには、イベントに関連付けられている[購入イベントプロパティ]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#purchase-properties) も入力されます。
- `ad_id`、`ad_id_type`、および`ad_tracking_enabled` の場合、ネイティブSDK を介してiOS IDFA およびAndroid Google アドID を明示的に収集する必要があります。[iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id) の詳細については、リンク先を参照してください。
- Kafka を使用して [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) データを取り込む場合は、`ad_id` 送信用のフィーチャーフリッパーを有効にするように、カスタマーサクセスマネージャーまたはアカウントマネージャーに依頼してください。
{% endapi %}

{% api %}
## ファーストセッションのイベント {#first-session-events}

{% apitags %}
セッション
{% endapitags %}

このイベントは、ユーザーがアプリケーション内で最初のセッションを開始したときに発生します。このデータを使用して、ユーザーがいつセッションを開始したかを追跡します。

{% alert tip %}
ユーザーが最初のセッションを開始すると、`FirstSession` イベントと `SessionStart` イベントの両方がトリガーされます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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
// First Session (users.behaviors.app.FirstSession)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
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

{% tab Segment %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) [DEPRECATED]",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [DEPRECATED]",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [DEPRECATED]",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) [DEPRECATED]",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## セッション終了イベント {#session-end-events}

{% apitags %}
セッション
{% endapitags %}

これは、ユーザーがアプリケーションを離脱したとき、つまり現在のセッションを終了したときに発生します。このデータを使用して、セッションの終了時点をを追跡し、対応するセッション開始イベントとあわせてセッション時間の長さを計算します。

{% tabs %}
{% tab Amplitude %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
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
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "duration" : "(optional, float) Duration of the session in seconds",
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

{% tab Segment %}
```json
// Session Ended (users.behaviors.app.SessionEnd)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "duration" : "(optional, float) Duration of the session in seconds",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## セッション開始イベント {#session-start-events}

{% apitags %}
セッション
{% endapitags %}

このイベントは、ユーザーがセッションを開始したときに発生します。このデータを使用して、ユーザーがいつセッションを開始したかを追跡します。

{% alert tip %}
ユーザーが最初のセッションを開始すると、`FirstSession` イベントと `SessionStart` イベントの両方がトリガーされます。
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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
// Session Start (users.behaviors.app.SessionStart)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
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

{% tab Segment %}
```json
// Session Started (users.behaviors.app.SessionStart)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## ライブ・アクティビティ・プッシュ・トゥ・スタート・トークン・チェンジ・イベント {#live-activity-push-to-start-token-change-events}

{% apitags %}
ライブアクティビティ、プッシュから開始トークン
{% endapitags %}

このイベントは、Braze がライブアクティビティプッシュを同期してユーザーのトークンを開始するときに発生します

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
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
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Push To Start Token Changed (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## ライブ・アクティビティ更新 トークン変更イベント {#live-activity-update-token-change-events}

{% apitags %}
ライブアクティビティ、更新トークン
{% endapitags %}

このイベントは、Braze がライブアクティビティ更新トークンをユーザと同期するときに発生します

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
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
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Update Token Changed (users.behaviors.liveactivity.UpdateTokenChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## プッシュ通知トークン状態変更イベント {#push-notification-token-state-change-events}

{% apitags %}
プッシュ、トークン状態変更
{% endapitags %}

このイベントは、プッシュトークンが挿入、更新、または削除されたときに発生します。プッシュトークンの状態を追跡するために使用します。

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
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
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Token State Changed (users.behaviors.pushnotification.TokenStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "platform" : "(optional, string) Platform of the device",
  "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
  "push_token_device_id" : "(optional, string) Device id of the push token",
  "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
  "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
  "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
  "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
}
```
{% endtab %}
{% endtabs %}

#### プロパティの詳細

- `push_token_foreground_push_disabled` フィールドは、プッシュトークンがフォアグラウンド・プッシュとバックグラウンド・プッシュのどちらを受け取ることができるかを示す。
  - ユーザーが自分のデバイスでプッシュ通知権限を明示的に許可している場合、これは`false` となり、トークンはフォアグラウンドのプッシュ通知を受け取ることができる。
  - ユーザーが自分のデバイスで明示的にプッシュ通知権限を拒否した場合、これは`true` となり、トークンはバックグラウンドプッシュ通知でのみ許可される。
  - プッシュ権限が不明な場合は空白になる。デフォルトでは、Brazeはフォアグラウンドプッシュ通知をトークンに送信しようとする。
- `push_token_provisionally_opted_in` フィールドはiOSプッシュトークンにのみ適用される。
  - [Provisional Authorization を]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push)設定している場合、暫定トークンにはこのフィールドが`true` に設定される。その他のプッシュトークンはすべて`false` となる。
- プッシュトークンがBrazeに入るたびに、そのライフサイクルイベントが記録される。`push_token_state_change_type` 、3種類のトークン変更イベント（"add"、"update"、"remove"）が記録される。以下の詳細に注目してほしい：
  - 今まで存在しなかった新しいトークンには、「add」イベントが1つインジェストされる。
  - 同じユーザーで同じトークン文字列を持つトークンを更新する場合（ゲートウェイまたは`foreground_push_disabled` 、あるいは他の「セカンダリ」フィールドが変更された）、これは同じトークンで1つの「更新」イベントをインジェストする。
  - トークンがあるユーザーから別のユーザーに移動した場合、旧ユーザーの "remove "イベントと新ユーザーの "add "イベントがインジェストされる。
  - 同じユーザーまたはデバイスが新しいトークンを生成した場合、古いトークンの "remove "イベントと新しいトークンの "add "イベントがインジェストされる。
  - トークンが（アンインストールや無効なトークンなどの理由で）削除される場合、トークンの "remove "イベントが1つインジェストされる。
{% endapi %}