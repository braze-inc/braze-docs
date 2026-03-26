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
### 푸시 반송: MismatchSenderId
`MismatchSenderId`는 인증 실패를 나타냅니다. Firebase Cloud Messaging(FCM)은 senderID와 FCM API 키라는 두 가지 주요 데이터로 인증합니다. 이 두 가지 모두 정확성을 검증해야 합니다. 자세한 내용은 이 문제에 대한 [Android 설명서](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes)를 참조하세요.

일반적인 실패 원인은 다음과 같습니다:
- 잘못된 [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- 다른 senderID를 사용하는 다른 푸시 서비스에 등록하여 다중 등록이 발생하는 경우

### 푸시 반송: InvalidRegistration
`InvalidRegistration`은 푸시 토큰이 잘못된 형식일 때 발생할 수 있습니다. 일반적인 실패 원인은 다음과 같습니다:
- Braze 등록 토큰을 수동으로 전달하면서 `getToken()`을 호출하지 않는 경우. 예를 들어, 전체 인스턴스 ID를 전달할 수 있습니다. 오류 메시지의 토큰은 `&#124;ID&#124;1&#124;:[regular token]`과 같은 형태입니다.  
- 여러 서비스에 등록하는 경우. 현재 푸시 등록 인텐트가 기존 방식으로 도착할 것으로 예상하므로, 여러 곳에서 등록하고 다른 서비스의 인텐트를 수신하면 잘못된 형식의 푸시 토큰을 받을 수 있습니다.

### 푸시 반송: NotRegistered {#notregistered}
`NotRegistered`는 일반적으로 앱이 기기에서 삭제되었음을 의미합니다(예: 앱 제거 신호). 이는 다중 등록이 발생하고 두 번째 등록이 Braze가 수신한 푸시 토큰을 무효화하는 경우에도 발생할 수 있습니다.

### DEVICE_UNREGISTERED {#device-unregistered}

이 오류는 메시지 활동 로그에 다음과 같이 표시됩니다:

`Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

이 오류는 일반적으로 다음 이유 중 하나로 발생합니다:

- 사용자가 앱을 제거한 경우. 가장 일반적인 원인입니다. 기기에서 앱이 제거되면 푸시 토큰이 무효화됩니다.
- 앱에서 푸시 자격 증명이 업데이트된 경우. 팀에서 앱에 번들된 FCM 자격 증명이나 인증서를 변경하면, 이전 자격 증명으로 등록한 사용자는 앱이 다시 등록할 때까지 유효하지 않은 토큰을 갖게 됩니다.
- 커스텀 로직이 사용자를 푸시에서 등록 해제하는 경우. 드문 경우이지만, Firebase/Android SDK를 사용하여 프로그래밍 방식으로 기기의 푸시 등록을 해제하는 것이 기술적으로 가능합니다.

{% alert note %}
이 오류는 사용자의 푸시가 비활성화되었다는 의미가 아니라, 특정 토큰이 프로필에서 제거되었다는 의미입니다. 이는 기능을 테스트하면서 앱을 자주 설치하고 제거하는 사용자에게 흔히 발생합니다. 사용자에게 여전히 유효한 토큰이 있는지 확인하려면 **사용자 검색**으로 이동하여 **참여** 탭의 **연락처 설정** 섹션을 확인하세요.
{% endalert %}

{% endtab %}
{% tab iOS %}

### 페이로드가 유효하지 않아 푸시 전송 중 오류 발생

이 메시지는 사용자 프로필 **참여** 탭의 **연락처 설정** > **푸시 체인지로그** 아래에 나타날 수 있습니다. Apple 푸시 알림 서비스(APNs)가 유효하지 않은 페이로드로 인해 푸시 요청을 거부할 때 발생합니다.

Braze에서 이 대시보드 메시지는 다음 APNs 오류 사유 중 하나에 매핑될 수 있습니다:

- `PayloadEmpty`: 전송되는 푸시 유형에 필요한 콘텐츠가 페이로드에 누락되었습니다.
- `PayloadTooLarge`: 페이로드가 APNs의 최대 페이로드 크기를 초과했습니다.

일반적인 원인은 다음과 같습니다:

- 커스텀 키(및 해당 값)로 인해 페이로드가 너무 커지는 경우(예상치 못하게 큰 Liquid 렌더링 값이 포함될 수 있습니다).
- 필수 항목인 알림 또는 본문이 비어 있거나 누락된 경우(또는 잘못된 형식의 `aps` 페이로드).

다음 단계:

- 커스텀 키를 줄이고 큰 동적 값을 축소하여 페이로드 크기를 줄이세요.
- API를 통해 전송하는 경우, 전송하기 전에 최종 JSON 페이로드(크기 포함)를 검증하세요.

### 푸시 반송: BadToken

`BadToken` 오류는 여러 가지 이유로 발생할 수 있습니다:
- 푸시 토큰이 Braze에 올바르게 전송되지 않는 경우(예: `registerDeviceToken:` 또는 해당 플랫폼의 동등한 메서드에서).
	- [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에서 토큰을 확인하세요. 일반적으로 긴 문자와 숫자의 문자열(예: `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`)처럼 보여야 합니다. 그렇지 않은 경우 Braze에 푸시 토큰을 전송하는 코드를 확인하세요.<br><br>
- 프로비저닝 환경 불일치:
	- 개발 인증서로 등록하고 프로덕션 인증서로 전송하려고 하면 이 오류가 발생할 수 있습니다.  
	- Braze는 프로덕션 환경에서만 범용 인증서를 지원합니다. 개발 환경에서 범용 인증서를 사용하여 푸시를 테스트하는 것은 작동하지 않습니다. 
	- 이 보고서는 프로덕션에서는 반송을 전송하지만 개발 환경에서는 전송하지 않습니다.<br><br>
- 프로비저닝 프로필 불일치:
	- 인증서가 토큰을 얻는 데 사용된 인증서와 일치하지 않으면 이 문제가 발생할 수 있습니다. 이것이 의심되는 경우 다음 단계를 수행하세요:
		- Braze 대시보드에서 푸시를 보내는 데 사용되는 푸시 인증서와 프로비저닝 프로필이 올바르게 구성되었는지 확인합니다.
		- APNS 인증서를 재생성한 후 APNS 인증서가 `app_id`에 구성되면 프로비저닝 프로필을 다시 생성합니다. 이렇게 하면 일부 눈에 띄는 문제를 해결할 수 있습니다.

### 번들 ID가 허용되지 않음

`TopicDisallowed` 오류는 APNs가 요청의 토픽(번들 ID)이 사용 중인 인증 자격 증명에 허용되지 않아 푸시를 거부했음을 의미합니다. 이를 해결하려면:

1. **번들 ID를 확인하세요.** Braze 앱 설정에 구성된 번들 ID가 앱의 번들 ID와 정확히 일치하는지 확인하세요. 접미사 변형(예: `.debug`, `.staging`)도 포함됩니다.
2. **APNs 인증 설정을 확인하세요.** 앱이 올바른 APNs `.p8` 키로 구성되어 있고, 해당 키가 전송 대상 앱과 동일한 Apple Developer Team에 연결되어 있는지 확인하세요.
3. **앱 환경을 확인하세요.** 개발 빌드와 프로덕션 빌드에 대해 Braze에서 별도의 앱 ID를 사용하는 경우, 각각 올바른 푸시 자격 증명과 환경으로 구성되어 있는지 확인하세요.

### Unregistered {#ios-unregistered}

이 오류는 메시지 활동 로그에 다음과 같이 표시됩니다:

`Received 'Unregistered' sending to '[Token String]'`

이는 Android의 [DEVICE_UNREGISTERED](#device-unregistered) 오류에 해당하는 iOS 버전입니다. 일반적으로 다음 이유 중 하나로 발생합니다:

- 사용자가 앱을 제거한 경우. 가장 일반적인 원인입니다.
- 푸시 인증서가 업데이트된 경우. 팀에서 APNs 인증서를 변경하거나 갱신하면, 이전 인증서로 등록한 사용자는 앱이 다시 등록할 때까지 유효하지 않은 토큰을 갖게 될 수 있습니다.
- 커스텀 로직이 사용자를 푸시에서 등록 해제하는 경우. 드문 경우이지만, iOS SDK를 사용하여 프로그래밍 방식으로 원격 알림 등록을 해제하는 것이 기술적으로 가능합니다.

{% alert note %}
이 오류는 사용자의 푸시가 비활성화되었다는 의미가 아니라, 특정 토큰이 프로필에서 제거되었다는 의미입니다. 사용자에게 여전히 유효한 토큰이 있는지 확인하려면 **사용자 검색**으로 이동하여 **참여** 탭의 **연락처 설정** 섹션을 확인하세요.
{% endalert %}

### InvalidProviderToken

`InvalidProviderToken` 오류는 APNs가 인증 토큰(`.p8` 키에서 생성)이나 푸시 인증서(`.p12`)가 앱의 번들 ID 또는 Team ID와 일치하지 않아 요청을 거부했음을 의미합니다. 이를 해결하려면:

1. **Team ID와 Key ID를 확인하세요:** `.p8` 인증 키를 사용하는 경우, Braze 대시보드(**설정** > **앱 설정** > iOS 앱 선택)에 구성된 **Team ID**와 **Key ID**가 Apple Developer 계정의 값과 일치하는지 확인하세요.
2. **번들 ID를 확인하세요:** Braze에 등록된 번들 ID가 앱의 번들 ID와 일치하는지 확인하세요. 대소문자 차이나 `.debug` 접미사와 같은 불일치가 이 오류를 유발합니다.
3. **키 또는 인증서를 다시 업로드하세요:** `.p8` 키 또는 `.p12` 인증서가 최근에 재생성되었거나 폐기된 경우, 새 키를 Braze에 업로드하고 이전 키를 제거하세요.
4. **APNs 환경을 확인하세요:** `.p12` 인증서를 사용하는 경우, 업로드 시 올바른 환경(개발 또는 프로덕션)을 선택했는지 확인하세요. `.p8` 키의 경우 이는 자동으로 처리됩니다.

### 푸시 반송: APNS 피드백 서비스에서 제거됨

일반적으로 누군가가 앱을 제거할 때 발생합니다. Braze는 매일 밤 APNS 피드백 서비스에 쿼리를 보내 유효하지 않은 토큰 목록을 가져옵니다. 자세한 내용은 Apple의 [APNs와의 통신](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)을 참조하세요.

{% endtab %}
{% endtabs %}