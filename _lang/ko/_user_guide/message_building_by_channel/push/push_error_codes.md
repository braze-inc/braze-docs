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

> 이 페이지에서는 푸시 메시징의 일반적인 오류 메시지에 대해 설명합니다.

{% tabs %}
{% tab Android %} 
### 푸시 반송됨: MismatchSenderId
`MismatchSenderId`은 인증 실패를 나타냅니다. Firebase Cloud Messaging(FCM)은 주요 데이터 조각인 senderID 및 FCM API 키로 인증합니다.  이들은 모두 정확성을 위해 검증되어야 합니다. 자세한 내용은 이 문제에 대한 [Android 설명서](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes)를 참조하십시오.

일반적인 실패에는 다음이 포함될 수 있습니다:
- 나쁜 [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- 다른 senderID로 다른 푸시 서비스에 등록하면 여러 번 등록됩니다

### 푸시 반송됨: InvalidRegistration
`InvalidRegistration`은 푸시 토큰이 잘못된 형식일 때 발생할 수 있습니다. 일반적인 실패에는 다음과 같은 경우가 포함될 수 있습니다.
- 사람들이 Braze 등록 토큰을 수동으로 전달하고 있지만 `getToken()`을(를) 호출하지 않습니다. 예를 들어, 그들은 전체 인스턴스 ID를 전달할 수 있습니다. 오류 메시지의 토큰은 `&#124;ID&#124;1&#124;:[regular token]`처럼 보입니다.  
- 사람들이 여러 서비스에 등록하고 있습니다. 현재 푸시 등록 의도가 구식으로 도착할 것으로 예상되므로, 사람들이 여러 장소에서 등록하고 다른 서비스에서 의도를 포착하면 잘못된 푸시 토큰을 받을 수 있습니다.

### 푸시 반송됨: NotRegistered
`NotRegistered`는 일반적으로 앱이 기기에서 삭제되었음을 의미합니다(예: 제거 신호). 이것은 여러 등록이 발생하고 두 번째 등록이 Braze가 받는 푸시 토큰을 무효화하는 경우에도 발생할 수 있습니다.

{% endtab %}
{% tab iOS %}

### 푸시 반송됨: BadToken

`BadToken` 오류는 여러 가지 이유로 발생할 수 있습니다:
- 푸시 토큰이 `[[Appboy sharedInstance] registerPushToken:]`에게 올바르게 전송되지 않고 있습니다
	- [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에서 토큰을 확인하세요. 일반적으로 긴 문자와 숫자의 문자열(예: `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`)처럼 보여야 합니다. 그렇지 않은 경우 Braze 푸시 토큰 오류 전송과 관련된 코드를 확인하세요.<br><br>
- 프로비저닝 환경이 일치하지 않음:
	- 개발 인증서로 등록하고 프로덕션 인증서로 보내려고 하면 이 오류를 볼 수 있습니다.  
	- Braze는 프로덕션 환경에서만 범용 인증서를 지원합니다. 개발 환경에서 보편적인 인증서를 사용하여 푸시를 테스트하는 것은 작동하지 않습니다. 
	- 이 보고서는 개발이 아닌 프로덕션에서 바운싱을 보냅니다.<br><br>
- 프로비저닝 프로필 불일치:
	- 인증서가 토큰을 얻는 데 사용된 것과 일치하지 않으면 이런 일이 발생할 수 있습니다. 이것이 의심되는 경우 다음 단계는 다음을 포함합니다:
		- 푸시 인증서가 Braze 대시보드에서 푸시를 보내는 데 사용되고 프로비저닝 프로필이 올바르게 구성되었는지 확인합니다.
		- APNS 인증서를 재생성한 후 APNS 인증서가 `app_id`에 구성되면 프로비저닝 프로필을 다시 생성합니다. 이것은 때때로 더 눈에 띄는 문제를 해결할 수 있습니다.

### 푸시 반송됨: APNS 피드백 서비스 제거됨

일반적으로 누군가가 프로그램을 제거할 때 발생합니다. Braze는 매일 밤 APNS 피드백 서비스에 쿼리를 보내 잘못된 토큰 목록을 가져옵니다. 자세한 내용은 Apple의 [APNs와의 통신](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)을 참조하십시오.

{% endtab %}
{% endtabs %}
