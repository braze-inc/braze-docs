---
nav_title: 데이터 소스 연결
article_title: 데이터 소스 연결
page_order: 1
description: "BrazeAI Decisioning Studio Go가 고객 참여 플랫폼을 통해 고객 데이터에 연결되는 방법을 알아보세요."
---

# 데이터 소스 연결

> BrazeAI Decisioning Studio™ Go는 고객 참여 플랫폼(CEP)을 통해 고객 데이터에 연결합니다. 이 글은 어떤 데이터가 사용되며 연결이 어떻게 작동하는지 설명합니다.

## Go가 고객 데이터에 접근하는 방법

다양한 소스와의 직접적인 데이터 통합을 지원하는 Decisioning Studio Pro와 달리, Decisioning Studio Go는 CEP를 통해 고객 데이터에 접근합니다. 이는 다음과 같은 의미입니다:

- **오디언스 데이터는** CEP(Braze, Salesforce Marketing Cloud 또는 Klaviyo)에서 정의된 세그먼트 또는 리스트에서 직접 추출되며, 특정 사전 정의된 속성(1P 데이터 제외)만 포함할 수 있습니다.
- **참여 데이터**(열람, 클릭, 발송)는 자동화된 쿼리 또는 CEP와의 네이티브 통합을 통해 수집됩니다.
- CEP에서 구성하는 것 외에 **추가적인 데이터 파이프라인 설정은** 필요**하지** 않습니다.

## 지원되는 통합 패턴

Decisioning Studio Go는 데이터 액세스를 위해 다음 CEP를 지원합니다:

| CEP | 오디언스 출처 | 참여 데이터 |
|-----|-----------------|-----------------|
| **Braze** | 세그먼트 | Braze 커런츠 내보내기 |
| **세일즈포스 마케팅 클라우드** | 데이터 확장 | SQL 쿼리 자동화 |
| **클라비요** | 세그먼트 | 네이티브 API 통합 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## CEP별 데이터 요구사항

{% tabs %}
{% tab Braze %}

### Braze 데이터 요구 사항

Braze 통합을 위해 Decisioning Studio Go에는 다음이 필요합니다:

1. **Braze 커런츠**: Braze 커런츠를 활성화하고 구성하여 참여 데이터를 Decisioning Studio Go로 내보내야 합니다. 이를 통해 에이전트는 고객의 응답으로부터 학습할 수 있습니다.

2. **세그먼트 접근**: 생성하는 API 키는 대상 오디언스를 정의하는 세그먼트에 접근할 수 있는 권한을 가져야 합니다.

3. **고객 프로필 데이터**: 에이전트가 고려해야 하는 모든 고객 프로필 속성 또는 커스텀 속성은 Braze API를 통해 접근 가능해야 합니다.

{% alert important %}
Braze 커런츠 내보내기 데이터에는 비교 대상 캠페인(BAU 캠페인 포함)의 데이터가 반드시 포함되도록 하십시오.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC 데이터 요구사항

Salesforce 마케팅 클라우드 통합을 위해 Decisioning Studio Go에는 다음이 필요합니다:

1. **데이터 확장**: 귀하의 오디언스는 Decisioning Studio Go가 접근할 수 있는 데이터 익스텐션에 정의되어야 합니다. 구독자 키를 기본 사용자 식별자로 사용하십시오.
2. **이벤트 추적 접근**: 설치된 앱 패키지가 종단 간 자동화를 지원하는 경우, 추가 구성이 필요하지 않습니다. 

데이터 확장 및 SQL 쿼리는 [오케스트레이션 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)의 일부로 구성됩니다.

{% endtab %}
{% tab Klaviyo %}

### 클라비요 데이터 요구사항

Klaviyo 통합을 위해 Decisioning Studio Go에는 다음이 필요합니다:

1. **세그먼트 접근**: 귀하의 오디언스는 API 키가 접근할 수 있는 Klaviyo 세그먼트로 정의되어야 합니다.
2. **프로필 데이터**: API 키는 고객 속성을 읽기 위해 프로필에 대한 전체 액세스 권한을 가져야 합니다.
3. **측정기준 접근**: API 키는 참여 데이터를 수집하기 위해 측정기준 및 이벤트에 대한 전체 액세스 권한을 가져야 합니다.

{% endtab %}
{% endtabs %}

## Best practices

- **데이터를 최신 상태로 유지하십시오**: 오디언스 세그먼트와 고객 데이터를 정기적으로(최소 매일) 업데이트하여 상담원이 최신 정보로 업무를 수행할 수 있도록 하십시오.
- **관련 속성을 포함하십시오**: 고객 특성이 어떤 메시지에 공감을 불러일으키는지 고려해 보십시오—인구통계학적 특성, 참여 이력, 구매 행동, 라이프사이클 단계 등이 모두 유용한 신호입니다.

## 다음 단계

Go가 데이터에 연결되는 방식을 이해하셨으니, 이제 CEP 통합 설정을 진행하세요:

- [오케스트레이션 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

