{% alert important %}
iOS 14以降、おおよその位置情報の権限のみを選択したユーザーに対しては、ジオフェンスが確実に動作しない。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: Brazeで有効にする

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### ステップ 2:アプリの位置情報サービスをイネーブルメントする

デフォルトでは、Brazeの位置情報サービスのイネーブルメントは有効になっていない。アプリでそれらをイネーブルメントするには、次のステップを完了する。ステップごとのチュートリアルについては、チュートリアルを[参照せよ。Brazeのロケーションとジオフェンス](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)。

#### ステップ 2.1: モジュ`BrazeLocation`ールを追加する

Xcodeで、**一般**タブを開け。**フレームワーク、ライブラリー、および埋め込みコンテンツ**の下に、モジュ`BrazeLocation`ールを追加する。

![XcodeプロジェクトにBrazeLocationモジュールを追加する]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### ステップ 2.2:`Info.plist` を更新する

アプリケーションで位置情報の追跡が必要である理由を説明する`info.plist`以下のキーのいずれかに値を`String`割り当てよ。この文字列は、ユーザーが位置情報サービスのイネーブルメントを求められる際に表示される。だから、この機能をイネーブルメントすることでアプリにどんな価値があるかを明確に説明するように。

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist Xcodeのロケーション文字列]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Appleは廃止した`NSLocationAlwaysUsageDescription`。詳細については、[Appleの開発者ドキュメントを](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)参照せよ。
{% endalert %}

### ステップ 3:コード内でジオフェンスをイネーブルメントする

アプリコード内で、ジオフェンスを有効にするには、\`Geofence\`インスタンス[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)を初期化する`Geofence`オブジェクト`configuration`の\`enabled\`プロパティ`true`を`true``location.geofencesEnabled`に設定する。その他の`location`設定オプションについては、[Braze SWIFT SDKリファレンスを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class)参照せよ。

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

#### ステップ 3.1:バックグラウンドレポートを有効にする（任意）

デフォルトでは、ジオフェンスイベントはアプリがフォアグラウンドにある場合、またはすべてのアプリケーション状態を監視する権限`Always`を持っている場合にのみ監視される。

ただし、アプリがバックグラウンドにある場合や[許可`When In Use`](#swift_request-authorization)を得ている場合、ジオフェンスイベントも監視することを選択できる。 

これらの追加のジオフェンスイベントを監視するには、Xcodeプロジェクトを開封し、次に**「署名」→&「機能**」に移動する。**バックグラウンド**モードで、**位置情報の更新に**チェックを入れる。

![Xcodeでは、バックグラウンドモード＞位置情報の更新]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

次に、アプリのコードで`allowBackgroundGeofenceUpdates`をイネーブルメントする。これにより、Brazeは位置情報の更新を継続的に監視することで、アプリの「使用中」ステータスを延長できる。この設定は、アプリがバックグラウンドにある時だけ機能する。アプリが再起動すると、既存のバックグラウンドプロセスはすべて一時停止され、代わりにフォアグラウンドプロセスが優先される。

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
バッテリーの消耗とレート制限を防ぐため、アプリの特定のニーズに合った値に`distanceFilter`設定せよ。`distanceFilter` をより高い値に設定すると、アプリがユーザーの場所を要求しすぎないようにします。
{% endalert %}

### ステップ 4: 承認を要求する {#request-authorization}

ユーザーから権限を要求する際は、権限`Always`か権限`When In Use`のいずれかを要求する。

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

ただし、最初に  を呼び出し`requestWhenInUseAuthorization()`、最初の`When In Use`  認証を受け取った後に  `requestAlwaysAuthorization()`を呼び出すことで、ユーザーに即座にプロンプトを表示させることもできる。

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

Braze では、バックグラウンドプッシュ通知を使用してジオフェンスがデバイスと同期されます。サーバーからのジオフェンス更新を適切に処理するため、[サイレントプッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)するには以下の手順に従うこと。

{% alert note %}
Brazeのジオフェンス同期通知を受信した際に、アプリケーションが不要なアクションを行わないようにするには、[サイレントプッシュ]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications)通知を[無視]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications)する方法の記事に従うこと。
{% endalert %}

## 手動でジオフェンスをリクエストする {#manually-request-geofences}

Braze SDKがバックエンドにジオフェンスを要求すると、ユーザーの現在位置をレポートし、レポートされた位置に基づいて最適に関連性が高いと判断されたジオフェンスを受け取る。

最も関連性の高いジオフェンスを受信するために、SDKがレポートする位置をコントロールするには、希望する座標を提供してジオフェンスを手動でリクエストできる。

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

### ステップ 2:手動で`requestGeofences`呼び出す

コードでは、適切な緯度と経度でジオフェンスをリクエストする。

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

#### なぜ自分の端末でジオフェンス通知が届かないんだ？

デバイスでジオフェンスが受信されているかどうかを確認するには、まず[SDKデバッガ]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk)ーツールを使ってSDKのログを確認する。その後、サーバーからジオフェンスが正常に受信されているか、また顕著なエラーがあるかどうかを確認できる。

以下は、ジオフェンスが端末で受信されないその他の可能性のある理由だ：

##### iOSオペレーティングシステムの制限

iOSオペレーティングシステムでは、特定のアプリに対して最大20個のジオフェンスしか保存できない。ジオフェンスを有効にすると、Braze ではこれら20個の利用可能スロットの一部が使用されます。

アプリ内の他のジオフェンス関連機能が誤って、または意図せず妨げられるのを防ぐには、ダッシュボードで個々のアプリに対して位置情報ジオフェンスをイネーブルメントする必要がある。位置情報サービスが正しく動作するには、アプリで利用可能なジオフェンススポットがすべて使用されていないことを確認してください。

##### レート制限

Brazeは不要なリクエストを避けるため、1セッションあたり1回のジオフェンス更新に制限している。

#### Brazeと非Brazeのジオフェンス機能を両方使っている場合、どう動作するのか？

前述の通り、iOSでは単一のアプリが最大20個のジオフェンスを保存できる。このストレージは、Brazeと非Brazeのジオフェンスの両方で共有され、[CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager)によって管理される。

例えば、アプリに非Brazeのジオフェンスが20個含まれている場合、Brazeのジオフェンスをトラッキングするストレージは存在しない（逆も同様だ）。新しいジオフェンスを受信するには、[Appleの位置情報API](https://developer.apple.com/documentation/corelocation)を使用して、デバイス上の既存のジオフェンスの一部を監視を停止する必要がある。

#### ジオフェンス機能は、デバイスがオフラインの状態で使用できるか？

デバイスは、更新が行われる時だけインターネットに接続する必要がある。サーバーからジオフェンスを正常に受信した後、デバイスがオフライン状態であっても、ジオフェンスのエントリや退場を記録することが可能である。これは、デバイスの位置情報はインターネット接続とは別個に動作するためだ。

例えば、あるデバイスがセッション開始時にジオフェンスを正常に受信・登録した後、オフライン状態になったとする。登録済みのジオフェンスのいずれかに入ると、Brazeキャンペーンがトリガーされる。

#### アプリがバックグラウンド状態になったり終了したりすると、なぜジオフェンスが監視されなくなるのか？

許可`Always`がない場合、Appleはアプリが使用されていない間、位置情報サービスが動作するのを制限する。これはオペレーティングシステムによって強制されるものであり、Braze SDKのコントロール範囲外である。Brazeはアプリがバックグラウンドにある間もサービスを実行するための個別の設定を提供しているが、ユーザーからの明示的な許可を得ずに終了されたアプリについては、これらの制限を回避する方法はない。