---
nav_title: 시작하기
article_title: BrazeAI Operator<sup>TM</sup> 시작하기
page_order: 1
description: "BrazeAI Operator<sup>TM</sup>에 액세스하고 사용하는 방법, 기능 및 모범 사례를 알아봅니다."
---

# BrazeAI Operator 시작하기

> 대시보드에 내장된 AI 어시스턴트인 BrazeAI Operator<sup>TM</sup>에 액세스하고 사용하는 방법, 기능 및 모범 사례를 알아봅니다.

## Operator 열기

Braze 대시보드의 모든 페이지에서 Operator를 엽니다.

1. 사용자 프로필 옆의 **BrazeAI Operator<sup>TM</sup>** 를 선택합니다.

![사용자 프로필 옆의 BrazeAI Operator 아이콘.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Operator 채팅 패널이 화면 오른쪽에 열립니다.

![Operator 채팅 패널.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
패널을 최대화하면 읽기 편하고, 최소화하면 작업하면서 Operator를 계속 사용할 수 있습니다.
{% endalert %}

## Operator 사용하기

자연어로 수행하려는 작업을 설명합니다. 프롬프트는 간단한 질문부터 복잡한 요청까지 다양합니다.

- **간단한 예:** Liquid가 렌더링되지 않는 이유는?
- **복잡한 예:** 메시지의 `abort_message` 태그에 중단 원인이 된 사용자 속성을 포함하려면 어떻게 하나요?

Operator는 단계별 지침, Braze 문서 링크, 쉬운 설명을 제공합니다. 명확하고 구체적인 질문일수록 더 유용한 답변을 받을 수 있습니다. Operator는 복잡한 다단계 작업에 적합한 강력한 추론을 제공하는 [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)를 사용합니다.

## 모범 사례

Operator를 검색 엔진이 아닌 대화처럼 사용합니다. 짧고 자연스러운 프롬프트가 가장 효과적입니다.

- **구체적으로:** "Canvas에 대해 알려줘" 대신 "Canvas에서 액션 경로를 어떻게 사용하나요?"라고 질문합니다.
- **후속 질문하기:** 첫 답변이 부족하면 명확히 하거나 추가 세부 정보를 요청합니다.
- **페이지 인식 컨텍스트 활용:** Operator는 Braze 내 위치를 파악합니다. 관련 페이지를 열어 둔 상태에서 Operator를 사용하면 가장 정확한 결과를 얻을 수 있습니다.

## 경험 맞춤화

### 브랜드 가이드라인 적용

Operator 답변이 브랜드의 음성, 톤, 성격에 맞도록 브랜드 가이드라인을 컨텍스트로 추가할 수 있습니다. Operator는 워크스페이스에 구성된 브랜드 가이드라인을 사용하여 제안하는 문구나 기능 설명의 일관성을 유지합니다.

브랜드 가이드라인을 설정하려면 **설정** > **브랜드 가이드라인** 으로 이동합니다. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/)을 참조하세요.

![Operator 채팅 패널에서 브랜드 가이드라인 선택.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### 페이지 인식 컨텍스트 활용

Operator는 Braze 내 위치를 자동으로 파악하고 해당 컨텍스트에 맞춰 답변합니다. 예를 들어 Canvas를 작성하는 동안 Operator를 열면 관련 단계를 제안하거나 Canvas 기능에 대한 지침을 제공하며, 작업 위치를 설명할 필요가 없습니다.

이 컨텍스트 인식 덕분에 "Canvas 워크플로에 지연 단계를 어떻게 추가하나요?" 대신 "지연을 어떻게 추가하나요?"처럼 더 짧고 자연스러운 질문을 할 수 있습니다.

## Operator 답변으로 작업하기

### 제안된 입력으로 시작하기

Operator를 열면 일반적인 작업과 현재 페이지를 기반으로 제안이 표시됩니다. 빠르게 시작하려면 하나를 선택하거나 직접 질문을 입력합니다.

### Operator 사고 과정 확인하기

Operator는 **Reasoned** 라고 표시된 접이식 영역에 사고 과정을 표시합니다. 드롭다운을 펼쳐 해당 영역을 확장하고 Operator가 답변에 도달한 과정을 확인합니다.

![Operator 답변의 접힌 "Reasoned" 드롭다운.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operator로 액션 실행하기

Operator는 Braze 대시보드에서 직접 변경 사항을 제안하고 실행할 수 있습니다(예: 폼 필드 채우기, 설정 조정, 콘텐츠 생성). 제안된 각 변경 사항은 검토 및 승인을 위해 액션 카드로 표시됩니다. 자세한 내용은 [액션 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)를 참조하세요.

## 세션 관리

### 답변 중단하기

Operator가 답변을 생성하는 동안 **보내기** 버튼이 **중지** 로 바뀝니다. 질문을 바꾸거나 답변이 잘못된 방향으로 가면 **중지** 를 선택해 조기에 답변을 종료할 수 있습니다.

### 기록 지우기

처음부터 시작하거나 대화에서 민감한 정보를 제거하려면 **채팅 기록 지우기** 를 선택합니다. 현재 내용이 삭제되고 대화 컨텍스트가 초기화됩니다.

### 피드백 남기기

각 답변 아래의 👍 또는 👎 버튼으로 빠른 피드백을 남길 수 있습니다. 피드백은 Operator 답변 개선에 도움이 됩니다.

## 다음 단계

- [액션 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) – Operator가 제안한 변경 사항 검토 및 승인
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) – 일반적인 문제와 해결 방법
