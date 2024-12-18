---
nav_title: 위치 추적
article_title: iOS용 위치 추적
platform: Swift
page_order: 6
description: "이 문서는 Swift SDK에 대한 위치 추적을 구성하는 방법을 보여줍니다."
Tool:
  - Location

---

# 위치 추적

> 기본값으로, Braze는 위치 추적을 비활성화합니다. 호스트 애플리케이션이 위치 추적을 옵트인하고 사용자로부터 권한을 얻은 후 위치 추적을 활성화합니다. 사용자가 위치 추적을 옵트인한 경우, Braze는 세션 시작 시 각 사용자에 대해 단일 위치를 기록합니다.

## 자동 위치 추적 활성화

[위치 서비스 권한 요청](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services)을 검토하고 애플리케이션 용도 문자열을 구성해야 합니다. Braze 위치 기능을 사용할 때, 위치 서비스 사용 권한을 요청하는 것은 애플리케이션의 책임입니다. 

위치 추적을 활성화하려면 애플리케이션 구성 페이지의 **일반** 탭에 `BrazeLocation` 모듈을 추가하십시오.

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
{% tab 목표-C %}

`AppDelegate.m` 파일의 파일 상단에서 `BrazeLocation` 모듈을 가져옵니다. Braze 구성에 `BrazeLocationProvider` 인스턴스를 추가하고, 구성에 대한 모든 변경 사항이 Braze(configuration:) 호출 전에 완료되었는지 확인합니다. 사용 가능한 구성은 `BRZConfigurationLocation`을 참조하십시오.

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

### 위치 데이터를 Braze에 전달

다음 메서드를 사용하여 사용자의 마지막으로 알려진 위치를 수동으로 설정할 수 있습니다. 이 예제들은 AppDelegate에서 Braze 인스턴스를 변수로 할당했다고 가정합니다.



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
{% tab 목표-C %}

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

자세한 내용은 [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/)을 참조하십시오.

