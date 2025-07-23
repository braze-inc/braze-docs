## 제거 추적 설정

### 1단계: FCM 설정

Android Braze SDK는 Firebase 클라우드 메시징(FCM)을 사용하여 제거 추적 분석을 수집하는 데 사용되는 무음 푸시 알림을 전송합니다. 아직 설정하지 않았다면 푸시 알림을 위해 Firebase 클라우드 메시징 API를 [설정하거나]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) [마이그레이션하세요]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

### 2단계: 제거 추적 수동 감지(선택 사항)

기본적으로 Android Braze SDK는 제거 추적과 관련된 무음 푸시 알림을 자동으로 감지하고 무시합니다. 그러나 제거 추적을 수동으로 감지하도록 선택하면 [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) 메서드를 사용하여 수동으로 탐지할 수 있습니다.

{% alert important %}
제거 추적에 대한 무음 알림은 Braze 푸시 콜백으로 전달되지 않으므로, 이 방법은 Braze에 푸시 알림을 전달하기 전에만 사용할 수 있습니다.
{% endalert %}

### 3단계: 자동 서버 핑 제거

무음 푸시 알림은 앱이 아직 실행 중이 아닌 경우 앱을 깨우고 `Application` 컴포넌트를 인스턴스화합니다. 따라서 사용자 정의 [`Application`](https://developer.android.com/reference/android/app/Application) 서브클래스가 있는 경우, 수명 주기 메서드 중에 서버를 자동으로 핑하는 로직을 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) 라이프사이클 메서드에서 자동으로 서버를 핑하는 로직을 제거하세요.

### 4단계: 제거 추적 활성화

마지막으로 Braze에서 제거 추적을 활성화합니다. 전체 안내는 [제거 추적 사용을]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) 참조하세요.

{% alert important %}
제거 추적은 정확하지 않을 수 있습니다. Braze에 표시되는 지표는 지연되거나 부정확할 수 있습니다.
{% endalert %}
