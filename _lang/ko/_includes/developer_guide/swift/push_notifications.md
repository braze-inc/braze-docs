## 요금 제한

푸시 알림은 전송 횟수에 제한이 있으므로 애플리케이션에 필요한 만큼 많이 보내는 것을 두려워하지 마세요. iOS 및 Apple 푸시 알림 서비스(APN) 서버가 알림 전송 빈도를 제어하므로 너무 많이 보내도 문제가 발생하지 않습니다. 푸시 알림이 제한되는 경우, 기기가 다음 번에 연결 유지 패킷을 보내거나 다른 알림을 받을 때까지 지연될 수 있습니다.

## 푸시 알림 설정하기

### 1단계: APN 토큰 업로드

{% multi_lang_include developer_guide/swift/apns_token.md %}

### 2단계: 푸시 기능 사용

Xcode에서 기본 앱 대상의 **서명 및 기능** 섹션으로 이동하여 푸시 알림 기능을 추가합니다.

![Xcode 프로젝트의 '서명 및 기능' 섹션]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### 3단계: 푸시 처리 설정

Swift SDK를 사용하여 Braze에서 수신한 원격 알림의 처리를 자동화할 수 있습니다. 이는 푸시 알림을 처리하는 가장 간단한 방법이며 권장되는 처리 방법입니다.

{% tabs local %}
{% tab 자동 %}
#### 3.1 단계: 푸시 속성에서 자동화 사용 설정

자동 푸시 통합을 활성화하려면 `push` 구성의 `automation` 속성정보를 `true`로 설정합니다.

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

이렇게 하면 SDK에 다음을 지시합니다:
- 시스템에서 푸시 알림 신청을 등록하세요.
- 초기화 시 푸시 알림 승인/허가를 요청하세요.
- 푸시 알림 관련 시스템 위임 메서드에 대한 구현을 동적으로 제공합니다.

{% alert note %}
SDK에서 수행하는 자동화 단계는 코드베이스의 기존 푸시 알림 처리 통합과 호환됩니다. SDK는 Braze에서 수신한 원격 알림의 처리만 자동화합니다. 자체 또는 다른 서드파티 SDK 원격 알림을 처리하기 위해 구현된 모든 시스템 핸들러는 `automation`이 활성화되어 있어도 계속 작동합니다.
{% endalert %}

{% alert warning %}
푸시 알림 자동화를 활성화하려면 기본 스레드에서 SDK를 초기화해야 합니다. SDK 초기화는 애플리케이션 실행이 완료되기 전 또는 AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 구현에서 수행해야 합니다.
애플리케이션에 SDK를 초기화하기 전에 추가 설정이 필요한 경우 [지연된 초기화]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) 문서 페이지를 참조하세요.
{% endalert %}

#### 3.2 단계: 개별 구성 재정의(선택 사항)

보다 세분화된 제어를 위해 각 자동화 단계를 개별적으로 활성화 또는 비활성화할 수 있습니다:

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

사용 가능한 모든 옵션은 [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class)을 참조하고, 자동화 동작에 대한 자세한 내용은 [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property)을 참조하세요.
{% endtab %}

{% tab 매뉴얼 %}
{% alert note %}
앱에 특정한 추가 동작을 위해 푸시 알림에 의존하는 경우 여전히 수동 푸시 알림 통합 대신 자동 푸시 통합을 사용할 수 있습니다. [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) 메서드를 통해 Braze에서 처리된 원격 알림을 수신할 수 있습니다.
{% endalert %}

#### 3.1 단계: APN으로 푸시 알림 등록하기

앱의 [`application:didFinishLaunchingWithOptions:` 델리게이트 메서드에](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 적절한 코드 샘플을 포함시켜 사용자의 디바이스가 APN에 등록할 수 있도록 합니다. 애플리케이션의 메인 스레드에서 모든 푸시 연동 코드를 호출해야 합니다.

Braze는 푸시 액션 버튼 지원을 위한 기본 푸시 카테고리도 제공하며, 이 카테고리는 푸시 등록 코드에 수동으로 추가해야 합니다. 추가 통합 단계는 [푸시 작업 버튼을]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) 참조하세요.

앱 위임의 `application:didFinishLaunchingWithOptions:` 메소드에 다음 코드를 추가합니다. 

{% alert note %}
다음 코드 샘플에는 임시 푸시 인증(5번째 줄 및 6번째 줄)을 위한 통합 기능이 포함되어 있습니다. 앱에서 프로비전 권한 부여를 사용하지 않으려면 `requestAuthorization` 옵션에 `UNAuthorizationOptionProvisional`을 추가하는 코드 줄을 제거할 수 있습니다.<br>푸시 프로비전 인증에 대한 자세한 내용은 [iOS 알림 옵션]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)을 참조하세요.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

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

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
앱 실행이 완료되기 전에 `center.delegate = self`를 사용하여 위임 오브젝트를 동기적으로 할당해야 합니다(가급적이면 `application:didFinishLaunchingWithOptions:`에서 할당). 그렇게 하지 않으면 앱에서 수신 푸시 알림을 놓칠 수 있습니다. Apple의 [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) 문서를 참조하세요.
{% endalert %}

#### 3.2 단계: Braze에 푸시 토큰 등록

APN 등록이 완료되면 결과 `deviceToken`을 Braze에 전달하여 사용자에 대한 푸시 알림을 활성화합니다.  

{% subtabs %}
{% subtab Swift %}

앱의 `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` 메소드에 다음 코드를 추가합니다:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

앱의 `application:didRegisterForRemoteNotificationsWithDeviceToken:` 메소드에 다음 코드를 추가합니다:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` 위임 메서드는 `application.registerForRemoteNotifications()` 호출 후 항상 호출됩니다. <br><br>다른 푸시 서비스에서 Braze로 마이그레이션하고 사용자 기기가 이미 APN에 등록되어 있는 경우, 이 메서드는 다음에 메서드를 호출할 때 기존 등록에서 토큰을 수집하며, 사용자는 푸시에 다시 옵트인하지 않아도 됩니다.
{% endalert %}

#### 3.3 단계: 푸시 처리 사용

다음으로, 수신한 푸시 알림을 Braze에 전달합니다. 이 단계는 푸시 분석 및 링크 처리를 로깅하는 데 필요합니다. 애플리케이션의 메인 스레드에서 모든 푸시 연동 코드를 호출해야 합니다.

##### 기본 푸시 처리

{% subtabs %}
{% subtab Swift %}
Braze 기본 푸시 처리를 활성화하려면 앱의 `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메소드에 다음 코드를 추가하세요:

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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Braze 기본 푸시 처리를 활성화하려면 애플리케이션의 `application:didReceiveRemoteNotification:fetchCompletionHandler:` 메소드에 다음 코드를 추가하세요:

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
{% endsubtab %}
{% endsubtabs %}

##### 포 그라운드 푸시 처리

{% subtabs %}
{% subtab Swift %}
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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 테스트 알림 {#push-testing}

명령줄을 통해 인앱 및 푸시 알림을 테스트하려면 터미널을 통해 CURL 및 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)를 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` - **설정** > **API 키에서** 사용할 수 있습니다.
- `YOUR_EXTERNAL_USER_ID` - **사용자 검색** 페이지에서 사용할 수 있습니다. 자세한 내용은 [사용자 ID 할당하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id) 참조하세요.
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

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

{% tab OBJECTIVE-C %}

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

## 푸시 프라이머 {#push-primers}

푸시 프라이머 캠페인은 사용자가 기기에서 앱에 대한 푸시 알림을 활성화할 것을 권장합니다. [노코드 푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)를 사용하면 SDK 사용자 지정 없이도 이 작업을 수행할 수 있습니다.

## 동적 APN 게이트웨이 관리

동적 APN(Apple 푸시 알림 서비스) 게이트웨이 관리는 올바른 APN 환경을 자동으로 감지하여 iOS 푸시 알림의 안정성과 효율성을 향상시킵니다. 이전에는 푸시 알림을 위한 APN 환경(개발 또는 프로덕션)을 수동으로 선택해야 했기 때문에 잘못된 게이트웨이 구성, 배달 실패 및 `BadDeviceToken` 오류가 발생하는 경우가 있었습니다.

동적 APN 게이트웨이 관리를 사용하면 다음과 같은 이점이 있습니다:

- **안정성이 향상되었습니다:** 알림은 항상 올바른 APN 환경으로 전달되므로 전달 실패가 줄어듭니다.
- **간소화된 구성:** 더 이상 APN 게이트웨이 설정을 수동으로 관리할 필요가 없습니다.
- **오류 복원력:** 유효하지 않거나 누락된 게이트웨이 값은 정상적으로 처리되어 중단 없는 서비스를 제공합니다.

### Prerequisites

Braze는 다음 SDK 버전 요구 사항과 함께 iOS에서 푸시 알림을 위한 동적 APN 게이트웨이 관리를 지원합니다:

{% sdk_min_versions swift:10.0.0 %}

### How it works

iOS 앱이 Braze Swift SDK와 통합되면 다음과 같은 디바이스 관련 데이터를 전송합니다. [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) 를 포함한 기기 관련 데이터를 Braze SDK API로 전송합니다(가능한 경우). `apns_gateway` 값은 앱이 개발(`dev`) 또는 프로덕션(`prod`) APN 환경을 사용하는지 여부를 나타냅니다.

Braze는 또한 각 디바이스에 대해 보고된 게이트웨이 값을 저장합니다. 유효한 새 게이트웨이 값이 수신되면 Braze는 저장된 값을 자동으로 업데이트합니다.

Braze에서 푸시 알림을 보내는 경우:

- 디바이스에 대해 유효한 게이트웨이 값(개발 또는 프로덕트)이 저장되어 있으면, Braze는 이를 사용하여 올바른 APN 환경을 확인합니다.
- 게이트웨이 값이 저장되지 않은 경우, Braze는 **앱 설정** 페이지에서 구성된 APN 환경으로 기본 설정됩니다.

### Frequently asked questions

#### 이 기능이 도입된 이유는 무엇인가요?

동적 APN 게이트웨이 관리를 사용하면 올바른 환경이 자동으로 선택됩니다. 이전에는 APN 게이트웨이를 수동으로 구성해야 했기 때문에 `BadDeviceToken` 오류, 토큰 무효화 및 잠재적인 APN 속도 제한 문제가 발생할 수 있었습니다.

#### 이것이 푸시 전송 성능에 어떤 영향을 미칠까요?

이 기능은 푸시 토큰을 항상 올바른 APN 환경으로 라우팅하여 잘못 구성된 게이트웨이로 인한 오류를 방지함으로써 전송 속도를 향상시킵니다.

#### 이 기능을 비활성화할 수 있나요?

동적 APN 게이트웨이 관리는 기본적으로 켜져 있으며 안정성 향상을 제공합니다. 수동 게이트웨이 선택이 필요한 특정 사용 사례가 있는 경우 [Braze 지원팀에]({{site.baseurl}}/user_guide/administrative/access_braze/support/) 문의하세요.
