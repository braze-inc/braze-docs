---
nav_title: 오케스트레이션 설정하기
article_title: 오케스트레이션 설정하기
page_order: 2
description: "고객 참여 플랫폼으로 이동하여 개인화된 커뮤니케이션을 가능하게 하는 BrazeAI Decisioning Studio 연결 방법 알아보기."
toc_headers: h2
---

# 오케스트레이션 설정하기

> 개인화된 커뮤니케이션을 오케스트레이션하려면 BrazeAI Decisioning Studio™ Go를 고객 참여 플랫폼(CEP)에 연결해야 합니다. 이 문서에서는 지원되는 각 CEP에 대해 통합을 설정하는 방법을 설명합니다.

## 지원되는 CEP

디시전킹 스튜디오 고는 다음과 같은 고객 참여 플랫폼을 지원합니다:

| CEP | 통합 유형 | 주요 기능 |
|-----|-----------------|--------------|
| **Braze** | API로 시작된 캠페인 | 네이티브 통합, 실시간 트리거링 |
| **Salesforce 마케팅 클라우드** | API 이벤트가 포함된 여정 빌더 | SQL 쿼리 자동화, 데이터 확장 |
| **클라비요** | 측정기준 트리거가 있는 흐름 | 템플릿 기반, 트리거 분할 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

통합 설정을 시작하려면 아래에서 해당 CEP를 선택하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정하기

Decisioning Studio Go를 Braze와 통합하려면 API 키를 만들고, API 트리거 캠페인을 구성하고, 필요한 식별자를 Decisioning Studio Go 포털에 제공해야 합니다.

### 1단계: Create a REST API key

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
6\. API 키를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 2단계: 이메일 표시 이름 찾기

1. Braze 대시보드에서 **설정** > **이메일 환경설정으로** 이동합니다.
2. BrazeAI Decisioning Studio™ Go에 사용할 표시 이름을 찾습니다.
3. 보낸 사람 **표시 이름을** 복사하여 BrazeAI Decisioning Studio™ Go 포털에 **이메일 표시 이름으로** 붙여넣습니다.
4. 연결된 이메일 주소를 복사하여 지역 부분과 도메인을 결합한 **발신자 이메일 주소로** BrazeAI Decisioning Studio™ Go 포털에 붙여넣습니다.

### 3단계: Braze URL 및 앱 ID 찾기

**Braze URL을 찾으려면:**
1. Braze 대시보드로 이동합니다.
2. 브라우저 창에서 Braze URL은 `https://` 으로 시작하고 `braze.com` 으로 끝납니다. Braze URL의 예는 `https://dashboard-01.braze.com` 입니다.

**앱 ID(API 키)를 찾으려면:**

{% alert note %}
Braze는 활동을 워크스페이스의 특정 앱과 연결하는 등 추적 목적으로 사용할 수 있는 앱 ID(Braze 대시보드에서 API 키라고 함)를 제공합니다. 앱 ID를 사용하는 경우, BrazeAI Decisioning Studio™ Go는 각 실험자에게 앱 ID를 연결할 수 있도록 지원합니다.<br><br>앱 ID를 사용하지 않는 경우 입력 안내 문자로 임의의 문자열을 입력할 수 있습니다.
{% endalert %}

1. Braze 대시보드에서 **설정** > **앱 설정으로** 이동합니다.
2. 추적하려는 앱으로 이동합니다.
3. **API 키를** 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 4단계: API 트리거 캠페인 만들기

1. Braze 대시보드에서 **메시징** > 캠페인으로 이동합니다.
2. **캠페인 만들기를** 선택합니다.
3. 캠페인 유형은 **API 캠페인을** 선택합니다.
4. 캠페인 이름을 입력합니다. 예를 들어 "Decisioning Studio Go 이메일"이 있습니다.

!["Decisioning Studio Go 이메일"이라는 이름의 API 캠페인.]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. 메시징 채널의 경우 **이메일을** 선택합니다.

![API 캠페인에 사용할 메시징 채널을 선택하는 옵션입니다.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. **추가 옵션에서** **사용자가 캠페인을 다시 받을 수 있도록 허용** 확인란을 선택합니다.
7\. 다시 자격을 얻으려면 **1을** 입력하고 드롭다운에서 **시간을** 선택합니다.

![선택한 API 캠페인에 대한 자격이 다시 부여됩니다.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. **캠페인 저장을** 선택합니다.

### 5단계: 캠페인 및 메시지 ID 복사하기

1. API 캠페인에서 **캠페인 ID를** 복사합니다. 그런 다음 BrazeAI Decisioning Studio™ Go 포털로 이동하여 **캠페인 ID를** 붙여넣습니다.

![복사하여 붙여넣을 메시지 변형 ID 예시입니다.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. **메시지 변형 ID를** 복사합니다. 그런 다음 BrazeAI Decisioning Studio™ Go 포털로 이동하여 **메시지 변형 ID를** 붙여넣습니다.

### 6단계: 테스트 사용자 ID 찾기

통합을 테스트하려면 사용자 ID가 필요합니다:

1. Braze 대시보드에서 **오디언스** > **사용자 검색으로** 이동합니다.
2. 외부 사용자 ID, 사용자 별칭, 이메일, 전화번호 또는 푸시 토큰으로 사용자를 검색합니다.
3. 설정에서 참조할 사용자 ID를 복사합니다.

![ID로 사용자를 찾은 고객 프로필 예시.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정하기

Decisioning Studio Go를 Salesforce Marketing Cloud와 통합하려면 앱 패키지를 설정하고, 데이터 쿼리 자동화를 만들고, 트리거된 전송을 처리하는 여정을 구축해야 합니다.

### 1부: SFMC 앱 패키지 설정하기

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
9\. 앱 패키지에 대해서만 다음 권장 범위를 선택하세요:
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

### 2부: 데이터 쿼리 자동화 설정하기

#### 1단계: 새로운 자동화 만들기

1. Salesforce 마케팅 클라우드 홈에서 **여정 빌더로** 이동하여 **자동화 스튜디오를** 선택합니다.

![여정 빌더 탐색의 자동화 스튜디오 옵션.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. **새 자동화를** 선택합니다.
3\. **스케줄** 노드를 **시작 소스로** 드래그 앤 드롭합니다.

!["여정의 시작 소스로 '일정'을 선택합니다.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. **스케줄** 노드에서 **구성을** 선택합니다.
5\. 일정에 대해 다음을 설정합니다:
    - **시작 날짜:** 내일의 캘린더 날짜
    - **시간:** **12:00 AM**
    - **시간대:** **(GMT-05:00) 동부 표준시(미국 & 캐나다)**
6\. **반복에서** **매일을** 선택합니다.
7\. 이 일정을 종료하지 않도록 설정하세요.
8\. **완료를** 선택하여 일정을 저장합니다.

![2024년 1월 25일 오전 12시에 매일 반복되도록 정의된 일정의 예입니다.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### 2단계: SQL 쿼리 만들기

다음으로 가입자 쿼리와 참여 쿼리 등 2개의 SQL 쿼리를 만듭니다. 이러한 쿼리를 통해 BrazeAI Decisioning Studio™ Go는 데이터를 검색하여 오디언스를 채우고 참여 이벤트를 수집할 수 있습니다.

**가입한 가입자가 쿼리합니다:**

1. **SQL 쿼리를** 캔버스에 드래그 앤 드롭합니다.
2. **선택을** 선택합니다.
3. **새 쿼리 활동 만들기를** 선택합니다.
4. 쿼리에 이름과 외부 키를 입력합니다. BrazeAI Decisioning Studio™ Go 포털에 제공된 가입자 쿼리에 제안된 이름과 외부 키를 사용하는 것이 좋습니다.

![예: "OFE_Subscribers_query_Test5" 및 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. **다음**을 선택합니다.
6\. BrazeAI Decisioning Studio™ Go 포털에서 **가입자 쿼리 리소스** 아래에서 시스템 데이터 SQL 쿼리를 찾습니다.
7\. 쿼리를 복사하여 텍스트 상자에 붙여넣고 **다음을** 선택합니다.

![SQL 쿼리 섹션의 쿼리 예제입니다.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. BrazeAI Decisioning Studio™ Go 포털의 **리소스 사용** 섹션에서 타겟팅 데이터 확장의 외부 키를 찾습니다. 그런 다음 검색창에 붙여넣어 검색합니다.

![검색창에 붙여넣은 외부 키]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. 검색한 외부 키와 일치하는 데이터 확장자를 선택합니다. 타겟팅 데이터 확장자 이름은 상호 참조할 수 있도록 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 가입자 쿼리의 **데이터 확장자는** `BASE_AUDIENCE_DATA` 접미사로 끝나야 합니다.

![예제 외부 키와 일치하는 데이터 확장자 이름입니다.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. **덮어쓰기를** 선택한 후 **다음을** 선택합니다.

**참여 쿼리:**

1. **SQL 쿼리를** 캔버스에 드래그 앤 드롭합니다.

!["SQL 쿼리"가 여정의 활동으로 추가되었습니다.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. **선택을** 선택합니다.
3\. **새 쿼리 활동 만들기를** 선택합니다.
4\. 쿼리에 이름과 외부 키를 입력합니다. BrazeAI Decisioning Studio™ Go 포털에 제공된 참여 쿼리에 제안된 이름과 외부 키를 사용하는 것이 좋습니다.

![예: "OFE_Engagement_query" 및 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. **다음**을 선택합니다.
6\. BrazeAI Decisioning Studio™ Go 포털에서 **참여 쿼리 리소스** 아래에서 시스템 데이터 SQL 쿼리를 찾습니다.
7\. 쿼리를 복사하여 텍스트 상자에 붙여넣고 **다음을** 선택합니다.

![SQL 쿼리 섹션의 쿼리 예제입니다.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. BrazeAI Decisioning Studio™ Go 포털에서 지정된 참여 쿼리에 대한 타겟팅 데이터 확장을 찾아 선택합니다.

{% alert tip %}
타겟팅 데이터 확장자 이름은 상호 참조할 수 있도록 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 참여 쿼리에 대한 타겟팅 데이터 확장을 보고 있는지 확인하세요. 참여 쿼리의 **데이터 확장자는** ENGAGEMENT_DATA 접미사로 끝나야 합니다.
{% endalert %}

{: start="9"}
9\. **덮어쓰기를** 선택한 후 **다음을** 선택합니다.

![예제 외부 키와 일치하는 데이터 확장자 이름입니다.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### 3단계: 자동화 실행하기

1. 자동화에 이름을 지정하고 **저장을** 선택합니다.

![자동화 예시 "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. 그런 다음 **한 번 실행을** 선택하여 모든 것이 예상대로 작동하는지 확인합니다.
3\. 두 쿼리를 모두 선택하고 **실행을** 선택합니다.

![실행할 선택된 SQL 쿼리 활동 목록이 있는 자동화 "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. **지금 실행을** 선택합니다.

![선택한 SQL 쿼리 활동입니다.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

이제 자동화가 성공적으로 실행되고 있는지 확인할 수 있습니다. 자동화가 예상대로 실행되지 않는 경우 추가 지원이 필요한 경우 Braze 지원팀에 문의하세요.

### 3부: SFMC 여정 만들기

#### 1단계: 여정 설정

1. Salesforce 마케팅 클라우드에서 **여정 빌더** > **여정 빌더로** 이동합니다.
2. **새 여정 생성을** 선택합니다.
3. 여정 유형에 대해 **다단계 여정을** 선택한 다음 **생성을** 선택합니다.

![결정 분할 노드 및 여러 이메일 노드에 연결된 API 이벤트 입력 소스입니다.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### 2단계: 여정 구축

**항목 소스를 만듭니다:**

1. 엔트리 소스의 경우 **API 이벤트를** 여정 빌더로 드래그합니다.

![입력 소스로 "API 이벤트"를 선택합니다.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. **API 이벤트**에서 **이벤트 생성을** 선택합니다.

![API 이벤트의 '이벤트 만들기' 옵션을 클릭합니다.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. **데이터 확장자 선택을** 선택합니다. BrazeAI Decisioning Studio™ Go에서 권장 사항을 작성할 데이터 확장을 찾아 선택합니다.
4\. **요약을** 선택하여 변경 내용을 저장합니다.
5\. **완료를** 선택하여 API 이벤트를 저장합니다.

![API 이벤트 요약.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**결정 분할을 추가합니다:**

1. **API 입력 이벤트** 후 **결정 분할을** 드래그 앤 드롭합니다.
2. **결정 분할** 세부 정보에서 첫 번째 경로에 대해 **편집을** 선택합니다.

!["편집" 버튼으로 결정 분할 세부 정보를 수정합니다.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. 권장 사항 데이터 확장에서 전달된 템플릿 ID를 사용하도록 **결정 분할을** 업데이트합니다. **여정 데이터에서** 해당 필드를 찾습니다.

![결정 분할의 경로 1에 있는 여정 데이터 섹션입니다.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. 입력 이벤트를 선택하고 원하는 템플릿 ID 필드를 찾은 다음 작업 영역으로 드래그합니다.

![포함할 이메일 템플릿 ID입니다.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. 첫 번째 이메일 템플릿의 템플릿 ID를 입력한 다음 **완료를** 선택합니다.
6\. **요약을** 선택하여 이 경로를 저장합니다.
7\. 각 이메일 템플릿에 대한 경로를 추가한 다음 위의 4~6단계를 반복하여 템플릿 ID가 각 템플릿의 ID 값과 일치하도록 필터 기준을 설정합니다.
8\. **완료를** 선택하여 **결정 분할** 노드를 저장합니다.

![각 이메일 템플릿 ID에 대한 결정 분할의 두 가지 경로.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**각 결정 분할에 대해 이메일을 추가합니다:**

1. **이메일** 노드를 **결정 분할의** 각 경로로 드래그합니다.
2. **이메일을** 선택한 다음 각 경로에 들어갈 적절한 템플릿을 선택합니다(즉, ID 값이 있는 템플릿이 결정 분할의 로직과 일치해야 함).

![여정에 추가된 이메일 노드입니다.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### 3단계: 여정 활성화

여정을 설정한 후 활성화하고 다음 세부 정보를 BrazeAI Decisioning Studio™ Go 팀과 공유하세요:

* 여정 ID
* 여정 이름
* API 이벤트 정의 키
* 권장 사항 데이터 확장 외부 키

{% alert note %}
BrazeAI Decisioning Studio™ Go 포털은 가입자와 참여 데이터를 매일 한 번 내보내기 위해 프로비저닝한 SFMC 자동화를 보여줍니다. SFMC에서 이 자동화를 열면 일시 중지했다가 다시 라이브로 전환해야 합니다.
{% endalert %}

1. BrazeAI Decisioning Studio™ Go 포털에서 **여정 이름을** 복사합니다.
2. 다음으로 Salesforce 마케팅 클라우드 여정 빌더에서 여정 이름을 검색창에 붙여넣습니다.
3. 여정 이름을 선택합니다. 여정은 현재 초안 상태입니다.
4. **유효성 검사를** 선택합니다.

![완료된 여정을 활성화합니다.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. 그런 다음 유효성 검사 결과를 검토하고 **활성화를** 선택합니다.

![유효성 검사 규칙 섹션에 나열된 권장 사항입니다.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. **여정 활성화** 요약에서 **활성화를** 다시 선택합니다.

![여정을 위한 요약.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 전송 트리거를 시작할 수 있습니다.

{% endtab %}
{% tab Klaviyo %}

## 클라비요 통합 설정하기

Decisioning Studio Go와 Klaviyo를 통합하려면 API 키를 설정하고, 입력 안내 템플릿 플로우를 만들고, 트리거된 전송을 처리하는 플로우를 구축해야 합니다.

### 1부: 클라비요 API 키 설정하기

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

### 2부: 클라비요에서 입력 안내 템플릿 만들기

BrazeAI Decisioning Studio™ Go는 Klaviyo 계정의 기존 흐름과 연결된 템플릿을 가져옵니다. 어떤 플로우와도 연결되지 않은 템플릿을 사용하려면 사용하려는 템플릿이 포함된 입력 안내 플로우를 만들면 됩니다. 흐름은 초안으로 남겨둘 수 있으며 라이브 상태일 필요는 없습니다.

{% alert note %}
이 입력 안내자 흐름의 목적은 원하는 콘텐츠를 BrazeAI Decisioning Studio™ Go로 가져오기 위한 것입니다. 이후 단계에서 별도의 플로우를 생성해야 하며, 이 플로우는 실험자가 라이브 상태가 되면 활성화를 트리거하는 데 BrazeAI Decisioning Studio™ Go가 사용합니다.
{% endalert %}

**1단계: 흐름 설정**

1. 클라비요에서 **플로우를** 선택합니다.
2. **흐름 만들기** > **처음부터 만들기를** 선택합니다.
3. 입력 안내자 흐름에 알아볼 수 있는 이름을 지정한 다음 **흐름 만들기를** 선택합니다.

!["OFE 입력 안내서 플로우"라는 이름의 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. 트리거를 선택한 다음 플로우를 저장합니다.
5\. **확인을** 선택하고 **저장합니다**.

**2단계: 입력 안내 템플릿 만들기**

1. **트리거** 뒤에 **이메일** 노드를 드래그 앤 드롭합니다.

![트리거 노드와 이메일 노드가 있는 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. **이메일** 노드에서 **템플릿 선택을** 선택합니다.
3\. 그런 다음 사용할 템플릿을 선택하고 **템플릿 사용을** 선택합니다.
4\. **저장** > **완료를** 선택합니다.
5\. (선택 사항) BrazeAI Decisioning Studio™ Go에서 사용할 템플릿을 더 추가하려면 다른 **이메일** 노드를 추가하고 2~4단계를 반복합니다.
6\. 모든 이메일을 **초안** 모드로 두고 플로우를 종료합니다.

BrazeAI Decisioning Studio™ Go 포털의 입력 안내 흐름에서 템플릿을 선택할 수 있어야 합니다.

![의사 결정 스튜디오 Go 포털의 입력 안내 클라비요 템플릿의 예입니다.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

### 3부: 클라비요에서 플로우 만들기

{% alert important %}
설정하는 모든 새 실험자에 대해 클라비요에서 새 플로우를 만들어야 합니다. 이전에 템플릿을 가져오기 위해 입력 안내자 플로우를 만든 경우에는 새 플로우를 만들어야 하며 이전 입력 안내자 플로우는 재사용할 수 없습니다.
{% endalert %}

Klaviyo에서 플로우를 만들기 전에 참조할 수 있는 BrazeAI Decisioning Studio™ Go 포털의 다음 세부 정보가 있어야 합니다:

- 흐름 이름
- 트리거 이벤트 이름

#### 1단계: 흐름 설정

1. 클라비요에서 **플로우** > **플로우 만들기를** 선택합니다.
2. **나만의 구축하기를** 선택합니다.
3. **이름에** BrazeAI Decisioning Studio™ Go 포털의 흐름 이름을 입력합니다. 그런 다음 **수동 생성을** 선택합니다.

![예제 플로우에 대해 '수동으로 만들기' 옵션을 선택했습니다.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. 트리거를 선택합니다.
5\. 측정기준 이름을 BrazeAI Decisioning Studio™ Go 포털의 트리거 이벤트 이름과 일치시킵니다.

![트리거 이벤트 이름과 일치하는 측정기준 이름 예시 "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Select **Save**.

{% alert note %}
실험자에게 기본 템플릿이 하나만 있는 경우 2단계로 진행합니다. 실험자에게 기본 템플릿이 두 개 이상인 경우 [3단계로 건너뜁니다: 흐름에 트리거 분할 추가](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

#### 2단계: 흐름에 이메일 추가(단일 템플릿)

1. **트리거** 노드 뒤에 **이메일** 노드를 드래그 앤 드롭합니다.
2. **이메일 세부 정보에서** **템플릿 선택을** 선택합니다.

!['이메일 세부정보' 섹션에서 '템플릿 선택' 옵션을 선택합니다.]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. 기본 템플릿을 찾아 선택합니다. BrazeAI Decisioning Studio™ Go 포털의 **사용할 리소스** 섹션에서 템플릿 이름으로 템플릿을 검색할 수 있습니다.

![클라비요의 기본 템플릿 예시입니다.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. **템플릿 사용** > **저장을** 선택합니다.
5\. **제목란에** {% raw %}`{{event.SubjectLine}}`{% endraw %} 을 입력합니다.
6\. **발신자 이름과** **발신자 이메일 주소에** 사용하려는 세부 정보를 입력합니다.

!["이메일 1"의 제목란, 발신자 이름 및 발신자 이메일 주소 예시입니다.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. **완료를** 선택합니다.
8\. **최근에 이메일로 받은 프로필 건너뛰기** 확인란을 선택 취소한 다음 **저장을** 선택합니다.
9\. 이메일 노드에서 모드를 **임시** 보관에서 **실시간** 보관으로 업데이트합니다.

![이메일 노드에 연결된 트리거 노드를 보여주는 클라비요 플로우 에디터.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 활성화를 트리거할 수 있습니다.

#### 3단계: 흐름에 트리거 분할 추가(여러 템플릿)

1. **트리거 노드** 뒤에 트리거 **분할** 노드를 드래그 앤 드롭합니다.
2. **트리거 분할** 노드를 선택하고 **차원을** **EmailTemplateID로** 설정합니다.

![차원 이메일 템플릿ID로 구성된 트리거 분할을 공급하는 트리거 노드를 보여주는 클라비요 플로우 다이어그램.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

**이메일 템플릿을 추가합니다:**

1. BrazeAI Decisioning Studio™ Go 포털의 **리소스 사용** 섹션에서 첫 번째 템플릿의 **이메일 템플릿 ID를** 찾습니다. **차원** 필드에 **이메일 템플릿 ID를** 입력한 다음 **저장을** 선택합니다.
2. **이메일** 노드를 **트리거 분할의** **예** 분기로 드래그 앤 드롭합니다.

![이메일 노드로 연결되는 Yes 브랜치와 다른 트리거 분할에 연결되는 No 브랜치가 있는 트리거 분할 노드가 있는 클라비요 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. **이메일 세부 정보에서** **템플릿 선택을** 선택합니다.
4\. 기본 템플릿을 찾아 선택합니다. BrazeAI Decisioning Studio™ Go 포털의 **리소스 사용** 섹션에서 기본 템플릿 이름으로 템플릿을 검색할 수 있습니다.
5\. **템플릿 사용** > **저장을** 선택합니다.
6\. **제목란에** {% raw %}`{{event.SubjectLine}}`{% endraw %} 을 입력합니다.
7\. **발신자 이름과** **발신자 이메일 주소에** 사용하려는 세부 정보를 입력합니다.

![선택한 이메일 템플릿과 제목란, 발신자 이름, 발신자 이메일 주소에 대한 필드입니다.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. **완료를** 선택합니다.
9\. **최근에 이메일로 받은 프로필 건너뛰기** 확인란을 선택 취소한 다음 **저장을** 선택합니다.
10\. 이메일 노드에서 모드를 **임시** 보관에서 **실시간** 보관으로 업데이트합니다.

**각 추가 템플릿에 대해 새로운 트리거 분할을 추가합니다:**

1. 다른 **트리거 분할** 노드를 이전 **트리거 분할** 노드의 분기 **없음으로** 드래그 앤 드롭합니다.
2. **차원을** **이메일** **템플릿 ID로** 설정하고 설정 중인 기본 템플릿의 **이메일 템플릿 ID로** **차원** 값을 입력합니다.
3. Select **Save**.

![트리거 분할로 이어지는 트리거 노드를 보여주는 Klaviyo 흐름 편집기의 다이어그램. 트리거 분할에는 이메일 노드로 연결되는 예 분기와 추가 이메일 노드로 연결되는 다른 트리거 분할에 연결되는 아니요 분기가 있습니다.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. 새 트리거 분할의 **예** 브랜치에 **이메일** 노드를 드래그 앤 드롭합니다.
5\. 위의 이메일 템플릿 설정 단계를 반복하여 해당 템플릿을 선택합니다.
6\. **제목란을** {% raw %}`{{event.SubjectLine}}`{% endraw %} 으로 설정하고 **최근 이메일로 받은 프로필 건너뛰기** 확인란을 선택 취소합니다.
7\. 실험자가 사용 중인 각 기본 템플릿에 대해 **트리거 분할** 노드와 **이메일** 노드가 하나씩 생길 때까지 이 과정을 반복합니다. 마지막 트리거 분할은 "아니요" 브랜치에 아무것도 없어야 합니다.

![여러 이메일 노드로 분기되는 여러 트리거 분할 노드가 있는 클라비요 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="8"}
8\. 각 **이메일** 노드에서 모드를 **임시** 보관에서 **실시간** 보관으로 업데이트합니다.

![노드 상태를 '라이브'로 업데이트하는 옵션입니다.]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 활성화를 트리거할 수 있습니다.

{% endtab %}
{% endtabs %}

## 다음 단계

오케스트레이션을 설정했으니 이제 상담원 디자인을 진행하세요:

- [에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
