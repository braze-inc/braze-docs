---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Braze 대시보드에 내장된 AI 기반 어시스턴트인 BrazeAI Operator<sup>TM</sup>의 기능과 모범 사례를 포함한 접근 및 사용 방법을 알아보세요."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup>는 대시보드에 내장된 AI 기반 어시스턴트입니다. Operator는 질문에 답변하고, 설정을 안내하며, 문제를 해결하고, 아이디어를 함께 고민하는 등 다양한 업무를 도와줍니다.

## Operator 접근하기

Braze 대시보드의 모든 페이지에서 Operator를 열 수 있습니다.  

1. 고객 프로필 옆에 있는 **BrazeAI Operator<sup>TM</sup>**를 선택하세요.

![고객 프로필 옆의 BrazeAI Operator 아이콘.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Operator 채팅 패널이 화면 오른쪽에 열립니다.

![Operator 채팅 패널.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
패널을 최대화하여 읽기 편하게 확장하거나, 작업 중에도 Operator를 사용할 수 있도록 최소화하세요.  
{% endalert %} 

## Operator 사용하기

자연어로 달성하려는 목표를 설명하세요. 프롬프트는 간단한 질문부터 복잡한 요청까지 다양할 수 있습니다:

- **간단한 질문:** 왜 내 Liquid가 렌더링되지 않나요?
- **복잡한 요청:** 내 메시지의 `abort_message` 태그에 중단을 유발한 사용자 속성을 포함시키려면 어떻게 해야 하나요?

Operator는 단계별 지침, Braze 설명서 링크 및 쉬운 설명을 제공할 수 있습니다. 명확하고 구체적인 질문은 더 유용한 답변을 이끌어냅니다. Operator는 강력한 추론 능력을 제공하며 복잡한 다단계 작업에 적합한 [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)를 사용합니다. 

## 모범 사례

Operator를 검색 엔진이 아닌 대화 상대처럼 대하세요. 짧고 자연스러운 프롬프트가 가장 효과적입니다.

- **구체적으로 질문하세요:** "캔버스에 대해 알려주세요" 대신 "캔버스에서 행동 경로를 어떻게 사용하나요?"라고 물어보세요.  
- **추가 질문을 하세요:** 첫 번째 답변이 필요한 내용을 충족하지 못할 경우, 명확한 설명이나 추가 세부 정보를 요청하세요.
- **페이지 인식 컨텍스트를 활용하세요:** Operator는 Braze 내에서 사용자의 위치를 파악합니다. 가장 정확한 결과를 얻으려면 관련 페이지를 보면서 Operator를 열어주세요.

## 경험 커스텀하기

### 브랜드 가이드라인 적용

Operator 쿼리에 브랜드 가이드라인을 컨텍스트로 추가하여 응답이 브랜드의 목소리, 어조 및 개성을 반영하도록 하세요. Operator는 워크스페이스에 구성된 브랜드 가이드라인을 사용하므로, 문구를 제안하거나 기능을 설명할 때 일관된 메시징을 보장하는 데 도움이 됩니다.

브랜드 가이드라인을 설정하려면 **설정** > **브랜드 가이드라인**으로 이동하세요. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/)을 참조하세요.

![Operator 채팅 패널에서 브랜드 가이드라인 선택하기.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### 페이지 인식 컨텍스트 활용

Operator는 Braze 내에서 사용자의 위치를 자동으로 파악하고 해당 컨텍스트에 맞춰 응답을 조정합니다. 예를 들어, 캔버스를 구축하는 동안 Operator를 열면, 사용자가 워크플로에서 현재 위치를 설명하지 않아도 관련 단계를 제안하거나 캔버스 기능에 대한 안내를 제공할 수 있습니다.

이러한 컨텍스트 인식 기능 덕분에 "캔버스 워크플로에서 지연 단계를 추가하는 방법은 무엇인가요?" 대신 "지연을 추가하려면 어떻게 해야 하나요?"와 같이 더 짧고 자연스러운 질문을 할 수 있습니다.

## Operator 응답 활용하기

### 추천 프롬프트로 시작하기

Operator를 열면 일반적인 작업과 현재 페이지에 기반한 추천 프롬프트가 표시됩니다. 빠르게 시작하려면 하나를 선택하거나, 직접 커스텀 질문을 입력하세요.

### Operator의 사고 과정 이해하기

Operator는 **추론 과정**이라고 표시된 접을 수 있는 섹션에 추론 단계를 보여줍니다. 드롭다운을 선택하여 해당 섹션을 확장하고 Operator가 답변을 어떻게 도출했는지 확인하세요. 이는 제안의 배경 논리를 이해하거나 접근 방식을 검증하고자 할 때 유용합니다.

![Operator 응답에서 접힌 "추론 과정" 드롭다운.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operator와 함께 동작 실행하기

Operator는 Braze 대시보드에서 직접 변경 사항을 제안하고 실행할 수 있습니다. 예를 들어, 양식 필드 입력, 설정 업데이트 또는 콘텐츠 생성이 가능합니다. 제안된 각 변경 사항은 동작 카드로 제시되며, 적용되기 전에 검토하고 승인해야 합니다. 이 기능의 작동 방식에 대한 자세한 내용은 [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)를 참조하세요.

## 세션 관리

### 응답 중지

Operator가 응답을 생성하는 동안, **보내기** 버튼이 **중지** 버튼으로 바뀝니다. 질문을 다시 표현해야 하거나 응답이 잘못된 방향으로 흘러갈 경우, **중지**를 선택하여 응답을 조기에 종료하세요.

### 기록 지우기

대화를 새로 시작하거나 민감한 정보를 삭제하려면 **대화 기록 지우기**를 선택하세요. 이렇게 하면 현재 모든 내용이 제거되고 대화 컨텍스트가 초기화됩니다.

### 피드백 제공

각 응답 하단에 있는 좋아요 또는 싫어요 버튼을 사용하여 빠른 피드백을 제공하세요. 피드백은 시간이 지남에 따라 Operator의 답변을 개선하는 데 도움이 됩니다.

## 데이터 프라이버시 및 보안

### HIPAA(미국의료정보보호법) 준수

AI Operator는 현재 OpenAI의 제로 데이터 보존 정책에 부합하지 않는 다중 턴 대화 기술을 활용합니다. AI Operator는 OpenAI의 수정된 악용 모니터링 데이터 보존 정책을 사용하지만, Braze와 OpenAI 간의 비즈니스 제휴 계약(BAA)의 적용을 받지 않습니다. 사용자는 Braze에 저장된 보호 대상 건강 정보(PHI)에 접근하도록 AI Operator에 요청하거나, 이 기능에 PHI를 제출해서는 안 됩니다.

### 모델 제공자를 하위 처리자 또는 제3자 제공자로 지정

Braze 서비스를 통해 Braze가 제공하는 LLM 제공자와의 통합("Braze 제공 LLM")을 사용할 경우, 해당 Braze 제공 LLM의 제공자는 귀하와 Braze 간의 데이터 처리 부속서(DPA) 조건에 따라 Braze의 하위 처리자로서 역할을 수행합니다. BrazeAI Operator<sup>TM</sup>는 OpenAI와 통합됩니다.

### OpenAI에서 데이터가 사용되는 방식

OpenAI를 활용하는 BrazeAI 기능을 통해 AI 출력("출력")을 생성하기 위해, Braze는 특정 정보("입력")를 OpenAI로 전송합니다. 입력은 사용자의 프롬프트, 대시보드에 표시되는 콘텐츠, 그리고 사용자의 쿼리와 관련된 워크스페이스 데이터로 구성됩니다. [OpenAI의 API 플랫폼 약관](https://openai.com/enterprise-privacy/)에 따라, Braze를 통해 OpenAI API로 전송된 데이터는 OpenAI 모델의 훈련 또는 개선에 사용되지 않습니다. 귀하와 Braze 사이에서, 출력은 귀하의 지적 재산입니다. Braze는 해당 출력에 대해 저작권 소유권을 주장하지 않습니다. Braze는 출력을 포함한 모든 AI 생성 콘텐츠에 대해 어떠한 종류의 보증도 하지 않습니다.

## 다음 단계

- [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Operator가 제안한 변경 사항을 검토하고 승인하는 방법을 알아보세요
- [고객지원 티켓 제출]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/): Operator에서 직접 고객지원 티켓을 제출하세요
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): 일반적인 문제 및 해결 방법을 참조하세요