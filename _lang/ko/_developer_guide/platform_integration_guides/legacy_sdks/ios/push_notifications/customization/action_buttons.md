---
nav_title: 실행 버튼
article_title: iOS용 푸시 액션 버튼
platform: iOS
page_order: 1
description: "이 참조 문서에서는 iOS 푸시 알림에서 실행 버튼을 구현하는 방법을 다룹니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 실행 버튼 {#push-action-buttons-integration}

Braze iOS SDK는 각 푸시 실행 버튼에 대한 URL 처리 지원을 포함하여 기본 푸시 카테고리를 지원합니다. 현재 기본 카테고리에는 네 가지 푸시 액션 버튼 세트가 있습니다: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, `More` 입니다. 

![푸시 메시지를 아래로 당겨서 두 개의 사용자 지정 가능한 작업 버튼을 표시하는 GIF.]({% image_buster /assets/img_archive/iOS8Action.gif %})

기본 푸시 카테고리를 등록하려면 통합 지침을 따릅니다.

## 1단계: Braze 기본 푸시 카테고리 추가하기

[푸시를 등록할]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze) 때 다음 코드를 사용하여 기본 푸시 카테고리에 등록하세요:

{% tabs %}
{% tab 목표-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

백그라운드 활성화 모드에서 푸시 동작 버튼을 클릭하면 알림만 해제되고 앱은 열리지 않습니다. 다음에 사용자가 앱을 열면 이 작업에 대한 버튼 클릭 분석이 서버로 플러시됩니다.

나만의 사용자 지정 알림 카테고리를 만들려면 [작업 버튼 사용자 지정을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization) 참조하세요.

## 2단계: 대화형 푸시 처리 사용

`UNNotification` 프레임워크를 사용하고 Braze [델리게이트를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) 구현한 경우 이 메서드가 이미 통합되어 있을 것입니다. 

클릭 분석 및 URL 라우팅을 포함한 푸시 액션 버튼 처리를 활성화하려면 앱의 `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 델리게이트 메서드에 다음 코드를 추가하세요:

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

UNNotification 프레임워크를 사용하지 않는 경우, 앱의 `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:`에 다음 코드를 추가하여 푸시 실행 버튼 처리를 활성화해야 합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
`handleActionWithIdentifier`를 사용하시는 사용자는 `UNNotification` 프레임워크를 사용하기 시작하도록 강력히 권장합니다. [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc)의 사용 중단으로 인해 권장합니다.
{% endalert %}

## 푸시 카테고리 사용자 지정

Braze는 [기본 푸시 카테고리]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/) 세트를 제공하는 것 외에도 사용자 지정 알림 카테고리 및 작업을 지원합니다. 애플리케이션에 카테고리를 등록한 후 Braze 대시보드를 사용하여 사용자에게 알림 카테고리를 보낼 수 있습니다.

`UserNotifications` 프레임워크를 사용하지 않는 경우 [대체 카테고리](https://developer.apple.com/documentation/usernotifications/unnotificationcategory) 문서를 참조하세요.

그런 다음 대시보드를 통해 이러한 카테고리를 푸시 알림에 할당하여 디자인의 액션 버튼 구성을 트리거할 수 있습니다. 다음은 기기에 표시되는 `LIKE_CATEGORY`를 활용하는 예제입니다.

!['싫어요' 및 '좋아요' 푸시 동작 버튼 두 개를 표시하는 푸시 메시지]({% image_buster /assets/img_archive/push_example_category.png %})


