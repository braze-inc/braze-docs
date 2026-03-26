---
nav_title: 에이전트
article_title: 에이전트 단계
alias: /agent_step/
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Canvas에서 에이전트 단계를 사용하여 콘텐츠를 생성하거나 실시간으로 지능적인 결정을 내리는 방법을 다룹니다."
tool: Canvas
toc_headers: h2
---

# 에이전트 단계  

> 에이전트 단계를 사용하면 AI 기반의 의사 결정 및 콘텐츠 생성을 캔버스 워크플로우에 직접 추가할 수 있습니다. 더 자세한 정보는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)를 참조하세요. 

![캔버스 사용자 여정의 에이전트 단계입니다.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## 작동 방식

사용자가 캔버스의 에이전트 단계에 도달하면, Braze는 구성한 입력 데이터(전체 컨텍스트 또는 선택된 필드)를 선택한 에이전트에 전송합니다. 그런 다음 에이전트는 모델과 지침을 사용하여 입력을 처리하고 출력을 반환합니다. 해당 출력은 단계에서 정의한 출력 변수에 저장됩니다.

이 변수는 세 가지 주요 방법으로 사용할 수 있습니다:

- **의사 결정:** 에이전트의 응답에 따라 사용자를 다른 캔버스 경로로 라우팅합니다. 예를 들어, 리드 점수 에이전트가 1에서 10 사이의 숫자를 반환할 수 있습니다. 이 점수를 사용하여 사용자에게 계속 메시지를 보낼지 아니면 여정에서 제외할지를 결정할 수 있습니다.
- **개인화:** 에이전트의 응답을 메시지에 직접 삽입합니다. 예를 들어, 에이전트가 고객 피드백을 분석하고 고객의 의견을 참조하며 해결책을 제안하는 공감적인 후속 이메일을 생성할 수 있습니다.
- **사용자 데이터 처리:** 사용자 데이터를 분석하고 표준화한 다음 고객 프로필에 저장하거나 웹훅을 사용하여 전송합니다. 예를 들어, 에이전트가 감정 점수 또는 제품 친밀도 할당을 반환할 수 있습니다. 해당 데이터를 고객 프로필에 저장하여 향후 사용할 수 있습니다.

## 전제 조건

에이전트 단계는 [캔버스 컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables)를 사용하여 관련 컨텍스트를 수집하고 캔버스에서 활용할 수 있는 변수를 출력합니다.

## 에이전트 단계 생성

### 1단계: 단계 추가

사이드바에서 **에이전트** 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택한 후 **에이전트**를 선택합니다.  

### 2단계: 에이전트 선택  

이 단계에서 데이터를 처리할 에이전트를 선택합니다. 기존 에이전트를 선택하세요. 설정 안내는 [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)을 참조하세요.

### 3단계: 에이전트의 출력 설정 {#define-the-output-variable}

에이전트 출력은 "출력 변수"라고 하며, 쉽게 접근할 수 있도록 [컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types)에 저장됩니다. 출력 변수를 정의하려면 변수에 이름을 지정하세요.

출력 변수의 데이터 유형은 [에이전트 콘솔]({{site.baseurl}}/user_guide/brazeai/agents)에서 설정됩니다. 에이전트 출력은 문자열, 숫자, 부울 또는 오브젝트로 저장할 수 있습니다. 따라서 텍스트 개인화와 캔버스의 조건 로직 모두에 유연하게 사용할 수 있습니다. 각 유형의 일반적인 사용 사례는 다음과 같습니다:

| 데이터 유형 | 일반적인 사용 |
| --- | --- |
| 문자열 | 메시지 개인화(제목란, 카피, 응답) |
| 숫자 | 점수 매기기, 임계값, [오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)에서의 라우팅 |
| 부울 | [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)에서의 예/아니오 분기 |
| 오브젝트 | 예측 가능한 데이터 구조에서 단일 LLM 호출로 위의 데이터 유형 중 하나 이상을 활용 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

컨텍스트 변수와 동일한 템플릿 구문을 사용하여 캔버스 전체에서 출력 변수를 사용할 수 있습니다. **컨텍스트 변수** 세그먼트 필터를 사용하거나, Liquid를 사용하여 에이전트 응답을 직접 템플릿화하세요: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

오브젝트 출력 변수에서 특정 등록정보를 사용하려면 Liquid에서 점 표기법을 사용하여 해당 등록정보에 접근하세요: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![변수 "agent_output"에 대한 오브젝트 데이터 유형 출력을 가진 Body HTML Writer 에이전트 단계.]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### 4단계: 추가 컨텍스트 추가(선택 사항)

에이전트 단계가 실행될 때 참조할 추가 컨텍스트 값을 포함할 수 있습니다. 캔버스에서 일반적으로 사용하는 Liquid 템플릿 값을 입력할 수 있습니다.

{% alert note %}
에이전트는 이미 **지침** 섹션에서 구성된 컨텍스트를 자동으로 수신하고 있습니다. 해당 섹션에서 이미 구성된 Liquid 변수는 여기에서 다시 입력할 필요가 없습니다.
{% endalert %}

![Liquid를 사용하여 에이전트 단계에 추가 컨텍스트를 추가하는 옵션.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### 5단계: 에이전트 테스트

에이전트 단계를 설정한 후, 이 단계의 출력을 테스트하고 미리 볼 수 있습니다.

![무작위 사용자로 에이전트 출력을 미리봅니다.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## 오류 처리  

- 연결된 모델이 사용량 제한 오류를 반환하면, Braze는 지수 백오프를 사용하여 최대 5번 재시도합니다.  
- 에이전트가 타임아웃 오류나 잘못된 API 키와 같은 다른 이유로 실패하면 출력 변수는 `null`로 설정됩니다.
    - 에이전트가 일일 호출 한도에 도달하면 출력 변수는 `null`로 설정됩니다. 
- 오류에 대비하려면 [기본 Liquid 값]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values)을 사용하세요. 예를 들어, **개인화 추가** 모달에서 {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} 또는 {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}와 같은 기본 Liquid 값을 입력할 수 있습니다.
- 응답은 동일한 입력에 대해 캐시되며, 몇 분 이내에 반복되는 동일한 호출에 재사용될 수 있습니다.
    - 캐시된 값을 사용하는 응답도 총 호출 수 및 일일 호출 수에 포함됩니다.
- 에이전트 단계는 대량의 사용자를 처리하는 데 시간이 걸릴 수 있습니다. 이 단계에서 아직 대기 중인 사용자가 보이면 로그를 확인하여 호출이 진행되고 있는지 확인하세요.

## 분석  

다음 측정기준을 참조하여 에이전트 단계의 성능을 추적하세요:  

| 측정기준 | 설명 |
| --- | --- |
| _진입_ | 사용자가 에이전트 단계에 진입한 횟수입니다. |
| _다음 단계로 진행_ | 에이전트 단계를 통과한 후 플로우의 다음 단계로 진행한 사용자 수입니다. |
| _캔버스 종료_ | 에이전트 단계를 통과한 후 캔버스를 종료한 사용자 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 자주 묻는 질문

### 에이전트 단계를 언제 사용해야 하나요?

일반적으로, 특정 상황별 데이터를 LLM에 제공하고 인간이 불가능한 규모로 에이전트가 캔버스 컨텍스트 변수를 지능적으로 할당하도록 하고 싶을 때 에이전트 단계를 사용하는 것을 권장합니다.

이전에 초콜릿과 딸기를 주문한 사용자에게 새로운 아이스크림 맛을 추천하는 개인화된 메시지를 보내는 경우를 가정해 보겠습니다. 에이전트 단계와 AI 항목 추천을 사용하는 것의 차이점은 다음과 같습니다:

- **에이전트 단계:** LLM을 사용하여 에이전트에게 제공된 지침 및 상황별 데이터 포인트를 기반으로 사용자가 원하는 것을 정성적으로 판단합니다. 이 예에서 에이전트 단계는 사용자가 다양한 맛을 시도하고 싶어할 가능성을 고려하여 새로운 맛을 추천할 수 있습니다.
- **AI 항목 추천:** 머신 러닝 모델을 사용하여 과거 사용자 이벤트(예: 구매)를 기반으로 사용자가 가장 원할 가능성이 높은 제품을 예측합니다. 이 예에서 AI 항목 추천은 사용자의 이전 두 주문(초콜릿과 딸기)과 워크스페이스 내 다른 사용자의 행동을 비교하여 맛(바닐라)을 제안합니다.

### 에이전트 단계는 입력 데이터를 어떻게 사용하나요?

에이전트 단계는 에이전트가 사용하도록 구성된 컨텍스트 데이터와 에이전트에 [제공된 추가 컨텍스트](#step-4-add-any-additional-context-optional)를 분석합니다.

## 관련 문서  

- [Braze Agents 개요]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [에이전트 배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [에이전트 참조]({{site.baseurl}}/user_guide/brazeai/agents/reference/)