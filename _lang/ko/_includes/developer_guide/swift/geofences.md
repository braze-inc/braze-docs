{% alert important %}
iOS 14부터, 지오펜스는 대략적인 위치 권한만 부여한 사용자에게 신뢰할 수 있게 작동하지 않습니다.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 지오펜스 설정 {#setting-up-geofences}

### 1단계: Braze에서 활성화

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### 2단계: 앱의 위치 서비스를 활성화하세요

기본적으로, Braze 위치 서비스는 활성화되어 있지 않습니다. 앱에서 활성화하려면, 다음 단계를 완료하세요. 단계별 튜토리얼은 [튜토리얼:에서 확인하세요. Braze 위치 및 지오펜스](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)입니다.

#### 2.1 단계: `BrazeLocation` 모듈 추가

Xcode에서 **일반** 탭을 엽니다. **프레임워크, 라이브러리 및 포함된 콘텐츠** 아래에 `BrazeLocation` 모듈을 추가합니다.

![Xcode 프로젝트에 BrazeLocation 모듈 추가]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### 2.2 단계: `Info.plist` 업데이트

`info.plist`에서, 애플리케이션이 위치를 추적해야 하는 이유를 설명하는 `String` 값을 다음 키 중 하나에 할당합니다. 이 문자열은 사용자가 위치 서비스 요청을 받을 때 표시되므로, 앱의 이 기능을 활성화하는 것의 가치를 명확히 설명해야 합니다.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist Xcode의 위치 문자열]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple은 `NSLocationAlwaysUsageDescription`를 더 이상 지원하지 않습니다. 자세한 정보는 [Apple의 개발자 문서](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)를 참조하세요.
{% endalert %}

### 3단계: 코드에서 지오펜스를 활성화하세요

앱의 코드에서 `location.geofencesEnabled`을 `true`로 설정하여 `configuration` 객체에서 [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) 인스턴스를 초기화할 때 지오펜스를 활성화합니다. 다른 `location` 구성 옵션은 [Braze Swift SDK 참조](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class)를 참조하세요.

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

#### 3.1 단계: 백그라운드 보고 활성화(선택 사항)

기본적으로, 지오펜스 이벤트는 앱이 포그라운드에 있거나 `Always` 권한이 있는 경우에만 모니터링됩니다. 이 권한은 모든 애플리케이션 상태를 모니터링합니다.

그러나 앱이 백그라운드에 있거나 [`When In Use` 권한](#swift_request-authorization)이 있는 경우에도 지오펜스 이벤트를 모니터링하도록 선택할 수 있습니다. 

이 추가 지오펜스 이벤트를 모니터링하려면 Xcode 프로젝트를 열고 **서명 & 기능**으로 이동합니다. **백그라운드 모드**에서 **위치 업데이트**를 체크합니다.

![Xcode에서, 백그라운드 모드 > 위치 업데이트]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

다음으로, 앱의 코드에서 `allowBackgroundGeofenceUpdates`을 활성화합니다. 이렇게 하면 Braze가 위치 업데이트를 지속적으로 모니터링하여 앱의 "사용 중" 상태를 확장할 수 있습니다. 이 설정은 앱이 백그라운드에 있을 때만 작동합니다. 앱이 다시 열리면 모든 기존 백그라운드 프로세스가 일시 중지되고 포그라운드 프로세스가 우선시됩니다.

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
배터리 소모 및 속도 제한을 방지하기 위해 `distanceFilter`를 앱의 특정 요구 사항에 맞는 값으로 구성합니다. `distanceFilter`를 더 높은 값으로 설정하면 앱에서 사용자의 위치를 너무 자주 요청하는 것을 방지할 수 있습니다.
{% endalert %}

### 4단계: 권한 요청 {#request-authorization}

사용자에게 권한을 요청할 때 `When In Use` 또는 `Always` 권한 중 하나를 요청합니다.

{% tabs local %}
{% tab When In Use %}
`When In Use` 인증을 요청하려면 `requestWhenInUseAuthorization()` 방법을 사용합니다:

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
기본적으로 `requestAlwaysAuthorization()`은 앱에 `When In Use` 권한만 부여하고, 일정 시간이 지나면 사용자에게 `Always` 권한 부여를 요청하는 프롬프트를 다시 표시합니다.

그러나 먼저 `requestWhenInUseAuthorization()`을 호출한 다음 초기 `When In Use` 권한을 받은 후 `requestAlwaysAuthorization()`를 호출하여 사용자에게 즉시 프롬프트를 표시하도록 선택할 수 있습니다.

{% alert important %}
`Always` 권한은 한 번만 즉시 요청할 수 있습니다.
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

### 5단계: 백그라운드 푸시 확인

Braze는 백그라운드 푸시 알림을 사용하여 지오펜스를 기기와 동기화합니다. 서버에서 지오펜스 업데이트가 제대로 처리되도록 [무음 푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)에 대한 지침을 따르십시오.

{% alert note %}
Braze 지오펜스 동기화 알림을 수신할 때 애플리케이션이 원치 않는 작업을 수행하지 않도록 하려면 [무음 푸시 무시]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) 기사를 따르십시오.
{% endalert %}

## 지오펜스 수동 요청 {#manually-request-geofences}

Braze SDK가 백엔드에서 지오펜스를 요청할 때, 사용자의 현재 위치를 보고하고 보고된 위치를 기반으로 최적의 관련성이 있다고 판단되는 지오펜스를 수신합니다.

SDK가 가장 관련성 높은 지오펜스를 수신하기 위해 보고하는 위치를 제어하려면 원하는 좌표를 제공하여 지오펜스를 수동으로 요청할 수 있습니다.

### 1단계: `automaticGeofenceRequests`를 `false`로 설정

`configuration` 오브젝트에서 [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:))로 전달되는 자동 지오펜스 요청을 비활성화할 수 있습니다. `automaticGeofenceRequests`를 `false`로 설정합니다.

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

### 2단계: `requestGeofences`을(를) 수동으로 호출하십시오.

코드에서 적절한 위도와 경도로 지오펜스를 요청하십시오.

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

## 자주 묻는 질문(FAQ) {#faq}

#### 내 기기에서 지오펜스를 수신하지 못하는 이유는 무엇입니까?

기기에서 지오펜스가 수신되고 있는지 확인하려면 먼저 [SDK 디버거 도구]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk)를 사용하여 SDK의 로그를 확인하십시오. 그런 다음 서버에서 지오펜스가 성공적으로 수신되고 있는지와 주목할 만한 오류가 있는지 확인할 수 있습니다.

아래는 기기에서 지오펜스가 수신되지 않을 수 있는 다른 가능한 이유입니다:

##### iOS 운영 체제의 제한

iOS 운영 체제는 주어진 앱에 대해 최대 20개의 지오펜스를 저장할 수 있습니다. 지오펜스를 활성화하면 Braze는 사용 가능한 20개의 슬롯 중 일부를 사용합니다.

앱의 다른 지오펜스 관련 기능에 대한 우발적이거나 원치 않는 중단을 방지하기 위해 대시보드에서 개별 앱에 대한 위치 지오펜스를 활성화해야 합니다. 위치 서비스가 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 지점을 사용하고 있지 않은지 확인합니다.

##### 사용량 제한

Braze는 불필요한 요청을 피하기 위해 세션당 1개의 지오펜스 새로고침 한도를 가지고 있습니다.

#### Braze와 비-Braze 지오펜스 기능을 모두 사용하는 경우 어떻게 작동합니까?

위에서 언급했듯이, iOS는 단일 앱이 최대 20개의 지오펜스를 저장할 수 있도록 허용합니다. 이 저장소는 Braze와 비-Braze 지오펜스가 공유하며 [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager)에 의해 관리됩니다.

예를 들어, 앱에 20개의 비-Braze 지오펜스가 포함되어 있다면 Braze 지오펜스를 추적할 저장소가 없게 됩니다(또는 그 반대의 경우). 새로운 지오펜스를 수신하려면 [Apple의 위치 API](https://developer.apple.com/documentation/corelocation)를 사용하여 기기에서 기존 지오펜스 중 일부의 모니터링을 중지해야 합니다.

#### 기기가 오프라인일 때 지오펜스 기능을 사용할 수 있습니까?

기기는 새로고침이 발생할 때만 인터넷에 연결되어 있어야 합니다. 서버에서 지오펜스를 성공적으로 수신한 후에는 기기가 오프라인일지라도 지오펜스 진입 또는 종료를 기록할 수 있습니다. 이는 기기의 위치가 인터넷 연결과 별개로 작동하기 때문입니다.

예를 들어, 기기가 세션 시작 시 지오펜스를 성공적으로 수신하고 등록한 후 오프라인 상태가 되었다고 가정해 보십시오. 그것이 등록된 지오펜스 중 하나에 들어가면, Braze 캠페인을 트리거할 수 있습니다.

#### 내 앱이 백그라운드에서 실행 중이거나 종료되었을 때 지오펜스가 모니터링되지 않는 이유는 무엇인가요?

`Always` 권한 없이 Apple은 앱이 사용 중이지 않을 때 위치 서비스가 실행되는 것을 제한합니다. 이는 운영 체제에 의해 시행되며 Braze SDK의 제어 범위를 벗어납니다. Braze는 앱이 백그라운드에서 서비스를 실행할 수 있도록 별도의 구성을 제공하지만, 사용자의 명시적인 권한을 받지 않고 종료된 앱에 대한 이러한 제한을 우회할 방법은 없습니다.