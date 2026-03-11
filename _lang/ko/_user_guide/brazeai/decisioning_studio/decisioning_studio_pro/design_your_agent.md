---
nav_title: 에이전트 설계
article_title: 에이전트 설계
page_order: 3
description: "AI 의사결정 서비스 팀과 함께 청중 정의, 성공 측정기준 및 차원을 포함하여 Decisioning Studio Pro 에이전트를 디자인하는 방법을 배우십시오."
---

# 에이전트 설계

> 에이전트 설정의 첫 번째 단계는 AI 의사결정 서비스 팀과 협력하여 에이전트를 디자인하는 것입니다. 이 문서에서는 주요 디자인 결정과 청중을 정의하는 방법을 다룹니다.

의사결정 에이전트에 대한 기본 개념—성공 측정기준, 차원, 행동 은행 및 제약 조건—에 대해서는 [의사결정 에이전트 디자인]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)을 참조하십시오.

## 주요 디자인 결정

AI 의사결정 서비스 팀과 협력하여 다음 결정을 내리게 됩니다:

| 결정 | 설명 | 예시 |
|----------|-------------|----------|
| **성공 측정기준** | 에이전트가 고객 참여를 개인화할 때 무엇을 극대화할 것인가? | 매출, LTV, ARPU, 전환, 유지 |
| **Audience** | Decisioning Studio 에이전트가 고객 참여 결정을 내릴 대상은 누구인가? | 모든 고객, 로열티 회원, 위험에 처한 구독자 |
| **실험 그룹** | Decisioning Studio의 무작위 대조 시험은 어떻게 구성해야 합니까? | Decisioning Studio, 무작위 대조, BAU, 보류 |
| **치수** | 에이전트가 개인화해야 할 결정은 무엇인가? | 시간, 제목란, 빈도, 제안, 채널 |
| **옵션** | 에이전트가 작업할 수 있는 옵션은 무엇인가? | 특정 템플릿, 제안, 시간 창 |
| **제약 조건** | 에이전트가 *절대* 내리지 말아야 할 결정은 무엇인가? | 지리적 제한, 예산 한도, 자격 규정 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

이러한 결정 각각은 에이전트가 생성할 수 있는 추가적인 상승 효과의 양과 속도에 영향을 미칩니다. 우리의 AI 의사결정 서비스 팀은 귀하의 비즈니스 규칙을 존중하면서 최대 가치를 생성하는 에이전트를 설계하기 위해 귀하와 협력할 것입니다.

![의사결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## 귀하의 오디언스 정의하기

사용 사례 오디언스는 일반적으로 고객 참여 플랫폼(예: Braze 또는 Salesforce Marketing Cloud)에서 정의된 후 의사결정 스튜디오 에이전트로 전송됩니다. 에이전트는 무작위 대조 시험을 수행하기 위해 고객을 치료 그룹으로 나눕니다.

### 치료 그룹

| 그룹 | 설명 |
|-------|-------------|
| **의사결정 스튜디오** | AI 최적화 추천을 받는 고객 |
| **무작위 대조** | 무작위로 선택된 옵션을 받는 고객(기준 비교) |
| **일상 비즈니스(선택 사항)** | 현재 마케팅 여정을 받는 고객(기존 성과와 비교하기 위해) |
| **홀드아웃(선택 사항)** | 커뮤니케이션을 받지 않는 고객(전체 캠페인 영향을 측정하기 위해) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 귀하의 오디언스 구성하기

{% tabs %}
{% tab Braze %}

**Braze에서 오디언스 구성:**

1. 대상으로 삼고 싶은 오디언스를 위한 세그먼트를 만드세요.
2. 세그먼트 ID를 귀하의 AI 의사결정 서비스 팀에 제공하세요.

{% alert note %}
Braze의 경우 여러 세그먼트를 수집하고 결합하여 오디언스를 생성할 수 있습니다. Decisioning Studio는 비즈니스-일상 비교 캠페인을 위한 세그먼트를 수집할 수 있습니다. 이 모든 패턴은 허용됩니다.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Salesforce Marketing Cloud에서 오디언스 구성:**

1. 오디언스를 위한 SFMC 데이터 확장을 구성하고 데이터 확장 ID를 제공하십시오.
2. API 통합을 위한 SFMC 설치 패키지를 설정하고 Decisioning Studio에서 요구하는 적절한 권한을 부여하십시오.
3. 이 데이터 확장이 매일 새로 고쳐지도록 하십시오. Decisioning Studio는 최신 증분 데이터에서 가져옵니다.

확장 ID와 API 키를 Braze 서비스 팀에 제공하십시오. 그들이 고객 데이터를 수집하는 다음 단계에 도움을 줄 것입니다.

{% endtab %}
{% tab Klaviyo %}

**Klaviyo에서 오디언스 정의:**

1. 오디언스 세그먼트를 생성하십시오.
2. 개인 API 키를 생성하고 이를 Braze AI Decisioning 팀에 제공하십시오.
3. 세그먼트 ID와 API 키를 Braze 서비스 팀에 제공하십시오.

이 단계를 수행하는 방법에 대한 자세한 정보는 [Klaviyo 설명서](https://help.klaviyo.com/hc/en-us/articles/115005237908)를 참조하십시오.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

오디언스가 현재 Braze, SFMC 또는 Klaviyo에 저장되어 있지 않은 경우, 다음 최선의 단계는 Braze가 제어하는 Google Cloud Services 버킷으로 직접 자동 내보내기를 구성하는 것입니다.

이것이 가능한지 여부를 판단하려면 Martech 플랫폼의 설명서를 참조하십시오. 예를 들어, mParticle은 [Google Cloud Storage와의 네이티브 통합](https://www.mparticle.com/integration/google-cloud-storage/)을 제공합니다. 이 경우, 오디언스 데이터를 내보내기 위해 GCS 버킷을 제공할 수 있습니다.

유사한 페이지가 있습니다:
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [어도비 경험 플랫폼](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## 프로 기능

결정 스튜디오 프로는 AI 결정의 모든 힘을 제공합니다:

| 기능 | 세부 정보 |
|------------|---------|
| **모든 성공 지표** | 매출, 전환, ARPU, LTV 또는 모든 비즈니스 KPI에 최적화 |
| **무제한 차원** | 제안, 채널, 타이밍, 빈도, 크리에이티브 등을 통해 개인화 |
| **모든 CEP** | Braze, SFMC, Klaviyo와의 네이티브 통합 + 모든 플랫폼에 대한 커스텀 통합 |
| **AI 결정 서비스** | Braze의 데이터 과학 팀으로부터의 전담 지원 |
| **고급 실험 설계** | 완전히 사용자 정의 가능한 처리 그룹 및 보류 그룹 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Best practices

결정 스튜디오 에이전트를 설계하기 위한 몇 가지 모범 사례:

1. **데이터 풍부성 극대화**: 에이전트가 고객에 대한 정보가 많을수록 성능이 향상됩니다.
2. **행동 다양화**: 에이전트가 취할 수 있는 행동의 세트가 다양할수록 각 사용자에 대한 전략을 개인화할 수 있습니다.
3. **제약 최소화**: 당신의 에이전트에 대한 제약이 적을수록 더 좋습니다. 제약은 비즈니스 규칙을 존중하면서 에이전트 주도의 실험을 최대한 자유롭게 할 수 있도록 설계되어야 합니다.

## 다음 단계

핵심 설계 결정이 이루어지면, 우리는 출시를 진행할 수 있습니다:

- [당신의 에이전트를 시작하세요]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)