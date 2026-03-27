---
page_order: 1.3
nav_title: 디버깅
article_title: Braze SDK 디버깅하기 
description: "앱에서 상세 로깅을 수동으로 활성화하지 않고도 SDK 기반 채널의 문제를 해결할 수 있도록 Braze SDK 디버거를 사용하는 방법을 알아보세요."
---

# Braze SDK 디버깅하기

> 앱에서 상세 로깅을 활성화하지 않고도 SDK 기반 채널의 문제를 해결할 수 있도록 Braze SDK에 내장된 디버거를 사용하는 방법을 알아보세요.

{% alert tip %}
더 심층적인 조사가 필요한 경우, [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하여 자세한 SDK 출력을 캡처하고, 특정 채널에 대한 [상세 로그를 읽는 방법]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)도 확인할 수 있습니다.
{% endalert %}

## 필수 조건

Braze SDK 디버거를 사용하려면 "PII 보기" 및 "고객 프로필 보기(PII 삭제됨)" 세분화 권한(또는 "PII 준수 고객 프로필 보기" 레거시 권한)이 필요합니다. 디버깅 세션 로그를 다운로드하려면 "사용자 데이터 내보내기" 권한도 필요합니다. 또한 Braze SDK는 다음 최소 버전 이상이어야 합니다: 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Braze SDK 디버깅하기

{% alert tip %}
Braze 웹 SDK의 디버깅을 활성화하려면 [URL 매개변수를 사용]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging)하면 됩니다.
{% endalert %}

### 1단계: 앱 닫기

디버깅 세션을 시작하기 전에 현재 문제가 발생하고 있는 앱을 닫으세요. 세션 시작 시 앱을 다시 실행할 수 있습니다.

### 2단계: 디버깅 세션 생성

Braze에서 **설정**으로 이동한 다음 **설정 및 테스트**에서 **SDK 디버거**를 선택합니다.

!["SDK 디버거"가 강조 표시된 "설정 및 테스트" 섹션.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

**디버깅 세션 생성**을 선택합니다.

!["SDK 디버거" 페이지.]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### 3단계: 사용자 선택

이메일 주소, `external_id`, 사용자 별칭 또는 푸시 토큰을 사용하여 사용자를 검색합니다. 세션을 시작할 준비가 되면 **사용자 선택**을 선택합니다.

![선택한 사용자의 디버깅 페이지.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### 4단계: 앱 다시 실행

먼저 앱을 실행하고 기기가 페어링되었는지 확인합니다. 페어링에 성공하면 앱을 다시 실행하세요&#8212;이렇게 하면 앱의 초기화 로그가 완전히 캡처됩니다.

### 5단계: 재현 단계 완료

앱을 다시 실행한 후 오류를 재현하는 단계를 따라 진행합니다.

{% alert tip %}
오류를 재현할 때는 재현 단계를 가능한 한 정확히 따라 [양질의 로그](#step-6-export-your-session-logs-optional)를 생성할 수 있도록 하세요.
{% endalert %}

### 6단계: 세션 종료

재현 단계를 완료했으면 **세션 종료** > **닫기**를 선택합니다.

!["세션 종료" 버튼이 표시된 디버깅 세션.]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
세션 길이와 네트워크 연결 상태에 따라 로그를 생성하는 데 몇 분 정도 걸릴 수 있습니다.
{% endalert %}

### 7단계: 세션 공유 또는 내보내기(선택 사항)

세션이 끝나면 세션 로그를 CSV 파일로 내보낼 수 있습니다. 또한 다른 사람이 **세션 ID**를 사용하여 디버그 세션을 검색할 수 있으므로 로그를 직접 보낼 필요가 없습니다.

![세션 종료 후 "로그 내보내기" 및 "세션 ID 복사"가 표시된 디버깅 페이지.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})