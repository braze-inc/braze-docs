---
nav_title: 추적 세션
article_title: Android 및 FireOS에 대한 추적 세션
platform: 
  - Android
  - FireOS
page_order: 0
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 대한 세션 업데이트에 가입하는 방법을 보여줍니다."

---

# 추적 세션

> Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. SDK는 다음 세션 의미 체계에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 '세션 시작' 및 '세션 종료' 데이터 포인트를 생성합니다. 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 대한 세션 업데이트에 가입하는 방법을 보여줍니다.

## 세션 수명 주기

권장되는 [활동 라이프사이클 콜백 통합]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), `openSession()` 및 `closeSession()` 이 앱의 각 활동에 대해 자동으로 호출됩니다. 기본적으로, Android에서는 `openSession()`에 대한 첫 번째 호출 시 세션이 열리고, 앱이 포그라운드에서 10초 넘게 벗어난 후에는 세션이 닫힙니다. `closeSession()`을 호출해도 세션이 즉시 종료되지 않습니다. 오히려 사용자가 중간에 `openSession()`을 호출하지 않으면(예: 다른 활동으로 이동) 10초 후에 세션을 닫습니다.

Android 세션은 호스트 애플리케이션에서 아무런 통신이 없으면 10초 후에 제한 시간이 초과됩니다. 즉, 사용자가 앱을 백그라운드로 전환하고 9초 후에 돌아오면 동일한 세션이 계속됩니다. 사용자가 앱을 백그라운드에 둔 상태에서 세션이 닫히면 앱이 다시 열릴 때까지 해당 데이터가 서버로 플러시되지 않을 수 있습니다.

{% alert note %}
새 세션을 강제로 시작해야 하는 경우 사용자를 변경하면 됩니다.
{% endalert %}

## 세션 시간 초과 사용자 지정
세션 시간 초과를 사용자 지정하려면 [`braze.xml`]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml) 파일에 `com_braze_session_timeout` 를 추가합니다. `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` 의 최소값은 1초입니다.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## 테스트 세션 추적

사용자를 통해 세션을 감지하려면 대시보드에서 사용자를 찾고 고객 프로필에서 **앱 사용**으로 이동합니다. 세션 추적이 예상대로 작동하는지 확인하려면 세션 메트릭이 예상대로 증가하는지 확인하십시오.

![발생한 세션 수, 앱을 처음 사용한 시기, 마지막으로 사용한 시기를 보여주는 사용자 프로필 구성 요소입니다.]({% image_buster /assets/img_archive/test_session.png %})

## 세션 업데이트에 가입

Braze SDK는 세션 업데이트를 수신 대기하기 위해 [`subscribeToSessionUpdates`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html) 가입자를 제공합니다.

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

