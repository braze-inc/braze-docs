---
nav_title: 통합
article_title: iOS용 푸시 통합
platform: Swift
page_order: 0
description: "이 참조 문서에서는 Braze Swift SDK의 푸시 알림을 설정하는 방법을 다룹니다."
channel:
  - push
  
---

# 푸시 알림 통합

> 이 참조 문서에서는 Braze Swift SDK의 푸시 알림을 설정하는 방법을 다룹니다.

[푸시 알림]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)을 사용하면 중요한 이벤트가 발생할 때 앱에서 알림을 보낼 수 있습니다. 전달할 새 인스턴트 메시지, 송출할 뉴스 속보 알림 또는 오프라인으로 시청할 수 있도록 다운로드할 준비가 된 사용자가 좋아하는 TV 프로그램의 최신 에피소드가 있을 때 푸시 알림을 전송할 수 있습니다. 푸시 알림은 앱의 인터페이스를 업데이트하거나 백그라운드 작업을 트리거할 때만 사용하도록 [무음으로]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) 설정할 수도 있습니다. 

푸시 알림은 백그라운드 가져오기 사이의 지연이 허용되지 않을 수도 있는 산발적이지만 바로 중요한 콘텐츠에 적합합니다. 필요할 때만 애플리케이션이 실행되므로 푸시 알림은 백그라운드 가져오기보다 훨씬 효율적일 수도 있습니다. 

푸시 알림은 전송 횟수에 제한이 있으므로 애플리케이션에 필요한 만큼 많이 보내는 것을 두려워하지 마세요. iOS 및 Apple 푸시 알림 서비스(APN) 서버가 알림 전송 빈도를 제어하므로 너무 많이 보내도 문제가 발생하지 않습니다. 푸시 알림이 제한되는 경우, 기기가 다음 번에 연결 유지 패킷을 보내거나 다른 알림을 받을 때까지 지연될 수 있습니다.

## 초기 설정

### 1단계: APN 인증서 업로드

Braze를 사용하여 iOS 푸시 알림을 보내려면 먼저 Apple에서 제공하는 `.p8` 푸시 알림 파일을 제공해야 합니다. Apple [개발자 설명서](https://developer.apple.com/documentation/usernotifications)에서 설명합니다.

1. Apple 개발자 계정에서 [**인증서, 식별자 및 프로필**](https://developer.apple.com/account/ios/certificate)로 이동합니다.
2. **키**에서 **모두**를 선택하고 오른쪽 상단에 있는 추가 버튼(+)을 클릭합니다.
3. **키 설명**에 서명 키의 고유한 이름을 입력합니다.
4. **주요 서비스에서** **Apple 푸시 알림 서비스(APN)** 확인란을 선택한 다음 **계속을** 클릭합니다. **확인**을 클릭합니다.
5. 키 ID를 기록해 두세요. **다운로드**를 클릭하여 키를 생성하고 다운로드합니다. 다운로드한 파일은 두 번 이상 다운로드할 수 없으므로 안전한 곳에 저장하세요.
6. Braze에서 **설정** > **앱 설정으로** 이동하여 **Apple 푸시 인증서** 아래에 `.p8` 파일을 업로드합니다. 개발 또는 프로덕션 푸시 인증서를 업로드할 수 있습니다. 앱이 App Store에 출시된 후 푸시 알림을 테스트하려면 앱의 개발 버전을 위한 별도의 워크스페이스를 설정하는 것이 좋습니다.
7. 프롬프트가 표시되면 앱의 [번들 ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), [키 ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) 및 [팀 ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id)를 입력한 다음, **저장**을 클릭합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **설정 관리** > **설정**에서 `.p8` 파일을 업로드할 수 있습니다.
{% endalert %}

### 2단계: 푸시 기능 사용

Xcode에서 기본 앱 대상의 **서명 및 기능** 섹션으로 이동하여 푸시 알림 기능을 추가합니다.

![Xcode 프로젝트의 '서명 및 기능' 섹션]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## 자동 푸시 통합

Swift SDK는 구성 전용 접근 방식을 제공하여 Braze에서 수신한 원격 알림을 자동으로 처리합니다. 이 방법은 푸시 알림을 통합하는 가장 간단한 방법이며 대부분의 고객에게 권장됩니다.

자동 푸시 통합을 활성화하려면 `push` 구성의 `automation` 속성정보를 `true`로 설정합니다.

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab 목표-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

이렇게 하면 SDK에 다음을 지시합니다:
- 시스템에서 푸시 알림 신청을 등록하세요.
- 초기화 시 푸시 알림 승인/허가를 요청하세요.
- 푸시 알림 관련 시스템 위임 메서드에 대한 구현을 동적으로 제공합니다.

{% alert note %}
SDK에서 수행하는 자동화 단계는 코드베이스의 기존 푸시 알림 처리 통합과 호환됩니다. SDK는 Braze에서 수신한 원격 알림의 처리만 자동화합니다. 자체 또는 다른 서드파티 SDK 원격 알림을 처리하기 위해 구현된 모든 시스템 핸들러는 `automation`이 활성화되어 있어도 계속 작동합니다.
{% endalert %}

{% alert warning %}
푸시 알림 자동화를 활성화하려면 기본 스레드에서 SDK를 초기화해야 합니다. SDK 초기화는 애플리케이션 실행이 완료되기 전 또는 AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 구현에서 수행해야 합니다.
애플리케이션에 SDK를 초기화하기 전에 추가 설정이 필요한 경우 [지연된 초기화]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) 문서 페이지를 참조하세요.
{% endalert %}

### 개별 구성 재정의하기

보다 세분화된 제어를 위해 각 자동화 단계를 개별적으로 활성화 또는 비활성화할 수 있습니다:

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab 목표-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

사용 가능한 모든 옵션은 [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class)을 참조하고, 자동화 동작에 대한 자세한 내용은 [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property)을 참조하세요.

자동 푸시 통합 기능을 사용하는 경우 다음 섹션을 건너뛰고 [딥링킹](#deep-linking)을 계속 진행할 수 있습니다.

## 수동 푸시 통합

푸시 알림은 수동으로 통합할 수도 있습니다. 이 섹션에서는 이 통합에 필요한 단계를 설명합니다. 

{% alert note %}
앱에 특정한 추가 동작을 위해 푸시 알림에 의존하는 경우 여전히 수동 푸시 알림 통합 대신 자동 푸시 통합을 사용할 수 있습니다. [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) 메서드를 통해 Braze에서 처리된 원격 알림을 수신할 수 있습니다.
{% endalert %}

### 1단계: APN으로 푸시 알림 등록하기

앱의 [`application:didFinishLaunchingWithOptions:` 델리게이트 메서드에](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 적절한 코드 샘플을 포함시켜 사용자의 디바이스가 APN에 등록할 수 있도록 합니다. 애플리케이션의 메인 스레드에서 모든 푸시 연동 코드를 호출해야 합니다.

Braze는 푸시 액션 버튼 지원을 위한 기본 푸시 카테고리도 제공하며, 이 카테고리는 푸시 등록 코드에 수동으로 추가해야 합니다. 추가 통합 단계는 [푸시 작업 버튼을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/) 참조하세요.

앱 위임의 `application:didFinishLaunchingWithOptions:` 메소드에 다음 코드를 추가합니다. 

{% alert note %}
다음 코드 샘플에는 임시 푸시 인증(5번째 줄 및 6번째 줄)을 위한 통합 기능이 포함되어 있습니다. 앱에서 프로비전 권한 부여를 사용하지 않으려면 `requestAuthorization` 옵션에 `UNAuthorizationOptionProvisional`을 추가하는 코드 줄을 제거할 수 있습니다.<br>푸시 프로비전 인증에 대한 자세한 내용은 [iOS 알림 옵션]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)을 참조하세요.
{% endalert %}

{% tabs %}
{% tab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endtab %}
{% tab 목표-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
앱 실행이 완료되기 전에 `center.delegate = self`를 사용하여 위임 오브젝트를 동기적으로 할당해야 합니다(가급적이면 `application:didFinishLaunchingWithOptions:`에서 할당). 그렇게 하지 않으면 앱에서 수신 푸시 알림을 놓칠 수 있습니다. Apple의 [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) 문서를 참조하세요.
{% endalert %}

### 2단계: Braze에 푸시 토큰 등록

APN 등록이 완료되면 결과 `deviceToken`을 Braze에 전달하여 사용자에 대한 푸시 알림을 활성화합니다.  

{% tabs %}
{% tab Swift %}

앱의 `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` 메소드에 다음 코드를 추가합니다:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab 목표-C %}

앱의 `application:didRegisterForRemoteNotificationsWithDeviceToken:` 메소드에 다음 코드를 추가합니다:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` 위임 메서드는 `application.registerForRemoteNotifications()` 호출 후 항상 호출됩니다. <br><br>다른 푸시 서비스에서 Braze로 마이그레이션하고 사용자 기기가 이미 APN에 등록되어 있는 경우, 이 메서드는 다음에 메서드를 호출할 때 기존 등록에서 토큰을 수집하며, 사용자는 푸시에 다시 옵트인하지 않아도 됩니다.
{% endalert %}

### 3단계: 푸시 처리 사용

다음으로, 수신한 푸시 알림을 Braze에 전달합니다. 이 단계는 푸시 분석 및 링크 처리를 로깅하는 데 필요합니다. 애플리케이션의 메인 스레드에서 모든 푸시 연동 코드를 호출해야 합니다.

#### 기본 푸시 처리

{% tabs %}
{% tab Swift %}
Braze의 기본 푸시 처리를 활성화하려면 앱의 `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메소드에 다음 코드를 추가하세요:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

다음으로 앱의 `userNotificationCenter(_:didReceive:withCompletionHandler:)` 메소드에 다음을 추가합니다:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endtab %}

{% tab 목표-C %}
Braze의 기본 푸시 처리를 활성화하려면 애플리케이션의 `application:didReceiveRemoteNotification:fetchCompletionHandler:` 메소드에 다음 코드를 추가하세요:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

다음으로 앱의 `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 메소드에 다음 코드를 추가합니다:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endtab %}
{% endtabs %}

#### 포 그라운드 푸시 처리

{% tabs %}
{% tab Swift %}
포그라운드 푸시 알림을 활성화하고 수신 시 Braze에서 이 알림을 인식하려면 `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`를 구현합니다. 사용자가 포그라운드 알림을 탭하면 `userNotificationCenter(_:didReceive:withCompletionHandler:)` 푸시 델리게이트가 호출되고 Braze는 푸시 클릭 이벤트를 기록합니다.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endtab %}

{% tab 목표-C %}
포그라운드 푸시 알림을 활성화하고 수신 시 Braze에서 이 알림을 인식하려면 `userNotificationCenter:willPresentNotification:withCompletionHandler:`를 구현합니다. 사용자가 포그라운드 알림을 탭하면 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 푸시 델리게이트가 호출되고 Braze는 푸시 클릭 이벤트를 기록합니다.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endtab %}
{% endtabs %}

## 딥링킹

푸시에서 앱으로의 딥링킹은 표준 푸시 통합 설명서를 통해 자동으로 처리됩니다. 앱의 특정 위치에 딥링크를 추가하는 방법에 대해 자세히 알아보려면 [고급 사용 사례]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation)를 참조하세요.

## 푸시 알림 업데이트 구독하기

Braze에서 처리하는 푸시 알림 페이로드에 액세스하려면 [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/) 메서드를 사용합니다.

`payloadTypes` 매개변수를 사용하여 푸시 열람 이벤트, 푸시 수신 이벤트 또는 둘 다와 관련된 알림의 가입 여부를 지정할 수 있습니다.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
푸시 수신 이벤트는 포그라운드 알림 및 `content-available` 백그라운드 알림에 대해서만 트리거됩니다. 종료된 상태에서 받은 알림이나 `content-available` 필드가 없는 백그라운드 알림에 대해서는 트리거되지 않습니다.
{% endalert %}

{% endtab %}

{% tab 목표-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
푸시 수신 이벤트는 포그라운드 알림 및 `content-available` 백그라운드 알림에 대해서만 트리거됩니다. 종료된 상태에서 받은 알림이나 `content-available` 필드가 없는 백그라운드 알림에 대해서는 트리거되지 않습니다.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
자동 푸시 통합을 사용하는 경우, `subscribeToUpdates(_:)`는 Braze에서 처리한 원격 알림을 받을 수 있는 유일한 방법입니다. Braze에서 알림을 자동으로 처리하는 경우 `UIAppDelegate` 및 `UNUserNotificationCenterDelegate` 시스템 메서드는 호출되지 않습니다.
{% endalert %}

{% alert tip %}
`application(_:didFinishLaunchingWithOptions:)` 에서 푸시 알림 구독을 생성하여 최종 사용자가 앱이 종료된 상태에서 알림을 탭한 후 구독이 트리거되도록 합니다.
{% endalert %}

## 테스트 {#push-testing}

명령줄을 통해 인앱 및 푸시 알림을 테스트하려면 터미널을 통해 CURL 및 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)를 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` - **설정** > **API 키에서** 사용할 수 있습니다.
- `YOUR_EXTERNAL_USER_ID` - **사용자 검색** 페이지에서 사용할 수 있습니다. 자세한 내용은 [사용자 ID 할당하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id) 참조하세요.
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 이러한 페이지는 다른 위치에 있습니다: <br>- **API 키는** **개발자 콘솔** > **API 설정에서** 찾을 수 있습니다. <br>- **사용자 검색**은 **사용자** > **사용자 검색**에 있음
{% endalert %}

다음 예제에서는 `US-01` 인스턴스를 사용하고 있습니다. 이 인스턴스를 사용하고 있지 않다면 [API 설명서를]({{site.baseurl}}/api/basics/) 참조하여 요청할 엔드포인트를 확인하세요.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## 푸시 프라이머 {#push-primers}

푸시 프라이머 캠페인은 사용자가 기기에서 앱에 대한 푸시 알림을 활성화할 것을 권장합니다. [노코드 푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)를 사용하면 SDK 사용자 지정 없이도 이 작업을 수행할 수 있습니다.

