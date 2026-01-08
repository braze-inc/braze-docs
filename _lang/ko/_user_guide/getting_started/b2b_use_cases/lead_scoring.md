---
nav_title: 리드 득점
article_title: 리드 스코어링 워크플로 만들기
page_order: 1
page_type: reference
description: "Braze를 사용하여 간단한 리드 스코어링, 외부 리드 스코어링 및 리드 핸드오프를 수행하는 방법을 알아보세요."
---

# 리드 스코어링 워크플로 만들기

> 이 사용 사례는 Braze를 사용하여 사용자 리드 점수를 실시간으로 업데이트하고 자동으로 영업 팀에 리드를 전달하는 방법을 보여줍니다.

Braze에서 리드 스코어링 워크플로우를 만드는 데는 두 가지 핵심 단계가 있습니다:

1. Braze에서 리드 채점 캔버스를 만들거나 외부 리드 채점 도구를 통합하세요:
- [간단한 리드 득점](#simple-lead-scoring)
- [외부 리드 득점](#external-lead-scoring)

2. 웹훅 캠페인을 만들어 자격을 갖춘 리드를 영업팀으로 전송하세요:
- [리드 핸드오프: 세일즈에 대한 MQL(검증된 리드) 마케팅](#lead-handoff)

## 간단한 리드 득점

### 1단계: 캔버스 만들기

1. **메시징** > **캔버스로** 이동하여 캔버스 **만들기를** 선택한 다음 캔버스 기본 사항을 입력합니다.

2. 캔버스에 '리드 스코어링 캔버스'와 같은 관련성 있는 이름을 지정하고, 더 쉽게 찾을 수 있도록 '리드 관리'와 같은 태그를 붙이세요.<br><br>"리드 스코어링 캔버스"라는 이름의 캔버스를 만들고 "리드 관리"라는 태그를 붙이는 1단계.]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### 2단계: 참가 기준 설정

1. **입력 일정** 단계로 진행하여 **작업 기반** 입력 일정을 선택합니다. 이렇게 하면 사용자가 특정 작업을 수행할 때 캔버스에 입력됩니다.

2. **작업 기반 옵션에서** 다음 두 가지 작업을 추가합니다:
    - 리드 스코어링 속성의 이름(예: `lead score`)으로 **커스텀 속성 값을 변경합니다**. 아직 리드 스코어링 속성을 만들지 않았다면 [커스텀 속성의]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) 단계를 따르세요. 이렇게 하면 리드 점수가 변경될 때마다 사용자가 캔버스에 입력됩니다.
    - **이메일 주소 추가**

'액션 기반'의 입력 일정과 커스텀 속성 '리드 점수'를 변경하고 이메일 주소를 추가하는 액션 기반 옵션으로 캔버스를 생성하는 2단계입니다.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### 3단계: 타겟 오디언스 식별하기

#### 3a단계: 세그먼트 선택

모든 사용자가 리드 스코어링을 받을 수 있으므로 타겟팅할 사용자 [세그먼트를]({{site.baseurl}}/user_guide/engagement_tools/segments/) 선택하고 추가 [필터를]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) 적용하여 스코어링 대상에 대한 회사별 규칙을 추가할 수 있습니다. 예를 들어 직원, 이미 고객인 사용자 등을 제외할 수 있습니다. 

\![세그먼트 및 필터 선택 옵션이 있는 캔버스 만들기 3단계로, 참가 대상을 세분화할 수 있습니다.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### 3b단계: 캔버스 재사용 자격 설정하기

사용자는 회원님의 라이프사이클 동안 이 캔버스를 여러 번 통과하게 되므로 이전에 나갔던 것처럼 빠르게 다시 들어올 수 있도록 해야 합니다. 이는 자격 재설정 설정을 통해 수행할 수 있습니다. 

**항목 컨트롤에서** 다음을 수행합니다:
- **사용자가 이 캔버스에 다시 입력하도록 허용을** 선택합니다.
- **지정된 창을** 선택합니다.
- 재적격 기간을 "0" **초로** 설정합니다.

0초의 "지정된 창"에서 "사용자가 이 캔버스에 다시 들어갈 수 있도록 허용"에 대한 선택 항목이 있는 "항목 제어" 섹션을 선택합니다.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### 3c단계: 보내기 설정 업데이트

이 캔버스의 운영 특성과 이러한 사용자에게 메시징이 전송되지 않는다는 사실을 고려할 때 구독 상태를 고수할 필요가 없습니다.

**구독 설정에서** **다음 사용자에게 보내기:** **탈퇴한 사용자를 포함한 모든 사용자를** 선택합니다. 

\![메시지 전송 옵션 설정을 위한 캔버스 만들기 4단계.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### 4단계: 캔버스 구축하기

#### 4a단계: 행동 경로 추가하기

배리언트 아래에서 더하기 아이콘을 선택한 다음 **행동 경로를** 선택합니다.

더하기 아이콘으로 열린 메뉴에 '행동 경로'가 표시된 캔버스.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### 4b단계: 액션 그룹 만들기

각 액션 그룹은 동일한 포인트 증가 또는 감소로 이어지는 모든 액션을 담당하게 됩니다. 액션 그룹은 최대 8개까지 설정할 수 있습니다. 이 시나리오에서는 4개의 그룹을 설정합니다.

행동 경로에 다음 그룹을 추가합니다:

- **그룹 1:** 1점 단위로 계산되는 모든 이벤트.
- **그룹 2:** 5점 단위로 계산되는 모든 이벤트.
- **그룹 3:** 1점 감소에 포함되는 모든 이벤트.
- **그 외 모든 사람:** 행동 경로를 사용하면 사용자가 '다른 모든 사람' 그룹으로 드롭하기 전에 사용자가 어떤 행동을 취하는지 기다릴 기간을 정의할 수 있습니다. 리드 점수의 경우, '비활동'에 대한 점수를 낮출 수 있는 기회입니다.

1점, 5점, 10점을 더하는 행동 그룹, 1점, 10점을 빼는 행동 그룹, '그 외 모든 사람'을 포함하는 행동 경로입니다.]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### 4c단계: 관련 이벤트를 포함하도록 각 그룹을 구성하세요.

각 액션 그룹에서 **트리거 선택을** 선택하고 해당 특정 액션 그룹의 점수를 더할 이벤트를 선택합니다. 리드 점수를 1씩 증가시키는 모든 이벤트를 포함하도록 트리거를 더 추가하세요. 예를 들어, 사용자가 앱에서 세션을 시작하거나 웨비나 등록 또는 참여와 같은 커스텀 이벤트를 수행할 때 점수를 1점씩 높일 수 있습니다. 

"모든 앱에서 세션 시작" 및 "커스텀 이벤트 수행"의 트리거가 있는 포인트를 추가하기 위한 액션 그룹입니다.]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### 4d 단계: 사용자 업데이트 단계 추가

행동 경로 아래에 생성된 각 캔버스 경로에 사용자 업데이트 단계를 추가합니다. 

각 작업 그룹에 대한 분기된 사용자 업데이트 경로가 있는 작업 경로를 표시하는 캔버스.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
각 사용자 업데이트 단계의 **작성** 탭에서 각 필드에 대해 다음을 수행합니다:

| 필드 | 액션 |
| --- | --- |
| **속성 이름** | 2단계에서 선택한 리드 점수 속성을 선택합니다(`lead score`).|
| **액션** | 경로가 점수를 증가시키는 경우 동작을 **증분으로**, 경로가 점수를 감소시키는 경우 **감소 기준으로** 변경합니다. |
| **증가** 또는 **감소 기준** | 리드 점수에서 증가 또는 감소할 점수를 입력합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 5단계: 캔버스 시작하기

그거예요! 리드 스코어링 캔버스를 시작할 준비가 되었습니다.

## 외부 리드 득점

[기술 파트너]({{site.baseurl}}/partners/home/), 자체적인 내부 리드 스코어링 모델, 머신 러닝, 기타 리드 스코어링 도구 등 다양한 옵션을 제공합니다.

### 외부 파트너

리드 스코어링 기능을 제공하는 B2B 파트너에 대해 알아보려면 [기술 파트너를]({{site.baseurl}}/partners/home) 확인하세요. 원하는 도구가 보이지 않나요? 통합은 저희의 [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) API 엔드포인트를 호출하여 통합할 수 있습니다. 

### 내부 리드 스코어링 데이터 모델

다양한 방법으로 리드 스코어링 모델을 포함한 내부 데이터 모델과 Braze를 통합할 수 있습니다. 아래에서 고객이 Braze와 통합한 몇 가지 일반적인 사례를 살펴보세요.

#### 통합 클라우드 데이터 웨어하우스

{% tabs %}
{% tab Braze as a data source %}

마케팅 도구인 Braze에는 팀의 내부 리드 점수 모델을 보완할 수 있는 매우 관련성 높은 데이터가 포함되어 있습니다. 

예를 들어, 메시징 참여 데이터(이메일 열기 및 클릭, 랜딩 페이지 참여 등)를 통해 리드의 참여 수준을 파악할 수 있습니다. 이 데이터를 클라우드 데이터 웨어하우스로 다시 전달하고 Braze 스트리밍 데이터 내보내기 솔루션을 사용하여 리드 스코어링 모델의 입력으로 사용할 수 있습니다:

- [Braze 커런츠]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Snowflake 보안 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze as a destination %}

내부 팀에서 리드 스코어링 모델을 생성하고 실행한 후에는 해당 데이터를 다시 Braze로 가져와서 리드를 더 잘 세분화하고 관련 메시징을 타겟팅할 수 있습니다. [Braze Cloud 데이터 수집으로]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) 이를 수행할 수 있습니다. 

클라우드 데이터 수집을 사용하면 내부 팀에서 사용자 식별자, 최신 리드 점수, 점수가 업데이트된 타임스탬프가 포함된 새 테이블 또는 보기를 만들 수 있습니다. Braze는 테이블 또는 뷰를 선택하여 고객 프로필에 리드 점수를 추가합니다.

{% endtab %}
{% endtabs %}

## 리드 핸드오프: 세일즈에 대한 MQL(검증된 리드) 마케팅 {#lead-handoff}

리드 핸드오프에 대한 권장 접근 방식은 각 사용자에 해당하는 리드 또는 연락처를 Braze에 첨부하는 것입니다. 이러한 리드는 리드 상태가 MQL 단계로 변경되면 영업 팀의 대기줄에 들어가게 되며, 이 시점에서 Salesforce는 리드 라우팅 또는 할당 워크플로우를 시작합니다. 

Salesforce의 리드 레코드를 Braze의 리드 상태로 업데이트하려면 트리거된 웹훅 템플릿을 사용하는 것이 좋습니다.

### 1단계: 웹훅 캠페인 만들기

### 2단계: 웹훅 구성하기

#### 2a단계: 웹훅 작성하기

1. 웹훅 캠페인의 이름을 "Salesforce > 리드를 MQL로 업데이트"와 같이 지정합니다.

2. {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} 형식의 웹훅 URL을 입력합니다. Braze 사용자 ID( {% raw %}`{{$user_id}}}`{% endraw %} )는 Salesforce 연락처 ID와 일치해야 합니다. 그렇지 않은 경우 {% raw %}`{{$user_id}}}`{% endraw %} 대신 별칭을 사용하세요.

3. **HTTP 메서드를** **PATCH로** 업데이트합니다.

4. 해당 리드의 리드 점수가 미리 정의된 임계값을 초과하는 경우에만 Salesforce에서 리드 레코드를 업데이트하도록 페이로드를 구성하세요. 리드 점수가 100점 이상인 경우 아래 요청 본문 예시를 참조하세요.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5\. 다음 헤더를 포함하세요:

| 헤더 | 콘텐츠 |
| --- | --- |
| 권한 부여 | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>토큰을 검색하려면 OAuth 2.0 클라이언트 자격 증명 흐름에 대해 [연결된 앱을 구성한](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) 다음 연결된 콘텐츠를 사용하여 Salesforce에서 무기명을 검색합니다: <br><br>{% raw %}<code>{% connected_content https://[인스턴스].my.salesforce.com/services/oauth2/token <br>메서드 포스트 <br> body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:결과 저장 %}{% endraw %} <br> 무기명 {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

웹훅은 Salesforce 웹훅 URL, PATCH HTTP 메서드, 원시 텍스트 요청 본문 및 요청 헤더로 구성됩니다.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### 2b단계: 웹훅 전송 예약하기

캠페인은 사용자의 리드 점수가 변경될 때마다 트리거되어야 합니다. 이 캠페인은 점수가 변경되는 모든 사용자에 대해 트리거되지만, 현재 MQL이 아니며 이전 단계에서 설정한 임계값을 넘은 사용자에게만 영향을 미칩니다.

**전달 예약** 단계에서 다음을 선택합니다:
- **실행 기반** 전달 유형
- 리드 스코어링 속성의 이름과 **새 값의** 액션이 포함된 **커스텀 속성 값 변경의** 트리거 동작입니다.

#### 2c단계: 타겟 오디언스 식별하기

**타겟 오디언스** 단계에서 리드 상태가 이미 MQL 이상인 사용자를 제외하는 필터(예: "`lead_status` `is none of` `MQL`")를 포함하세요.

!!! 필터가 “lead_status” 인 웹훅 타겟팅 옵션은 "MQL"이 아닙니다.]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### 3단계: 캠페인 시작

**실행을** 선택하고 고객이 MQL 리드 점수 임계값을 넘으면 Salesforce에서 리드 상태가 변경되는 것을 확인합니다.

