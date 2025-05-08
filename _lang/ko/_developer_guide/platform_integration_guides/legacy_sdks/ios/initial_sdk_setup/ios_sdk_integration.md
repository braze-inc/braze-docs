---
nav_title: SDK 통합 가이드(선택 사항)
article_title: iOS용 Braze SDK 통합 가이드(선택 사항)
alias: "/ios_sdk/"
description: "이 iOS 통합 SDK 가이드는 iOS SDK와 핵심 구성요소를 애플리케이션에 처음 통합할 때 설정 모범 사례에 대한 단계별 여정을 안내합니다. 이 가이드는 BrazeManager.swift 헬퍼 파일을 빌드하는 데 도움이 됩니다."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze iOS SDK 통합 가이드

> 이 iOS 통합 SDK 가이드(선택 사항)는 iOS SDK와 핵심 구성요소를 애플리케이션에 처음 통합할 때 설정 모범 사례에 대한 단계별 여정을 안내합니다. 이 가이드는 나머지 프로덕션 코드에서 Braze iOS SDK에 대한 모든 종속성을 분리하는 `BrazeManager.swift` 헬퍼 파일을 빌드하여 전체 애플리케이션에서 하나의 `import AppboyUI` 헬퍼 파일을 생성하는 데 도움이 됩니다. 이 접근 방식은 과도한 SDK 가져오기로 인해 발생하는 문제를 제한하여 코드를 쉽게 추적, 디버그 및 변경할 수 있도록 합니다. 

{% alert important %}
이 가이드에서는 이미 Xcode 프로젝트에 [SDK를 추가]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/)했다고 가정합니다.
{% endalert %}

## 통합 개요

다음 단계는 프로덕션 코드가 호출되는 `BrazeManager` 헬퍼 파일을 빌드하는 데 도움이 됩니다. 이 헬퍼 파일은 나열된 다음 통합 주제에 대한 다양한 확장을 추가하여 모든 Braze 관련 종속성을 처리합니다. 각 주제에는 Swift 및 Objective-C 모두에 가로 탭 단계와 코드 스니펫이 포함됩니다. 애플리케이션에서 이러한 채널을 사용할 계획이 없는 경우 콘텐츠 카드 및 인앱 메시지 단계는 통합에 필요하지 않습니다.

- [BrazeManager.swift 생성](#create-brazemanagerswift)
- [SDK 초기화](#initialize-the-sdk)
- [푸시 알림](#push-notifications)
- [사용자 변수 및 메서드 액세스](#access-user-variables-and-methods)
- [로그 분석](#log-analytics)
- [인앱 메시지(선택 사항)](#in-app-messages)
- [콘텐츠 카드(선택 사항)](#content-cards)
- [다음 단계](#next-steps)

### BrazeManager.swift 생성

{% tabs local %}
{% tab 신속한 BrazeManager 생성 %}

##### BrazeManager.swift 생성
`BrazeManager.swift` 파일을 빌드하려면 _BrazeManager_라는 이름의 Swift 파일을 새로 생성하여 원하는 위치의 프로젝트에 추가합니다. 그런 다음, `import Foundation`을 `import AppboyUI`(SPM의 경우) 또는 `import Appboy_iOS_SDK`(CocoaPods의 경우)로 바꾸고, 모든 Braze 관련 메서드와 변수를 호스팅하는 데 사용할 `BrazeManager` 클래스를 생성합니다. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager`는 구조가 아닌 `NSObject` 클래스이므로 `ABKInAppMessageUIDelegate`와 같은 ABK 위임을 준수할 수 있습니다.
- `BrazeManager`는 싱글톤 클래스이므로 이 클래스의 인스턴스만 사용하도록 설계되었습니다. 이는 개체에 대한 통합 액세스 지점을 제공하기 위해 수행됩니다.
{% endalert %} 

1. `BrazeManager` 클래스를 초기화하는 _shared라는_ 정적 변수를 추가합니다. 이는 한 번만 느린 시작을 보장합니다.
2. 그런 다음, _apiKey_라는 비공개 상수 변수를 추가하고 Braze 대시보드의 워크스페이스에서 API 키 값으로 설정합니다.
3. SDK에 대한 구성 값을 저장할 _appboyOptions_라는 비공개 계산 변수를 추가합니다. 지금은 비어 있습니다.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()
  
  // 2
  private let apikey = "YOUR-API-KEY"
  
  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager
 
// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}
 
// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}
 
// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### SDK 초기화

{% tabs local %}
{% tab 1단계: BrazeManager에서 SDK 초기화하기 %}

##### BrazeManager.swift에서 SDK 초기화
다음으로 SDK를 초기화해야 합니다. 이 가이드에서는 이미 Xcode 프로젝트에 [SDK를 추가]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/)했다고 가정합니다. 또한 [워크스페이스 SDK 엔드포인트]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#step-2-specify-your-data-cluster)가 있어야 하고 `Info.plist` 파일 또는 `appboyOptions`에서 [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#braze-log-level)이 설정되어 있어야 합니다.

`BrazeManager.swift` 파일에서 반환 유형 없이 `AppDelegate.swift` 파일에서 `didFinishLaunchingWithOptions` 메서드를 추가합니다. `BrazeManager.swift` 파일에 비슷한 방법을 생성하면 `AppDelegate.swift` 파일에 `import AppboyUI` 문이 생기지 않습니다. 

그런 다음, 새로 선언한 `apiKey` 및 `appboyOptions` 변수를 사용하여 SDK를 초기화합니다.

{% alert important %}
초기화는 메인 스레드에서 수행해야 합니다.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab 2단계: Appboy 초기화 처리 %}

##### AppDelegate.swift에서 Appboy 초기화 처리
그런 다음, `AppDelegate.swift` 파일로 돌아가 AppDelegate의 `didFinishLaunchingWithOptions` 메서드에 다음 코드 스니펫을 추가하여 `BrazeManager.swift` 헬퍼 파일에서 Appboy 초기화를 처리합니다. `AppDelegate.swift` 에 `import AppboyUI` 문을 추가할 필요가 없다는 점을 기억하세요.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication, 
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch
 
  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];
   
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다.<br><br>이 시점에서 SDK가 가동 및 실행 중이어야 합니다. 대시보드에서 더 진행하기 전에 세션이 기록되는지 관찰합니다.
{% endalert %}

### 푸시 알림

{% tabs local %}
{% tab 1단계: 푸시 인증서 추가 %}

##### 푸시 인증서 추가

Braze 대시보드에서 기존 작업 공간으로 이동합니다. **푸시 알림 설정에서** 푸시 인증서 파일을 Braze 대시보드에 업로드하고 저장합니다. 

![]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab 2단계: 알림 등록하기 %}

{% alert important %}
이 단계의 마지막에 있는 전용 체크포인트를 놓치지 마세요!
{% endalert %}

##### 푸시 알림 등록하기

다음으로 푸시 알림을 등록합니다. 이 가이드에서는는 Apple 개발자 포털 및 Xcode 프로젝트에서 [푸시 자격 증명을 올바르게 설정]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/)했다고 가정합니다. 

푸시 알림을 등록하는 코드는 `BrazeManager.swift` 파일의 `didFinishLaunching...` 메소드에 추가됩니다. 초기화 코드는 다음과 같이 완성되어야 합니다:

1. 사용자와 상호 작용하기 위한 권한 요청 콘텐츠를 구성합니다. 이러한 옵션은 예시로 나열되어 있습니다.
2. 사용자에게 푸시 알림을 보낼 수 있는 권한을 요청하세요. 푸시 알림을 허용하거나 거부하는 사용자의 응답은 `granted` 변수에서 추적됩니다.
3. 사용자가 알림 프롬프트와 상호 작용한 후 푸시 인증 결과를 Braze에 전달합니다.
4. APN으로 등록 프로세스를 시작합니다. 이 작업은 기본 스레드에서 수행해야 합니다. 등록이 성공하면 앱이 `AppDelegate` 객체의 `didRegisterForRemoteNotificationsWithDeviceToken` 메서드를 호출합니다. 

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1 
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2 
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3 
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  
  // 4 
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
   
  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
 
  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다.
- 더 진행하기 전에 앱에서 푸시 알림 메시지가 표시되는지 확인하세요.
- 프롬프트가 표시되지 않으면 앱을 삭제한 후 다시 설치하여 이전에 푸시 알림 프롬프트가 표시되지 않았는지 확인합니다.

더 진행하기 전에 푸시 알림 메시지가 표시되는지 확인합니다.
{% endalert %}

{% endtab %}
{% tab 3단계: 메서드 전달 %}

##### 전달 푸시 알림 방법

그런 다음, Braze iOS SDK에서 처리하도록 시스템 푸시 알림 메서드를 `AppDelegate.swift`에서 `BrazeManager.swift`로 전달합니다.

###### 1단계: 푸시 알림 코드 확장 만들기

`BrazeManager.swift` 파일에 푸시 알림 코드의 확장을 생성하여 다음과 같이 헬퍼 파일에서 어떤 용도를 지원하는지 보다 체계적으로 파악할 수 있도록 합니다.

1. `AppDelegate`에 `import AppboyUI` 문을 포함하지 않는 패턴에 따라 `BrazeManager.swift` 파일에서 푸시 알림 방법을 처리합니다. 사용자의 디바이스 토큰은 `didRegisterForRemote...` 메소드를 통해 Braze에 전달되어야 합니다. 이 방법은 무음 푸시 알림을 구현하는 데 필요합니다. 그런 다음, `BrazeManager` 클래스의 `AppDelegate`에서 동일한 메서드를 추가합니다.
2. 메서드 안에 다음 줄을 추가하여 디바이스 토큰을 Braze에 등록합니다. 이는 Braze가 토큰을 현재 장치와 연결하기 위해 필요합니다. 

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1 
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2 
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### 2단계: 원격 알림 지원
**서명 및 기능** 탭에서 **백그라운드 모드** 지원을 추가하고 **원격 알림을** 선택하여 Braze에서 발생하는 원격 푸시 알림 지원을 시작하세요.<br><br>![서명 및 기능]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### 3단계: 원격 알림 처리
Braze SDK는 Braze에서 발생하는 원격 푸시 알림을 처리할 수 있습니다. 원격 알림을 Braze로 전달합니다. 그러면 SDK는 Braze에서 발생하지 않은 푸시 알림을 자동으로 무시합니다. 푸시 알림 확장의 `BrazeManager.swift` 파일에 다음 메서드를 추가합니다.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication, 
  didReceiveRemoteNotification userInfo: [AnyHashable : Any], 
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application, 
    didReceiveRemoteNotification: userInfo, 
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### 4단계: 알림 응답 전달

Braze SDK는 Braze에서 발생하는 푸시 알림의 응답을 처리할 수 있습니다. 알림의 응답을 Braze로 전달합니다. 그러면 SDK는 Braze에서 발생하지 않은 푸시 알림의 응답을 자동으로 무시합니다. `BrazeManager.swift` 파일에 다음 메서드를 추가합니다:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter, 
  didReceive response: UNNotificationResponse, 
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center, 
    didReceive: response, 
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response 
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center 
                   didReceiveNotificationResponse:response 
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다. <br><br>더 진행하기 전에 Braze 대시보드에서 푸시 알림을 직접 보내고 푸시 알림에서 분석이 기록되는지 관찰합니다.
{% endalert %}

### 사용자 변수 및 메서드 액세스

{% tabs local %}
{% tab 사용자 변수 및 메서드 생성 %}

##### 사용자 변수 및 메서드 생성

다음으로 `ABKUser` 변수와 메서드에 쉽게 액세스할 수 있어야 합니다. `BrazeManager.swift` 파일에 사용자 코드의 확장을 생성하여 다음과 같이 헬퍼 파일에서 어떤 용도를 지원하는지 보다 체계적으로 파악할 수 있도록 합니다.

1. `ABKUser` 개체는 iOS 애플리케이션에서 알려진 사용자 또는 익명 사용자를 나타냅니다. `ABKUser`를 검색하도록 컴퓨팅 변수를 추가합니다. 이 변수는 사용자에 대한 변수를 검색하는 데 재사용됩니다.
2. 사용자 변수를 쿼리하여 `userId` 에 쉽게 액세스할 수 있습니다. 다른 변수 중에서도 `ABKUser` 오브젝트는 `firstName`, `lastName`, `phone`, `homeCity` 등을 담당합니다.
3. 해당 `userId`로 `changeUser()`를 호출하여 사용자를 설정합니다.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2 
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}
   
   // 2 
- (NSString *)userId {
  return [self user].userID;
}
 
  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다.<br><br>로그인/가입에 성공한 사용자를 식별해 보세요. 적절한 사용자 식별자와 부적절한 사용자 식별자를 확실히 이해해야 합니다. <br><br>대시보드에서 더 진행하기 전에 사용자 식별자가 기록되는지 관찰합니다.
{% endalert %} 

### 로그 분석

{% tabs local %}
{% tab 1단계: 사용자 지정 이벤트 %}

##### 로그 사용자 지정 이벤트 메서드 생성

다음 Braze SDK `logCustomEvent` 메소드를 기반으로 일치하는 메소드를 생성합니다. 

**Braze `logCustomEvent` 참조 메서드**<br>
`BrazeManager.swift` 파일만 Braze iOS SDK 메서드에 직접 액세스할 수 있기 때문에 의도된 것입니다. 따라서 일치하는 메서드를 생성하면 결과는 동일하며 프로덕션 코드에서 Braze iOS SDK에 직접 종속될 필요 없이 수행됩니다.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**매칭 방법**<br>
`Appboy` 오브젝트에서 Braze로 커스텀 이벤트를 기록합니다. `Properties`는 기본값이 nil인 선택적 매개변수입니다. 사용자 지정 이벤트에는 속성이 필요하지 않지만 이름이 있어야 합니다. 

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 2단계: 사용자 지정 속성 %}

##### 로그 사용자 지정 속성 만들기 메서드 

SDK는 다양한 유형을 사용자 정의 속성으로 기록할 수 있습니다. 설정할 수 있는 각 값 유형에 대해 헬퍼 메서드를 만들 필요가 없습니다. 대신 적절한 값으로 필터링할 수 있는 하나의 메서드만 노출하세요.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

사용자 지정 속성은 `ABKUser` 객체에서 로깅됩니다. 

속성에 설정할 수 있는 모든 유형을 포괄하는 **하나의 메서드**를 생성합니다. 분석 확장의 `BrazeManager.swift` 파일에 이 메서드를 추가합니다. 유효한 커스텀 속성 유형을 필터링하고 일치하는 유형과 연결된 메서드를 호출하면 됩니다.

- `value` 매개변수는 `Equatable` 프로토콜을 따르는 일반 유형입니다. 이 작업은 명시적으로 수행되므로 유형이 Braze iOS SDK가 예상하는 것과 다르면 컴파일 시 오류가 발생합니다.
- `key` 및 `value` 매개변수는 메서드에서 조건부로 래핑 해제되는 선택적 매개변수입니다. nil이 아닌 값이 Braze iOS SDK에 전달되도록 보장하는 한 가지 방법일 뿐입니다.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 3단계: 구매 %}

##### 로그 구매 방법 만들기

다음으로, 다음 Braze SDK `logPurchase` 메서드를 기반으로 일치하는 메서드를 생성합니다. 

**Braze `logPurchase` 참조 메서드**<br>
`BrazeManager.swift` 파일만 Braze iOS SDK 메서드에 직접 액세스할 수 있기 때문에 의도된 것입니다. 따라서 일치하는 메서드를 생성하면 결과는 동일하며 프로덕션 코드에서 Braze iOS SDK에 직접 종속될 필요 없이 수행됩니다. 

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**매칭 방법**<br>
`Appboy` 객체에서 구매를 Braze에 기록합니다. SDK에는 구매를 기록하는 여러 가지 방법이 있으며, 이는 한 가지 예일 뿐입니다. 이 메서드는 `NSDecimal` 및 `UInt` 객체 생성도 처리합니다. 이 부분을 어떻게 처리할 것인지는 여러분이 결정할 수 있으며, 이는 하나의 예시일 뿐입니다.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다. <br><br>사용자 지정 이벤트를 로깅해 보세요.<br><br>대시보드에서 더 진행하기 전에 사용자 지정 이벤트가 기록되는지 확인합니다.
{% endalert %}

### 인앱 메시지

{% tabs local %}
{% tab 1단계: 위임 준수 %}

{% alert important %}
애플리케이션에서 이 채널을 사용할 계획이 없는 경우 다음 인앱 메시지 섹션은 통합에 필요하지 않습니다.
{% endalert %}

##### ABKInAppMessageUIDelegate 준수

그런 다음, `ABKInAppMessageUIDelegate`를 준수하도록 `BrazeManager.swift` 파일 코드를 활성화하여 관련 메서드를 직접 처리합니다. 

위임을 준수하기 위한 코드는 `BrazeManager.swift` 파일의 `didFinishLaunching...` 메서드에 추가됩니다. 초기화 코드는 다음과 같이 완성됩니다:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
   
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 2단계: 위임 메서드 추가 %}

##### 델리게이트 메서드 추가
그런 다음 `ABKInAppMessageUIDelegate` 을 준수하는 확장자를 만듭니다.

분석 섹션에 다음 코드 스니펫을 추가합니다. `BrazeManager.swift` 오브젝트가 위임으로 설정되어 있으며, 여기에서 `BrazeManager.swift` 파일이 모든 `ABKInAppMessageUIDelegate` 메서드를 처리합니다. 

{% alert important %}
`ABKInAppMessageUIDelegate`에는 필수 메서드가 제공되지 않지만 다음은 한 가지 예입니다.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다. <br><br>인앱 메시지를 직접 보내 보세요. <br><br>`BrazeManager.swift` 파일에서 예제 `ABKInAppMessageUIDelegate` 메서드의 항목에 중단점을 설정합니다. 더 진행하기 전에 인앱 메시지를 직접 보내고 중단점에 도달했는지 확인합니다.
{% endalert %}

### 콘텐츠 카드

{% tabs local %}
{% tab 콘텐츠 카드 변수 및 메서드 생성 %}

{% alert important %}
애플리케이션에서 이 채널을 사용할 계획이 없는 경우 다음 콘텐츠 카드 섹션은 통합에 필요하지 않습니다.
{% endalert %}

##### 콘텐츠 카드 변수 및 메서드 만들기

프로덕션 코드에서 불필요한 `import AppboyUI` 문 없이도 콘텐츠 카드 보기 컨트롤러를 표시할 수 있습니다. 

`BrazeManager.swift` 파일에 콘텐츠 카드 코드의 확장을 생성하여 다음과 같이 헬퍼 파일에서 어떤 용도를 지원하는지 보다 체계적으로 파악할 수 있도록 합니다.

1. `ABKContentCardsTableViewController` 을 표시합니다. `navigationController` 옵션은 보기 컨트롤러를 표시하거나 푸시하는 데 필요한 유일한 매개변수입니다.
2. `ABKContentCardsTableViewController` 개체를 초기화하고 선택적으로 제목을 변경합니다. 또한 초기화된 보기 컨트롤러를 탐색 스택에 추가해야 합니다.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1 
  func displayContentCards(navigationController: UINavigationController?) {
      
    // 2 
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행합니다.<br><br>더 진행하기 전에 애플리케이션에 `ABKContentCardsTableViewController`를 표시해 보세요.
{% endalert %}

## 다음 단계

축하합니다! 이 모범 사례 통합 가이드를 완료하셨습니다! 예제 `BrazeManager` 헬퍼 파일은 [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)에서 찾을 수 있습니다.

나머지 프로덕션 코드에서 Braze iOS SDK에 대한 종속성을 분리했으므로 다음 고급 구현 가이드(선택 사항)를 확인하세요.
- [고급 푸시 알림 구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [고급 인앱 메시지 구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [고급 콘텐츠 카드 구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

