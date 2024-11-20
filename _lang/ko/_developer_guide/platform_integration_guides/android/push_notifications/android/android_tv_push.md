---
nav_title: Android TV 푸시
article_title: Android TV 푸시
platform: Android
page_order: 8
description: "이 문서에서는 Android TV 푸시를 구현하고 테스트하는 방법을 설명합니다."
channel:
  - push

---

# Android TV 푸시
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> 기본 기능은 아니지만 Braze Android SDK와 Firebase 클라우드 메시징을 활용하여 Android TV용 푸시 토큰을 등록하면 Android TV 푸시 통합이 가능합니다. 그러나 알림 페이로드가 수신된 후 이를 표시하는 UI를 빌드해야 합니다.

## 구현

1. **Braze 안드로이드 SDK 통합**<br>
먼저, 아직 완료하지 않은 경우 [Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true)를 통합해야 합니다.<br><br>
2. **푸시 알림 통합**<br>
다음으로, 아직 완료하지 않은 경우 [Android 푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)을 통합해야 합니다.<br><br>
3. **커스텀 토스트 보기 생성**<br>
그런 다음 앱에서 사용자 지정 보기를 만들어 알림을 표시합니다.<br><br>
4. **사용자 지정 알림 팩토리 만들기**<br>
마지막으로, [커스텀 알림 팩토리]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications)를 생성해야 합니다. 그러면 기본 SDK 동작이 재정의되고 알림을 수동으로 표시할 수 있습니다. `null`을 반환하면 SDK가 처리되지 않으며, 알림을 표시할 커스텀 코드가 필요합니다. 이 단계가 완료되면 Android TV로 푸시 전송을 시작할 수 있습니다!<br><br>
5. **클릭 애널리틱스 추적 설정(선택 사항)**<br>
Braze는 메시지 표시를 자동으로 처리하지 않으므로 클릭 분석을 효과적으로 추적하려면 이를 수동으로 처리해야 합니다. Braze 푸시 열기 및 수신 의도를 수신 대기하도록 [푸시 콜백]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback)을 생성하면 됩니다.

{% alert note %}
이 알림은 **지속되지 않으며**, 기기에 표시될 때만 사용자에게 표시됩니다. 이는 Android TV의 알림 센터가 기록 알림을 지원하지 않기 때문입니다.
{% endalert %} 

## Android TV에서 푸시 테스트 방법

푸시 구현이 성공적인지 테스트하려면 평소 Android 기기에서와 마찬가지로 Braze 대시보드에서 알림을 보냅니다.

- **신청이 마감된 경우**: 푸시 메시지가 화면에 건배 알림을 표시합니다.
- **애플리케이션이 열려 있는 경우**: 자체 호스팅 UI에 메시지를 표시할 수 있습니다. Android 모바일 SDK 인앱 메시지의 UI 스타일을 따르는 것이 좋습니다.

## 추가 정보
Braze에서 마케팅 최종사용자의 경우, Android TV에 대해 캠페인을 시작하는 것은 Android 모바일 앱에 대해 푸시를 시작하는 것과 동일합니다. 이러한 기기를 독점적으로 타겟팅하려면 세분화에서 Android TV 앱을 선택하는 것이 좋습니다. 

FCM이 반환하는 전달 및 클릭 응답은 모바일 Android 기기와 동일한 규칙을 따르므로 메시지 활동 로그에 오류가 표시됩니다.

