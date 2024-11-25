---
nav_title: 실행 버튼
article_title: iOS용 푸시 액션 버튼
platform: Swift
page_order: 1
description: "이 문서에서는 Swift SDK용 iOS 푸시 알림에서 실행 버튼을 구현하는 방법을 다룹니다."
channel:
  - push

---

# 실행 버튼 {#push-action-buttons-integration}

> Braze Swift SDK는 푸시 액션 버튼에 대한 URL 처리 지원을 제공합니다. 

Braze 기본 푸시 카테고리에는 네 가지 기본 푸시 실행 버튼 세트(`Accept/Decline`, `Yes/No`, `Confirm/Cancel`, `More`)가 있습니다. 

![푸시 메시지를 아래로 당겨서 두 개의 사용자 지정 가능한 작업 버튼을 표시하는 GIF.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

나만의 사용자 지정 알림 카테고리를 만들려면 [작업 버튼 사용자 지정을](#push-category-customization) 참조하세요.

## 자동 통합(권장)

`configuration.push.automation` 구성 옵션을 사용하여 푸시를 통합하는 경우, Braze는 기본 푸시 카테고리에 대한 액션 버튼을 자동으로 등록하고 푸시 액션 버튼 클릭 분석 및 URL 라우팅을 처리합니다.

## 수동 통합

이러한 푸시 실행 버튼을 수동으로 활성화하려면 먼저 기본 푸시 카테고리에 등록합니다. 그런 다음 `didReceive(_:completionHandler:)` 델리게이트 메서드를 사용하여 푸시 동작 버튼을 활성화합니다.

### 1단계: Braze 기본 푸시 카테고리 추가하기 {#registering}

[푸시 등록]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) 시 다음 코드를 사용하여 기본 푸시 카테고리에 등록하세요:

{% tabs %}
{% tab swift %}

```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab 목표-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
백그라운드 활성화 모드에서 푸시 동작 버튼을 클릭하면 알림만 해제되고 앱은 열리지 않습니다. 다음에 사용자가 앱을 열면 이 작업에 대한 버튼 클릭 분석이 서버로 플러시됩니다.
{% endalert %}

### 2단계: 대화형 푸시 처리 활성화 {#enable-push-handling}

클릭 분석 및 URL 라우팅을 포함한 푸시 액션 버튼 처리를 활성화하려면 앱의 `didReceive(_:completionHandler:)` 델리게이트 메서드에 다음 코드를 추가하세요:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

`UNNotification` 프레임워크를 사용하고 Braze [알림 방법을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) 구현한 경우 이 방법이 이미 통합되어 있을 것입니다. 

## 푸시 카테고리 사용자 지정

Braze는 기본 푸시 카테고리 세트를 제공할 뿐만 아니라 커스텀 알림 카테고리 및 작업을 지원합니다. 애플리케이션에 카테고리를 등록한 후 Braze 대시보드를 사용하여 이러한 사용자 지정 알림 카테고리를 사용자에게 보낼 수 있습니다.

그런 다음 대시보드를 통해 이러한 카테고리를 푸시 알림에 할당하여 디자인의 액션 버튼 구성을 트리거할 수 있습니다. 

### 사용자 지정 푸시 카테고리 예시

다음은 기기에 표시되는 `LIKE_CATEGORY`를 활용하는 예제입니다.

!['싫어요' 및 '좋아요' 푸시 동작 버튼 두 개를 표시하는 푸시 메시지]({% image_buster /assets/img_archive/push_example_category.png %})

#### 1단계: 카테고리 등록

앱에 카테고리를 등록하려면 다음과 유사한 방법을 사용합니다:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab 목표-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
`UNNotificationAction`을 생성할 때 작업 옵션 목록을 지정할 수 있습니다. 예를 들어 `UNNotificationActionOptions.foreground`는 사용자가 실행 버튼을 탭한 후 앱을 열도록 합니다. '앱 열기' 및 '애플리케이션으로 딥 링크'와 같은 탐색 관련 클릭 시 동작에 필요합니다. 자세한 내용은 [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)를 참조하세요.
{% endalert %}

#### 2단계: 카테고리 선택

카테고리를 등록한 후 Braze 대시보드를 사용하여 해당 유형의 알림을 사용자에게 발송합니다.

{% alert tip %}
앱으로 딥링킹하거나 URL을 여는 등 _특별한 동작이_ 있는 액션 버튼에 대해서만 사용자 지정 알림 카테고리를 정의하면 됩니다. 알림을 해제하기만 하는 실행 버튼에 대해서는 정의할 필요가 없습니다.
{% endalert %}

1. Braze 대시보드에서 **메시징** > **푸시 알림**을 선택한 다음, iOS [푸시 캠페인]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message)을 선택합니다.
2. **푸시 알림 작성에서** **작업 버튼을** 켭니다.
3. **iOS 알림 카테고리** 드롭다운에서 **미리 등록한 커스텀 iOS 카테고리 입력**을 선택합니다.
4. 마지막으로 앞서 만든 카테고리 중 하나를 입력합니다. 다음 예에서는 사용자 지정 카테고리를 사용합니다: `LIKE_CATEGORY`.

![사용자 지정 카테고리를 설정할 수 있는 푸시 알림 캠페인 대시보드]({% image_buster /assets/img_archive/ios-notification-category.png %})

