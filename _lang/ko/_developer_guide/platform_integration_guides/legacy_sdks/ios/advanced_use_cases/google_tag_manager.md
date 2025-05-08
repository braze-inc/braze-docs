---
nav_title: Google 태그 관리자
article_title: iOS용 Google Tag Manager
platform: iOS
page_order: 7
description: "이 문서에서는 iOS 앱용 Google Tag Manager를 초기화, 구성 및 구현하는 방법을 다룹니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 Google Tag Manager

## SDK 초기화 {#initializing-ios-google-tag-provider}

Braze iOS SDK는 [Google 태그 관리자](https://tagmanager.google.com/) 내에서 구성된 태그를 통해 초기화 및 제어할 수 있습니다.

Google Tag Manager를 사용하기 전에 먼저 [초기 SDK 설정]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/)을 따르세요.

## Google Tag Manager 구성 {#configuring-ios-google-tag-manager}

이 예에서는 사용자가 노래를 들을 때 다양한 이벤트를 기록하려는 음악 스트리밍 앱이라고 가정해 보겠습니다. iOS용 Google Tag Manager를 사용하면 이 이벤트를 수신할 서드파티 공급업체를 제어하고 Braze 전용 태그를 만들 수 있습니다.

### 사용자 지정 이벤트

커스텀 이벤트는 `actionType`이 `logEvent`로 설정되어 기록됩니다. 예제의 Braze 커스텀 태그 공급자는 `eventName`을 사용하여 커스텀 이벤트 이름을 설정한다고 예상합니다.

시작하려면 `played song`과 동일한 '이벤트 이름'을 찾는 트리거를 만듭니다.

!['이벤트 이름'이 '재생된 노래'와 같을 때 일부 이벤트에 대해 트리거되도록 설정된 Google 태그 관리자의 사용자 지정 트리거입니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

그런 다음, 새 태그('Function Call')를 만들고 [커스텀 태그 공급자](#adding-ios-google-tag-provider)(이 문서의 뒷부분에서 설명함)의 클래스 경로를 입력합니다. 

이 태그는 방금 만든 `played song` 이벤트를 기록할 때 트리거됩니다. 

예제 태그의 커스텀 매개변수(키-값 페어)에서는 `eventName`을 `played song`으로 설정했으며, 이는 Braze에 기록되는 커스텀 이벤트 이름이 됩니다.

{% alert important %}
커스텀 이벤트를 보낼 때는 다음 예제와 같이 `actionType`을 `logEvent`로 설정하고 `eventName`에 대한 값을 설정합니다. 

이 예제에서 커스텀 태그 공급자는 이 키를 사용하여 Google Tag Manager에서 데이터를 수신할 때 수행할 작업과 Braze에 전송할 이벤트 이름을 결정합니다.
{% endalert %}

![클래스 경로 및 키-값 페어 필드에서 Google Tag Manager의 태그. 이 태그는 이전에 생성된 'played song' 트리거로 트리거되도록 설정됩니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

태그에 추가적인 키-값 페어 인수를 포함할 수 있습니다. 그러면 Braze에 커스텀 이벤트 속성정보로 전송됩니다. `eventName` 및 `actionType`은 커스텀 이벤트 속성정보에 대해 무시되지 않습니다. 다음 예제 태그에서는 `genre`를 전달합니다. 이 항목은 Google Tag Manager에서 태그 변수를 사용하여 정의되며, 해당 변수는 앱에 기록된 커스텀 이벤트에서 가져옵니다.

`genre` 이벤트 속성정보는 iOS용 Google Tag Manager가 데이터 레이어로 Firebase를 사용하기 때문에 'Firebase - 이벤트 매개변수' 변수로 Google Tag Manager에 전송됩니다.

![Google Tag Manager의 변수로, "Braze - Played Song Event" 태그에 "genre"가 이벤트 매개변수로 추가됩니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

마지막으로, 사용자가 앱에서 노래를 재생하면 Firebase 및 Google Tag Manager를 통해 태그의 트리거 이름(`played song`)과 일치하는 Firebase 분석 이벤트 이름을 사용하여 이벤트를 기록합니다.

{% tabs %}
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
{% tab 목표-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### changeUser 호출

`actionType`을 `changeUser`로 설정하고 `changeUser()`에 대한 호출이 수행됩니다. Braze 커스텀 태그 공급자는 태그 내 `externalUserId` 키-값 페어를 통해 Braze 사용자 ID를 설정한다고 예상합니다.

{% tabs %}
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

"클래스 경로"를 파일에 기록해 두십시오. 이는 [Google Tag Manager](https://tagmanager.google.com/) 콘솔에서 태그를 설정할 때 입력할 내용입니다.

이 예제에서는 커스텀 태그 공급자를 구성하는 여러 가지 방법 중 하나를 보여줍니다. 여기서는 Google Tag Manager에서 전송된 `actionType` 키-값 페어에 따라 호출할 Braze SDK 메서드를 결정합니다.

이 예제에서 지원되는 `actionType`은 `logEvent`, `customAttribute`, `changeUser`이지만, 태그 공급자가 Google Tag Manager에서 데이터를 처리하는 방식을 변경할 수도 있습니다.

`BrazeGTMTagManager.h` 파일에 다음 코드를 추가합니다:

{% tabs %}
{% tab 목표-C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

그리고 `BrazeGTMTagManager.m` 파일에 다음 코드를 추가합니다:

{% tabs %}
{% tab 목표-C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
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
  
  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                             andStringValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                                 andBOOLValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                              andIntegerValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDoubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Appboy custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:customAttributeKey
                                                           array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [[Appboy sharedInstance] changeUser:userId];
}

@end
```

{% endtab %}
{% endtabs %}

