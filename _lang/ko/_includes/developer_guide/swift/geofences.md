{% alert important %}
iOS 14부터 대략적인 위치 권한만 허용하도록 선택한 사용자에게는 지오펜스가 안정적으로 작동하지 않습니다.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 지오펜스 설정하기 {#setting-up-geofences}

### 1단계: Braze에서 인에이블먼트하기

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### 2단계: 앱의 위치 서비스 인에이블먼트하기

기본값으로 Braze 위치 서비스는 인에이블먼트되지 않습니다. 앱에서 인에이블먼트하려면 다음 단계를 완료하세요. 단계별 튜토리얼은 [튜토리얼을 참조하세요: Braze 위치 및 지오펜스](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### 2.1 단계: `BrazeLocation` 모듈 추가

Xcode에서 **일반** 탭을 엽니다. **프레임워크, 라이브러리 및 임베디드 콘텐츠에서** `BrazeLocation` 모듈을 추가합니다.

![Xcode 프로젝트에 BrazeLocation 모듈을 추가합니다.]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### 2.2 단계: `Info.plist` 업데이트

`info.plist` 에서 애플리케이션이 위치를 추적해야 하는 이유를 설명하는 `String` 값을 다음 키 중 하나에 할당합니다. 이 문자열은 사용자에게 위치 서비스를 묻는 메시지가 표시될 때 표시되므로 앱에 이 기능을 인에이블먼트할 때의 가치를 명확하게 설명해야 합니다.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist Xcode의 위치 문자열]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple은 `NSLocationAlwaysUsageDescription` 을 더 이상 사용하지 않습니다. 자세한 내용은 [Apple의 개발자 설명서를](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription) 참조하세요 [.](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)
{% endalert %}

### 3단계: 코드에서 지오펜스 인에이블먼트하기

앱 코드에서 `configuration` 객체를 초기화하는 객체에서 `location.geofencesEnabled` 을 `true` 으로 설정하여 지오펜스를 인에이블먼트합니다. [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) 인스턴스를 초기화합니다. 기타 `location` 구성 옵션은 [Braze Swift 소프트웨어 개발 키트 참조를](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class) 참조하세요.

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

#### 3.1 단계: 백그라운드 보고 인에이블먼트(선택 사항)

기본값으로 앱이 포그라운드에 있거나 모든 애플리케이션 상태를 모니터링하는 `Always` 권한이 있는 경우에만 지오펜스 이벤트가 모니터링됩니다.

그러나 앱이 백그라운드에 있거나 [`When In Use` 권한이](#swift_request-authorization) 있는 경우 지오펜스 이벤트도 모니터링하도록 선택할 수 있습니다. 

이러한 추가 지오펜싱 이벤트를 모니터링하려면 Xcode 프로젝트를 연 다음 **서명 & 기능으로** 이동합니다. **백그라운드 모드에서** **위치 업데이트를** 확인합니다.

![Xcode에서 백그라운드 모드 > 위치 업데이트]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

그런 다음 앱 코드에서 `allowBackgroundGeofenceUpdates` 을 인에이블먼트합니다. 이를 통해 Braze는 위치 업데이트를 지속적으로 모니터링하여 앱의 "사용 중" 상태를 연장할 수 있습니다. 이 설정은 앱이 백그라운드에 있을 때만 작동합니다. 앱이 다시 열리면 기존의 모든 백그라운드 프로세스가 일시 중지되고 대신 포그라운드 프로세스가 우선순위를 갖습니다.

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
배터리 소모 및 속도 제한을 방지하려면 `distanceFilter` 을 앱의 특정 요구 사항에 맞는 값으로 구성하세요. `distanceFilter`를 더 높은 값으로 설정하면 앱에서 사용자의 위치를 너무 자주 요청하는 것을 방지할 수 있습니다.
{% endalert %}

### 4단계: 승인 요청 {#request-authorization}

사용자에게 인증을 요청할 때는 `When In Use` 또는 `Always` 인증을 요청하세요.

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

그러나 초기 `When In Use` 승인을 받은 후 `requestWhenInUseAuthorization()` 으로 전화한 다음 `requestAlwaysAuthorization()` 으로 전화하여 사용자에게 즉시 메시지를 표시하도록 선택할 수 있습니다.

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

Braze는 백그라운드 푸시 알림을 사용하여 지오펜스를 기기와 동기화합니다. 서버의 지오펜스 업데이트가 제대로 처리되도록 [무음 푸시 알림을 설정하려면]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) 다음 지침을 따르세요.

{% alert note %}
애플리케이션이 Braze 지오펜스 동기화 알림을 수신할 때 원치 않는 작업을 수행하지 않도록 하려면 [무음 푸시 무시하기]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) 도움말을 따르세요.
{% endalert %}

## 수동으로 지오펜스 요청하기 {#manually-request-geofences}

Braze 소프트웨어 개발 키트는 백엔드에 지오펜스를 요청하면 사용자의 현재 위치를 보고하고 보고된 위치를 기반으로 최적의 관련성이 있다고 판단되는 지오펜스를 수신합니다.

가장 관련성이 높은 지오펜스를 수신하기 위해 소프트웨어 개발 키트에서 보고하는 위치를 제어하려면 원하는 좌표를 제공하여 지오펜스를 수동으로 요청할 수 있습니다.

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

### 2단계: `requestGeofences` 수동으로 전화하기

코드에서 적절한 위도와 경도로 지오펜스를 요청하세요.

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

#### 내 기기에 지오펜싱이 수신되지 않는 이유는 무엇인가요?

기기에서 지오펜싱이 수신되고 있는지 확인하려면 먼저 [소프트웨어 개발 키트 디버거 도구를]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) 사용하여 SDK의 로그를 확인하세요. 그러면 서버에서 지오펜싱이 성공적으로 수신되고 있는지, 눈에 띄는 오류가 있는지 확인할 수 있습니다.

다음은 기기에 지오펜싱이 수신되지 않을 수 있는 다른 가능한 이유입니다:

##### iOS 운영 체제 제한 사항

iOS 운영 체제에서는 특정 앱에 대해 최대 20개의 지오펜스만 저장할 수 있습니다. 지오펜스를 활성화하면 Braze는 사용 가능한 20개의 슬롯 중 일부를 사용합니다.

앱의 다른 지오펜스 관련 기능이 실수로 또는 원치 않게 중단되는 것을 방지하려면 대시보드에서 개별 앱에 대해 위치 지오펜스를 인에이블먼트해야 합니다. 위치 서비스가 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 지점을 사용하고 있지 않은지 확인합니다.

##### 사용량 제한

Braze는 불필요한 요청을 방지하기 위해 세션당 지오펜스 새로고침 횟수를 1회로 제한합니다.

#### Braze와 비 Braze 지오펜스 기능을 모두 사용하는 경우 어떻게 작동하나요?

위에서 언급했듯이 iOS에서는 하나의 앱에 최대 20개의 지오펜스를 저장할 수 있습니다. 이 스토리지는 Braze 및 비 Braze 지오펜스에서 공유되며 [CLLocationManager가](https://developer.apple.com/documentation/corelocation/cllocationmanager) 관리합니다.

예를 들어 앱에 20개의 비(非)Braze 지오펜스가 포함된 경우, Braze 지오펜스를 추적할 수 있는 스토리지가 없습니다(또는 그 반대의 경우도 마찬가지). 새로운 지오펜스를 수신하려면 [Apple의 위치 API를](https://developer.apple.com/documentation/corelocation) 사용하여 기기에 있는 기존 지오펜스 중 일부의 모니터링을 중지해야 합니다.

#### 기기가 오프라인 상태일 때 지오펜스 기능을 사용할 수 있나요?

기기는 새로고침이 발생할 때만 인터넷에 연결해야 합니다. 서버로부터 지오펜싱을 성공적으로 수신하면 기기가 오프라인 상태에서도 지오펜스 진입 또는 퇴장을 기록할 수 있습니다. 이는 기기의 위치가 인터넷 연결과 별개로 작동하기 때문입니다.

예를 들어 세션 시작 시 기기가 지오펜싱을 성공적으로 수신하고 등록한 후 오프라인 상태가 되었다고 가정해 보겠습니다. 그런 다음 등록된 지오펜스 중 하나에 들어가면 Braze 캠페인을 트리거할 수 있습니다.

#### 앱이 백그라운드/종료되었을 때 지오펜싱이 모니터링되지 않는 이유는 무엇인가요?

`Always` 승인이 없으면 Apple은 앱을 사용하지 않는 동안 위치 서비스가 실행되지 않도록 제한합니다. 이는 운영 체제에 의해 시행되며 Braze 소프트웨어 개발 키트에서 제어할 수 없습니다. Braze는 앱이 백그라운드에서 서비스를 실행하는 동안 별도의 구성을 제공하지만, 사용자의 명시적인 승인을 받지 않고 종료된 앱의 경우 이러한 제한을 우회할 수 있는 방법이 없습니다.