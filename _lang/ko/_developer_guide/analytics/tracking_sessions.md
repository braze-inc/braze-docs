---
nav_title: 추적 세션
article_title: Braze SDK를 통한 세션 추적
page_order: 3.3
description: "Braze SDK를 통해 세션을 추적하는 방법을 알아보세요."

---

# 세션 추적

> Braze SDK를 통해 세션을 추적하는 방법을 알아보세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

## 세션 수명 주기 정보

세션은 앱이 실행된 후 Braze SDK가 앱에서 사용자 활동을 추적하는 기간을 의미합니다. [ `changeUser()` 메서드를 호출하여]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id) 새 세션을 강제로 생성할 수도 있습니다.

{% tabs %}
{% tab android %}
{% alert note %}
활동 라이프사이클 콜백]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) (Android의 경우)]을 설정한 경우, Braze는 앱의 각 활동에 대해 자동으로 `openSession()` 및 `closeSession()` 으로 전화합니다.
{% endalert %}

기본적으로 세션은 `openSession()` 을 처음 호출할 때 시작됩니다. 앱이 백그라운드로 전환되면 세션은 [기본 세션 시간 제한을 변경하지](#changing-the-default-session-timeout) 않는 한 `10` 초 동안 활성 상태로 유지되거나 사용자가 앱을 닫습니다. 사용자가 백그라운드에서 앱을 닫는 경우, 앱을 다시 열 때까지 세션 데이터가 Braze로 설정되지 않을 수 있다는 점에 유의하세요. 

`closeSession()` 으로 전화해도 세션이 즉시 종료되지는 않습니다. 대신 사용자가 다른 활동을 시작하여 `openSession()` 을 다시 호출하지 않으면 10초 후에 세션이 종료됩니다.
{% endtab %}

{% tab swift %}
기본적으로 세션은 `Braze.init(configuration:)` 으로 전화하면 시작됩니다. 이는 `UIApplicationWillEnterForegroundNotification` 알림이 트리거되면 앱이 포그라운드에 진입했음을 의미합니다.

앱이 백그라운드로 이동하면 `UIApplicationDidEnterBackgroundNotification` 이 트리거됩니다. 세션은 [기본 세션 시간 제한을 변경하거나](#changing-the-default-session-timeout) 사용자가 앱을 닫지 않는 한 `10` 초 동안 활성 상태로 유지됩니다.
{% endtab %}

{% tab 웹 %}
기본적으로 세션은 `braze.openSession()` 을 처음 호출할 때 시작됩니다. 세션은 [기본 세션 시간 제한을 변경하거나](#change-session-timeout) 사용자가 앱을 닫지 않는 한 최대 `30` 분 동안 활성 상태로 유지됩니다.
{% endtab %}
{% endtabs %}

## 세션 업데이트에 가입

### 1단계: 업데이트 가입

세션 업데이트를 구독하려면 `subscribeToSessionUpdates()` 방법을 사용하세요.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
세션 종료 콜백을 등록하면 앱이 포그라운드로 돌아갈 때 콜백이 실행됩니다. 세션 시간은 앱이 열리거나 포그라운드에서 닫히거나 배경이 될 때까지 측정됩니다.

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

비동기 스트림을 구독하려면 대신 [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) 대신

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
현재 웹브레이즈 SDK에서는 세션 업데이트 구독이 지원되지 않습니다.
{% endtab %}
{% endtabs %}

### 2단계: 테스트 세션 추적(선택 사항)

세션 추적을 테스트하려면 디바이스에서 세션을 시작한 다음 Braze 대시보드를 열고 관련 사용자를 검색합니다. 사용자 프로필에서 **세션 개요를** 선택합니다. 메트릭이 예상대로 업데이트되면 세션 추적이 올바르게 작동하는 것입니다.

![사용자 프로필의 세션 개요 섹션에 세션 수, 마지막으로 사용한 날짜, 처음 사용한 날짜가 표시됩니다.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
앱별 세부 정보는 두 개 이상의 앱을 사용한 사용자에 대해서만 표시됩니다.
{% endalert %}

## 기본 세션 시간 초과 변경하기 {#change-session-timeout}

세션이 자동으로 시간 초과되기까지 경과하는 시간을 변경할 수 있습니다.

{% tabs %}
{% tab Android %}
기본적으로 세션 시간 제한은 `10` 초로 설정되어 있습니다. 이를 변경하려면 `braze.xml` 파일을 열고 `com_braze_session_timeout` 매개 변수를 추가합니다. `1` 보다 크거나 같은 정수로 설정할 수 있습니다.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
기본적으로 세션 시간 제한은 `10` 초로 설정되어 있습니다. 이를 변경하려면 `configuration` 객체에 전달된 `sessionTimeout` 를 [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). `1` 보다 크거나 같은 정수로 설정할 수 있습니다.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
기본적으로 세션 시간 제한은 `30` 초로 설정되어 있습니다. 이 옵션을 변경하려면 `sessionTimeoutInSeconds` 옵션을 [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 함수에 전달하세요. `1` 보다 크거나 같은 정수로 설정할 수 있습니다. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}
{% endtabs %}

{% alert note %}
세션 시간 제한을 설정하면 모든 세션 시맨틱이 설정된 시간 제한까지 자동으로 연장됩니다.
{% endalert %}
