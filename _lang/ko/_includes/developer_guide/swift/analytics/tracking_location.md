## 현재 위치 기록하기

### 1단계: 프로젝트 구성

{% alert important %}
Braze 위치 기능을 사용할 때, 위치 서비스 사용 권한을 요청하는 것은 애플리케이션의 책임입니다. [Apple Developer를 검토하세요: 사용자 위치 서비스에 인증 요청하기](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).
{% endalert %}

위치 추적을 사용하려면 Xcode 프로젝트를 열고 앱을 선택합니다. **일반** 탭에서 `BrazeLocation` 모듈을 추가합니다.

{% tabs %}
{% tab swift %}

`AppDelegate.swift` 파일의 파일 상단에서 `BrazeLocation` 모듈을 가져옵니다. Braze 구성에 `BrazeLocationProvider` 인스턴스를 추가하고, 구성에 대한 모든 변경 사항이 `Braze(configuration:)` 호출 전에 완료되었는지 확인합니다. 사용 가능한 구성은 `Braze.Configuration.Location`을 참조하십시오.

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

`AppDelegate.m` 파일의 파일 상단에서 `BrazeLocation` 모듈을 가져옵니다. Braze 구성에 `BrazeLocationProvider` 인스턴스를 추가하고, 구성에 대한 모든 변경 사항이 `Braze(configuration:)` 호출 전에 완료되었는지 확인합니다. 사용 가능한 구성은 `BRZConfigurationLocation`을 참조하십시오.

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

### 2단계: 사용자 위치 기록

다음으로, 사용자의 마지막으로 알려진 위치를 Braze에 기록합니다. 다음 예제에서는 `AppDelegate` 에 Braze 인스턴스를 변수로 할당했다고 가정합니다.

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
자세한 내용은 [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/)를 참조하세요.
{% endalert %}
