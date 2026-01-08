# 에이전트 구축

> BrazeAI Decisioning Studio™를 위한 에이전트를 구축하여 수동 A/B 테스트 없이도 개인화된 실험을 자동화하고 전환, 리텐션, 매출 등의 결과를 최적화하는 방법을 알아보세요.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## 에이전트 소개

AI 의사 결정 에이전트는 특정 비즈니스 목표에 부합하도록 맞춤화된 BrazeAI™ 의사 결정 엔진의 커스텀 구성입니다.

일례로, 초기 판매 후 후속 전환을 늘리기 위해 재구매 에이전트를 구축할 수 있습니다. 사용자는 Braze에서 오디언스와 메시지를 정의하고, 의사 결정 에이전트는 매일 실험을 실행하여 각 고객에 대해 제품 오퍼, 메시지 타이밍 및 빈도의 다양한 조합을 자동으로 테스트합니다. 시간이 지남에 따라 BrazeAI™는 가장 효과적인 방법을 학습하고, 재구매율을 극대화하기 위해 Braze를 통해 개인화된 전송을 오케스트레이션합니다.

좋은 에이전트 구축하려면 다음과 같이 해야 합니다.

- BrazeAI™ 최적화를 위한 성공 측정기준을 선택합니다(예: 매출, 전환 또는 ARPU).
- 테스트할 차원을 정의합니다(예: 오퍼, 제목란, 크리에이티브, 채널 또는 발송 시간).
- 각 차원에 대한 옵션을 선택합니다(예: 이메일 vs SMS, 또는 일일 vs 주간 빈도).

![추천 이메일에 대한 Decisioning Studio 에이전트의 예시 다이어그램.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## 샘플 에이전트

다음은 BrazeAI Decisioning Studio™로 구축할 수 있는 에이전트의 몇 가지 예입니다. AI 의사 결정 에이전트는 모든 고객 상호 작용을 통해 학습하고 이러한 인사이트를 다음날의 행동에 적용합니다.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## 에이전트 구축

### 필수 조건

에이전트를 구축하려면 먼저 [BrazeAI Decisioning Studio™를 통합]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration)해야 합니다.

### 1단계: AI 전문가 서비스에 문의하기

AI 전문가 서비스 팀은 고객과 긴밀히 협력하여 의사 결정 에이전트의 범위 설정, 설계 및 구축을 지원합니다. 아직 시작하지 않았다면 지금 바로 [문의](https://www.braze.com/get-started/)하여 시작하세요.

다음 단계를 함께 완료하여 고객에게 적합한 커스텀 에이전트를 구축할 수 있습니다.

### 2단계: 에이전트 설계

AI 전문가 서비스 팀과 함께 다음을 정의합니다.

- 타겟 오디언스 
- 최적화할 비즈니스 측정기준 
- BrazeAI™ 의사 결정 에이전트의 행동 
- 에이전트가 비즈니스 성과를 높이기 위해 활용해야 하는 모든 퍼스트파티 고객 데이터. 

설계가 완료되면 이 팀이 고객과 협력하여 추가 통합 요구 사항을 식별하고 완료합니다.

### 3단계: 전송 플랫폼 설정

다음으로, AI 전문가 서비스 팀이 마케팅 자동화 플랫폼을 설정하는 데 도움을 드립니다. Decisioning Studio는 Braze와 가장 잘 작동하지만, 다른 다양한 플랫폼도 지원합니다. 추가 리소스가 필요한 경우 AI 전문가 서비스 팀에 문의하세요.

{% tabs local %}
{% tab Braze %}
Braze를 설정하려면:

1. [캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 또는 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule)를 만듭니다. BrazeAI Decisioning Studio™는 이 전송 방법을 사용하여 정의된 오디언스에 속한 사용자에게 개인화된 일대일 활성화 이벤트를 전송합니다.
2. Braze [대조군]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)을 포함하지 않고 대신 BrazeAI™를 전용 대조군으로 사용할 수 있습니다.
3. 규모에 따라 크리에이티브 콘텐츠에 Liquid 태그를 구성하여 메시징에 BrazeAI™ 추천을 동적으로 채울 수 있습니다. BrazeAI™는 Braze API를 통해 템플릿의 Liquid 태그에 고객별 콘텐츠를 전달합니다.
{% endtab %}
{% endtabs %}

### 4단계: 시작 및 모니터링

에이전트를 시작한 후에는 AI 전문가 서비스 팀이 지속적으로 모니터링하고 합의된 설계에 맞게 조정합니다. 또한 필요한 경우 에이전트를 조정, 확장 또는 수정하는 데 도움을 드립니다.
