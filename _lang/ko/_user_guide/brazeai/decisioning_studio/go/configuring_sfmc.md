---
nav_title: Salesforce 마케팅 클라우드로 구성하기
article_title: Salesforce 마케팅 클라우드를 사용하여 구성하기 BrazeAI Decisioning Studio Go
page_order: 5
description: "Salesforce 마케팅 클라우드에서 데이터 쿼리 자동화 및 여정을 설정하여 BrazeAI Decisioning <sup>StudioTM</sup> Go와 함께 사용하는 방법을 알아보세요."
toc_headers: h2
---

# Salesforce 마케팅 클라우드로 구성하는 BrazeAI Decisioning Studio™ Go

> Salesforce 마케팅 클라우드(SFMC)에서 여정을 설정하여 BrazeAI Decisioning Studio™ Go를 통해 전송 트리거를 시작하세요.

## 데이터 쿼리 자동화 설정하기

### 1단계: 새로운 자동화 만들기

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

### 2단계: SQL 쿼리 만들기

다음으로 가입자 쿼리와 참여 쿼리라는 두 가지 SQL 쿼리를 만들어 보겠습니다. 이러한 쿼리를 통해 BrazeAI Decisioning Studio™ Go는 데이터를 검색하여 오디언스를 채우고 참여 이벤트를 수집할 수 있습니다.

{% tabs %}
{% tab Subscribers query %}
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
8\. BrazeAI Decisioning Studio™ Go 포털의 ' **사용할 리소스** ' 섹션에서 타겟팅 데이터 확장의 외부 키를 찾습니다. 그런 다음 검색창에 붙여넣어 검색합니다.

![검색창에 붙여넣은 외부 키]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. 검색한 외부 키와 일치하는 데이터 확장자를 선택합니다. 타겟팅 데이터 확장자 이름은 상호 참조할 수 있도록 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다. 가입자 쿼리의 **데이터 확장자는** `BASE_AUDIENCE_DATA` 접미사로 끝나야 합니다.

![예제 외부 키와 일치하는 데이터 확장자 이름입니다.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. **덮어쓰기를** 선택한 후 **다음을** 선택합니다.
{% endtab %}
{% tab Engagement query %}
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
타겟팅 데이터 확장자 이름은 상호 참조할 수 있도록 BrazeAI Decisioning Studio™ Go 포털에도 제공됩니다.  참여 쿼리에 대한 타겟팅 데이터 확장을 보고 있는지 확인하세요. 참여 쿼리의 **데이터 확장자는** ENGAGEMENT_DATA 접미사로 끝나야 합니다.
{% endalert %}

{: start="9"}
9\. **덮어쓰기를** 선택한 후 **다음을** 선택합니다.

![예제 외부 키와 일치하는 데이터 확장자 이름입니다.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### 3단계: 자동화 실행하기

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

## SFMC 여정 만들기

### 1단계: 여정 설정

1. Salesforce 마케팅 클라우드에서 **여정 빌더** > **여정 빌더로** 이동합니다.
2. **새 여정 생성을** 선택합니다.
3. 여정 유형에 대해 **다단계 여정을** 선택한 다음 **생성을** 선택합니다.

![결정 분할 노드 및 여러 이메일 노드에 연결된 API 이벤트 입력 소스입니다.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### 2단계: 여정 구축

#### 2.1 단계: 항목 소스 만들기

1. 엔트리 소스의 경우 **API 이벤트를** 여정 빌더로 드래그합니다.

![입력 소스로 "API 이벤트"를 선택합니다.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. **API 이벤트**에서 **이벤트 생성을** 선택합니다.

![API 이벤트의 '이벤트 만들기' 옵션을 클릭합니다.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. **데이터 확장자 선택을** 선택합니다. BrazeAI Decisioning Studio™ Go에서 권장 사항을 작성할 데이터 확장을 찾아 선택합니다.
4\. **요약을** 선택하여 변경 내용을 저장합니다.
5\. **완료를** 선택하여 API 이벤트를 저장합니다.

![API 이벤트 요약.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### 2.2 단계: 결정 분할 추가

1. **API 입력 이벤트** 후 **결정 분할을** 드래그 앤 드롭합니다. 
2. **결정 분할** 세부 정보에서 첫 번째 경로에 대해 **편집을** 선택합니다.

!['편집' 버튼으로 결정 분할 세부 정보를 수정합니다.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

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

#### 2.3 단계: 각 결정 분할에 이메일 추가하기

1. **이메일** 노드를 **결정 분할의** 각 경로로 드래그합니다.
2. **이메일을** 선택한 다음 각 경로에 들어갈 적절한 템플릿을 선택합니다(즉, ID 값이 있는 템플릿이 결정 분할의 로직과 일치해야 함).

![여정에 추가된 이메일 노드입니다.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### 3단계: 여정 활성화

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
