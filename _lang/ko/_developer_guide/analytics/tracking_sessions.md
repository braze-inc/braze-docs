---
nav_title: 세션 추적
article_title: Braze SDK를 통한 세션 추적
page_order: 3.3
description: "Braze SDK를 통해 세션을 추적하는 방법을 알아보세요."

---

# 세션 추적

> Braze SDK를 통해 세션을 추적하는 방법을 알아보세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## 비활성 정의

비활성이 정의되고 측정되는 방식을 이해하는 것은 Web SDK에서 세션 수명 주기를 효과적으로 관리하는 데 핵심입니다. 비활성이란 Braze Web SDK가 사용자로부터 추적된 이벤트를 감지하지 못하는 기간을 의미합니다.

### 비활성 측정 방식

Web SDK는 [SDK 추적 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events)를 기반으로 비활성을 추적합니다. SDK는 추적된 이벤트가 전송될 때마다 재설정되는 내부 타이머를 유지합니다. 구성된 타임아웃 기간 내에 SDK 추적 이벤트가 발생하지 않으면 세션은 비활성으로 간주되어 종료됩니다.

Web SDK에서 세션 수명 주기가 구현되는 방식에 대한 자세한 내용은 [Braze Web SDK GitHub 리포지토리](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts)의 세션 관리 소스 코드를 참조하세요.

**기본적으로 활동으로 간주되는 항목:**
- 웹 앱 열기 또는 새로고침
- Braze 기반 UI 요소와의 상호작용(예: [인앱 메시지]({{site.baseurl}}/developer_guide/in_app_messages/) 또는 [콘텐츠 카드]({{site.baseurl}}/developer_guide/content_cards/))
- 추적된 이벤트를 전송하는 SDK 메서드 호출(예: [커스텀 이벤트]({{site.baseurl}}/developer_guide/analytics/logging_events/) 또는 [사용자 속성 업데이트]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**기본적으로 활동으로 간주되지 않는 항목:**
- 다른 브라우저 탭으로 전환
- 브라우저 창 최소화
- 브라우저 포커스 또는 블러 이벤트
- 페이지에서의 스크롤 또는 마우스 움직임

{% alert note %}
Web SDK는 브라우저 가시성 변경, 탭 전환 또는 사용자 포커스를 자동으로 추적하지 않습니다. 하지만 브라우저의 [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)를 사용하여 커스텀 이벤트 리스너를 구현하고 Braze에 [커스텀 이벤트]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)를 전송하면 이러한 브라우저 수준의 상호작용을 추적할 수 있습니다. 예제 구현은 [커스텀 비활성 추적](#tracking-custom-inactivity)을 참조하세요.
{% endalert %}

### 세션 타임아웃 구성

기본적으로 Web SDK는 추적된 이벤트가 30분 동안 없으면 세션을 비활성으로 간주합니다. SDK를 초기화할 때 `sessionTimeoutInSeconds` 매개변수를 사용하여 이 임계값을 커스텀할 수 있습니다. 코드 예제를 포함한 이 매개변수 구성에 대한 자세한 내용은 [기본 세션 타임아웃 변경하기](#changing-the-default-session-timeout)를 참조하세요.

### 예시: 비활성 시나리오 이해하기

다음 시나리오를 살펴보겠습니다:

1. 사용자가 웹사이트를 열면 SDK가 [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)을 호출하여 세션을 시작합니다.
2. 사용자가 다른 웹사이트를 보기 위해 다른 브라우저 탭으로 30분 동안 전환합니다.
3. 이 시간 동안 웹사이트에서 SDK 추적 이벤트가 발생하지 않습니다.
4. 30분간의 비활성 후 세션이 자동으로 종료됩니다.
5. 사용자가 웹사이트 탭으로 다시 돌아와 SDK 이벤트(예: 페이지 보기 또는 콘텐츠와의 상호작용)를 트리거하면 새로운 세션이 시작됩니다.

### 커스텀 비활성 추적

브라우저 가시성 또는 탭 전환을 기반으로 비활성을 추적해야 하는 경우 JavaScript 코드에서 커스텀 이벤트 리스너를 구현하세요. `visibilitychange`와 같은 브라우저 이벤트를 사용하여 사용자가 페이지를 떠나는 시점을 감지하고, 필요에 따라 Braze에 [커스텀 이벤트]({{site.baseurl}}/developer_guide/analytics/logging_events/)를 수동으로 전송하거나 [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)을 호출하세요.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

커스텀 이벤트 로깅에 대한 자세한 내용은 [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/)을 참조하세요. 세션 수명 주기 및 타임아웃 구성에 대한 자세한 내용은 [기본 세션 타임아웃 변경하기](#change-session-timeout)를 참조하세요.

## 세션 업데이트 구독하기

### 1단계: 업데이트 구독

세션 업데이트를 구독하려면 `subscribeToSessionUpdates()` 메서드를 사용하세요.

{% tabs %}
{% tab web %}
현재 Web Braze SDK에서는 세션 업데이트 구독이 지원되지 않습니다.
{% endtab %}

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
세션 종료 콜백을 등록하면 앱이 포그라운드로 돌아올 때 콜백이 실행됩니다. 세션 지속 시간은 앱이 열리거나 포그라운드로 전환되는 시점부터 닫히거나 백그라운드로 전환되는 시점까지 측정됩니다.

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

비동기 스트림을 구독하려면 [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream)을 대신 사용할 수 있습니다.

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

{% tab react native %}
React Native SDK는 세션 업데이트를 직접 구독하는 메서드를 제공하지 않습니다. 세션 수명 주기는 기본 네이티브 SDK에서 관리되므로, 업데이트를 구독하려면 **Android** 또는 **Swift** 탭의 네이티브 플랫폼 접근 방식을 사용하세요.
{% endtab %}
{% endtabs %}

### 2단계: 세션 추적 테스트(선택 사항)

세션 추적을 테스트하려면 기기에서 세션을 시작한 다음 Braze 대시보드를 열고 해당 사용자를 검색합니다. 고객 프로필에서 **세션 개요**를 선택합니다. 측정기준이 예상대로 업데이트되면 세션 추적이 올바르게 작동하고 있는 것입니다.

![사용자 프로필의 세션 개요 섹션으로, 세션 수, 마지막 사용 날짜 및 첫 사용 날짜를 보여줍니다.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
앱별 세부 정보는 두 개 이상의 앱을 사용한 사용자에게만 표시됩니다.
{% endalert %}

## 기본 세션 타임아웃 변경하기 {#change-session-timeout}

세션이 자동으로 타임아웃되기까지의 시간을 변경할 수 있습니다.

{% tabs %}
{% tab web %}
기본적으로 세션 타임아웃은 `30`분으로 설정되어 있습니다. 이를 변경하려면 [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 함수에 `sessionTimeoutInSeconds` 옵션을 전달하세요. `1` 이상의 정수로 설정할 수 있습니다.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
기본적으로 세션 타임아웃은 `10`초로 설정되어 있습니다. 이를 변경하려면 `braze.xml` 파일을 열고 `com_braze_session_timeout` 매개변수를 추가하세요. `1` 이상의 정수로 설정할 수 있습니다.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
기본적으로 세션 타임아웃은 `10`초로 설정되어 있습니다. 이를 변경하려면 [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class)에 전달되는 `configuration` 오브젝트에서 `sessionTimeout`을 설정하세요. `1` 이상의 정수로 설정할 수 있습니다.

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

{% tab react native %}
React Native SDK는 세션 관리를 네이티브 SDK에 의존합니다. 기본 세션 타임아웃을 변경하려면 네이티브 레이어에서 구성하세요:

- **Android:** `braze.xml` 파일에서 `com_braze_session_timeout`을 설정하세요. 자세한 내용은 **Android** 탭을 선택하세요.
- **iOS:** `Braze.Configuration` 오브젝트에서 `sessionTimeout`을 설정하세요. 자세한 내용은 **Swift** 탭을 선택하세요.
{% endtab %}
{% endtabs %}

{% alert note %}
세션 타임아웃을 설정하면 모든 세션 시맨틱이 설정된 타임아웃까지 자동으로 연장됩니다.
{% endalert %}

## 문제 해결

### 고객 프로필의 세션 수가 0인 경우

SDK 외부에서 사용자가 생성된 경우 고객 프로필의 세션 수가 0일 수 있습니다:

- **REST API로 생성된 경우:** [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트를 통해 요청에 `app_id`를 포함하여 사용자를 생성하면, 프로필은 해당 앱과 연결되어 표시되지만 해당 사용자에 대해 SDK가 초기화된 적이 없으므로 세션 데이터가 없습니다.
- **CSV 가져오기로 생성된 경우:** 첫 번째 또는 마지막 세션 필드에 값 없이 [CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/)를 통해 사용자를 가져오면 프로필은 세션 수 0으로 존재합니다.