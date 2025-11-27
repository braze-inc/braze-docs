## 現在地を記録する

### ステップ 1: プロジェクトを構成する

{% alert important %}
Braze の位置情報機能を使用する場合、アプリケーションでは位置情報サービスを使用するための権限がリクエストされます。[アップル開発者のレビューをぜひ：ユーザーロケーションサービスへの認可を要求する](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) 。
{% endalert %}

位置情報の追跡を有効にするには、Xcodeプロジェクトを開封し、アプリを選択する。**General**タブで、`BrazeLocation` モジュールを追加する。

{% tabs %}
{% tab swift %}

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
{% tab objective-c %}

`AppDelegate.m` ファイルの先頭にある `BrazeLocation` モジュールをインポートします。Braze の構成に `BrazeLocationProvider` インスタンスを追加し、構成に対するすべての変更が `Braze(configuration:)` を呼び出す前に実行されるようにします。利用可能な構成については、`BRZConfigurationLocation` を参照してください。

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

### ステップ 2: ユーザーの位置情報を記録する

次に、ユーザーが最後に知った場所をBrazeに記録する。以下の例では、Brazeインスタンスを`AppDelegate` の変数として代入していると仮定している。

{% tabs %}
{% tab swift %}

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
{% tab objective-c %}

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

{% alert tip %}
詳細については、[`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/) を参照してください。
{% endalert %}
