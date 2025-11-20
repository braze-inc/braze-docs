---
nav_title: 일반적인 푸시 오류 메시지
article_title: 일반적인 푸시 오류 메시지
page_order: 22
page_type: reference
description: "이 문서에서는 iOS 및 Android의 일반적인 푸시 관련 오류 메시지를 다루고 잠재적인 해결 방법을 안내합니다."
channel: push
platform:
- iOS
- Android
---

# 일반적인 푸시 오류 메시지

> 이 페이지에서는 푸시 메시징에 대한 일반적인 오류 메시지를 다룹니다.

{% tabs %}
{% tab Android %} 
### 푸시가 반송되었습니다: 불일치 발신자 ID
`MismatchSenderId` 는 인증 실패를 나타냅니다. Firebase 클라우드 메시징(FCM)은 몇 가지 주요 데이터인 발신자 ID와 FCM API 키로 인증합니다.  이 두 가지 모두 정확성을 검증해야 합니다. 자세한 내용은 이 문제에 대한 [Android 설명서를](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) 참조하세요.

일반적인 오류는 다음과 같습니다:
- 잘못된 [발신자 ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- 다른 발신자 ID로 다른 푸시 서비스에 등록하는 경우 중복 등록

### 푸시가 반송되었습니다: 유효하지 않은 등록
`InvalidRegistration` 푸시 토큰이 잘못되었을 때 발생할 수 있습니다. 일반적인 실패 사례로는 다음과 같은 경우가 있습니다:
- 사람들이 Braze 등록 토큰을 수동으로 전달하고 있지만 `getToken()` 으로 전화하지 않습니다. 예를 들어 전체 인스턴스 ID를 전달할 수 있습니다. 오류 메시지의 토큰은 `&#124;ID&#124;1&#124;:[regular token]` 처럼 보입니다.  
- 사람들이 여러 서비스에 등록하고 있습니다. 현재 푸시 등록 의도가 구식으로 도착할 것으로 예상되므로, 사람들이 여러 곳에서 등록하는 경우 다른 서비스에서 의도를 포착하면 잘못된 푸시 토큰을 받을 수 있습니다.

### 푸시가 반송되었습니다: 등록되지 않음
`NotRegistered` 는 일반적으로 앱이 기기에서 삭제되었음을 의미합니다(예: 제거 신호). 여러 번의 등록이 진행 중이고 두 번째 등록으로 인해 Braze가 받은 푸시 토큰이 무효화되는 경우에도 이러한 문제가 발생할 수 있습니다.

{% endtab %}
{% tab iOS %}

### 푸시가 반송되었습니다: BadToken

`BadToken` 오류는 여러 가지 이유로 발생할 수 있습니다:
- 푸시 토큰이 올바르게 전송되지 않습니다. `[[Appboy sharedInstance] registerPushToken:]`
	- [메시지 활동 로그에서]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) 토큰을 확인합니다. 일반적으로 문자와 숫자의 긴 문자열(예: `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`)처럼 보여야 합니다. 그렇지 않은 경우 Braze 푸시 토큰 오류 전송과 관련된 코드를 확인하세요.<br><br>
- 프로비저닝 환경이 일치하지 않습니다:
	- 개발자 인증서로 등록하고 프로덕션 인증서로 보내려고 하면 이 오류가 표시될 수 있습니다.  
	- Braze는 프로덕션 환경에 대한 범용 인증서만 지원합니다. 범용 인증서가 있는 개발자 환경에서는 푸시 테스트가 작동하지 않습니다. 
	- 이 보고는 프로덕션에서는 바운싱을 보내지만 개발자는 보내지 않습니다.<br><br>
- 프로비저닝 프로필이 일치하지 않습니다:
	- 이는 토큰을 받을 때 사용한 인증서와 인증서가 일치하지 않는 경우 발생할 수 있습니다. 이러한 문제가 의심되는 경우 다음 단계를 수행합니다:
		- Braze 대시보드에서 푸시 전송에 사용되는 푸시 인증서와 프로비저닝 프로필이 올바르게 구성되었는지 확인합니다.
		- APNS 인증서를 다시 생성한 후 프로비저닝 프로필을 다시 생성하여 `app_id`. 이렇게 하면 때때로 더 눈에 띄는 문제를 해결할 수 있습니다.

### 푸시가 반송되었습니다: APN 피드백 서비스 제거됨

이는 일반적으로 누군가 설치를 제거할 때 발생합니다. Braze는 매일 밤 APNS 피드백 서비스를 쿼리하여 유효하지 않은 토큰 목록을 가져옵니다. 자세한 내용은 Apple의 [APN과 통신하기를](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) 참조하세요.

{% endtab %}
{% endtabs %}
