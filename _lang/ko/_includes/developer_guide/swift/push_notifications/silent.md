{% multi_lang_include developer_guide/prerequisites/swift.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 합니다.

## iOS 제한 사항

iOS 운영 체제에서는 일부 기능에 대한 알림을 차단할 수 있습니다. 이 기능들에 어려움을 겪고 있다면, iOS의 무음 알림 게이트가 원인일 수 있습니다. 자세한 내용은 Apple의 [인스턴스 메서드](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) 및 [미수신 알림](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) 문서를 참조하세요.

## 무음 푸시 알림 설정하기

백그라운드 작업을 트리거하기 위해 무음 푸시 알림을 사용하려면 앱이 백그라운드에 있을 때에도 알림을 받도록 앱을 구성해야 합니다. Xcode에서 **서명 및 기능** 창을 사용하여 백그라운드 모드 기능을 기본 앱 대상에 추가합니다. **원격 알림** 확인란을 선택합니다.

!['기능' 아래에 '원격 알림' 모드 확인란이 표시된 Xcode.]({% image_buster /assets/img_archive/background_mode.png %} "백그라운드 모드 사용")

원격 알림 백그라운드 모드가 활성화되어 있어도 사용자가 애플리케이션을 강제 종료한 경우 시스템은 백그라운드로 앱을 실행하지 않습니다. 사용자가 애플리케이션을 명시적으로 실행하거나 기기를 재부팅해야 시스템에서 백그라운드로 앱을 자동으로 실행할 수 있습니다.

자세한 내용은 [백그라운드 업데이트 푸시하기](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) 및 `application:didReceiveRemoteNotification:fetchCompletionHandler:` [문서를](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) 참조하세요.

## 무음 푸시 알림 보내기

무음 푸시 알림을 보내려면 푸시 알림 페이로드에서 `content-available` 플래그를 `1`로 설정합니다. 

{% alert note %}
Apple에서 원격 알림이라고 부르는 것은 `content-available` 플래그가 설정된 일반 푸시 알림일 뿐입니다.
{% endalert %}

`content-available` 플래그는 Braze 대시보드와 [메시징 API의]({{site.baseurl}}/api/endpoints/messaging/) [Apple 푸시 개체]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) 내에서 설정할 수 있습니다.

{% alert warning %}
제목과 본문에 모두 `content-available=1`을 첨부하는 작업은 정의되지 않은 동작을 유발할 수 있으므로 권장되지 않습니다. 실제로 무음 알림인지 확인하려면 `content-available` 플래그를 `1.`로 설정할 때 제목과 본문을 모두 제외합니다. 자세한 내용은 공식 [백그라운드 업데이트에 대한 Apple 설명서](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)를 참조하세요.
{% endalert %}

![푸시 작성기의 '설정' 탭에 있는 '콘텐츠 사용 가능' 확인란이 표시된 Braze 대시보드.]({% image_buster /assets/img_archive/remote_notification.png %} "콘텐츠 사용 가능")

무음 푸시 알림을 보낼 때 애플리케이션에서 이벤트를 참조할 수 있도록 알림 페이로드에 일부 데이터를 포함할 수도 있습니다. 그러면 몇 개의 네트워킹 요청을 절약하고 앱의 응답성을 높일 수 있습니다.

## 내부 푸시 알림 무시하기

Braze는 무음 푸시 알림을 사용하여 제거 추적 또는 지오펜스와 같은 특정 고급 기능을 내부적으로 처리합니다. 앱이 애플리케이션 실행 또는 백그라운드 푸시에서 자동 작업을 수행하는 경우 내부 푸시 알림에 의해 트리거되지 않도록 해당 활동을 게이팅하는 것을 고려하세요.

예를 들어, 백그라운드 푸시 또는 애플리케이션이 실행될 때마다 새 콘텐츠를 위해 서버를 호출하는 로직이 있는 경우 불필요한 네트워크 트래픽을 피하기 위해 Braze의 내부 푸시가 트리거되지 않도록 설정할 수 있습니다. Braze는 특정 종류의 내부 푸시를 거의 동시에 모든 사용자에게 전송하기 때문에, 내부 푸시의 온런치 네트워크 호출이 게이트되지 않으면 상당한 서버 부하가 발생할 수 있습니다.

### 1단계: 앱에서 자동 동작 확인

애플리케이션에서 다음 위치에서 자동 동작이 있는지 확인하고 Braze의 내부 푸시를 무시하도록 코드를 업데이트하세요:

1. **푸시 수신기.** 백그라운드 푸시 알림은 `UIApplicationDelegate`에서 `application:didReceiveRemoteNotification:fetchCompletionHandler:`를 호출합니다.
2. **애플리케이션 위임.** 백그라운드 푸시는 [일시 중단](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)된 앱을 백그라운드로 실행하여 `UIApplicationDelegate`에서 `application:willFinishLaunchingWithOptions:` 및 `application:didFinishLaunchingWithOptions:` 메서드를 트리거할 수 있습니다. 백그라운드 푸시에서 애플리케이션이 실행되었는지 확인하려면 이러한 메서드의 `launchOptions`를 확인합니다.

### 2단계: 내부 푸시 유틸리티 방법 사용

`Braze.Notifications`에서 정적 유틸리티 메서드를 사용하여 앱이 Braze 내부 푸시를 수신했는지 또는 앱이 실행되었는지 확인할 수 있습니다. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:))은 제거 추적, 기능 플래그 동기화 및 지오펜스 동기화 알림을 포함한 모든 Braze 내부 푸시 알림에서 `true`를 반환합니다.

For example:

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
{% tab OBJECTIVE-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}
