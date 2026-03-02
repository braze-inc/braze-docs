---
nav_title: 데이터 소스 연결
article_title: 데이터 소스 연결
page_order: 1
description: "고객 참여 플랫폼을 통해 BrazeAI Decisioning Studio Go가 고객 데이터에 어떻게 연결되는지 알아보세요."
---

# 데이터 소스 연결

> BrazeAI Decisioning Studio™ Go는 고객 참여 플랫폼(CEP)을 통해 고객 데이터에 연결합니다. 이 문서에서는 어떤 데이터가 사용되고 연결이 어떻게 작동하는지 설명합니다.

## Go가 고객 데이터에 액세스하는 방법

다양한 데이터 소스와의 직접적인 데이터 통합을 지원하는 Decisioning Studio Pro와 달리, Decisioning Studio Go는 CEP를 통해 고객 데이터에 액세스합니다. 즉,

- **오디언스 데이터는** CEP에 정의된 세그먼트 또는 목록(Braze 또는 Salesforce 마케팅 클라우드)에서 직접 가져오며, 1P 데이터가 아닌 사전 정의된 특정 속성만 포함할 수 있습니다.
- **참여 데이터** (열기, 클릭, 전송)는 자동화된 쿼리 또는 CEP와의 기본 통합을 통해 캡처됩니다.
- CEP에서 구성한 것 외에 **추가적인 데이터 파이프라인 설정이** 필요하지 **않습니다.** 

## 지원되는 통합 패턴

Decisioning Studio Go는 데이터 액세스를 위해 다음과 같은 CEP를 지원합니다:

| CEP | 오디언스 소스 | 참여 데이터 |
|-----|-----------------|-----------------|
| **Braze** | 세그먼트 | Braze 커런츠 수출 |
| **Salesforce 마케팅 클라우드** | 데이터 확장 | SQL 쿼리 자동화 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## CEP별 데이터 요구 사항

{% tabs %}
{% tab Braze %}

### Braze 데이터 요구 사항

Braze 통합을 위해서는 Decisioning Studio Go가 필요합니다:

1. **Braze 커런츠**: 참여 데이터를 Decisioning Studio Go로 내보내려면 Braze 커런츠를 활성화하고 구성해야 합니다. 이를 통해 상담원은 고객의 응답을 통해 학습할 수 있습니다.

2. **세그먼트 액세스**: 생성하는 API 키에는 타겟 오디언스를 정의하는 세그먼트에 액세스할 수 있는 권한이 있어야 합니다.

3. **사용자 프로필 데이터**: 상담원이 고려할 고객 프로필 속성이나 커스텀 속성은 모두 Braze API를 통해 액세스할 수 있어야 합니다.

{% alert important %}
Braze 커런츠 내보내기에 비교하려는 모든 캠페인의 데이터가 포함되어 있는지 확인하세요(BAU 캠페인 포함).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC 데이터 요구 사항

Salesforce 마케팅 클라우드 통합을 위해서는 Decisioning Studio Go가 필요합니다:

1. **데이터 확장**: 오디언스는 Decisioning Studio Go가 액세스할 수 있는 데이터 확장에 정의되어 있어야 합니다. 구독자키를 기본 사용자 식별자로 사용합니다.
2. **이벤트 액세스 추적**: 설치된 앱 패키지가 엔드투엔드 자동화 설정을 지원하는 한, 추가 구성이 필요하지 않습니다. 

데이터 확장 및 SQL 쿼리는 [오케스트레이션 설정의]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) 일부로 구성됩니다.

{% endtab %}
{% endtabs %}

## Best practices

- **데이터를 최신 상태로 유지하세요**: 오디언스 세그먼트와 고객 데이터를 정기적으로(최소 매일) 업데이트하여 상담원이 최신 정보로 작업할 수 있도록 하세요.
- **관련 속성을 포함하세요**: 인구통계, 참여 이력, 구매 행동, 고객 생애주기 단계 등 어떤 고객 특성이 어떤 메시징에 영향을 미칠 수 있는지 생각해 보세요.

## 다음 단계

이제 Go가 데이터에 연결하는 방법을 이해했으니 CEP 통합 설정을 진행하세요:

- [오케스트레이션 설정하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

