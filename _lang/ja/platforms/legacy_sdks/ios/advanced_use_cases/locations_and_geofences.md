---
nav_title: 位置情報とジオフェンス
article_title: iOS の位置情報とジオフェンス
platform: iOS
page_order: 6
description: "このリファレンス記事では、iOS アプリケーションに位置情報とジオフェンスを実装する方法について説明します。"
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 位置情報とジオフェンス

iOS のジオフェンスをサポートするには:

1. 統合がバックグラウンドプッシュ通知に対応している必要があります。
2. Braze ジオフェンスを有効にするには、SDK を通じて位置情報の収集を有効にするか (暗示的)、ジオフェンスの収集を[有効にする (明示的) 必要があります]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking)。これらはデフォルトでは有効になっていません。

{% alert important %}
iOS 14 の時点では、おおよその位置情報の提供許可を選択しているユーザーの場合、ジオフェンスが確実に機能しないことがあります。
{% endalert %}

## ステップ1:バックグラウンドのプッシュを有効にする

ジオフェンス同期ストラテジを完全に使用するには、標準のプッシュ統合に加えて、[background push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work) を有効にする必要があります。

## ステップ2: ジオフェンスを有効にする

デフォルトでは、ジオフェンスは位置情報の自動収集が有効かどうかに基づいて有効になります。ジオフェンスを有効にするには、`Info.plist` ファイルを使用します。`Braze` ディクショナリを `Info.plist` ファイルに追加します。`Braze` ディクショナリ内にブール値の `EnableGeofences` サブエントリを追加し、値を `YES` に設定します。なお、Braze iOS SDK v4.0.2より前のバージョンでは、`Braze` の代わりに辞書キー `Appboy` を使用する必要があります。

また、[`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) メソッドを使用して、アプリの起動時にgeofences を有効にすることもできます。`appboyOptions` ディクショナリで、`ABKEnableGeofencesKey` を `YES` に設定します。以下に例を示します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## ステップ 3: Braze のバックグラウンドプッシュを確認する

Braze では、バックグラウンドプッシュ通知を使用してジオフェンスがデバイスと同期されます。[iOS のカスタマイズ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/)に関する記事に従って、Braze のジオフェンス同期通知を受信したときにアプリケーションで不要なアクションが実行されないようにします。

## ステップ 4:NSLocationAlwaysUsageDescriptionをInfo.plistに追加します

アプリケーションで位置情報を追跡する必要がある理由の説明を含んだ `String` 値を使用して、キー `NSLocationAlwaysUsageDescription` および `NSLocationAlwaysAndWhenInUseUsageDescription` を `info.plist` に追加します。iOS 11 以降では両方のキーが必要です。
この説明は、システムの位置情報プロンプトで権限がリクエストされ、ユーザーに位置情報の追跡の利点を明確に説明する必要がある場合に表示されます。

## ステップ 5:ユーザーに権限をリクエストする

ジオフェンス機能は、位置情報に対する権限 `Always` が付与されている場合にのみ機能します。

位置情報権限 `Always` をリクエストするには、次のコードを使用します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## ステップ 6:ダッシュボードでジオフェンスを有効にする

iOS では、1 つのアプリに保存できるジオフェンスは 20 個までとなっています。位置情報を使用すると、これら 20 個の使用可能なジオフェンススロットの一部が使用されます。アプリ内の他のジオフェンス関連機能への偶発的または不要な中断を防ぐため、位置情報ジオフェンスはダッシュボード上で個々のアプリに対して有効にする必要があります。

位置情報が正しく動作するには、アプリが利用可能なジオフェンススポットをすべて使用していないことも確認する必要があります。

### 場所ページからジオフェンスを有効にする

![Braze 場所ページのジオフェンスオプション。]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})()

### 設定ページからジオフェンスを有効にする

![Braze の設定ページにあるジオフェンスのチェックボックス。]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})()

## 自動ジオフェンスリクエストを無効にする

iOS SDK バージョン 3.21.3 以降では、ジオフェンスが自動的にリクエストされないようにすることができます。これを行うには、`Info.plist` ファイルを使用します。`Braze` ディクショナリを `Info.plist` ファイルに追加します。`Braze` ディクショナリ内にブール値の `DisableAutomaticGeofenceRequests` サブエントリを追加し、値を `YES` に設定します。

[`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) メソッドを使用して、アプリの起動時に位置情報の自動追跡を有効にすることもできます。`appboyOptions` ディクショナリで、`ABKDisableAutomaticGeofenceRequestsKey` を `YES` に設定します。以下に例を示します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

このオプションの使用を選択した場合、機能が動作するよう、ジオフェンスを手動でリクエストする必要があります。

## ジオフェンスの手動リクエスト

Braze SDK からジオフェンスにバックエンドからの監視がリクエストされると、ユーザーの現在の位置情報がレポートされ、レポートされた位置情報に基づいて最も関連性が高いと特定されたジオフェンスが受信されます。ジオフェンスの更新には、各セッションで 1 回というレート制限があります。

SDK でレポートされる位置情報をコントロールして、最も関連性の高いジオフェンスを受信できるようにするため、iOS SDK バージョン 3.21.3 以降では、位置の緯度と経度を指定することでジオフェンスを手動でリクエストできるようになっています。この方法を使用する場合は、自動ジオフェンスリクエストを無効にすることをお勧めします。そのためには、次のコードを使用します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}


