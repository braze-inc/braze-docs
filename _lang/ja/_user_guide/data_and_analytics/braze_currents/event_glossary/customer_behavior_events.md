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

{% details Explanation of customer behavior and user event structure and platform values %}

### イベントの構造 

この顧客行動とユーザーイベントの内訳は、一般的に顧客行動やユーザーイベントに含まれる情報のタイプを示します。開発者とビジネスインテリジェンス戦略チームは、情報の構成要素をしっかり理解したうえで、受信した Currents イベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。 

![Breakdown of a user event showing a purchase event with the listed properties grouped by user-specific properties, behavior-specific properties, and device-specific properties]({% image_buster /assets/img/customer_engagement_event.png %})

顧客行動およびユーザーイベントは、**ユーザー固有**のプロパティ、**行動固有**のプロパティ、および**デバイス固有**のプロパティで構成されます。 

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
上記のスキーマは、弊社がデータウェアハウスパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルのイベントデータにのみ適用され、Segment のコネクターでは使用できないことに注意してください。他のパートナーに適用されるスキーマについては、 [利用可能なパートナー]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) のリストを参照し、それぞれのページを確認してください。<br><br>さらに、Currents は 900 KB 超の過度に大きいペイロードを持つイベントをドロップすることに注意してください。 

{% endalert %}
{% api %}

## カスタムイベント

{% apitags %}
カスタムイベント
{% endapitags %}

このイベントは、特定のカスタムイベントがトリガーされたときに発生します。これを使用して、ユーザーがアプリケーションでカスタムイベントを実行したタイミングを追跡します。

```json
// Custom Event: users.behaviors.CustomEvent
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "name": (required, string) name of the custom event,
  "properties": (required, string) JSON encoded string of the properties for this event,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```

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

```json
// Purchase Event: users.behaviors.Purchase
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "product_id": (required, string) ID of the product purchased,
  "price": (required, float) price of the purchase,
  "currency": (required, string) three letter alpha ISO 4217 currency code,
  "properties": (required, string) JSON encoded string of the custom properties for this event,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
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

```json
// Session Start: users.behaviors.app.FirstSession
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "session_id": (required, string) ID of the session,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) ID of the device on which the session occurred,
  "gender": (optional, string) gender of the user (This field has been deprecated and will always return null),
  "country": (optional, string) country of the user (This field has been deprecated and will always return null),
  "language": (optional, string) language of the user (This field has been deprecated and will always return null),
  "sdk_version": (optional, string) version of the Braze SDK in use during the session (This field has been deprecated and will always return null)
}
```
{% endapi %}

{% api %}

## セッション開始イベント

{% apitags %}
セッション
{% endapitags %}

このイベントは、ユーザーがセッションを開始したときに発生します。このデータを使用して、ユーザーがセッションを開始した時点を追跡します。

{% alert tip %}
ユーザーが最初のセッションを開始すると、`FirstSession` イベントと `SessionStart` イベントの両方がトリガーされます。
{% endalert %}

```json
// Session Start: users.behaviors.app.SessionStart
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "session_id": (required, string) ID of the session,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) ID of the device on which the session occurred
}
```

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

```json
// Session End: users.behaviors.app.SessionEnd
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "duration": (optional, float) seconds session lasted,
  "session_id": (required, string) ID of the session,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) ID of the device on which the session occurred
}
```
{% endapi %}

{% api %}

## ロケーションイベント

{% apitags %}
ロケーション
{% endapitags %}

このイベントは、ユーザーが特定のロケーションに移動したときにトリガーされます。これを使用して、アプリ内でロケーションイベントをトリガーするユーザーを追跡します。

```json
// Location Event: users.behaviors.Location
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) ID for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "latitude": (required, float) latitude of recorded location,
  "longitude": (required, float) longitude of recorded location,
  "altitude": (optional, float) altitude of recorded location,
  "ll_accuracy": (optional, float) latitude/longitude accuracy of recorded location,
  "alt_accuracy": (optional, float) altitude accuracy of recorded location,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) ID of the device on which the event occurred,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
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

```json
// Install Attribution Event: users.behaviors.InstallAttribution
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "source": (required, string) the source of the attribution
}
```

{% endapi %}

{% api %}

## ランダムバケット番号イベント

{% apitags %}
ランダムバケット番号
{% endapitags %}

このユーザーイベントは、ワークスペース内で新規ユーザーが作成されるたびに発生します。このイベントの間、新規ユーザーのそれぞれにランダムなバケット番号が割り当てられます。このバケット番号を使用して、ランダムなユーザーの一様分布セグメントを作成できます。これを使用して、ランダムバケット番号値の範囲をグループ化し、キャンペーンとキャンペーンバリアント間でパフォーマンスを比較します。 

```json
// Random Bucket Number Event: users.RandomBucketNumberUpdate
{
  "id": (required, string) unique ID of this event,
  "app_group_id": (required, string) AppGroup API ID,
  "user_id": (required, string) Braze user ID of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) UTC time of the event in milliseconds since the epoch,
  "random_bucket_number": (required, int) new random bucket number
  "prev_random_bucket_number":  (optional, int) old random bucket number, optional
}
```

{% alert important %}
この Currents イベントは「すべてのイベントコネクター」を購入した場合にのみ利用でき、ストレージイベントコネクター (Amazon S3、Microsoft Azure、Google Cloud Storage) についてのみ利用できることに注意してください。
<br><br>このイベントを有効にして、ワークスペース内の既存ユーザーのランダムバケット番号の埋め戻しをスケジュールする方法については、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% endapi %}
