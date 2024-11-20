---
nav_title: 지연된 초기화
article_title: 브레이즈 스위프트 SDK의 초기화가 지연되었습니다.
platform: Swift
page_order: 6
description: "이 문서에서는 SDK가 비동기적으로 초기화될 때 푸시 알림 처리를 유지하기 위해 Swift SDK 지연 초기화를 구현하는 방법에 대해 설명합니다."

---

# 브레이즈 스위프트 SDK의 초기화가 지연되었습니다.

> 푸시 알림 처리를 유지하면서 Braze Swift SDK를 비동기식으로 초기화하는 방법을 알아보세요. 서버에서 구성 데이터를 가져오거나 사용자 동의를 기다리는 등 SDK를 초기화하기 전에 다른 서비스를 설정해야 할 때 유용할 수 있습니다.

## 지연된 초기화 설정

### 1단계: 지연된 초기화를 위한 SDK 준비하기

기본적으로 앱이 종료된 상태에서 최종 사용자가 푸시 알림을 열면 SDK가 초기화되기 전에는 푸시 알림을 처리할 수 없습니다.

[Braze Swift SDK 버전 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) 이상부터는 정적 헬퍼 메서드( [Braze.prepareForDelayedInitialization(pushAutomation:)를](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) 사용하여 이 작업을 처리할 수 있습니다. 이 방법은 푸시 자동화 시스템을 설정하여 지연 초기화를 위해 SDK를 준비합니다.

SDK가 초기화되기 전에 Braze에서 발생하는 모든 푸시 알림이 캡처되어 대기열에 대기합니다. SDK가 초기화되면 해당 푸시 알림은 SDK에 의해 처리됩니다. 이 메서드는 애플리케이션 수명 주기에서 가능한 한 빨리 호출해야 하며, `AppDelegate` 의 `application(_:didFinishLaunchingWithOptions:)` 메서드 내부 또는 그 이전에 호출해야 합니다.

{% alert note %}
Swift SDK는 Braze가 아닌 푸시 알림은 캡처하지 않으며, 시스템 델리게이트 메서드를 통해 계속 처리됩니다.
{% endalert %}

{% tabs %}
{% tab Swift - UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift - SwiftUI %}
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

### 2단계: Braze SDK 초기화하기

지연 초기화를 위해 SDK를 준비한 후에는 나중에 언제든지 비동기식으로 SDK를 초기화할 수 있습니다. 그러면 SDK가 Braze에서 발생한 대기열에 있는 모든 푸시 알림 이벤트를 처리합니다.

Braze SDK를 초기화하려면 [표준 Swift SDK 초기화 프로세스를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/) 따르세요.

## 고려 사항

`Braze.prepareForDelayedInitialization(pushAutomation:)` 을 사용하면 푸시 알림 자동화 기능을 자동으로 사용하도록 SDK를 구성하게 됩니다. 푸시 알림을 처리하는 시스템 델리게이트 메서드는 Braze에서 발생하는 푸시 알림에 대해서는 호출되지 않습니다.

SDK는 SDK가 초기화된 **후에만** Braze 푸시 알림과 그에 따른 동작을 처리합니다. 예를 들어 사용자가 딥링크를 여는 푸시 알림을 탭하면 `Braze` 인스턴스가 초기화된 후에만 딥링크가 열립니다.

Braze 푸시 알림에 대한 추가 처리를 수행해야 하는 경우 [푸시 알림 업데이트 구독하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates) 참조하세요. 이전에 대기열에 추가된 푸시 알림의 업데이트를 받으려면 SDK를 초기화한 후 바로 구독 핸들러를 구현해야 한다는 점에 유의하세요.
