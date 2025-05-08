---
nav_title: 내부 푸시 무시
article_title: iOS용 Braze 내부 푸시 알림 무시하기
platform: Swift
page_order: 6
description: "이 문서에서는 Swift SDK에 대한 Braze 내부 푸시 알림을 무시하는 방법을 다룹니다."
channel:
  - push

---

# 내부 푸시 알림 무시하기

> Braze는 특정 고급 기능의 내부 구현을 위해 [무음 푸시 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) 사용합니다. 대부분의 통합에서는 앱 측에서 변경하지 않아도 됩니다. 그러나 내부 푸시 알림(예: 제거 추적 또는 지오펜스)에 의존하는 Braze 기능을 통합하는 경우 앱을 업데이트하여 Braze의 내부 푸시를 무시할 수 있습니다.

앱이 애플리케이션 실행 또는 백그라운드 푸시에서 자동 작업을 수행하는 경우 해당 활동이 내부 푸시 알림에 의해 트리거되지 않도록 활동의 게이팅을 고려합니다. 예를 들어, 백그라운드 푸시 또는 애플리케이션 실행 시 새 콘텐츠를 위해 서버를 호출하는 로직이 있는 경우 불필요한 네트워크 트래픽을 유발할 수 있으므로 Braze의 내부 푸시 트리거를 원치 않을 수 있습니다. 또한 Braze는 특정 종류의 내부 푸시를 거의 동시에 모든 사용자에게 전송하기 때문에 내부 푸시에서 실행 시 네트워크 호출을 게이팅하지 않으면 상당한 서버 부하가 발생할 수 있습니다.

## 앱에서 자동 동작 확인

애플리케이션에서 다음 위치에서 자동 동작이 있는지 확인하고 Braze의 내부 푸시를 무시하도록 코드를 업데이트하세요:

1. **푸시 수신기.** 백그라운드 푸시 알림은 `UIApplicationDelegate`에서 `application:didReceiveRemoteNotification:fetchCompletionHandler:`를 호출합니다.
2. **애플리케이션 위임.** 백그라운드 푸시는 [일시 중단](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)된 앱을 백그라운드로 실행하여 `UIApplicationDelegate`에서 `application:willFinishLaunchingWithOptions:` 및 `application:didFinishLaunchingWithOptions:` 메서드를 트리거할 수 있습니다. 백그라운드 푸시에서 애플리케이션이 실행되었는지 확인하려면 이러한 메서드의 `launchOptions`를 확인합니다.

## 내부 푸시 유틸리티 방법 사용

`Braze.Notifications`에서 정적 유틸리티 메서드를 사용하여 앱이 Braze 내부 푸시를 수신했는지 또는 앱이 실행되었는지 확인할 수 있습니다. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:))은 제거 추적, 기능 플래그 동기화 및 지오펜스 동기화 알림을 포함한 모든 Braze 내부 푸시 알림에서 `true`를 반환합니다.

## 구현 예시 {#internal-push-implementation-example}

{% tabs %}
{% tab swift %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab 목표-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}

