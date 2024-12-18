---
nav_title: 문제 해결
article_title: FireOS용 푸시 문제 해결
platform: FireOS
page_order: 20
page_type: solution
description: "이 참조 문서에서는 푸시 알림과 관련하여 발생할 수 있는 문제에 대한 FireOS 문제 해결 시나리오를 제공합니다."
channel: push

---

# 문제 해결

> 이 문서에서는 몇 가지 FireOS 문제 해결 시나리오를 제공합니다.

## 푸시 오류 로그 활용하기

Braze는 메시지 활동 로그 내에서 푸시 알림 오류를 제공합니다. 이 오류 로그는 캠페인이 예상대로 작동하지 않는 이유를 파악하는 데 매우 유용한 다양한 경고를 제공합니다. 오류 메시지를 클릭하면 특정 인시던트 문제를 해결하는 데 도움이 되는 관련 설명서로 리디렉션됩니다.

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## 문제 해결 시나리오

### Braze 대시보드에 '푸시 등록' 사용자가 표시되지 않음(메시지 전송 전)

- 앱이 푸시 알림을 허용하도록 올바르게 구성되어 있는지 확인합니다.
- Braze 대시보드에 구성된 클라이언트 ID와 클라이언트 비밀번호가 올바른지 확인하세요.

### 사용자 디바이스에 표시되지 않는 푸시 알림

이러한 문제가 발생하는 데에는 몇 가지 이유가 있습니다:

- 애플리케이션을 강제 종료하면 앱이 실행되지 않는 동안 푸시 알림이 표시되지 않습니다.
- 캠페인에서 [알림 우선순위]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) 설정이 `HIGH` 로 설정되어 있는지 확인합니다.
- `api_key.txt` 의 ADM API 키가 올바르지 않거나 잘못된 문자가 포함되어 있습니다.
- `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` 및 `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />`에 대한 의도 필터를 사용해 `AndroidManifest.xml`에 `BrazeAmazonDeviceMessagingReceiver`가 제대로 등록되지 않았습니다.

### 메시지 전송 후 '푸시 등록' 사용자가 더 이상 활성화되지 않음

일반적으로 사용자가 애플리케이션을 제거하여 ADM 등록 ID가 유효하지 않게 된 경우에 이 문제가 발생합니다.

