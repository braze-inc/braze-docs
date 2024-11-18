---
nav_title: 설치 제거 추적
article_title: Android 및 FireOS용 제거 추적
platform: 
  - Android
  - FireOS
page_order: 7
description: "이 문서에서는 Android 또는 FireOS 애플리케이션에 대한 제거 추적을 구성하는 방법을 다룹니다."

---

# 제거 추적

> 제거 추적은 제거된 기기를 감지하기 위해 Firebase 클라우드 메시징에서 무음 푸시를 사용합니다. Braze는 제거 추적 알림을 지능적으로 삭제하고 일반적인 무음 푸시 의도로 앱에서 커스텀 푸시 콜백을 깨우지 않습니다. 이 문서에서는 Android 또는 FireOS 애플리케이션에 대한 제거 추적을 구성하는 방법을 다룹니다.

푸시 알림이 제거 추적인지 직접 추적하려면 [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html)를 사용합니다.

{% alert important %}
제거 추적 무음 푸시는 Braze 푸시 콜백으로 전달되지 않기 때문에, 이 메서드는 푸시 알림이 Braze로 전달되기 전에만 사용할 수 있습니다. 예를 들어 커스텀 [Firebase 메시징 서비스]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service)를 사용할 때와 같습니다.
{% endalert %}

커스텀 [`Application`](https://developer.android.com/reference/android/app/Application) 서브클래스가 있는 경우, [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) 라이프사이클 메서드에서 서버를 핑하는 자동 로직이 없도록 하십시오. 앱이 이미 실행 중이 아닌 경우 무음 푸시가 앱을 깨우고 `Application` 구성요소를 인스턴스화하기 때문입니다.

자세한 내용은 당사 사용자 안내서의 [제거 추적]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking)을 참조하십시오.

