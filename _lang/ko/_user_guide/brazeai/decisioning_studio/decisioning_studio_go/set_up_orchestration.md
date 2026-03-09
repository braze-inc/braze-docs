---
nav_title: 오케스트레이션 설정
article_title: 오케스트레이션 설정
page_order: 2
description: "BrazeAI Decisioning Studio Go를 고객 참여 플랫폼에 연결하여 개인화된 커뮤니케이션을 인에이블먼트하는 방법을 알아보세요."
toc_headers: h2
---

# 오케스트레이션 설정

> BrazeAI Decisioning Studio™ Go는 개인화된 커뮤니케이션을 오케스트레이션하기 위해 고객 참여 플랫폼(CEP)에 연결해야 합니다. 이 문서는 지원되는 각 CEP에 대한 통합 설정 방법을 설명합니다.

## 지원되는 CEP

Decisioning Studio Go는 다음 고객 참여 플랫폼을 지원합니다:

| CEP | 통합 유형 | 주요 기능 |
|-----|-----------------|--------------|
| **Braze** | API로 시작된 캠페인 | 네이티브 통합, 실시간 트리거링 |
| **세일즈포스 마케팅 클라우드** | API 이벤트를 지원하는 여정 빌더 | SQL 쿼리 자동화, 데이터 확장 |
| **클라비요** | 메트릭 트리거가 있는 플로우 | 템플릿 기반 트리거 분할 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

아래에서 CEP를 선택하여 통합 설정을 시작하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정

Decisioning Studio Go를 Braze와 통합하려면 API 키를 생성하고, API 트리거 캠페인을 구성한 후, 필요한 식별자를 Decisioning Studio Go 포털에 제공해야 합니다.

### 1단계: Create a REST API key

1. Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동하세요.
2. **API 키 생성을** 선택합니다.
3. API 키의 이름을 입력하세요. 예를 들어 "DecisioningStudioGoEmail"이 있습니다.
4. 다음 범주에 따라 권한을 선택하십시오:
    - **사용자 데이터:** 선택`users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **메시지:** 선택 `messages.send`
    - **캠페인:** 나열된 모든 권한 선택
    - **캔버스:** 나열된 모든 권한 선택
    - **세그먼트:** 나열된 모든 권한 선택
    - **템플릿:** 나열된 모든 권한 선택

{: start="5"}
5\. **API 키 생성을** 선택합니다.
6\. API 키를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 2단계: 이메일 표시 이름을 찾으세요

1. Braze 대시보드에서 **설정** > **이메일 기본 설정**으로 이동하세요.
2. BrazeAI Decisioning Studio™ Go와 함께 사용할 표시 이름을 찾아주세요.
3. **'From Display Name**'을 복사하여 BrazeAI Decisioning Studio™ Go 포털의 **'이메일 Display Name**'으로 붙여넣으십시오.
4. 관련 이메일 주소를 로컬 부분과 도메인을 결합한 **발신 이메일 **주소로 BrazeAI Decisioning Studio™ Go 포털에 복사하여 붙여넣으십시오.

### 3단계: Braze URL과 앱 ID를 찾으세요

**Braze URL을 찾으려면:**
1. Braze 대시보드로 이동하세요.
2. 브라우저 창에서 Braze URL은  로 시작하고  `https://`로 끝납니다`braze.com`. Braze URL의 예시는 다음과 같습니다`https://dashboard-01.braze.com`.

**앱 ID(API 키)를 찾으려면:**

{% alert note %}
Braze는 추적 목적으로 사용할 수 있는 앱 ID(Braze 대시보드에서는 API 키로 지칭됨)를 제공합니다. 예를 들어, 작업 공간 내 특정 앱과 활동을 연결하는 데 활용할 수 있습니다. 앱 ID를 사용하는 경우, BrazeAI Decisioning Studio™ Go는 각 실험 담당자와 앱 ID를 연결하는 기능을 지원합니다.<br><br>앱 ID를 사용하지 않는 경우, 입력 안내로 임의의 문자열을 입력할 수 있습니다.
{% endalert %}

1. Braze 대시보드에서 **설정** > **앱 설정**으로 이동하세요.
2. 추적하려는 앱으로 이동하세요.
3. **API 키**를 복사하여 BrazeAI Decisioning Studio™ Go 포털에 붙여넣으세요.

### 4단계: API로 트리거되는 캠페인 생성

1. Braze 대시보드에서 **메시징** > **캠페인**으로 이동하세요.
2. **캠페인 생성을** 선택하세요.
3. 캠페인 유형으로 **API 캠페인을** 선택하십시오.
4. 캠페인 이름을 입력하세요. 예를 들어 "Decisioning Studio Go 이메일"이 있습니다.

!["Decisioning Studio Go 이메일"이라는 API 캠페인.]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. 메시징 채널로 **이메일을** 선택하십시오.

![API 캠페인용 메시징 채널 선택 옵션.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. **추가 옵션**에서 **'사용자가 캠페인 수신 자격을 다시 획득할 수 있도록 허용'** 확인란을 선택하십시오.
7\. 재자격 획득 시점을 설정하려면 **1을** 입력하고 드롭다운에서 **'시간'을** 선택하십시오.

![선택한 API 캠페인에 대한 재자격 부여]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. **캠페인 저장을** 선택하세요.

### 5단계: 캠페인 및 메시지 ID를 복사하세요

1. API 캠페인에서 **캠페인 ID**를 복사하세요. 그런 다음 BrazeAI Decisioning Studio™ Go 포털로 이동하여 **캠페인 ID**를 붙여넣으세요.

![복사하여 붙여넣을 예시 메시지 변형 ID.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. **메시지 변형 ID**를 복사하세요. 그런 다음 BrazeAI Decisioning Studio™ Go 포털로 이동하여 **메시지 변형 ID**를 붙여넣으십시오.

### Step 6: 테스트 사용자 ID를 찾으십시오

통합을 테스트하려면 사용자 ID가 필요합니다:

1. Braze 대시보드에서 **오디언스** > **사용자 검색**으로 이동하세요.
2. 사용자의 외부 ID, 사용자 별칭, 이메일, 전화번호 또는 푸시 토큰으로 검색하십시오.
3. 사용자 ID를 복사하여 설정 시 참조하십시오.

![ID로 사용자를 찾아낸 예시 고객 프로필.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정

Decisioning Studio Go를 Salesforce Marketing Cloud와 통합하려면 앱 패키지를 설정하고, 데이터 쿼리 자동화를 생성하며, 트리거된 발송을 처리하기 위한 여정을 구축해야 합니다.

### 1부: SFMC 앱 패키지 설정

1. 마케팅 클라우드 홈페이지로 이동하십시오.
2. 글로벌 헤더에서 메뉴를 열고 **설정을** 선택하세요.
3. 사이드 패널 탐색에서 **플랫폼 도구** 아래의 **앱으로** 이동한 후 **설치된 패키지를** 선택하세요.
4. **새로** 만들기를 선택하여 앱 패키지를 생성합니다.
5. 앱 패키지에 이름과 설명을 지정하세요.

!["실험자 1 - 테스트 5"라는 이름의 앱 패키지.]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. **구성 요소 추가를** 선택하십시오.
7\. **구성** **요소 **유형에서 **API 통합을** 선택하십시오. 그런 다음, **다음을** 선택하십시오.
8\. **통합 유형**에 대해 **서버 간을** 선택하십시오. 그런 다음, **다음을** 선택하십시오.
9\. 앱 패키지에 대해 다음 권장 범위를 선택하십시오:
    \- 채널 > 이메일 > 읽기, 쓰기, 보내기
    \- 채널 > OTT > 읽기
    \- 채널 > 푸시 > 읽기
    \- 채널 > SMS > 읽기
    \- 채널 > 소셜 > 읽기
    \- 채널 > 웹 > 읽기
    \- 자산 > 문서 및 이미지 > 읽기, 쓰기
    \- 자산 > 저장된 콘텐츠 > 읽기, 쓰기
    \- 자동화 > 자동화 > 읽기, 쓰기, 실행
    \- 자동화 > 여정 > 읽기, 쓰기, 실행, 활성화/중지/일시정지/전송/예약
    \- 연락처 > 오디언스 > 읽기
    \- 연락처 > 목록 및 가입자 > 읽기, 쓰기
    \- 크로스 클라우드 플랫폼 > 시장 오디언스 > 보기
    \- 크로스 클라우드 플랫폼 > 시장 오디언스 회원 > 보기
    \- 크로스 클라우드 플랫폼 > 마케팅 클라우드 커넥트 > 읽기
    \- 데이터 > 데이터 확장 > 읽기, 쓰기
    \- 데이터 > 파일 위치 > 읽기
    \- 데이터 > 이벤트 추적 > 읽기, 쓰기
    \- 이벤트 알림 > 콜백 > 읽기
    \- 이벤트 알림 > 구독 > 읽기

{% details Show image of recommended scopes %}

![Salesforce Marketing Cloud 앱 패키지에 권장되는 범위.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Select **Save**.
11\. 다음 필드를 BrazeAI Decisioning Studio™ Go 포털에 복사하여 붙여넣으십시오: **클라이언트 ID**, **클라이언트 시크릿**, **인증 기본 URI**, **REST 기본 URI**, **SOAP 기본 URI**.

### 2부: 데이터 쿼리 자동화 설정

#### 1단계: 새 자동화 생성

1. Salesforce Marketing Cloud 홈 화면에서 **여정 빌더**(**Journey Builder**)로 이동한 후 **자동화 스튜디오(Automation Studio)를** 선택하세요.

![자니 빌더 탐색 메뉴의 자동화 스튜디오 옵션]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. **새 자동화** 선택.
3\. **시작 **소스로 **스케줄** 노드를 드래그 앤 드롭하십시오.

!["일정"을 여정의 시작점으로 설정합니다.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. **스케줄** 노드에서 **구성을** 선택하십시오.
5\. 일정에 대해 다음을 설정하십시오:
    - **시작일:** 내일의 캘린더 날짜
    - **시간:** **자정**
    - **시간대:** **(GMT-05:00) 동부 (미국&캐나다)**
6\. **반복** 설정에서 **'매일'을** 선택하세요.
7\. 이 일정을 영원히 지속되도록 설정하세요.
8\. **완료를** 선택하여 일정을 저장하세요.

![2024년 1월 25일 오전 12시(미국 동부 시간)에 정의된 예시 일정으로, 매일 반복됩니다.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### 2단계: SQL 쿼리를 생성하세요

다음으로, 가입자 쿼리와 참여도 쿼리라는 두 개의 SQL 쿼리를 생성하십시오. 이러한 쿼리를 통해 BrazeAI Decisioning Studio™ Go는 오디언스를 구성하고 참여 이벤트를 수집하기 위한 데이터를 가져올 수 있습니다.

**가입자 문의:**

1. **SQL **쿼리를 캔버스로 드래그 앤 드롭하세요.
2. 선택**하세요**.
3. **새 쿼리 활동 생성을** 선택하십시오.
4. 쿼리에 이름과 외부 키를 지정하십시오. BrazeAI Decisioning Studio™ Go 포털에서 제공된 가입자 쿼리에 대해 제안된 이름과 외부 키를 사용하는 것을 권장합니다.

![예시와"OFE_Subscribers_query_Test5" 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. **다음**을 선택합니다.
6\. BrazeAI Decisioning Studio™ Go 포털에서 **'가입자 쿼리 리소스'** 아래에 있는 '시스템 데이터 SQL 쿼리'를 찾으십시오.
7\. 쿼리를 텍스트 상자에 복사하여 붙여넣고 **다음을** 선택하십시오.

![SQL 쿼리 섹션의 예시 쿼리.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. BrazeAI Decisioning Studio™ Go 포털의 **'사용할** **리소스'** 섹션에서 대상 데이터 익스텐션의 외부 키를 찾으십시오. 그런 다음 검색창에 붙여넣어 검색하세요.

![검색창에 붙여넣은 외부 키]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. 검색한 외부 키와 일치하는 데이터 확장을 선택하십시오. 대상 데이터 확장 이름은 교차 참조를 위해 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 가입자 쿼리의 **데이터 확장자는** `BASE_AUDIENCE_DATA`접미사로 끝나야 합니다.

![예시 외부 키와 일치하는 데이터 확장자 이름.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. **덮어쓰기를** 선택한 다음 **다음을** 선택하십시오.

**참여 쿼리:**

1. **SQL **쿼리를 캔버스로 드래그 앤 드롭하세요.

!["SQL 쿼리"가 여정에 활동으로 추가되었습니다.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. 선택**하세요**.
3\. **새 쿼리 활동 생성을** 선택하십시오.
4\. 쿼리에 이름과 외부 키를 지정하십시오. BrazeAI Decisioning Studio™ Go 포털에서 제공된 참여 쿼리에 대해 권장되는 이름과 외부 키를 사용하는 것을 권장합니다.

![예시와"OFE_Engagement_query" 외부 키.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. **다음**을 선택합니다.
6\. BrazeAI Decisioning Studio™ Go 포털에서 **'참여 쿼리 리소스'** 아래에 있는 '시스템 데이터 SQL 쿼리'를 찾으십시오.
7\. 쿼리를 텍스트 상자에 복사하여 붙여넣고 **다음을** 선택하십시오.

![SQL 쿼리 섹션의 예시 쿼리.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. BrazeAI Decisioning Studio™ Go 포털에서 지정된 참여 쿼리에 대한 대상 데이터 익스텐션을 찾아 선택하십시오.

{% alert tip %}
대상 데이터 확장 이름은 교차 참조를 위해 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 참여 쿼리의 대상 데이터 익스텐션을 확인하고 있는지 반드시 확인하십시오. 참여 쿼리의 **데이터 확장은** ENGAGEMENT_DATA접미사로 끝나야 합니다.
{% endalert %}

{: start="9"}
9\. **덮어쓰기를** 선택한 다음 **다음을** 선택하십시오.

![예시 외부 키와 일치하는 데이터 확장자 이름.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### 3단계: 자동화를 실행하세요

1. 자동화에 이름을 지정한 후 **저장을** 선택하세요.

![자동화 예시    "OFE_Experimenter_Test5_Automation".]({%image_buster/assets/img/decisioning_studio_go/query3.png%})

{: start="2"}
2\. 다음으로, **'한 번 실행'을** 선택하여 모든 것이 예상대로 작동하는지 확인하십시오.
3\. 두 쿼리를 모두 선택하고 **실행을** 선택하십시오.

![선택된 SQL 쿼리 작업 목록을 실행하는"OFE_Experimenter_Test5_Automation" 자동화.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. **지금 실행을** 선택하십시오.

![선택된 SQL 쿼리 활동.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

이제 자동화가 성공적으로 실행되고 있는지 확인할 수 있습니다. 자동화가 예상대로 실행되지 않는 경우 추가 지원을 위해 Braze 지원팀에 문의하십시오.

### 3부: SFMC 여정을 시작하세요

#### 1단계: 여정을 설정하세요

1. Salesforce Marketing Cloud에서 **여정 빌더** > **여정 빌더**로 이동하십시오.
2. **새 여정 만들기를** 선택하세요.
3. 여행 유형으로 **'다단계 여정'을** 선택한 후 **'생성'을** 선택하세요.

![결정 분할 노드와 여러 이메일 노드에 연결된 API 이벤트 입력 소스.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### 2단계: 여정을 구축하라

**항목 소스 생성:**

1. 입력 소스로 **API 이벤트를** 여정 빌더로 드래그하세요.

![입력 소스로 "API 이벤트"가 선택되었습니다.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. **API **이벤트에서 **이벤트 생성을** 선택하십시오.

![API 이벤트의 "이벤트 생성" 옵션.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. **데이터 확장 선택** BrazeAI Decisioning Studio™ Go가 추천을 작성할 데이터 익스텐션을 찾아 선택하십시오.
4\. 변경 사항을 저장하려면 **'요약'을** 선택하세요.
5\. **완료를** 선택하여 API 이벤트를 저장하십시오.

![API 이벤트 요약.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**결정 분할 추가:**

1. **API 진입 이벤트** 뒤에 **결정 분할(Decision Split)**을 드래그 앤 드롭하세요.
2. **결정 분할** 세부 정보에서 첫 번째 경로에 대해 **편집을** 선택하십시오.

!["편집" 버튼을 사용하여 결정 분할 세부 정보를 확인하세요.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. 추천 데이터 확장에서 전달된 템플릿 ID를 사용하도록 **결정 분할을** 업데이트하십시오. **여정 데이터** 아래에서 적절한 필드를 찾으십시오.

![결정 분할의 경로 1에 있는 여정 데이터 섹션.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. 입력 이벤트를 선택하고 원하는 템플릿 ID 필드를 찾은 후 작업 영역으로 드래그하세요.

![포함할 이메일 템플릿 ID.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. 첫 번째 이메일 템플릿의 템플릿 ID를 입력한 후 **완료를** 선택하세요.
6\. **요약을** 선택하여 이 경로를 저장하십시오.
7\. 각 이메일 템플릿에 대한 경로를 추가한 후, 위의 4~6단계를 반복하여 필터 기준을 설정하세요. 이렇게 하면 템플릿 ID가 각 템플릿의 ID 값과 일치하게 됩니다.
8\. **완료를** 선택하여 **결정 분할** 노드를 저장하십시오.

![각 이메일 템플릿 ID에 대한 결정 분할의 두 가지 경로.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**각 결정 분할마다 이메일을 추가하세요:**

1. **이메일** 노드를 **결정 **분할의 각 경로로 드래그하세요.
2. **이메일을** 선택한 후, 각 경로에 적용될 적절한 템플릿을 선택하십시오(즉, ID 값이 있는 템플릿이 결정 분할(Decision Split)의 논리와 일치해야 함).

![여정에 이메일 노드가 추가되었습니다.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### 3단계: 여정을 시작하세요

여정을 설정한 후 활성화하고 다음 세부 정보를 BrazeAI Decisioning Studio™ Go 팀과 공유하십시오:

* 여정 ID
* 여정 이름
* API 이벤트 정의 키
* 추천 데이터 확장 외부 키

{% alert note %}
BrazeAI Decisioning Studio™ Go 포털은 가입자 및 참여 데이터를 하루에 한 번 내보내기 위해 프로비저닝한 SFMC 자동화 작업을 보여줍니다. 이 자동화를 SFMC에서 열 경우, 일시 중지를 해제하고 다시 활성 상태로 전환해야 합니다.
{% endalert %}

1. BrazeAI Decisioning Studio™ Go 포털에서 **여정 **이름을 복사하십시오.
2. 다음으로 Salesforce Marketing Cloud Journey 빌더에서 검색창에 여정 이름을 붙여넣으세요.
3. 여정 이름을 선택하세요. 참고: 여정은 현재 초안 상태입니다.
4. **검증을** 선택하십시오.

![활성화할 완료된 여정.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. 그런 다음 검증 결과를 검토하고 **활성화를** 선택하십시오.

![검증 규칙 섹션에 나열된 권장 사항.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. **활성화 여정** 요약에서 다시 **'활성화'를** 선택하세요.

![여정을 위한 요약.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 전송을 트리거하기 시작할 수 있습니다.

{% endtab %}
{% tab Klaviyo %}

## Klaviyo 통합 설정

Decisioning Studio Go를 Klaviyo와 통합하려면 API 키를 설정하고, 입력 안내 템플릿 플로우를 생성한 후, 트리거된 발송을 처리할 플로우를 구축해야 합니다.

### 1부: Klaviyo API 키 설정

1. Klaviyo에서 **설정** > **API 키**로 이동하세요.
2. **개인 API 키 생성을** 선택하십시오.
3. Enter a name for the API key. 예를 들어 "결정 스튜디오 실험자들"이 있습니다.
4. API 키에 대해 다음 권한을 선택하십시오:
    - Campaigns: 읽기 권한
    - 데이터 프라이버시: 전체 액세스
    - 이벤트: 전체 액세스
    - 흐름: 전체 액세스
    - 이미지: 읽기 권한
    - 목록: 전체 액세스
    - 측정기준: 전체 액세스
    - 프로필: 전체 액세스
    - 세그먼트: 읽기 권한
    - 템플릿: 전체 액세스
    - 웹훅: 읽기 권한

![선택된 권한이 부여된 Klaviyo API 키.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Select **Create**.
6\. 이 API 키를 복사하여 BrazeAI Decisioning Studio™ Go 포털에서 요청되는 위치에 붙여넣으십시오.

### 2부: Klaviyo에서 입력 안내 템플릿 생성하기

BrazeAI Decisioning Studio™ Go는 Klaviyo 계정의 기존 플로우와 연결된 템플릿을 가져옵니다. 어떤 플로우에도 연결되지 않은 템플릿을 사용하려면, 사용하려는 템플릿을 포함하는 입력 안내 플로우를 생성할 수 있습니다. 흐름은 초안 상태로 남겨둘 수 있습니다; 반드시 실행될 필요는 없습니다.

{% alert note %}
이 입력 안내 흐름의 목적은 원하는 콘텐츠를 BrazeAI Decisioning Studio™ Go로 가져오는 것입니다. 추후 단계에서 별도의 플로우를 생성해야 합니다. 이는 실험자가 실행되면 BrazeAI Decisioning Studio™ Go가 활성화를 트리거하는 데 사용됩니다.
{% endalert %}

**1단계: 플로우 설정하기**

1. Klaviyo에서 **'플로우'를** 선택하세요.
2. **흐름 생성** > **새로 만들기** 선택.
3. 입력 안내에 알아볼 수 있는 이름을 지정한 후, **'플로우 생성'을** 선택하세요.

!["OFE 입력 안내 흐름"이라는 이름의 흐름.]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. 트리거를 선택한 후 플로우를 저장하세요.
5\. **확인하고 저장하기를** 선택하세요.

**2단계: 입력 안내 템플릿 생성**

1. **트리거** 뒤에 **이메일** 노드를 드래그 앤 드롭하세요.

![트리거 노드에 이어 이메일 노드가 있는 플로우.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. **이메일** 노드에서 **템플릿 선택을** 선택하십시오.
3\. 그런 다음 사용할 템플릿을 선택하고 **'템플릿 사용'을** 선택하세요.
4\. **저장** > **완료를** 선택하십시오.
5\. (선택 사항) BrazeAI Decisioning Studio™ Go에서 사용할 템플릿을 추가하려면, 다른 **이메일** 노드를 추가하고 2~4단계를 반복하십시오.
6\. 모든 이메일을 **초안** 상태로 남겨두고 플로우를 종료하십시오.

BrazeAI Decisioning Studio™ Go 포털에서, 귀하의 템플릿은 입력 안내 플로우 아래에서 선택 가능해야 합니다.

![Decisioning Studio Go 포털 내 클라비요(Klaviyo) 템플릿의 입력 안내 예시.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

### 3부: Klaviyo에서 플로우 생성하기

{% alert important %}
설정한 각 새로운 실험자마다 Klaviyo에서 새로운 플로우를 생성해야 합니다. 템플릿을 가져오기 위해 이전에 입력 안내 흐름을 생성한 경우, 새 흐름을 생성해야 하며 이전 입력 안내 흐름을 재사용할 수 없습니다.
{% endalert %}

Klaviyo에서 플로우를 생성하기 전에, 참조할 BrazeAI Decisioning Studio™ Go 포털의 다음 세부 정보를 반드시 준비해야 합니다:

- 흐름 이름
- 트리거 이벤트 이름

#### 1단계: 흐름 설정

1. Klaviyo에서 **플로우** > **플로우 생성을** 선택하세요.
2. **직접 구축** 선택
3. **이름**에는 BrazeAI Decisioning Studio™ Go 포털에서 사용 중인 플로우 이름을 입력하십시오. 그런 다음 **수동으로 만들기를** 선택하십시오.

![예시 흐름에 대해 선택된 "수동으로 생성" 옵션.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. 트리거를 선택하십시오.
5\. BrazeAI Decisioning Studio™ Go 포털에서 측정기준 이름을 트리거 이벤트 이름과 매칭하십시오.

![트리거 이벤트 이름과 일치하는 예시 "OFE_TEST_CASE_API_EVENT_TRIGGER".]({%image_buster/assets/img/decisioning_studio_go/flow2.png측정기준 이름    %})

{: start="6"}
6\. Select **Save**.

{% alert note %}
실험자가 하나의 기본 템플릿을 가지고 있다면, 2단계로 진행하십시오. 실험자가 두 개 이상의 기본 템플릿을 가지고 있다면, [3단계로 건너뛰세요: 플로우에 트리거 분할을](#step-3-add-a-trigger-split-to-your-flow) 추가하세요.
{% endalert %}

#### 2단계: 플로우에 이메일 추가하기 (단일 템플릿)

1. **트리거** 노드 뒤에 **이메일** 노드를 드래그 앤 드롭하세요.
2. **이메일 세부** 정보에서 **템플릿 선택을** 선택하십시오.

!["이메일 세부정보" 섹션의 "템플릿 선택" 옵션.]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. 기본 템플릿을 찾아 선택하세요. BrazeAI Decisioning Studio™ Go 포털의 **'사용할** **리소스**' 섹션에서 템플릿 이름으로 템플릿을 검색할 수 있습니다.

![Klaviyo의 예시 기본 템플릿.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. **사용할 템플릿** 선택 > **저장**
5\. **제목란**에는 을 입력하십시오{% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. **발신자 이름**과 **발신자 이메일 주소**에는 사용하고자 하는 세부 정보를 입력하십시오.

!["이메일 1"의 예시 제목란, 발신자 이름 및 발신자 이메일 주소]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. **완료** 선택.
8\. **최근에 이메일로 보낸 프로필 건너뛰기** 확인란의 선택을 해제한 다음 **저장을** 선택하십시오.
9\. 이메일 노드에서 모드를 '초안'에서 '실행'으로 업데이트하십시오.

![클라비요 플로우 에디터에서 이메일 노드에 연결된 트리거 노드를 보여주는 화면.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 활성화 트리거를 실행할 수 있습니다.

#### 3단계: 플로우에 트리거 분할 추가하기 (여러 템플릿)

1. **트리거 노드** 뒤에 **트리거 분할** 노드를 드래그 앤 드롭하십시오.
2. **트리거 분할** 노드를 선택하고 **차원을** **EmailTemplateID**로 설정합니다.

![Klaviyo 플로우 다이어그램으로, 트리거 노드가 '차원 EmailTemplateID'로 구성된 트리거 분할 노드에 데이터를 공급하는 모습을 보여줍니다.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

**이메일 템플릿을 추가하세요:**

1. BrazeAI Decisioning Studio™ Go 포털에서 **'사용할 리소스**' 섹션 아래에 있는 첫 번째 템플릿의 **이메일 템플릿 ID**를 찾으십시오. **차원** 필드에 **이메일 템플릿 ID**를 입력한 후 **저장을** 선택하십시오.
2. **이메일** 노드를 **트리거 **분기의 예(**Yes**) 분기로 드래그 앤 드롭하세요.

![트리거 분기 노드가 포함된 Klaviyo 플로우로, 예스 분기는 이메일 노드로 연결되고 노스 분기는 다른 트리거 분기에 연결됩니다.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. **이메일 세부** 정보에서 **템플릿 선택을** 선택하십시오.
4\. 기본 템플릿을 찾아 선택하세요. BrazeAI Decisioning Studio™ Go 포털의 **'사용할** **리소스**' 섹션에서 기본 템플릿 이름으로 템플릿을 검색할 수 있습니다.
5\. **사용할 템플릿** 선택 > **저장**
6\. **제목란**에는 을 입력하십시오{% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. **발신자 이름**과 **발신자 이메일 주소**에는 사용하고자 하는 세부 정보를 입력하십시오.

![선택된 이메일 템플릿과 제목란, 발신자 이름, 발신자 이메일 주소를 위한 필드.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. **완료** 선택.
9\. **최근에 이메일로 보낸 프로필 건너뛰기** 확인란의 선택을 해제한 다음 **저장을** 선택하십시오.
10\. 이메일 노드에서 모드를 '초안'에서 '실행'으로 업데이트하십시오.

**추가 템플릿마다 새로운 트리거 분할을 추가하십시오:**

1. 이전 **트리거 분할** 노드의 **'아니오'** 분기에 다른 **트리거 분할** 노드를 드래그 앤 드롭하세요.
2. 차원을 **EmailTemplateID**로 설정하고, **차원** 값에 설정 중인 기본 템플릿의 **이메일 템플릿 ID**를 입력하십시오.
3. Select **Save**.

![클라비요 플로우 편집기의 다이어그램으로, 트리거 노드가 트리거 분기로 이어지는 모습을 보여줍니다. 트리거 분기에는 '예' 분기가 이메일 노드로 연결되고, '아니오' 분기는 다른 트리거 분기로 연결되어 추가 이메일 노드로 이어집니다.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. 새 트리거 분기의 **'예'** 분기에 **이메일** 노드를 드래그 앤 드롭하세요.
5\. 위의 이메일 템플릿 설정 단계를 반복하여 해당 템플릿을 선택하십시오.
6\. **제목**란을 로 {% raw %}`{{event.SubjectLine}}`{% endraw %}설정하고, **최근에 이메일을 보낸 프로필 건너뛰기** 확인란의 선택을 해제하세요.
7\. 실험자가 사용하는 각 기본 템플릿에 대해 하나의 **트리거 분할** 노드와 하나의 **이메일** 노드가 생성될 때까지 이 과정을 반복하십시오. 마지막 트리거 분할의 "아니오" 분기에는 아무것도 포함되어서는 안 됩니다.

![여러 이메일 노드로 분기되는 여러 트리거 분기 노드가 포함된 Klaviyo 플로우]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="8"}
8\. 각 **이메일** 노드에서 모드를 '초안'에서 **'실행**'으로 업데이트하십시오.

![노드 상태를 "실시간"으로 업데이트하는 옵션.]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 활성화 트리거를 실행할 수 있습니다.

{% endtab %}
{% endtabs %}

## 다음 단계

오케스트레이션을 설정했으니, 이제 에이전트 설계를 진행하십시오:

- [에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
