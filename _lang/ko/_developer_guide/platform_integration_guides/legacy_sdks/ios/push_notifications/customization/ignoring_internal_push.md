---
nav_title: 내부 푸시 무시
article_title: iOS용 Braze 내부 푸시 알림 무시하기
platform: iOS
page_order: 4
description: "이 참고 문서에서는 Braze 내부 푸시 알림을 무시하는 방법에 대해 설명합니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze 내부 푸시 알림 무시하기

Braze는 특정 고급 기능의 내부 구현을 위해 무음 푸시 알림을 사용합니다. 대부분의 통합에서는 앱 측에서 변경하지 않아도 됩니다. 그러나 내부 푸시 알림(예: 제거 추적 또는 지오펜스)에 의존하는 Braze 기능을 통합하는 경우 앱을 업데이트하여 내부 푸시를 무시할 수 있습니다.

앱이 애플리케이션 실행 또는 백그라운드 푸시에서 자동 작업을 수행하는 경우 해당 활동이 내부 푸시 알림에 의해 트리거되지 않도록 활동의 게이팅을 고려해야 합니다. 예를 들어, 백그라운드 푸시 또는 애플리케이션 실행 시 새 콘텐츠를 위해 서버를 호출하는 로직이 있는 경우 불필요한 네트워크 트래픽을 유발할 수 있으므로 내부 푸시 트리거를 원치 않을 수 있습니다. 또한 Braze는 특정 종류의 내부 푸시를 거의 동시에 모든 사용자에게 전송하기 때문에 내부 푸시에서 실행 시 네트워크 호출을 게이팅하지 않으면 상당한 서버 부하가 발생할 수 있습니다.

## 앱에서 자동 동작 확인

다음 위치에서 애플리케이션의 자동 동작을 확인하고 내부 푸시를 무시하도록 코드를 업데이트해야 합니다.

1. **푸시 수신기.** 백그라운드 푸시 알림은 `UIApplicationDelegate`에서 `application:didReceiveRemoteNotification:fetchCompletionHandler:`를 호출합니다.
2. **애플리케이션 위임.** 백그라운드 푸시는 [일시 중단](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3)된 앱을 백그라운드로 실행하여 `UIApplicationDelegate`에서 `application:willFinishLaunchingWithOptions:` 및 `application:didFinishLaunchingWithOptions:` 메서드를 트리거할 수 있습니다. 백그라운드 푸시에서 애플리케이션이 실행되었는지 확인하려면 이러한 메서드의 `launchOptions`를 확인할 수 있습니다.

## Braze 내부 푸시 유틸리티 방법 사용

`ABKPushUtils`에서 유틸리티 메서드를 사용하여 앱이 Braze 내부 푸시를 수신했는지 또는 앱이 실행되었는지 확인할 수 있습니다. `isAppboyInternalRemoteNotification:`은 모든 Braze 내부 푸시 알림에서 `YES`를 반환하고 `isUninstallTrackingRemoteNotification:` 및 `isGeofencesSyncRemoteNotification:`는 각각 제거 추적 및 지오펜스 동기화에 대해 `YES`를 반환합니다. 메서드 선언은 [`ABKPushUtils.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h)를 참조하세요.

## 구현 예시 {#internal-push-implementation-example}

{% tabs %}
{% tab 목표-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] as? NSDictionary as? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

