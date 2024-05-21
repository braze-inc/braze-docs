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

## ステップ1: バックグラウンドのプッシュを有効にする

ジオフェンスの同期戦略を最大限に活用するには、標準のプッシュ統合を完了することに加えて、 [サイレントプッシュ通知][6]を有効にする必要があります。

## ステップ2: Braze の位置情報サービスを有効にする
Braze の位置情報サービスは、SDK を介して[有効にする必要があります][1]。これらはデフォルトでは有効になっていません。

## ステップ3: ジオフェンスを有効にする

ジオフェンスを有効にするには、[`Braze`][1] インスタンスを初期化する `configuration` オブジェクトで `location.geofencesEnabled` を `true` に設定します。その他の `location` 設定オプションは[こちら][2]で確認できます。
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
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

## ステップ4: Braze のバックグラウンドプッシュの確認

Braze では、バックグラウンドプッシュ通知を使用してジオフェンスがデバイスと同期されます。[サイレントプッシュの無視][7]に関する記事に従って、Braze のジオフェンス同期通知を受信したときにアプリケーションで不要なアクションが実行されないようにします。

## ステップ5: Info.plist への位置情報の使用説明文字列の追加

アプリケーションで位置情報を追跡する必要がある理由の説明を含む `String` 値が含まれる `info.plist` に、キー `NSLocationAlwaysUsageDescription`、`NSLocationAlwaysAndWhenInUseUsageDescription` または `NSLocationWhenInUseUsageDescription` を追加します。

この説明は、システムの位置情報プロンプトで権限がリクエストされ、ユーザーに位置情報の追跡の利点を明確に説明する必要がある場合に表示されます。

## ステップ6: ユーザーに対する権限のリクエスト

ジオフェンス機能は、`Always` 位置情報権限か、`Background Mode -> Location updates` 機能が有効な `AuthorizedWhenInUse` が付与されている場合にのみ動作します。

`Always` または `AuthorizedWhenInUse` 位置情報権限をリクエストするには、次のコードを使用します。

{% tabs %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
// or
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
// or
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
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] の下に [**場所**] が表示されます。
{% endalert %}

{:start="2"}
2\.ジオフェンスが現在有効になっているワークスペース内のアプリの数が、マップの下に表示されます。たとえば、[**ジオフェンスが有効になっているアプリ0/1**] と表示されます。このテキストをクリックします。
3\.ジオフェンスを有効にするアプリを選択します。[**完了**] をクリックします。
![The geofence options on the Braze locations page.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### [設定の管理] ページからジオフェンスを有効にする

アプリの設定からジオフェンスを有効にします。

1. [**設定**] > [**アプリ設定**] に移動します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**設定の管理**] > [**設定**] でジオフェンスを確認できます。
{% endalert %}

{:start="2"}
2\.ジオフェンスを有効にするアプリを選択します。
3\.[**ジオフェンスは有効です**] チェックボックスを選択します。[**保存**] をクリックします。

![The geofence checkbox located on the Braze settings pages.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## 自動ジオフェンスリクエストを無効にする

`[init(configuration)]`[4] に渡される `configuration` オブジェクトで、自動ジオフェンスリクエストを無効にできます。`automaticGeofenceRequests` を `false` に設定します。以下はその例です。

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

このオプションの使用を選択した場合、機能が動作するよう、ジオフェンスを手動でリクエストする必要があります。

## ジオフェンスの手動リクエスト

Braze SDK からジオフェンスにバックエンドからの監視がリクエストされると、ユーザーの現在の位置情報がレポートされ、レポートされた位置情報に基づいて最も関連性が高いと特定されたジオフェンスが受信されます。ジオフェンスの更新には、各セッションで1回というレート制限があります。

最も関連性の高いジオフェンスを受信するために、SDK でレポートされる位置情報をコントロールするには、位置の緯度と経度を指定して、ジオフェンスを手動でリクエストできます。この方法を使用する場合は、自動ジオフェンスリクエストを無効にすることをお勧めします。そのためには、次のコードを使用します。

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

[1]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/
[2]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/
[support]: {{site.baseurl}}/braze_support/
