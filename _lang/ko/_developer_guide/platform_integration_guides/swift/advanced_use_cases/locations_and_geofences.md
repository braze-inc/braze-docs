---
nav_title: 위치 및 지오펜스
article_title: iOS용 위치 및 지오펜스
platform: Swift
page_order: 4
description: "이 참조 문서에서는 Swift SDK에서 위치 및 지오펜스를 구현하는 방법을 다룹니다."
Tool:
  - Location

---

# 위치 및 지오펜스

> 이 문서에서는 iOS SDK 통합을 위한 지오펜스 설정을 다룹니다. 지오펜스는 일부 Braze 패키지에서만 사용할 수 있습니다. 시작하려면 Braze 고객 성공 관리자에게 문의하세요.

Braze의 실시간 위치 서비스의 핵심은 [지오펜스]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences) 개념입니다. 지오펜스는 위도와 경도를 반경과 결합하여 특정 글로벌 위치를 중심으로 원을 형성하는 가상의 지리적 영역입니다.

{% alert important %}
iOS 14부터 지오펜스는 대략적인 위치 권한을 제공하는 사용자의 경우 안정적으로 작동하지 않습니다.
{% endalert %}

## 1단계: 백그라운드 푸시 사용

지오펜스 동기화 전략을 최대한 활용하려면 표준 푸시 통합을 완료하는 것 외에도 [자동 푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)을 활성화해야 합니다.

## 2단계: Braze 위치 서비스 활성화
Braze 위치 서비스는 SDK를 통해 [활성화해야 합니다](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). 기본적으로 활성화되어 있지 않습니다.

## 3단계: 지오펜스 활성화

[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) 인스턴스를 초기화하는 `configuration` 오브젝트에서 `location.geofencesEnabled`를 `true`로 설정하여 지오펜스를 활성화합니다. 기타 `location` 구성 옵션은 [여기에서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class) 확인할 수 있습니다.
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

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab 목표-C %}

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

### 백그라운드 보고를 위한 지오펜스 구성

기본적으로 지오펜스는 앱이 포그라운드에 있거나 `Always` 권한(모든 애플리케이션 상태를 모니터링하는 권한)이 있는 경우에만 모니터링됩니다.

그러나 앱이 백그라운드에 있거나 `When In Use` 권한이 있을 때 Xcode 프로젝트에 `Background Mode -> Location updates` 기능을 추가하고 `allowBackgroundGeofenceUpdates`를 활성화하여 지오펜스 이벤트를 모니터링할 것인지 선택할 수 있습니다. 이를 통해 Braze는 위치 업데이트를 지속적으로 모니터링하여 앱의 '사용 중' 상태를 확장할 수 있습니다.

`allowBackgroundGeofenceUpdates`는 앱이 백그라운드에 있을 때만 작동합니다. 다시 열면 기존 백그라운드 프로세스가 일시 중지되므로 대신 포그라운드 프로세스가 우선할 수 있습니다.

{% alert important %}
배터리 소모 및 사용량 제한을 방지하려면 `distanceFilter`를 앱의 특정 요구 사항에 맞는 값으로 구성해야 합니다. `distanceFilter`를 더 높은 값으로 설정하면 앱에서 사용자의 위치를 너무 자주 요청하는 것을 방지할 수 있습니다.
{% endalert %}

## 4단계: Braze 백그라운드 푸시 확인

Braze는 백그라운드 푸시 알림을 사용하여 지오펜스를 기기와 동기화합니다. 애플리케이션이 Braze 지오펜스 동기화 알림을 수신할 때 원치 않는 조치를 취하지 않도록 하려면 [무음 푸시 무시]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) 문서를 참조하세요.

## 5단계: 위치 사용 설명 문자열을 Info.plist에 추가

`NSLocationAlwaysUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription` 또는 `NSLocationWhenInUseUsageDescription`를 `String` 값으로 `info.plist`에 추가합니다. 이 값에는 애플리케이션에서 위치를 추적해야 하는 이유에 대한 설명이 포함되어 있습니다.

이 설명은 시스템 위치 프롬프트가 승인을 요청할 때 표시되며, 사용자에게 위치 추적의 이점을 명확하게 설명해야 합니다.

## 6단계: 사용자로부터 권한 부여 요청

사용자로부터 권한을 요청할 때 [`When In Use`](#when-in-use) 또는 [`Always`](#always) 권한 부여를 요청할 수 있습니다.

### 사용 중일 때

`When In Use` 인증을 요청하려면 `requestWhenInUseAuthorization()` 방법을 사용합니다:

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endtab %}

{% tab 목표-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endtab %}
{% endtabs %}

### 항상

기본적으로 `requestAlwaysAuthorization()`은 앱에 `When In Use` 권한만 부여하고, 일정 시간이 지나면 사용자에게 `Always` 권한 부여를 요청하는 프롬프트를 다시 표시합니다. 그러나 먼저 `requestWhenInUseAuthorization()`을 호출한 다음, 초기 `When In Use` 권한을 받은 후 `requestAlwaysAuthorization()`을 호출하여 사용자에게 즉시 프롬프트를 표시하도록 선택할 수 있습니다.

{% alert important %}
`Always` 권한은 한 번만 즉시 요청할 수 있습니다.
{% endalert %}

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endtab %}

{% tab 목표-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endtab %}
{% endtabs %}

## 7단계: 대시보드에서 지오펜스 활성화

iOS에서는 특정 앱에 대해 최대 20개의 지오펜스만 저장하도록 허용합니다. 지오펜스를 활성화하면 Braze는 사용 가능한 20개의 슬롯 중 일부를 사용합니다. 앱의 다른 지오펜스 관련 기능이 실수로 또는 원치 않게 중단되는 것을 방지하려면 대시보드에서 개별 앱에 대해 위치 지오펜스를 활성화해야 합니다. 위치 서비스가 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 지점을 사용하고 있지 않은지 확인합니다.

특정 앱의 지오펜스를 활성화하는 방법은 **위치** 페이지 또는 **설정 관리** 페이지에서 두 가지가 있습니다.

### 위치 페이지에서 지오펜스 활성화

대시보드의 **위치** 페이지에서 지오펜스를 사용 설정합니다.

1. **오디언스** > **위치**로 이동합니다.
{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **인게이지먼트** 아래에서 **위치**를 찾을 수 있습니다.
{% endalert %}

{:start="2"}
2\. 예를 들어 현재 지오펜스가 활성화된 워크스페이스에서 앱 수가 맵 아래 표시됩니다. 예를 들어 다음과 같습니다. **지오펜스가 활성화된 앱 0/1개**. 이 텍스트를 클릭합니다.
3\. 지오펜스를 활성화하려면 앱을 선택합니다. **완료**를 클릭합니다.
![Braze 위치 페이지의 지오펜스 옵션]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### 설정 관리 페이지에서 지오펜스 활성화

앱 설정에서 지오펜스를 활성화합니다.

1. **설정** > **앱 설정으로** 이동합니다.
{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **설정 관리** > **설정**에서 지오펜스를 찾을 수 있습니다.
{% endalert %}

{:start="2"}
2\. 지오펜스를 활성화하려는 앱을 선택합니다.
3\. **지오펜스 활성화됨** 확인란을 선택합니다. **저장**을 클릭합니다.

![Braze 설정 페이지에 있는 지오펜스 확인란.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## 자동 지오펜스 요청 비활성화하기

`configuration` 오브젝트에서 [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:))로 전달되는 자동 지오펜스 요청을 비활성화할 수 있습니다. `automaticGeofenceRequests`를 `false`로 설정합니다. 예를 들어, 다음과 같습니다.

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
{% tab 목표-C %}

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

이 옵션을 사용하려는 경우 기능이 작동하도록 지오펜스를 수동으로 요청해야 합니다.

## 지오펜스 수동 요청

Braze SDK가 백엔드에서 모니터링하도록 지오펜스를 요청하면 사용자의 현재 위치를 보고하고 보고된 위치를 기반으로 최적의 관련성이 있는 것으로 판단되는 지오펜스를 수신합니다. 지오펜스 새로 고침 사용량 제한은 세션당 한 번입니다.

가장 관련성이 높은 지오펜스를 수신하기 위해 SDK가 보고하는 위치를 제어하도록 위치의 위도와 경도를 제공하여 지오펜스를 수동으로 요청할 수 있습니다. 이 방법을 사용할 때는 자동 지오펜스 요청을 비활성화하는 것이 좋습니다. 이렇게 하려면 다음 코드를 사용하세요:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

