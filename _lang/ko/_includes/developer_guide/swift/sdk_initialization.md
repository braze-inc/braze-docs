{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 지연 초기화 사용

Braze Swift SDK를 비동기적으로 초기화할 수 있으며 푸시 알림 처리가 유지됩니다. 서버에서 구성 데이터를 가져오거나 사용자 동의를 기다리는 등 SDK를 초기화하기 전에 다른 서비스를 설정해야 할 때 유용할 수 있습니다.

### 고려 사항

`Braze.prepareForDelayedInitialization(pushAutomation:)`을 사용할 때 SDK가 푸시 알림 자동화 기능을 자동으로 사용하도록 구성하고 있습니다. 푸시 알림을 처리하는 시스템 델리게이트 메서드는 Braze에서 발생하는 푸시 알림에 대해서는 호출되지 않습니다.

SDK는 SDK가 초기화된 **후에만** Braze 푸시 알림과 그에 따른 동작을 처리합니다. 예를 들어 사용자가 딥링크를 여는 푸시 알림을 탭하면 `Braze` 인스턴스가 초기화된 후에만 딥링크가 열립니다.

Braze 푸시 알림에 대한 추가 처리를 수행해야 하는 경우 [푸시 알림 업데이트 구독하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates) 참조하세요. 이전에 대기열에 추가된 푸시 알림의 업데이트를 받으려면 SDK를 초기화한 후 바로 구독 핸들러를 구현해야 한다는 점에 유의하세요.

### 1단계: SDK 준비

기본적으로 앱이 종료된 상태에서 최종 사용자가 푸시 알림을 열면 SDK가 초기화되기 전에는 푸시 알림을 처리할 수 없습니다.

[Braze Swift SDK 버전 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) 이상부터는 정적 헬퍼 메서드( [Braze.prepareForDelayedInitialization(pushAutomation:)를](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) 사용하여 이 작업을 처리할 수 있습니다. 이 방법은 푸시 자동화 시스템을 설정하여 지연 초기화를 위해 SDK를 준비합니다.

SDK가 초기화되기 전에 Braze에서 발생하는 모든 푸시 알림이 캡처되어 대기열에 대기합니다. SDK가 초기화되면 해당 푸시 알림은 SDK에 의해 처리됩니다. 이 메서드는 애플리케이션 수명 주기에서 가능한 한 빨리 호출해야 하며, `AppDelegate` 의 `application(_:didFinishLaunchingWithOptions:)` 메서드 내부 또는 그 이전에 호출해야 합니다.

{% alert note %}
Swift SDK는 Braze가 아닌 푸시 알림은 캡처하지 않으며, 시스템 델리게이트 메서드를 통해 계속 처리됩니다.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
SwiftUI 애플리케이션은 `prepareForDelayedInitialization()` 메서드를 호출하기 위해 [@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor) 프로퍼티 래퍼를 구현해야 합니다.

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation:)은 푸](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) 시 알림의 자동화 구성을 나타내는 `pushAutomation` 매개변수(선택 사항)를 사용합니다. 언제 [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) 가 `nil` 인 경우 실행 시 인증 요청을 제외한 모든 자동화 기능이 활성화됩니다.
{% endalert %}

### 2단계: SDK 초기화

지연 초기화를 위해 SDK를 준비한 후에는 나중에 언제든지 비동기식으로 SDK를 초기화할 수 있습니다. 그러면 SDK가 Braze에서 발생한 대기열에 있는 모든 푸시 알림 이벤트를 처리합니다.

Braze SDK를 초기화하려면 [표준 Swift SDK 초기화 프로세스를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/#step-2-update-your-app-delegate) 따르세요.

## Google Tag Manager 사용

Braze Swift SDK는 Google Tag Manager 내에서 구성된 태그를 통해 초기화 및 제어할 수 있습니다.

다음 예제에서 음악 스트리밍 앱은 사용자가 노래를 들을 때 다양한 이벤트를 기록하고자 합니다. iOS용 Google Tag Manager를 사용하여 Braze의 제3자 공급업체가 이 이벤트를 수신하는지 제어하고 Braze에 특정한 태그를 생성할 수 있습니다.

### 1단계: 커스텀 이벤트에 대한 트리거 생성

커스텀 이벤트는 `actionType`이 `logEvent`로 설정되어 기록됩니다. 이 예제에서 Braze 커스텀 태그 공급자는 커스텀 이벤트 이름이 `eventName`을 사용하여 설정되기를 기대하고 있습니다.

먼저, `played song`와 같은 `eventName`을 찾는 트리거를 생성합니다.

![Google 태그 관리자의 사용자 지정 트리거는 '이벤트 이름'이 '재생된 노래'와 같을 때 일부 이벤트에 대해 트리거되도록 설정합니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

다음으로, 새 태그( "Function Call"로도 알려짐)를 생성하고 이 기사에서 나중에 설명할 [커스텀 태그 공급자](#adding-ios-google-tag-provider)의 클래스 경로를 입력합니다. 이 태그는 `played song` 이벤트를 기록할 때 트리거됩니다. `eventName`이 `played song`로 설정되어 있으므로 Braze에 기록되는 커스텀 이벤트 이름으로 사용됩니다.

{% alert important %}
커스텀 이벤트를 보낼 때 `actionType`를 `logEvent`으로 설정하고 `eventName`에 값을 설정하여 Braze가 올바른 이벤트 이름과 수행할 작업을 수신하도록 합니다.
{% endalert %}

![클래스 경로 및 키-값 페어 필드에서 Google Tag Manager의 태그. 이 태그는 이전에 생성된 'played song' 트리거로 트리거되도록 설정됩니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

태그에 추가적인 키-값 페어 인수를 포함할 수 있습니다. 그러면 Braze에 커스텀 이벤트 속성정보로 전송됩니다. `eventName` 및 `actionType`은 커스텀 이벤트 속성정보에 대해 무시되지 않습니다. 다음 예제 태그에서 `genre`을 전달합니다. 이는 Google Tag Manager에서 태그 변수를 사용하여 정의되었으며 앱에서 기록된 커스텀 이벤트에서 가져온 것입니다.

`genre` 이벤트 속성정보는 iOS용 Google Tag Manager가 데이터 레이어로 Firebase를 사용하기 때문에 'Firebase - 이벤트 매개변수' 변수로 Google Tag Manager에 전송됩니다.

![Google Tag Manager의 변수로, "Braze - Played Song Event" 태그에 "genre"가 이벤트 매개변수로 추가됩니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

사용자가 앱에서 노래를 재생할 때 Firebase 및 Google Tag Manager를 통해 태그의 트리거 이름과 일치하는 Firebase 분석 이벤트 이름을 사용하여 이벤트를 기록합니다: `played song`:

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### 2단계: 커스텀 속성 기록

`actionType`을 `customAttribute`로 설정하여 커스텀 속성은 설정됩니다. Braze 커스텀 태그 공급자는 `customAttributeKey` 및 `customAttributeValue`를 통해 커스텀 속성 키-값을 설정한다고 예상합니다.

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### 3단계: `changeUser()` 호출

`actionType`을 `changeUser`로 설정하고 `changeUser()`에 대한 호출이 수행됩니다. Braze 커스텀 태그 공급자는 태그 내 `externalUserId` 키-값 페어를 통해 Braze 사용자 ID를 설정한다고 예상합니다.

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### 4단계: 커스텀 태그 제공자를 추가하세요 {#adding-ios-google-tag-provider}

태그 및 트리거를 설정한 상태에서 Google Tag Manager를 iOS 앱에서도 구현해야 합니다(Google [설명서](https://developers.google.com/tag-manager/ios/v5/) 참조).

Google Tag Manager가 앱에 설치된 후, Google Tag Manager 내에서 구성한 태그에 따라 Braze SDK 메서드를 호출하기 위해 커스텀 태그 제공자를 추가하세요.

파일의 '클래스 경로'는 [Google 태그 관리자](https://tagmanager.google.com/) 콘솔에서 태그를 설정할 때 입력하는 정보입니다.

이 예시는 커스텀 태그 제공자를 구조화할 수 있는 여러 방법 중 하나를 강조합니다. 특히, GTM 태그에서 전송된 `actionType` 키-값 페어에 따라 호출할 Braze SDK 메서드를 결정하는 방법을 보여줍니다. 이 예제에서는 AppDelegate에서 Braze 인스턴스를 변수로 할당했다고 가정합니다.

이 예제에서 지원되는 `actionType`은 `logEvent`, `customAttribute`, 및 `changeUser`이지만, Google Tag Manager에서 데이터를 처리하는 방법을 변경할 수 있습니다.
{% tabs %}
{% tab SWIFT %}

`BrazeGTMTagManager.swift` 파일에 다음 코드를 추가합니다.
```swift
import FirebaseAnalytics
import GoogleTagManager
import BrazeKit

let ActionTypeKey: String = "actionType"

// Custom Events
let LogEventAction: String = "logEvent"
let LogEventName: String = "eventName"

// Custom Attributes
let CustomAttributeAction: String = "customAttribute"
let CustomAttributeKey: String = "customAttributeKey"
let CustomAttributeValueKey: String = "customAttributeValue"

// Change User
let ChangeUserAction: String = "changeUser"
let ChangeUserExternalUserId: String = "externalUserId"

@objc(BrazeGTMTagManager)
final class BrazeGTMTagManager : NSObject, TAGCustomFunction {
  @objc func execute(withParameters parameters: [AnyHashable : Any]!) -> NSObject! {
    var parameters: [String : Any] = parameters as! [String : Any]
    guard let actionType: String = parameters[ActionTypeKey] as? String else {
      print("There is no Braze action type key in this call. Doing nothing.")
      return nil
    }
    parameters.removeValue(forKey: ActionTypeKey)
    if actionType == LogEventAction {
      logEvent(parameters: parameters)
    } else if actionType == CustomAttributeAction {
      logCustomAttribute(parameters: parameters)
    } else if actionType == ChangeUserAction {
      changeUser(parameters: parameters)
    }
    return nil
  }
  
  func logEvent(parameters: [String : Any]) {
    var parameters: [String : Any] = parameters
    guard let eventName: String = parameters[LogEventName] as? String else { return }
    parameters.removeValue(forKey: LogEventName)
    AppDelegate.braze?.logCustomEvent(name: eventName, properties: parameters)
  }
  
  func logCustomAttribute(parameters: [String: Any]) {
    guard let customAttributeKey = parameters[CustomAttributeKey] as? String else { return }
    let customAttributeValue = parameters[CustomAttributeValueKey]
    
    if let customAttributeValue = customAttributeValue as? String {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Date {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Double {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Bool {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Int {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttibuteValue = customAttributeValue as? [String] {
      AppDelegate.braze?.user.setCustomAttributeArray(key: customAttributeKey, array: customAttibuteValue)
    }
  }
  
  func changeUser(parameters: [String: Any]) {
    guard let userId = parameters[ChangeUserExternalUserId] as? String else { return }
    AppDelegate.braze?.changeUser(userId: userId)
  }
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
`BrazeGTMTagManager.h` 파일에 다음 코드를 추가합니다:

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

그리고 `BrazeGTMTagManager.m` 파일에 다음 코드를 추가합니다:

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "BrazeKit"
#import "AppDelegate.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventAction = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeAction = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserAction = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];
  
  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }
  
  [mutableParameters removeObjectForKey:ActionTypeKey];
  
  if ([actionType isEqualToString:LogEventAction]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeAction]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserAction]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [AppDelegate.braze logCustomEvent:eventName
                         properties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [AppDelegate.braze logCustomEvent:customAttributeKey
                           properties:parameters];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            dateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                              boolValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                               intValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            doubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Braze custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [AppDelegate.braze.user setCustomAttributeArrayWithKey:customAttributeKey
                                                     array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [AppDelegate.braze changeUser:userId];
}

@end
```
{% endtab %}
{% endtabs %}
