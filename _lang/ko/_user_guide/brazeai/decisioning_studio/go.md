---
nav_title: 의사 결정 스튜디오 Go
article_title: BrazeAI 의사 결정 스튜디오 Go
page_order: 0
description: "BrazeAI Decisioning <sup>StudioTM</sup> Go를 설정하고 통합하는 방법을 알아보세요."
---

# BrazeAI 의사 결정 스튜디오™ Go

> Braze에서 주요 정보를 찾아 BrazeAI Decisioning Studio™ Go와 통합을 시작하세요.

## 필수 항목

### Braze에서 REST API 키 생성하기

새 REST API 키를 만들려면 다음과 같이 하세요:

1. Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키로** 이동합니다.
2. **API 키 생성을** 선택합니다.
3. API 키의 이름을 입력합니다. 예를 들어 "DecisioningStudioGoEmail"이 있습니다.
4. 다음 카테고리를 기준으로 권한을 선택합니다:
    - **사용자 데이터:** `users.track`, `users.delete`, `users.export.ids` 을 선택합니다, `users.export.segment`
    - **메시지:** 선택 `messages.send`
    - **캠페인:** 나열된 모든 권한을 선택합니다.
    - **캔버스:** 나열된 모든 권한을 선택합니다.
    - **세그먼트:** 나열된 모든 권한을 선택합니다.
    - **템플릿:** 나열된 모든 권한 선택

{: start="5"}
5\. **API 키 생성을** 선택합니다.
6\. 그런 다음 API 키를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣습니다.

### Braze 이메일 표시 이름 찾기

Braze 이메일 표시명을 찾으려면:

1. Braze 대시보드에서 **설정** > **이메일 환경설정으로** 이동합니다.
2. BrazeAI Decisioning Studio™ Go에 사용할 표시 이름을 찾습니다.
3. 보낸 사람 **표시 이름을** 복사하여 BrazeAI Decisioning Studio™ Go 포털에 **이메일 표시 이름으로** 붙여넣습니다.
4. 연결된 이메일 주소를 복사하여 지역 부분과 도메인을 결합한 **발신자 이메일 주소로** BrazeAI Decisioning Studio™ Go 포털에 붙여넣습니다.

### 사용자 ID 찾기

사용자 ID를 찾으려면:

1. Braze 대시보드에서 **오디언스** > **사용자 검색으로** 이동합니다.
2. 외부 사용자 ID, 사용자 별칭, 이메일, 전화번호 또는 푸시 토큰으로 사용자를 검색합니다.
3. 설정에서 참조할 사용자 ID를 복사합니다.

![ID로 사용자를 찾은 고객 프로필 예시.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Braze URL 찾기

Braze URL 식별자:

1. Braze 대시보드로 이동합니다.
2. 브라우저 창에서 Braze URL은 `https://` 으로 시작하고 `braze.com` 으로 끝납니다. Braze URL의 예는 `https://dashboard-01.braze.com` 입니다.

### Braze API 키 찾기

{% alert note %}
Braze는 활동을 워크스페이스의 특정 앱과 연결하는 등 추적 목적으로 사용할 수 있는 앱 ID(Braze 대시보드에서 API 키라고 함)를 제공합니다. 앱 ID를 사용하는 경우, BrazeAI Decisioning Studio™ Go는 각 실험자에게 앱 ID를 연결할 수 있도록 지원합니다.<br><br>앱 ID를 사용하지 않는 경우 입력 안내 문자열로 아무 문자나 입력할 수 있습니다.
{% endalert %}

1. Braze 대시보드에서 **설정** > **앱 설정으로** 이동합니다.
2. 추적하려는 앱으로 이동합니다.
3. **API 키를** 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 클라비요 API 키 설정하기

BrazeAI Decisioning Studio™ Go에 Klaviyo를 사용하려면 API 키를 설정해야 합니다.

1. 클라비요에서 **설정** > **API 키로** 이동합니다.
2. **비공개 API 키 생성을** 선택합니다. 
3. Enter a name for the API key. 예를 들어 '의사 결정 스튜디오 실험자'가 있습니다.
4. API 키에 대해 다음 권한을 선택합니다:
    - Campaigns: 읽기 액세스
    - 데이터 프라이버시: 전체 액세스
    - 이벤트: 전체 액세스
    - 흐름: 전체 액세스
    - 이미지: 읽기 액세스
    - 목록: 전체 액세스
    - 측정기준: 전체 액세스
    - 프로필: 전체 액세스
    - 세그먼트: 읽기 액세스
    - 템플릿: 전체 액세스
    - 웹훅: 읽기 액세스

![선택한 권한이 있는 클라비요 API 키입니다.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Select **Create**.
6\. 이 API 키를 복사하여 메시지가 표시되는 곳에 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### SFMC 앱 패키지 설정하기

BrazeAI Decisioning Studio™ Go용 Salesforce 마케팅 클라우드를 사용하려면 Salesforce 마케팅 클라우드에서 앱 패키지를 설정해야 합니다. 

1. 마케팅 클라우드 홈페이지로 이동합니다. 
2. 글로벌 헤더에서 메뉴를 열고 **설정을** 선택합니다.
3. 사이드 패널 탐색의 **플랫폼 도구** 아래에서 **앱으로** 이동한 다음 **설치된 패키지를** 선택합니다.
4. **새로** 만들기를 선택하여 앱 패키지를 만듭니다.
5. 앱 패키지에 이름과 설명을 입력합니다.

!["실험자 1 - 테스트 5"라는 이름의 앱 패키지입니다.]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. **구성 요소 추가를** 선택합니다.
7\. **컴포넌트 유형에서** **API 통합을** 선택합니다. 그런 다음 **다음을** 선택합니다.
8\. **통합 유형에서** **서버 간을** 선택합니다. 그런 다음 **다음을** 선택합니다.
9\. 그런 다음 앱 패키지에 대해서만 다음 권장 범위를 선택합니다:
    \- 채널 > 이메일 > 읽기, 쓰기, 보내기
    \- 채널 > OTT > 읽기
    \- 채널 > 푸시 > 읽기
    \- 채널 > SMS > 읽기
    \- 채널 > 소셜 > 읽기
    \- 채널 > 웹 > 읽기
    \- 자산 > 설명서 및 이미지 > 읽기, 쓰기
    \- 자산 > 저장된 콘텐츠 > 읽기, 쓰기
    \- 자동화 > 자동화 > 읽기, 쓰기, 실행
    \- 자동화 > 여정 > 읽기, 쓰기, 실행, 활성화/중지/일시 중지/전송/예약
    \- 연락처 > 오디언스 > 읽기
    \- 연락처 > 목록 및 가입자 > 읽기, 쓰기
    \- 크로스 클라우드 플랫폼 > 마켓 오디언스 > 보기
    \- 크로스 클라우드 플랫폼 > 마켓 오디언스 회원 > 보기
    \- 교차 클라우드 플랫폼 > 마케팅 클라우드 연결 > 읽기
    \- 데이터 > 데이터 확장 > 읽기, 쓰기
    \- 데이터 > 파일 위치 > 읽기
    \- 데이터 > 이벤트 추적 > 읽기, 쓰기
    \- 이벤트 알림 > 콜백 > 읽기
    \- 이벤트 알림 > 구독 > 읽기

{% details Show image of recommended scopes %}

![Salesforce 마케팅 클라우드 앱 패키지의 권장 범위입니다.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Select **Save**.
11\. 다음 필드를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣습니다: **클라이언트 ID**, **클라이언트 비밀**, **인증 기본 URI**, **REST 기본 URI**, **SOAP 기본 URI**.