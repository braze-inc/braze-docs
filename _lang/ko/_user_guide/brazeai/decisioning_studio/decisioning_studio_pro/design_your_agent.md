---
nav_title: 에이전트 설계
article_title: 에이전트 설계
page_order: 3
description: "오디언스 정의, 성공 측정기준 및 차원을 포함하여 AI 디시전 서비스 팀과 함께 Decisioning Studio Pro 상담원을 디자인하는 방법을 알아보세요."
---

# 에이전트 설계

> 상담원 설정의 첫 번째 단계는 AI 의사 결정 서비스 팀과 협력하여 상담원을 설계하는 것입니다. 이 문서에서는 주요 디자인 결정 사항과 오디언스를 정의하는 방법에 대해 설명합니다.

성공 측정기준, 차원, 작업 은행 및 제약 조건 등 의사 결정 에이전트에 대한 기본 개념은 [의사 결정 에이전트 디자인하기를]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/) 참조하세요.

## 주요 설계 결정

AI 의사 결정 서비스 팀과 협력하면 다음과 같은 결정을 내릴 수 있습니다:

| 결정 | 설명 | 예시 |
|----------|-------------|----------|
| **성공 측정기준** | 상담원은 고객 참여를 개인화할 때 무엇을 극대화할 수 있을까요? | 매출, LTV, ARPU, 전환, 유지율 |
| **Audience** | Decisioning Studio 상담원은 누구를 위해 고객 참여 결정을 내릴까요? | 모든 고객, 로열티 회원, 위험에 처한 가입자 |
| **실험 그룹** | 디시전킹 스튜디오의 무작위 대조군 시험은 어떻게 구성해야 하나요? | 의사 결정 스튜디오, 무작위 제어, BAU, 홀드아웃 |
| **치수** | 상담원은 어떤 결정을 개인화해야 하나요? | 시간, 제목란, 빈도, 오퍼, 채널 |
| **옵션** | 상담원은 어떤 옵션으로 작업해야 하나요? | 특정 템플릿, 오퍼, 기간 |
| **제약 조건** | 상담원이 *절대* 해서는 안 되는 결정은 무엇인가요? | 지리적 제한, 예산 한도, 자격 규칙 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

이러한 각 결정은 에이전트가 얼마나 많은 점진적 상승을 일으킬 수 있는지, 그리고 얼마나 빨리 상승할 수 있는지에 영향을 미칩니다. AI 의사 결정 서비스 팀은 고객과 협력하여 모든 비즈니스 규칙을 준수하면서 최대의 가치를 창출하는 에이전트를 설계합니다.

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## 오디언스 정의하기

사용 사례 오디언스는 일반적으로 고객 참여 플랫폼(예: Braze 또는 Salesforce 마케팅 클라우드)에서 정의한 다음 Decisioning Studio 에이전트로 전송됩니다. 그런 다음 상담원은 무작위 대조 시험을 수행하기 위해 고객을 치료 그룹으로 나눕니다.

### 치료 그룹

| 그룹 | 설명 |
|-------|-------------|
| **의사 결정 스튜디오** | AI에 최적화된 커스텀 추천을 받는 고객 |
| **무작위 제어** | 무작위로 선택된 옵션을 받는 고객(기준 비교) |
| **평소와 같은 업무(선택 사항)** | 현재 마케팅 여정을 받는 고객(기존 성과와 비교를 위해) |
| **홀드아웃(선택 사항)** | 커뮤니케이션을 받지 않는 고객(전체 캠페인 영향력 측정) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 오디언스 구성하기

{% tabs %}
{% tab Braze %}

**Braze에서 오디언스를 구성합니다:**

1. 타겟팅할 오디언스를 위한 세그먼트를 만듭니다.
2. AI 의사 결정 서비스 팀에 세그먼트 ID를 제공하세요.

{% alert note %}
Braze의 경우 여러 세그먼트를 수집하고 이를 결합하여 오디언스를 생성할 수 있습니다. 디시전킹 스튜디오는 평소와 같은 비즈니스 비교 캠페인을 위해 세그먼트를 수집할 수 있습니다. 이러한 패턴은 모두 허용됩니다.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Salesforce 마케팅 클라우드에서 오디언스를 구성합니다:**

1. 오디언스에 대한 SFMC 데이터 확장을 구성하고 데이터 확장 ID를 제공합니다.
2. Decisioning Studio에 필요한 적절한 권한으로 API 통합을 위해 SFMC 설치 패키지를 설정합니다.
3. 의사 결정 스튜디오는 사용 가능한 최신 증분 데이터에서 가져오므로 이 데이터 확장을 매일 새로고침해야 합니다.

Braze 서비스 팀에 확장 ID와 API 키를 제공하세요. 고객 데이터 수집의 다음 단계를 지원합니다.

{% endtab %}
{% tab Klaviyo %}

**클라비요에서 오디언스를 정의하세요:**

1. 오디언스 세그먼트 만들기
2. 비공개 API 키를 생성하고 이를 Braze AI 의사 결정 팀에 제공하세요.
3. Braze 서비스 팀에 세그먼트 ID와 API 키를 제공합니다.

이러한 단계를 수행하는 방법에 대한 자세한 내용은 [클라비요 설명서를](https://help.klaviyo.com/hc/en-us/articles/115005237908) 참조하세요.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

오디언스가 현재 Braze, SFMC 또는 클라비요에 저장되어 있지 않은 경우 차선책으로 자동화된 내보내기를 구성하여 Braze가 제어하는 Google 클라우드 서비스 버킷으로 직접 내보내도록 하는 방법이 있습니다.

이것이 가능한지 확인하려면 사용 중인 마테크 플랫폼의 설명서를 참조하세요. 예를 들어, mParticle은 [Google Cloud Storage와의 기본 통합](https://www.mparticle.com/integration/google-cloud-storage/) 기능을 제공합니다. 이 경우 오디언스 데이터를 내보낼 수 있는 GCS 버킷을 제공할 수 있습니다.

유사한 페이지가 있습니다:
- [Twilio 세그먼트](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe 경험 플랫폼](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## 프로 기능

Decisioning Studio Pro는 AI 의사 결정의 모든 기능을 제공합니다:

| 기능 | 세부 정보 |
|------------|---------|
| **모든 성공 측정기준** | 매출, 전환, ARPU, LTV 또는 모든 비즈니스 KPI 최적화 |
| **무제한 크기** | 오퍼, 채널, 타이밍, 빈도, 크리에이티브 등에 걸쳐 개인화된 광고 제공 |
| **모든 CEP** | Braze, SFMC, Klaviyo와의 기본 통합 + 모든 플랫폼에 대한 커스텀 통합 제공 |
| **AI 의사 결정 서비스** | Braze 데이터 과학 팀의 헌신적인 지원 |
| **고급 실험 설계** | 완전히 사용자 지정 가능한 치료 그룹 및 홀드아웃 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Best practices

Decisioning Studio 상담원 설계를 위한 몇 가지 모범 사례입니다:

1. **데이터의 풍부함을 극대화하세요**: 상담원이 고객에 대해 더 많은 정보를 가지고 있을수록 더 나은 성능/성과를 낼 수 있습니다.
2. **행동을 다양화하세요**: 에이전트가 수행할 수 있는 작업 집합이 다양할수록 각 사용자에 대한 전략을 더 개인화할 수 있습니다.
3. **제약 조건을 최소화합니다**: 상담원에 대한 제약이 적을수록 좋습니다. 제약 조건은 비즈니스 규칙을 존중하면서 에이전트가 주도하는 실험을 최대한 자유롭게 할 수 있도록 설계되어야 합니다.

## 다음 단계

주요 디자인 결정이 내려지면 출시를 진행할 수 있습니다:

- [상담원 시작하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)