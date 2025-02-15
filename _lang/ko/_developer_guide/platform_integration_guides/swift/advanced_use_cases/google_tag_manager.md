---
nav_title: Google 태그 관리자
article_title: iOS용 Google Tag Manager
platform: Swift
page_order: 3
description: "이 문서에서는 Swift SDK용 Google Tag Manager를 초기화, 구성 및 구현하는 방법을 다룹니다."

---

# Google 태그 관리자

> Braze Swift SDK는 Google Tag Manager 내에서 구성된 태그를 통해 초기화 및 제어할 수 있습니다.

이 구현의 전제 조건으로 Swift SDK를 통합해야 합니다.

## Google Tag Manager 구성 {#configuring-ios-google-tag-manager}

이 예에서는 사용자가 노래를 들을 때 다양한 이벤트를 기록하려는 음악 스트리밍 앱이라고 가정해 보겠습니다. iOS용 Google Tag Manager를 사용하면 이 이벤트를 수신할 서드파티 공급업체를 제어하고 Braze 전용 태그를 만들 수 있습니다.

### 사용자 지정 이벤트

커스텀 이벤트는 `actionType`이 `logEvent`로 설정되어 기록됩니다. 이 예제의 Braze 사용자 지정 태그 공급자는 `eventName` 을 사용하여 사용자 지정 이벤트 이름을 설정할 것으로 예상하고 있습니다.

시작하려면 `played song`과 동일한 `eventName`을 찾는 트리거를 만듭니다.

![Google 태그 관리자의 사용자 지정 트리거는 '이벤트 이름'이 '재생된 노래'와 같을 때 일부 이벤트에 대해 트리거되도록 설정합니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

그런 다음, 새 태그('Function Call')를 만들고 [커스텀 태그 공급자](#adding-ios-google-tag-provider)(이 문서의 뒷부분에서 설명함)의 클래스 경로를 입력합니다. 

이 태그는 방금 만든 `played song` 이벤트를 기록할 때 트리거됩니다. 

예제 태그의 커스텀 매개변수(키-값 페어)에서는 `eventName`을 `played song`으로 설정했으며, 이는 Braze에 기록되는 커스텀 이벤트 이름이 됩니다.

{% alert important %}
커스텀 이벤트를 보낼 때는 다음 예제와 같이 `actionType`을 `logEvent`로 설정하고 `eventName`에 대한 값을 설정합니다.
<br><br>
이 예제에서 커스텀 태그 공급자는 이 키를 사용하여 Google Tag Manager에서 데이터를 수신할 때 수행할 작업과 Braze에 전송할 이벤트 이름을 결정합니다.
{% endalert %}

![클래스 경로 및 키-값 페어 필드에서 Google Tag Manager의 태그. 이 태그는 이전에 생성한 '재생된 노래' 트리거와 함께 트리거되도록 설정되어 있습니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

태그에 추가적인 키-값 페어 인수를 포함할 수 있습니다. 그러면 Braze에 커스텀 이벤트 속성정보로 전송됩니다. `eventName` 및 `actionType`은 커스텀 이벤트 속성정보에 대해 무시되지 않습니다. 다음 예제 태그에서는 `genre`를 전달합니다. 이 항목은 Google Tag Manager에서 태그 변수를 사용하여 정의되며, 해당 변수는 앱에 기록된 커스텀 이벤트에서 가져옵니다.

`genre` 이벤트 속성정보는 iOS용 Google Tag Manager가 데이터 레이어로 Firebase를 사용하기 때문에 'Firebase - 이벤트 매개변수' 변수로 Google Tag Manager에 전송됩니다.

![Google 태그 관리자에서 '장르'가 'Braze - 재생한 노래 이벤트' 태그의 이벤트 파라미터로 추가되는 변수입니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

마지막으로, 사용자가 앱에서 노래를 재생하면 Firebase 및 Google Tag Manager를 통해 태그의 트리거 이름(`played song`)과 일치하는 Firebase 분석 이벤트 이름을 사용하여 이벤트를 기록합니다.

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab 목표-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 로깅

`actionType`을 `customAttribute`로 설정하여 커스텀 속성은 설정됩니다. Braze 커스텀 태그 공급자는 `customAttributeKey` 및 `customAttributeValue`를 통해 커스텀 속성 키-값을 설정한다고 예상합니다.

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab 목표-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### changeUser 호출

`actionType`을 `changeUser`로 설정하고 `changeUser()`에 대한 호출이 수행됩니다. Braze 커스텀 태그 공급자는 태그 내 `externalUserId` 키-값 페어를 통해 Braze 사용자 ID를 설정한다고 예상합니다.

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab 목표-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

## Braze SDK 사용자 지정 태그 공급자 {#adding-ios-google-tag-provider}

태그 및 트리거를 설정한 상태에서 Google Tag Manager를 iOS 앱에서도 구현해야 합니다(Google [설명서](https://developers.google.com/tag-manager/ios/v5/) 참조).

앱에 Google Tag Manager를 설치한 후 Google Tag Manager 내에서 구성한 태그를 기반으로 Braze SDK 메서드를 호출하기 위해 커스텀 태그 제공자를 추가합니다. 

파일의 '클래스 경로'는 [Google 태그 관리자](https://tagmanager.google.com/) 콘솔에서 태그를 설정할 때 입력하는 정보입니다.

이 예제에서는 커스텀 태그 공급자를 구성하는 여러 가지 방법 중 하나를 보여줍니다. 여기서는 Google Tag Manager에서 전송된 `actionType` 키-값 페어에 따라 호출할 Braze SDK 메서드를 결정합니다. 이 예제에서는 AppDelegate에서 Braze 인스턴스를 변수로 할당했다고 가정합니다.

이 예제에서 지원되는 `actionType`은 `logEvent`, `customAttribute`, `changeUser`이지만, 태그 공급자가 Google Tag Manager에서 데이터를 처리하는 방식을 변경할 수도 있습니다.
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

