---
nav_title: 리드 스코어링
article_title: 리드 스코어링 워크플로우 생성
page_order: 1
page_type: reference
description: "Braze를 사용하여 간단한 리드 스코어링, 외부 리드 스코어링 및 리드 핸드오프를 수행하는 방법을 알아보세요."
---

# 리드 스코어링 워크플로우 생성

> 이 사용 사례는 Braze를 사용하여 실시간으로 사용자 리드 점수를 업데이트하고 자동으로 리드를 영업 팀에 전달하는 방법을 보여줍니다.

Braze에서 리드 스코어링 워크플로우를 만드는 두 가지 주요 단계가 있습니다.

1. Braze에서 리드 스코어링 캔버스를 만들기 또는 외부 리드 스코어링 도구 통합하기입니다.
- [간단한 리드 스코어링](#simple-lead-scoring)
- [외부 리드 스코어링](#external-lead-scoring)

2. 웹훅 캠페인을 만들어서 자격을 갖춘 리드를 영업 팀에 보내세요.
- [리드 핸드오프: 적격 리드(MQL) 마케팅부터 영업까지](#lead-handoff)

## 간단한 리드 스코어링

### 1단계: 캔버스 만들기

1. **메시징** > **캔버스**로 이동하여 **캔버스 생성**을 선택한 다음 캔버스 기본 사항을 입력합니다.

2. 캔버스에 "리드 스코어링 캔버스"와 같은 관련 이름을 지정하고, 더 나은 검색을 위해 "리드 관리"와 같은 태그를 지정하세요.<br><br>![캔버스 이름을 “리드 스코어링 캔버스”로 하고 태그를 “리드 관리”로 하여 캔버스를 만드는 1단계입니다.][1]{: style="max-width:80%;"}

### 2단계: 입력 기준 설정

1. **입장 일정** 단계로 이동하여 **행동 기반** 입장 일정을 선택하십시오. 사용자가 특정 작업을 수행하면 캔버스에 들어가게 됩니다.

2. **액션 기반 옵션**에서 다음 두 가지 액션을 추가하십시오:
    - 리드 점수 속성 이름으로 **커스텀 속성 값 변경하기**(예: `lead score`). If you haven’t created a lead scoring attribute yet, follow the steps in [Custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). 리드 점수가 변경될 때마다 사용자가 캔버스에 들어가게 됩니다.
    - **이메일 주소 추가**

![“액션 기반” 입력 일정 및 사용자 정의 속성 “리드 점수” 변경 및 이메일 주소 추가의 액션 기반 옵션으로 캔버스를 만드는 2단계입니다.][2]{: style="max-width:80%;"}

### 3단계: 타켓 오디언스 식별

#### 3a단계: 세그먼트 선택

모든 사용자는 리드 스코어링 자격이 있으므로, 타겟팅할 사용자 [세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/)를 선택하고 추가 [필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)를 적용하여 회사별 규칙을 추가할 수 있습니다. 예를 들어, 직원, 이미 고객인 사용자 등을 제외할 수 있습니다. 

![옵션을 사용하여 세그먼트 및 필터를 선택하여 항목 오디언스를 좁히는 캔버스 생성의 3단계입니다.][3]{: style="max-width:80%;"}

#### 3b단계: 캔버스 재사용 자격 설정

사용자는 귀하와의 생애주기 동안 이 캔버스를 여러 번 거치게 되므로 이전에 나갔던 것만큼 빨리 다시 들어올 수 있도록 하세요. 이것은 재적격성 설정을 통해 달성할 수 있습니다. 

**입력 제어**에서 다음을 수행하십시오:
- **사용자가 이 캔버스를 다시 입력할 수 있도록 허용**을 선택하십시오.
- **지정된 기간**을 선택하세요.
- 재자격을 '0' **초**로 설정하십시오.

![“입력 제어” 섹션에는 “지정된 기간”에서 0초 동안 사용자가 이 캔버스를 다시 입력할 수 있도록 선택할 수 있습니다.][4]{: style="max-width:80%;"}

#### 3단계 c: 전송 설정 업데이트

이 캔버스의 운영 특성과 이 사용자들에게 메시지가 전송되지 않는다는 사실을 감안할 때, 구독 상태를 준수할 필요가 없습니다.

**구독 설정**에서, **이 사용자에게 보내기:** **모든 사용자(구독 취소한 사용자 포함)**를 선택합니다. 

![메시지 전송 옵션 설정을 위한 캔버스 생성의 4단계입니다.][5]{: style="max-width:80%;"}

### 4단계: 캔버스 구축

#### 4a 단계: 행동 경로 추가

배리언트에서 더하기 아이콘을 선택한 다음 **작업 경로**를 선택합니다.

![더하기 아이콘으로 열린 메뉴에 "작업 경로"가 표시된 캔버스가 있습니다.][6]{: style="max-width:60%;"}

#### 4b단계: 작업 그룹 만들기

각 작업 그룹은 동일한 포인트 증가 또는 감소로 이어지는 모든 작업을 나타냅니다. 최대 8개의 작업 그룹을 설정할 수 있습니다. 이 시나리오에서는 네 개의 그룹을 설정할 것입니다.

다음 그룹을 행동 경로에 추가하십시오:

- **그룹 1:** 1점 증가에 해당하는 모든 이벤트.
- **그룹 2:** 5점 증가에 해당하는 모든 이벤트.
- **그룹 3:** 1점 감소에 해당하는 모든 이벤트.
- **다른 모든 사람:** 작업 경로를 사용하면 사용자가 조치를 취하는지 확인하기 위해 기다리는 창을 정의한 다음, 그들을 "기타 모든 사람" 그룹에 넣을 수 있습니다. 리드 스코어링의 경우, 이는 "비활동"에 대한 점수를 감소시킬 수 있는 기회입니다.

![1점, 5점, 10점을 더하는 액션 그룹, 1점, 10점을 빼는 액션 그룹 및 '기타 모든 사람'을 포함하는 액션 경로입니다.][7]

#### 4c 단계: 각 그룹에 관련 이벤트를 포함하도록 구성하십시오

각 작업 그룹에서 **트리거 선택**을 선택하고 해당 작업 그룹에 대해 포인트 수를 추가할 이벤트를 선택합니다. 트리거를 추가하여 리드 점수를 하나씩 증가시키는 모든 이벤트를 포함하세요. 예를 들어, 사용자가 세션을 시작할 때 앱에서 점수를 하나 올리거나 커스텀 이벤트(예: 등록 또는 웨비나 참여)를 수행할 수 있습니다. 

![“모든 앱에서 세션 시작” 및 “커스텀 이벤트 수행” 트리거로 포인트를 추가하기 위한 작업 그룹.][8]{: style="max-width:80%;"}

#### 4d 단계: 사용자 업데이트 단계 추가

각 행동 경로 아래에 생성된 각 캔버스 경로에 사용자 업데이트 단계를 추가하세요. 

![캔버스 행동 경로를 표시하고 각 행동 그룹에 대한 분기된 사용자 업데이트 경로를 표시합니다.][9]{: style="max-width:80%;"}

{: start=”2”}
각 사용자 업데이트 단계의 **작성** 탭에서 해당 필드에 대해 다음을 수행하십시오:

| 필드 | 작업 |
| --- | --- |
| **속성 이름** | 2단계(`lead score`)에서 선택한 리드 점수 속성을 선택합니다.|
| **작업** | 경로가 점수를 증가시키면 동작을 **증가**로 변경하고, 경로가 점수를 감소시키면 **감소**로 변경합니다. |
| **증가** 또는 **감소** | 리드 점수에서 증가하거나 감소할 포인트 수를 입력하세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 5단계: 캔버스를 실행합니다

끝입니다! 리드 스코어링 캔버스가 실행 준비되었습니다.

## 외부 리드 스코어링

당사의 [기술 파트너]({{site.baseurl}}/partners/home/), 자체 내부 리드 스코어링 모델, 머신 러닝 또는 다른 리드 스코어링 도구를 사용하는 경우, 여러 가지 옵션이 있습니다.

### 외부 파트너

[기술 파트너]({{site.baseurl}}/partners/home)를 확인하여 리드 스코어링 기능을 제공하는 당사의 B2B 파트너에 대해 알아보세요. 도구가 거기에 보이지 않나요? [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) API 엔드포인트를 호출하여 통합할 수 있습니다. 

### 내부 리드 스코어링 데이터 모델

Braze를 내부 데이터 모델(리드 스코어링 모델 포함)과 다양한 방식으로 통합할 수 있습니다. 다음은 고객들이 Braze와 통합한 일반적인 예시들입니다.

#### 통합 클라우드 데이터 웨어하우스

{% tabs %}
{% tab Braze를 데이터 소스로 사용 %}

마케팅 도구로서 Braze는 팀의 내부 리드 스코어 모델을 보완할 수 있는 매우 관련성 높은 데이터를 포함하고 있습니다. 

예를 들어, 메시징 참여 데이터(예: 이메일 열기 및 클릭, 랜딩 페이지 인게이지먼트 등)는 리드의 인게이지먼트를 결정할 수 있습니다. Braze 스트리밍 내보내기 데이터 솔루션을 사용하여 이 데이터를 클라우드 데이터 웨어하우스로 다시 전달하고 리드 스코어링 모델의 입력으로 사용할 수 있습니다:

- [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Snowflake 보안 데이터 공유]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)

{% endtab %}
{% tab 대상으로서 Braze %}

내부 팀이 리드 스코어링 모델을 생성하고 실행한 후, 해당 데이터를 Braze로 다시 가져와서 관련 메시징을 위해 리드를 더 잘 세그먼트하고 타겟팅할 수 있습니다. You can do this with [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/). 

클라우드 데이터 수집을 통해 내부 Teams는 사용자 식별자, 최신 리드 점수 및 점수가 업데이트된 타임스탬프가 포함된 새 테이블 또는 뷰를 생성합니다. Braze는 테이블 또는 뷰를 선택하고 리드 점수를 사용자 프로필에 추가합니다.

{% endtab %}
{% endtabs %}

## 리드 핸드오프: 적격 리드(MQL) 마케팅부터 영업까지{#lead-handoff}

Braze가 추천하는 리드 핸드오프 접근 방식은 Braze의 각 사용자에게 해당 리드 또는 연락처를 연결하는 것입니다. 이 리드는 리드 상태가 MQL 단계로 변경되면 귀하의 Sales Teams의 대기줄에 들어가며, 이 시점에서 Salesforce는 리드 라우팅 또는 할당 워크플로를 시작합니다. 

Salesforce에서 리드 상태를 Braze에서 업데이트하려면 트리거된 웹훅 템플릿을 사용하는 것이 좋습니다.

### 1단계: 웹훅 캠페인 생성

### 2단계: 웹훅 구성

#### 2a 단계: 웹훅 작성

1. 웹훅 캠페인에 "Salesforce > MQL로 리드 업데이트"와 같은 이름을 지정하세요.

2. {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} 형식으로 웹훅 URL을 입력하세요. {% raw %}`{{$user_id}}}`{% endraw %}의 Braze 사용자 ID는 Salesforce 연락처 ID와 일치해야 합니다. 그렇지 않으면 {% raw %}`{{$user_id}}}`{% endraw %} 대신 별칭을 사용하십시오.

3. **HTTP Method**을 **PATCH**로 업데이트하십시오.

4. 리드의 리드 점수가 미리 정의된 임계값을 초과하는 경우에만 Salesforce에서 리드 레코드를 업데이트하도록 페이로드를 구성하십시오. 다음 예시 요청 본문에서 리드 점수가 100보다 큰 경우를 참조하세요.

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
5\. 다음 헤더를 포함하십시오:

| 헤더 | 콘텐츠 |
| --- | --- |
| 승인 | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>토큰을 검색하려면 [OAuth 2.0 클라이언트 자격 증명 흐름에 대해 연결된 앱을 구성](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)한 다음 연결된 콘텐츠를 사용하여 Salesforce에서 베어러를 검색하세요: <br><br>{% raw %}<code>{% connected_content <mem_c25ac993-b31d-4e59-9db7-fff8795a2080/>[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]_mem_amp_client_secret=[client_secret]_mem_amp_grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

![웹훅이 Salesforce 웹훅 URL, PATCH HTTP 메서드, 원시 텍스트 요청 본문 및 요청 헤더로 구성됩니다.][10]{: style="max-width:80%;"}

#### 2b 단계: 웹훅 전송 예약

캠페인은 사용자의 리드 점수가 변경될 때마다 트리거되어야 합니다. 이 캠페인은 점수가 변경된 모든 사용자에게 트리거되지만, 현재 MQL이 아니고 이전 단계에서 설정한 임계값을 초과한 사용자에게만 영향을 미칩니다.

**전달 일정** 단계에서 다음을 선택하십시오:
- **행동 기반** 전달 유형
- 트리거 동작 **커스텀 속성 값 변경** 리드 스코어링 속성의 이름과 **새로운 값**의 동작

#### 2c 단계: 타겟 오디언스 식별

**타겟 오디언스** 단계에서 리드 상태가 이미 MQL 이상인 사용자를 제외하는 필터를 포함하세요. 예를 들어 "`lead_status` `is none of` `MQL`"과 같습니다.

![웹훅 타겟팅 옵션은 “lead_status” 필터가 “MQL”이 아닌 경우입니다.][11]{: style="max-width:80%;"}

### 3단계: 캠페인 시작

**시작**을 선택하고 고객이 MQL 리드 점수 임계값을 초과할 때 Salesforce에서 리드 상태가 변경되는 것을 확인하세요.

[1]: {% image_buster /assets/img/b2b/step_1_simple.png %}
[2]: {% image_buster /assets/img/b2b/step_2_simple.png %}
[3]: {% image_buster /assets/img/b2b/step_3_simple.png %}
[4]: {% image_buster /assets/img/b2b/entry_controls_simple.png %}
[5]: {% image_buster /assets/img/b2b/step_4_simple.png %}
[6]: {% image_buster /assets/img/b2b/action_paths_simple.png %}
[7]: {% image_buster /assets/img/b2b/action_paths_selected_simple.png %}
[8]: {% image_buster /assets/img/b2b/action_groups_simple.png %}
[9]: {% image_buster /assets/img/b2b/user_update_paths_simple.png %}
[10]: {% image_buster /assets/img/b2b/webhook.png %}
[11]: {% image_buster /assets/img/b2b/step_3_webhook.png %}