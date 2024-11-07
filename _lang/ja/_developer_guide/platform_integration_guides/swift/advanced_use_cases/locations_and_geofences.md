---
nav_title: 位置情報とジオフェンス
article_title: iOS の位置情報とジオフェンス
platform: Swift
page_order: 4
description: "このリファレンス記事では、Swift SDK に位置情報とジオフェンスを実装する方法について説明します。"
Tool:
  - Location

---

# 位置情報とジオフェンス

> この記事では、iOS SDK 統合用のジオフェンスの設定について説明します。ジオフェンスは、一部の Braze パッケージでのみ使用できます。最初に、Braze カスタマーサクセスマネージャーに連絡してください。

Braze のリアルタイム位置情報サービスの中核となるのが、[ジオフェンス]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences)の概念です。ジオフェンスは、緯度と経度を半径と組み合わせて表し、地球上の特定の位置の周りを円で囲んだ仮想的な地理的領域です。

{% alert important %}
iOS 14以降、おおよその位置情報の提供許可を選択したユーザーについては、ジオフェンスの信頼性が低下しました。
{% endalert %}

## ステップ1:バックグラウンドのプッシュを有効にする

ジオフェンスの同期戦略を最大限に活用するには、標準のプッシュ統合を完了することに加えて、 [サイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)を有効にする必要があります。

## ステップ 2:Braze の位置情報サービスを有効にする
Braze の位置情報サービスは、SDK を介して[有効にする必要があります](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)。これらはデフォルトでは有効になっていません。

## ステップ3: ジオフェンスを有効にする

ジオフェンスを有効にするには、[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) インスタンスを初期化する `configuration` オブジェクトで `location.geofencesEnabled` を `true` に設定します。その他の `location` 設定オプションは[こちら](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class)で確認できます。
{% tabs %}
{% tab SWIFT %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### バックグラウンドレポート用のジオフェンスの設定

デフォルトでは、ジオフェンスは、アプリがフォアグラウンドにある場合、または `Always` 権限 (すべてのアプリケーション状態を監視する権限) を持つ場合にのみ監視されます。

ただし、`Background Mode -> Location updates` 機能を Xcode プロジェクトに追加し、`allowBackgroundGeofenceUpdates` を有効にすることで、アプリがバックグラウンドにあるとき、または `When In Use` 権限があるときに、ジオフェンスイベントを監視するように選択できます。これにより、Braze は位置情報の更新を継続的に監視することで、アプリの「使用中」状態を拡張できます。

`allowBackgroundGeofenceUpdates` は、アプリがバックグラウンドにある場合にのみ機能します。再度開かれると、既存のバックグラウンド処理が一時停止されるため、フォアグラウンド処理を優先することができます。

{% alert important %}
バッテリーの消耗やレート制限を防ぐには、必ず`distanceFilter` をアプリ固有のニーズに合った値に設定してください。`distanceFilter` をより高い値に設定すると、アプリがユーザーの場所を要求しすぎないようにします。
{% endalert %}

## ステップ 4:Braze のバックグラウンドプッシュを確認する

Braze では、バックグラウンドプッシュ通知を使用してジオフェンスがデバイスと同期されます。[サイレントプッシュの無視]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/)に関する記事に従って、Braze のジオフェンス同期通知を受信したときにアプリケーションで不要なアクションが実行されないようにします。

## ステップ5:位置情報の使用状況を説明する文字列を Info.plist に追加する

アプリケーションで位置情報を追跡する必要がある理由の説明を含む `String` 値が含まれる `info.plist` に、キー `NSLocationAlwaysUsageDescription`、`NSLocationAlwaysAndWhenInUseUsageDescription` または `NSLocationWhenInUseUsageDescription` を追加します。

この説明は、システムの位置情報プロンプトで権限がリクエストされ、ユーザーに位置情報の追跡の利点を明確に説明する必要がある場合に表示されます。

## ステップ 6: ユーザーに権限をリクエストする

ユーザーから承認をリクエストする場合、[`When In Use`](#when-in-use) または[`Always`](#always) 承認をリクエストできます。

### 使用時

`When In Use` 権限を要求するには、`requestWhenInUseAuthorization()` メソッドを使用します。

{% tabs %}
{% tab SWIFT %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endtab %}
{% endtabs %}

### 常に

デフォルトでは、`requestAlwaysAuthorization()` はアプリに `When In Use` 権限のみを付与し、しばらく経過した後に、`Always` 権限をユーザーにもう一度要求します。ただし、まず `requestWhenInUseAuthorization()` を呼び出し、最初の `When In Use` 権限を受け取った後に `requestAlwaysAuthorization()` を呼び出すことで、ユーザーに即時にプロンプトで要求することもできます。

{% alert important %}
`Always` 権限を求める即時プロンプトを出せるのは一度のみです。
{% endalert %}

{% tabs %}
{% tab SWIFT %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endtab %}
{% endtabs %}

## ステップ 7: ダッシュボードでジオフェンスを有効にする

iOS では、1つのアプリに保存できるジオフェンスは20個までとなっています。ジオフェンスを有効にすると、Braze ではこれら20個の利用可能スロットの一部が使用されます。アプリ内の他のジオフェンス関連機能への偶発的または不要な中断を防ぐため、位置情報ジオフェンスはダッシュボード上で個々のアプリに対して有効にする必要があります。位置情報サービスが正しく動作するには、アプリで利用可能なジオフェンススポットがすべて使用されていないことを確認してください。

ジオフェンスを特定のアプリに対して有効にするには、[**場所**] ページから有効にする方法と、[**設定の管理**] ページから有効にする方法があります。

### [場所] ページからジオフェンスを有効にする

ダッシュボードの [**場所**] ページでジオフェンスを有効にします。

1. [**オーディエンス**] > [**場所**] に移動します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] の下に [**位置情報**] が表示されます。
{% endalert %}

{:start="2"}
2\.ジオフェンスが現在有効になっているワークスペース内のアプリの数が、マップの下に表示されます。たとえば、[**ジオフェンスが有効になっているアプリ0/1**] と表示されます。このテキストをクリックします。
3\.ジオフェンスを有効にするアプリを選択します。[**完了**] をクリックします。
![Braze 場所ページのジオフェンスオプション。]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### [設定の管理] ページからジオフェンスを有効にする

アプリの設定からジオフェンスを有効にします。

1. [**設定**] > [**アプリ設定**] に移動します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**設定の管理**] > [**設定**] でジオフェンスを確認できます。
{% endalert %}

{:start="2"}
2\.ジオフェンスを有効にするアプリを選択します。
3\.[**ジオフェンスは有効です**] チェックボックスを選択します。[**保存**] をクリックします。

![Braze の設定ページにあるジオフェンスのチェックボックス。]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## 自動ジオフェンスリクエストを無効にする

[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)) に渡される `configuration` オブジェクトで、自動ジオフェンスリクエストを無効にできます。`automaticGeofenceRequests` を `false` に設定します。以下に例を示します。

{% tabs %}
{% tab SWIFT %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

このオプションの使用を選択した場合、機能が動作するよう、ジオフェンスを手動でリクエストする必要があります。

## ジオフェンスの手動リクエスト

Braze SDK からジオフェンスにバックエンドからの監視がリクエストされると、ユーザーの現在の位置情報がレポートされ、レポートされた位置情報に基づいて最も関連性が高いと特定されたジオフェンスが受信されます。ジオフェンスの更新には、各セッションで1回というレート制限があります。

最も関連性の高いジオフェンスを受信するために、SDK でレポートされる位置情報をコントロールするには、位置の緯度と経度を指定して、ジオフェンスを手動でリクエストできます。この方法を使用する場合は、自動ジオフェンスリクエストを無効にすることをお勧めします。そのためには、次のコードを使用します。

{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

