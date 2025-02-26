---
nav_title: 位置情報の追跡
article_title: iOS の位置情報の追跡
platform: Swift
page_order: 6
description: "この記事では、Swift SDK の位置情報の追跡を構成する方法を紹介します。"
Tool:
  - Location

---

# 位置情報の追跡

> デフォルトでは、Braze で位置情報の追跡は無効です。位置情報の追跡は、ホストアプリケーションで位置情報の追跡がオプトインされ、ユーザーから許可を得た後に有効になります。ユーザーが位置情報の追跡をオプトインしている場合、Braze ではセッション開始時に各ユーザーの単一の位置情報がロギングされます。

## 位置情報の自動追跡を有効にする

[位置情報サービスの権限リクエスト](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services)に関する記事を参照し、アプリケーションの目的文字列を設定してください。Braze の位置情報機能を使用する場合、アプリケーションでは位置情報サービスを使用するための権限がリクエストされます。 

位置情報の追跡を有効にするには、アプリケーション構成ページの [**一般**] タブで `BrazeLocation` モジュールを追加します。

{% tabs %}
{% tab SWIFT %}

`AppDelegate.swift` ファイルの先頭にある `BrazeLocation` モジュールをインポートします。Braze の構成に `BrazeLocationProvider` インスタンスを追加し、構成に対するすべての変更が `Braze(configuration:)` を呼び出す前に実行されるようにします。利用可能な構成については、`Braze.Configuration.Location` を参照してください。

```swift
import UIKit
import BrazeKit
import BrazeLocation

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    configuration.logger.level = .info
    configuration.location.brazeLocationProvider = BrazeLocationProvider()
    configuration.location.automaticLocationCollection = true
    configuration.location.geofencesEnabled = true
    configuration.location.automaticGeofenceRequests = true
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    return true
  }

}

```

{% endtab %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイルの先頭にある `BrazeLocation` モジュールをインポートします。Braze の構成に `BrazeLocationProvider` インスタンスを追加し、構成に対するすべての変更が Braze(configuration:) を呼び出す前に実行されるようにします。利用可能な構成については、`BRZConfigurationLocation` を参照してください。

```objc
#import "AppDelegate.h"

@import BrazeKit;
@import BrazeLocation;

@implementation AppDelegate

#pragma mark - Lifecycle

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
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

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}

@end
```

{% endtab %}
{% endtabs %}

### 位置データを Braze に渡す

以下のメソッドは、ユーザーの既知の最終位置情報を手動で設定するために使用できます。これらの例では、AppDelegate で変数として Braze インスタンスを割り当てていると仮定しています。



{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
                                             longitude:longitude)
```

```swift
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
                                             longitude:longitude,
                                             altitude:altitude,
                                             horizontalAccuracy:horizontalAccuracy,
                                             verticalAccuracy:verticalAccuracy)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
                                               longitude:longitude
                                      horizontalAccuracy:horizontalAccuracy];

```

```objc
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
                                               longitude:longitude
                                      horizontalAccuracy:horizontalAccuracy
                                                altitude:altitude
                                        verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% endtabs %}

詳細については、[`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/) を参照してください。

