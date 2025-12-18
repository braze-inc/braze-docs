{% alert important %}
iOS 14の時点で、おおよその位置だけを許可することを選択したユーザーには、ジオフェンスは確実に機能しない。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: イネーブルメント in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### ステップ 2:アプリの位置情報サービスをイネーブルメントにする。

デフォルトでは、Brazeロケーションサービスは有効になっていない。アプリでイネーブルメントを有効にするには、以下のステップを完了する。ステップバイステップのチュートリアルについては、[チュートリアルを参照のこと：Brazeの位置とジオフェンス](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### ステップ 2.1: `BrazeLocation` モジュールを追加する。

Xcodeで**General**タブを開封する。**フレームワーク、ライブラリー、組み込みコンテンツ**」の下に、`BrazeLocation` モジュールを追加する。

![XcodeプロジェクトにBrazeLocationモジュールを追加する。]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### ステップ 2.2:`Info.plist` を更新する

`info.plist` で、アプリケーションが位置情報の追跡を必要とする理由を説明する、以下のキーの1つに`String` 値を割り当てる。この文字列は、ユーザーが位置情報サービスのプロンプトを表示したときに表示されるので、アプリでこの機能をイネーブルメントにする価値を明確に説明すること。

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist Xcodeの位置文字列]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
アップルは`NSLocationAlwaysUsageDescription` を廃止した。詳しくは[Appleの開発者ドキュメントを](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)参照のこと。
{% endalert %}

### ステップ 3:コードでジオフェンスをイネーブルメントにする

アプリのコードで、インスタンスを初期化する`configuration` オブジェクトの`location.geofencesEnabled` を`true` に設定して、ジオフェンスをイネーブルメントにする。 [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)インスタンスを初期化する。その他の`location` 設定オプションについては、[Braze Swift SDKリファレンスを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class)参照のこと。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Additional configuration customization...

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

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### ステップ 3.1:バックグラウンドレポートを有効にする（オプション）

デフォルトでは、ジオフェンス・イベントは、アプリがフォアグラウンドにあるか、`Always` 、すべてのアプリケーションの状態を監視する認可がある場合にのみ監視される。

しかし、アプリがバックグラウンドにある場合や、[`When In Use` 認証が](#swift_request-authorization)ある場合は、ジオフェンス・イベントを監視することもできる。 

これらの追加ジオフェンス・イベントをモニターするには、Xcodeプロジェクトを開封し、**Signing& Capabilitiesに**行く。**バックグラウンドモード]**で[**位置情報の更新]**をチェックする。

![Xcodeのバックグラウンドモード > ロケーション更新]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

次に、アプリのコードで`allowBackgroundGeofenceUpdates` 。これによりBrazeは、位置情報の更新を継続的に監視することで、アプリの「使用中」ステータスを拡張することができる。この設定は、アプリがバックグラウンドにあるときにのみ機能する。アプリが再び開封されると、既存のバックグラウンド・プロセスはすべて一時停止され、代わりにフォアグラウンド・プロセスが優先される。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
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

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
バッテリーの消耗やレート制限を防ぐには、`distanceFilter` 、アプリ固有のニーズを満たす値に設定する。`distanceFilter` をより高い値に設定すると、アプリがユーザーの場所を要求しすぎないようにします。
{% endalert %}

### ステップ 4: 認可を要請する {#request-authorization}

ユーザーに認可を要求する場合、`When In Use` または`Always` のいずれかの認可を要求する。

{% tabs local %}
{% tab When In Use %}
`When In Use` 権限を要求するには、`requestWhenInUseAuthorization()` メソッドを使用します。

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
デフォルトでは、`requestAlwaysAuthorization()` はアプリに `When In Use` 権限のみを付与し、しばらく経過した後に、`Always` 権限をユーザーにもう一度要求します。

しかし、最初に`requestWhenInUseAuthorization()` 、最初の`When In Use` の認可を受けた後に`requestAlwaysAuthorization()` 、即座にユーザーにプロンプトを出すこともできる。

{% alert important %}
`Always` 権限を求める即時プロンプトを出せるのは一度のみです。
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 5: バックグラウンドプッシュを確認する

Braze では、バックグラウンドプッシュ通知を使用してジオフェンスがデバイスと同期されます。以下の手順に従って、サーバーからのジオフェンス更新が適切に処理されるように、[サイレントプッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)する。

{% alert note %}
Brazeのジオフェンス同期通知を受信してもアプリケーションが不要なアクションを起こさないようにするには、[サイレントプッシュを無視する]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications)記事に従ってください。
{% endalert %}

## ジオフェンスを手動でリクエストする {#manually-request-geofences}

Braze SDKは、バックエンドからジオフェンスをリクエストすると、ユーザーのCurrentsをレポートし、レポートされたロケーションに基づいて最適に関連すると判断されたジオフェンスを受信する。

最も関連性の高いジオフェンスを受信する目的でSDKがレポートする位置をコントロールするには、希望する座標を提供してジオフェンスを手動でリクエストすることができる。

### ステップ 1: `automaticGeofenceRequests` を `false` に設定します

[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)) に渡される `configuration` オブジェクトで、自動ジオフェンスリクエストを無効にできます。`automaticGeofenceRequests` を `false` に設定します。

{% tabs %}
{% tab swift %}

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

### ステップ 2:`requestGeofences` に手動で電話をかける。

コードの中で、適切な緯度と経度を持つジオフェンスをリクエストする。

{% tabs %}
{% tab swift %}

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

## よくある質問 (FAQ) {#faq}

#### 私のデバイスでジオフェンスが受信できないのはなぜか？

ジオフェンスがデバイスで受信されているかどうかを確認するには、まず[SDK Debuggerツールを使って]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk)SDKのログをチェックする。そして、ジオフェンスがサーバーから正常に受信されているかどうか、また目立ったエラーがないかどうかを確認することができる。

以下は、お使いのデバイスでジオフェンスが受信されない場合に考えられるその他の理由である：

##### iOSオペレーティングシステムの制限

iOSのオペレーティングシステムでは、1つのアプリに保存できるジオフェンスは20個までとなっている。ジオフェンスを有効にすると、Braze ではこれら20個の利用可能スロットの一部が使用されます。

アプリ内の他のジオフェンス関連機能が誤って、または望まない形で中断されるのを防ぐため、ダッシュボードで個々のアプリの位置情報ジオフェンスをイネーブルメントにする必要がある。位置情報サービスが正しく動作するには、アプリで利用可能なジオフェンススポットがすべて使用されていないことを確認してください。

##### レート制限

Brazeでは、不要なリクエストを避けるため、ジオフェンスの更新は1セッションにつき1回に制限されている。

#### Brazeと非Brazeの両方のジオフェンス機能を使用している場合、どのように機能するのか？

前述の通り、iOSでは1つのアプリに最大20個のジオフェンスを保存できる。このストレージは、BrazeとBraze以外のジオフェンスの両方で共有され、[CLLocationManagerによって](https://developer.apple.com/documentation/corelocation/cllocationmanager)管理される。

例えば、アプリに20の非Brazeジオフェンスが含まれている場合、Brazeジオフェンスをトラッキング追跡するストレージはない（逆も同様）。新しいジオフェンスを受信するには、[アップルの位置情報APIを](https://developer.apple.com/documentation/corelocation)使用して、デバイス上の既存のジオフェンスの一部の監視を停止する必要がある。

#### ジオフェンス機能は、デバイスがオフラインの状態でも使用できるのか？

デバイスは、リフレッシュが発生したときだけインターネットに接続する必要がある。サーバーからのジオフェンス受信に成功すれば、デバイスがオフラインの状態でも、ジオフェンスのエントリやエグジットを記録することができる。これは、デバイスの位置情報がインターネット接続とは別に動作するためだ。

例えば、あるデバイスがセッション開始時にジオフェンスの受信と登録に成功し、オフラインになったとする。登録されたジオフェンスのいずれかに入ると、Brazeキャンペーンをトリガーすることができる。

#### アプリがバックグラウンド/終了すると、ジオフェンスが監視されないのはなぜか？

`Always` 、アップルはアプリが使用されていない間、位置情報サービスの実行を制限する。これはオペレーティングシステムによって強制され、Braze SDKのコントロール外である。Brazeは、アプリがバックグラウンドにある間にサービスを実行するための個別の設定を提供しているが、ユーザーからの明示的な承認を受けずに終了したアプリについては、これらの制限を回避する方法はない。