---
nav_title: Firebase 클라우드 메시징으로 마이그레이션
article_title: Firebase Cloud 메시징 API로 마이그레이션하기
platform: Android
page_order: 29
description: "이 문서에서는 더 이상 사용되지 않는 Google의 클라우드 메시징 API에서 Firebase 클라우드 메시징(FCM)으로 마이그레이션하는 방법을 다룹니다."
channel:
  - push
search_rank: 3
---

# Firebase Cloud 메시징 API로 마이그레이션하기

> 더 이상 사용되지 않는 Google의 클라우드 메시징 API에서 완전히 지원되는 Firebase 클라우드 메시징(FCM) API로 마이그레이션하는 방법을 알아봅니다. 자세한 내용은 Google의 [Firebase FAQ - 2023](https://firebase.google.com/support/faq#fcm-23-deprecation)을 참조하세요.

{% alert important %}
Android용 푸시 연동 기능을 처음 설정하는 경우에는 [표준 Android 푸시 연동 기능을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration) 참조하세요.
{% endalert %}

## 사용량 제한

Firebase 클라우드 메시징(FCM) API의 기본 사용량 제한은 분당 600,000건의 요청입니다. 이 제한에 도달하면 Braze는 몇 분 후에 자동으로 다시 시도합니다. 증액을 요청하려면 [Firebase 지원팀에](https://firebase.google.com/support) 문의하세요.

## FCM으로 마이그레이션

### 1단계: 프로젝트 ID 확인

먼저 Google Cloud를 엽니다. 프로젝트 홈 페이지의 **프로젝트 ID** 필드에서 숫자를 확인합니다. 이 숫자를 다음에 Firebase 프로젝트의 숫자와 비교합니다.

!['프로젝트 ID'가 강조 표시된 Google Cloud 프로젝트의 홈 페이지]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

그런 다음 Firebase 콘솔을 열고 <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정을** 선택합니다.

!["설정" 메뉴가 열려 있는 Firebase 프로젝트]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**일반** 탭에서 **프로젝트 ID**가 Google Cloud 프로젝트에 나열된 것과 일치하는지 확인합니다.

!['프로젝트 ID'가 강조 표시된 Firebase 프로젝트의 '설정' 페이지.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### 2단계: 발신자 ID 확인

먼저 Braze를 연 다음 <i class="fa-solid fa-gear"></i> **설정** > **앱 설정을** 선택합니다.

![Braze에서 '앱 설정'이 강조 표시된 상태로 '설정' 메뉴가 열립니다.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

Android 앱의 **푸시 알림 설정에서** **Firebase 클라우드 메시징 발신자 ID** 필드에 있는 숫자를 확인합니다(이 숫자는 다음에 Firebase 프로젝트의 숫자와 비교됩니다).

!['푸시 알림 설정' 양식]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

그런 다음 Firebase 콘솔을 열고 <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정을** 선택합니다.

!["설정" 메뉴가 열려 있는 Firebase 프로젝트]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messaging**을 선택합니다. **Cloud Messaging API(레거시)**에서 **발신자ID**가 Braze 대시보드에 나열된 것과 일치하는지 확인합니다.

!['발신자 ID'가 강조 표시된 Firebase 프로젝트의 '클라우드 메시징' 페이지.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### 3단계: Firebase 클라우드 메시징 API 활성화

Google Cloud에서 Android 앱이 사용 중인 프로젝트를 선택한 다음, [Firebase 클라우드 메시징 API](https://console.cloud.google.com/apis/library/fcm.googleapis.com)를 활성화합니다.

![Firebase 클라우드 메시징 API 사용]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### 4단계: 서비스 계정 만들기

다음으로 Braze가 FCM 토큰을 등록할 때 승인된 API 호출을 할 수 있도록 새 서비스 계정을 생성합니다. Google Cloud에서 **서비스 계정으로** 이동한 다음 프로젝트를 선택합니다. **서비스 계정** 페이지에서 **서비스 계정 생성**을 선택합니다.

!['서비스 계정 생성'이 강조 표시된 프로젝트의 서비스 계정 홈 페이지.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

서비스 계정 이름, ID, 설명을 입력한 다음, **생성 후 계속**을 선택합니다.

!['서비스 계정 세부 정보' 양식]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

**역할** 필드의 역할 목록에서 **Firebase Cloud 메시징 API 관리자를** 찾아 선택합니다. 보다 제한적인 액세스를 원하면 `cloudmessaging.messages.create` 권한으로 [커스텀 역할](https://cloud.google.com/iam/docs/creating-custom-roles)을 생성한 다음, 목록에서 해당 역할을 선택합니다. 완료했으면 **완료**를 선택합니다.

{% alert warning %}
_Firebase 클라우드 메시징 관리자_가 아닌 _Firebase 클라우드 메시징 **API** 관리자_를 선택해야 합니다.
{% endalert %}

!['Firebase 클라우드 메시징 API 관리자'가 역할로 선택된 '프로젝트에 대한 액세스 권한을 이 서비스 계정에 부여' 양식.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### 5단계: 권한 확인(선택 사항)

서비스 계정이 보유한 권한을 확인하려면 Google Cloud를 연 다음, 프로젝트로 이동하고 **IAM**을 선택합니다. **담당자별 보기에서** **초과 권한을** 선택합니다.

![각 주체에 대한 초과 권한 수가 나열된 '주체별 보기' 탭.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

이제 선택한 역할에 할당된 현재 권한을 검토할 수 있습니다.

![선택한 역할에 할당된 현재 권한 목록입니다.]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### 6단계: JSON 자격 증명 생성

다음으로 FCM 서비스 계정에 대한 JSON 자격 증명을 생성합니다. Google Cloud IAM 및 관리자에서 **서비스 계정**으로 이동한 다음, 프로젝트를 선택합니다. [이전에 만든](#step-4-create-a-service-account) FCM 서비스 계정을 찾은 다음, <i class="fa-solid fa-ellipsis-vertical"></i> **작업** > **키 관리**를 선택합니다.

![프로젝트의 서비스 계정 홈페이지에서 '작업' 메뉴가 열려 있습니다.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

**키 추가** > **새 키 생성**을 선택합니다.

{% alert note %}
새 키를 생성해도 기존 키는 제거되지 않습니다. **자격 증명 되돌리기**를 선택하여 새 키를 실수로 삭제하는 경우 Braze는 레거시 키를 백업으로 사용합니다.
{% endalert %}

!["키 추가" 메뉴가 열려 있는 선택한 서비스 계정]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

**JSON**을 선택한 다음, **생성**을 선택합니다. FCM 프로젝트 ID 이외의 Google Cloud 프로젝트 ID를 사용하여 서비스 계정을 생성한 경우, JSON 파일에서 `project_id`에 할당된 값을 수동으로 업데이트해야 합니다.

키를 다운로드한 위치를 기억해야 합니다. 다음 단계에 필요합니다.

!["JSON"을 선택한 상태에서 개인 키를 생성하는 양식입니다.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
비공개 키는 손상될 경우 보안 위험을 초래할 수 있습니다. 지금은 JSON 자격 증명을 보안 위치에 보관하고, Braze에 업로드한 후에 키를 삭제합니다.
{% endalert %}

### 7단계: Braze에 JSON 자격 증명 업로드하기

Braze에서 <i class="fa-solid fa-gear"></i> **설정** > **앱 설정을** 선택합니다.

![Braze에서 '앱 설정'이 강조 표시된 상태로 '설정' 메뉴가 열립니다.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

**푸시 알림 설정**에서 **JSON 파일 업로드**를 선택한 다음, [이전에 생성](#step-6-generate-json-credentials)한 파일을 선택합니다. 완료했으면 **저장을** 선택합니다.

!['Firebase 클라우드 메시징 서버 키' 필드에서 비공개 키가 업데이트된 '푸시 알림 설정' 양식.]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
비공개 키는 손상될 경우 보안 위험을 초래할 수 있습니다. 키가 Braze에 업로드되었으므로 [이전에 생성](#step-6-generate-json-credentials)한 파일을 컴퓨터에서 삭제합니다.
{% endalert %}

### 8단계: 새 자격 증명 테스트(선택 사항)

Braze에 자격 증명을 업로드하는 즉시 새 자격 증명을 사용하여 푸시 알림을 보낼 수 있습니다. 새 자격 증명을 테스트하려면 FCM 또는 Braze를 사용하여 앱에 실제 또는 테스트 푸시 알림을 보냅니다. 푸시 알림이 전송되면 모든 것이 정상적으로 작동하는 것입니다. 그렇지 않은 경우:

- [발신자 ID 확인](#step-2-verify-your-sender-id)
- [권한 확인](#step-5-verify-permissions-optional)
- [메시지 활동 로그에서]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) 푸시 알림 오류 검토

여전히 문제가 있는 경우 [자격 증명 되돌리기를](#reverting-your-credentials) 참조하세요.

## 자격 증명 되돌리기

언제든지 새 자격 증명을 삭제하고 레거시 자격 증명을 복원할 수 있습니다. 자격 증명이 복원되는 즉시 레거시 자격 증명을 사용하여 푸시 알림을 보내기 시작할 수 있습니다.

Braze에서 <i class="fa-solid fa-gear"></i> **설정** > **앱 설정을** 선택합니다. **푸시 알림 설정에서** **자격 증명 되돌리기를** 선택합니다.

{% alert warning %}
새 자격 증명을 삭제하면 나중에 복원할 수 없습니다. [새 자격 증명을 생성](#step-6-generate-json-credentials)하여 [Braze에 다시 업로드](#step-7-upload-your-json-credentials-to-braze)해야 합니다.
{% endalert %}

!['자격 증명 되돌리기' 버튼이 강조 표시된 '푸시 알림 설정' 양식.]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## 자주 묻는 질문(FAQ) {#faq}

### 새 인증정보가 제대로 작동하는지 어떻게 알 수 있나요?

새 자격 증명을 Braze에 업로드하는 즉시 작동이 시작됩니다. 이를 테스트하려면 **자격 증명 테스트**를 선택합니다. 오류가 발생하면 언제든지 [자격 증명을 되돌릴](#reverting-your-credentials) 수 있습니다.

### 사용하지 않는 앱이나 개발 앱에 대해 FCM으로 마이그레이션해야 하나요?

그러나 사용하지 않는 앱과 개발 앱에는 마이그레이션을 요청하는 경고 메시지가 계속 표시됩니다. 이 메시지를 제거하려면 새 자격 증명을 업로드하거나 워크스페이스에서 이러한 앱을 삭제하면 됩니다. 이러한 앱을 삭제하기로 선택한 경우, 다른 사람이 해당 앱을 사용하고 있는지 팀에 먼저 확인하시기 바랍니다.

### 오류 메시지는 어디에서 확인할 수 있나요?

[메시지 활동 로그에서]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) 푸시 알림 오류를 검토할 수 있습니다.

### 마이그레이션하기 전에 앱 또는 SDK를 업데이트해야 하나요?

아니요. 새 자격 증명을 Braze에 업로드하기만 하면 됩니다.

### 기존 레거시 자격 증명을 먼저 삭제해야 하나요?

아니요. 새 자격 증명을 삭제해야 하는 경우에도 [레거시 자격 증명을 대신 사용할 수 있습니다](#reverting-your-credentials).

### 마이그레이션 후에도 여전히 Braze에 경고 메시지가 표시되는 이유는 무엇인가요?

워크스페이스에 여전히 마이그레이션해야 하는 Android 앱이 하나 이상 있는 경우 이 경고 메시지가 계속 표시됩니다. 모든 Android 앱을 Google에서 완벽하게 지원하는 FCM API로 마이그레이션하세요.

### 마이그레이션 후 푸시 알림을 다시 보낼 때까지 얼마나 걸리나요?

마이그레이션 후에는 새 자격 증명을 사용하여 바로 푸시 알림을 보내기 시작할 수 있습니다.

### FCM 프로젝트가 아닌 다른 프로젝트를 사용하여 서비스 계정을 만들면 어떻게 되나요?

FCM 프로젝트 ID 이외의 Google Cloud 프로젝트 ID를 사용하여 서비스 계정을 생성한 경우, [새로 생성한 후에](#step-6-generate-json-credentials) JSON 파일에서 `project_id`에 할당된 값을 수동으로 업데이트해야 합니다.
