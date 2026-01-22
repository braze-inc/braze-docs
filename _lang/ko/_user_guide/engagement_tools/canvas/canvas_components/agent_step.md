---
nav_title: 에이전트
article_title: 상담원 단계
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "이 참조 문서에서는 캔버스에서 에이전트 단계를 사용하여 콘텐츠를 생성하거나 실시간으로 지능적인 결정을 내리는 방법에 대해 설명합니다."
tool: Canvas
---

# 상담원 단계  

> 에이전트 단계에서는 AI 기반 의사 결정 및 콘텐츠 생성을 캔버스 워크플로에 바로 추가할 수 있습니다. 자세한 내용은 [Braze 에이전트를]({{site.baseurl}}/user_guide/brazeai/agents/) 참조하세요. 

캔버스 사용자 여정의 에이전트 단계.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## 작동 방식

사용자가 캔버스에서 상담원 단계에 도달하면 Braze는 구성한 입력 데이터(전체 컨텍스트 또는 선택한 필드)를 선택한 상담원에게 전송합니다. 그런 다음 에이전트는 모델과 지침을 사용하여 입력을 처리하고 출력을 반환합니다. 해당 출력은 단계에서 정의한 출력 변수에 저장됩니다.

그런 다음 이 변수를 두 가지 주요 방법으로 사용할 수 있습니다:

- **의사 결정:** 상담원의 응답에 따라 사용자를 다양한 캔버스 경로로 라우팅하세요. 예를 들어 리드 채점 에이전트는 1에서 10 사이의 숫자를 반환할 수 있습니다. 이 점수를 사용하여 사용자에게 메시징을 계속할지 아니면 여정에서 삭제할지 결정할 수 있습니다.
- **개인화:** 상담원의 응답을 메시징에 바로 삽입하세요. 예를 들어 상담원이 고객 피드백을 분석하여 고객의 댓글을 참조하고 해결 방법을 제안하는 공감형 후속 이메일을 생성할 수 있습니다.

## 상담원 만들기 단계

### 1단계: 단계 추가

사이드바에서 **에이전트** 구성 요소를 드래그 앤 드롭하거나 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하고 **에이전트를** 선택합니다.  

### 2단계: 상담원 선택  

이 단계에서 데이터를 처리할 에이전트를 선택합니다. 기존 상담원을 선택하거나 이 단계에서 바로 새 상담원을 만들 수 있습니다. 설정 안내는 [커스텀 상담원 만들기를]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) 참조하세요.

### 3단계: 출력 변수 정의

상담원 출력을 "출력 변수"라고 하며 쉽게 액세스할 수 있도록 [컨텍스트 변수에]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) 저장됩니다. 출력 변수를 정의합니다:

1. 변수 이름을 지정합니다.
2. 데이터 유형을 선택합니다. 

상담원 출력은 문자열, 숫자 또는 부울로 저장할 수 있습니다. 이를 통해 캔버스에서 텍스트 개인화와 조건 로직 모두에 유연하게 사용할 수 있습니다. 다음은 각 유형에 대한 몇 가지 일반적인 용도입니다:

| 데이터 유형 | 일반적인 용도 |
| --- | --- |
| 문자열 | 메시지 개인화(제목란, 카피, 응답) |
| 번호 | [오디언스 경로의]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 점수, 임계값, 라우팅 |
| 부울 | [결정 분할에서]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 분기 예/아니요 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

정의되면 컨텍스트 변수를 사용할 때와 동일한 템플릿 구문을 사용하여 캔버스 전체에서 출력 변수를 사용할 수 있습니다. **컨텍스트 변수** 세그먼트 필터를 사용하거나 Liquid를 사용하여 직접 상담원 응답을 템플릿화하세요( {% raw %}`{{context.${response_variable_name}}}` {% endraw %}).

### 4단계: 상담원에게 제공할 컨텍스트 결정  

런타임에 에이전트가 수신할 데이터를 결정해야 합니다. 다음 옵션을 사용할 수 있습니다:  

- **모든 캔버스 컨텍스트를 포함합니다:** 사용 가능한 모든 캔버스 컨텍스트 변수(예: [캔버스 항목 속성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties))와 컨텍스트 단계를 통해 주어진 기타 컨텍스트를 전달합니다.  
- **값을 입력합니다:** 사용자의 이름이나 좋아하는 색상 등 선택한 속성만 전달합니다. 상담원에게 여기에 할당하는 값에 대한 액세스 권한만 부여하려면 이 옵션을 선택합니다. 각 **키에** 대해 특정 고객 프로필 필드 또는 컨텍스트 변수를 정의하는 [Liquid 태그를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) 입력합니다.  

{% alert note %}
Braze는 상담원에게 처음 10KB의 콘텐츠만 전달합니다. 총 값이 10KB를 초과하는 값을 제공하면 잘리게 됩니다. 비용을 저장하기 위해 캔버스의 Braze 에이전트는 동일한 입력에 대한 LLM 응답에 단기 캐시를 사용합니다. 모든 캔버스 컨텍스트를 포함하면 캐시된 결과를 사용할 수 없을 가능성이 높아져 LLM 비용이 증가할 수 있습니다.
{% endalert %}

## 오류 처리  

- 연결된 모델이 속도 제한 오류를 반환하면 Braze는 지수 백오프를 통해 최대 5회까지 재시도합니다.  
- 에이전트가 다른 이유(예: 잘못된 API 키)로 실패하면 출력 변수는 `null` 로 설정됩니다.  
- 반복 호출을 줄이기 위해 동일한 입력에 대한 응답이 캐시됩니다.  

## 분석  

다음 측정기준을 참조하여 상담원 단계의 성능/성과를 추적하세요:  

| 측정기준 | 설명 |
| --- | --- |
| _입력_ | 사용자가 상담원 단계를 입력한 횟수입니다. |
| _다음 단계로 진행_ | 상담원 단계를 통과한 후 흐름의 다음 단계로 진행한 사용자 수입니다. |
| _종료된 캔버스_ | 상담원 단계를 통과한 후 캔버스에서 나간 사용자 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 관련 문서  

- [Braze 에이전트 개요]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [커스텀 상담원 만들기]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [상담원 배포하기]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  