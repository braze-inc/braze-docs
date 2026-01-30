## 제거 추적 설정하기

### 1단계: FCM 설정하기

Android Braze 소프트웨어 개발 키트는 FCM(Firebase 클라우드 메시징)을 사용하여 제거 추적 분석을 수집하는 데 사용되는 자동 푸시 알림을 전송합니다. 아직 설정하지 않았다면 푸시 알림을 위해 Firebase Cloud 메시징 API를 [설정하거나]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) [마이그레이션하세요]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

### 2단계: 수동으로 제거 추적 감지(선택 사항)

기본값으로 Android Braze 소프트웨어 개발 키트는 제거 추적과 관련된 무음 푸시 알림을 자동으로 감지하고 무시합니다. 그러나 제거 추적을 수동으로 감지하려면 [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) 메서드를 사용하여 수동으로 탐지할 수 있습니다.

{% alert important %}
제거 추적을 위한 무음 알림은 어떤 Braze 푸시 콜백에도 전달되지 않으므로 이 방법은 푸시 알림을 Braze에 전달하기 전에만 사용할 수 있습니다.
{% endalert %}

### 3단계: 자동 서버 핑 제거하기

무음 푸시 알림은 앱이 아직 실행되고 있지 않은 경우 앱을 깨우고 `Application` 컴포넌트를 인스턴스화합니다. 따라서 커스텀된 [`Application`](https://developer.android.com/reference/android/app/Application) 서브클래스가 있다면, 수명 주기 동안 서버를 자동으로 핑하는 로직을 모두 제거하세요. [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) 라이프사이클 메서드에서 자동으로 서버를 핑하는 로직을 제거하세요.

### 4단계: 제거 추적 활성화

마지막으로 Braze에서 제거 추적을 인에이블먼트합니다. 전체 안내는 [제거 추적 사용을]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) 참조하세요.

{% alert important %}
제거 추적은 정확하지 않을 수 있습니다. Braze에 표시되는 지표는 지연되거나 부정확할 수 있습니다.
{% endalert %}
