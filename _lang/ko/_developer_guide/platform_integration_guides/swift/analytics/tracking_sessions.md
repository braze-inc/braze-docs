---
nav_title: 세션 추적
article_title: iOS용 세션 추적
platform: Swift
page_order: 0
search_rank: 1
description: "이 참조 문서에서는 Swift SDK의 세션 업데이트에 가입하는 방법을 보여줍니다."

---

# 세션 추적

> Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. 

SDK는 다음 세션 의미 체계에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 '세션 시작' 및 '세션 종료' 데이터 포인트를 생성합니다.

## 세션 수명 주기

`Braze.init(configuration:)` 으로 전화하면 세션이 시작됩니다. 기본적으로 `UIApplicationWillEnterForegroundNotification` 알림이 실행될 때(앱이 포그라운드로 표시될 때) 수행됩니다. 앱이 포그라운드를 벗어날 때(예: `UIApplicationDidEnterBackgroundNotification` 알림이 실행되거나 앱이 종료될 때) 세션이 종료됩니다.

{% alert note %}
새 세션을 강제로 시작해야 하는 경우 사용자를 변경하면 됩니다.
{% endalert %}

## 세션 시간 초과 사용자 지정

[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class)에 전달된 `configuration` 오브젝트에서 `sessionTimeout`을 원하는 정수 값으로 설정할 수 있습니다.

{% tabs %}
{% tab swift %}

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
{% endtab %}
{% tab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

세션 시간 제한을 설정한 경우 세션 시맨틱은 모두 해당 사용자 지정 시간 제한으로 확장됩니다.

{% alert note %}
`sessionTimeout` 의 최소값은 1초입니다. 기본값은 10초입니다.
{% endalert %}

## 테스트 세션 추적

사용자를 통해 세션을 감지하려면 대시보드에서 사용자를 찾고 고객 프로필에서 **세션 개요**로 이동합니다. '세션' 측정기준이 예상했던 시점에 증가하는지 확인하여 세션 추적 기술이 작동함을 확인할 수 있습니다. 앱별 세부 정보는 사용자가 두 개 이상의 앱을 사용한 후에 표시됩니다.

![사용자 프로필의 세션 개요 섹션에 세션 수, 마지막으로 사용한 날짜, 처음 사용한 날짜가 표시됩니다.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

앱별 세부 정보는 사용자가 두 개 이상의 앱을 사용한 후에만 표시됩니다.

## 세션 업데이트에 가입

세션 업데이트를 수신하려면 [`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)) 메서드를 사용합니다. 세션 시작 및 종료 이벤트는 앱이 포그라운드에서 실행 중일 때만 기록됩니다. 세션 종료 이벤트에 콜백을 등록하고 앱이 백그라운드에 있는 경우 앱이 다시 포그라운드에 표시되면 콜백이 실행됩니다. 그러나 세션 지속 시간은 여전히 앱이 열리거나 포그라운드에 표시된 시점부터 앱이 닫히거나 백그라운드로 이동될 때까지의 시간으로 측정됩니다.

{% tabs %}
{% tab swift %}
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
{% endtab %}

{% tab objective-c %}
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
{% endtab %}
{% endtabs %}

또는 Swift에서 [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) `AsyncStream`을 사용하여 비동기 변경 사항을 관찰할 수 있습니다.

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

