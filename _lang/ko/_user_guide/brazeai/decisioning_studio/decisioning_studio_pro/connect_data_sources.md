---
nav_title: 데이터 소스 연결
article_title: 데이터 소스 연결
page_order: 1
description: "개인화된 AI 의사 결정을 위해 고객 데이터 소스를 BrazeAI Decisioning Studio Pro에 연결하는 방법을 알아보세요."
---

# 데이터 소스 연결

> 효과적인 의사 결정을 내리기 위해서는 BrazeAI Decisioning Studio™ Pro 상담원이 고객의 상황을 완전히 이해해야 합니다. 이 문서에서는 고객 데이터 소스를 Decisioning Studio Pro에 연결하는 방법에 대해 설명합니다.

{% alert tip %}
AI 의사 결정 서비스 팀이 최적의 성능/성과를 위한 데이터 연결을 구성할 수 있도록 지원합니다.
{% endalert %}

## 지원되는 통합 패턴

Decisioning Studio Pro는 고객 데이터 연결을 위한 다양한 통합 패턴을 지원합니다:

| 통합 패턴 | Best for | 설정 복잡성 |
|---------------------|----------|------------------|
| **Braze 데이터 플랫폼** | 이미 Braze를 사용 중인 고객 | 낮음 |
| **Braze 클라우드 데이터 수집(CDI)** | 외부 데이터 웨어하우스 연결 | 미디엄 |
| **클라우드 스토리지(GCS, AWS, Azure)** | 다른 플랫폼에서 직접 데이터 내보내기 | 미디엄 |
| **CEP 통합** | SFMC, 클라비요 데이터 확장 | 미디엄 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 고객 데이터 유형

다음 고객 데이터 자산은 상담원이 보다 효과적으로 개인화할 수 있도록 도와줍니다:

| 데이터 유형 | 설명 | 예시 |
|-----------|-------------|----------|
| **고객 프로필** | 정적이고 천천히 변화하는 기여도 속성 | 고객 연도, 지역, 획득 채널, 만족 수준, 생애주기 가치 추정치 |
| **고객 행동** | 활동 및 참여 패턴 | 계정 로그인, 기기 유형, 고객 서비스 상호 작용, 제품 사용량 |
| **트랜잭션 내역** | 구매 및 전환 데이터 | 구매한 제품, 트랜잭션 금액, 결제 방법, 구매 채널 |
| **마케팅 참여** | 커뮤니케이션에 대한 응답 | 이메일 열기/클릭, SMS 참여, 웹 및 모바일 활동, 설문조사 응답 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
상담원이 고객에 대해 더 많은 정보를 가지고 있을수록 더 나은 성능/성과를 낼 수 있습니다. 비즈니스에 특히 중요한 인사이트에 대한 데이터를 포함하는 것을 고려하세요(예: AI가 로열티 고객을 어떻게 다르게 대하는지 확인하고 싶으신가요?). 로열티 상태가 고객 데이터에 있는지 확인).
{% endalert %}

## 플랫폼별 데이터 연결

{% tabs %}
{% tab Braze %}

### Braze를 통해 고객 데이터 보내기

BrazeAI Decisioning Studio는 사용자가 이미 Braze 데이터 플랫폼으로 전송하고 있는 모든 데이터를 사용할 수 있습니다.

현재 사용자 프로필이나 커스텀 속성에 저장되어 있지 않은 Decisioning Studio에 사용하려는 고객 데이터가 있는 경우, 다른 소스에서 데이터를 수집하기 위해 [Braze 클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) 사용하는 것이 좋습니다.

CDI는 다음과 직접 통합을 지원합니다:

- Snowflake
- 레드쉬프트
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

지원되는 소스의 전체 목록은 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) 참조하세요.

Braze 데이터 플랫폼으로 전송하는 데이터가 만족스럽다면 AI 의사 결정 서비스 팀에 문의하여 AI 의사 결정에 사용할 사용자 프로필 또는 커스텀 속성의 필드에 대해 논의하세요.

이 프로세스를 간소화하려면 의사 결정 스튜디오에서 사용해야 하는 고객 행동을 가장 잘 대표한다고 생각되는 Braze 고객 프로필 속성 목록을 만드세요( [사용 가능한 필드 목록]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export) 참조). 또한 서비스 팀은 AI 의사 결정에 가장 적합한 분야를 결정하기 위한 디스커버리 세션을 진행할 수 있도록 도와드릴 수 있습니다.

데이터 전송을 위한 다른 옵션은 다음과 같습니다:

- 소프트웨어 개발 키트를 통해 Braze 커스텀 이벤트 보내기
- REST 엔드포인트를 사용하여 이벤트 보내기([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

이러한 패턴은 더 많은 엔지니어링 작업이 필요하지만 현재 Braze 커런츠 구성에 따라 선호되는 경우도 있습니다. 자세히 알아보려면 AI 의사 결정 서비스 팀에 문의하세요.

{% endtab %}
{% tab SFMC %}

### SFMC를 통한 고객 데이터 전송

Salesforce 마케팅 클라우드 통합의 경우:

1. 고객 데이터에 대한 SFMC 데이터 확장 구성
2. Decisioning Studio에 필요한 적절한 권한으로 API 통합을 위해 SFMC 설치 패키지를 설정합니다.
3. 의사 결정 스튜디오는 사용 가능한 최신 증분 데이터에서 가져오므로 데이터 확장을 매일 새로고침해야 합니다.

AI 의사 결정 서비스 팀에 확장 ID와 API 키를 제공하세요. 고객 데이터 수집의 다음 단계를 지원합니다.

{% endtab %}
{% tab Klaviyo %}

### 클라비요를 통해 고객 데이터 보내기

클라비요 통합의 경우:

1. 클라비요 프로필에서 고객 프로필 데이터를 사용할 수 있는지 확인합니다.
2. 프로필에 대한 전체 액세스 권한이 있는 비공개 API 키 생성하기
3. AI 의사 결정 서비스 팀에 API 키를 제공하세요.

API 키 설정에 대한 자세한 내용은 [클라비요 설명서를](https://help.klaviyo.com/hc/en-us/articles/115005237908) 참조하세요.

{% endtab %}
{% tab Cloud Storage %}

### 기타 클라우드 솔루션(Google Cloud Storage, Azure, AWS)

고객 데이터가 현재 Braze, SFMC 또는 Klaviyo에 저장되어 있지 않은 경우 차선책으로 자동화된 내보내기를 구성하여 Braze가 제어하는 Google Cloud Storage 버킷으로 직접 내보내도록 하는 것이 좋습니다. AWS 또는 Azure로 내보내기를 지원할 수도 있습니다(GCS가 더 좋지만). 이러한 플랫폼의 경우, 해당 클라우드 플랫폼의 내부 클라우드 스토리지로 내보내면 Braze에서 해당 데이터를 가져올 수 있습니다.

이것이 가능한지 확인하려면 사용 중인 마테크 플랫폼의 설명서를 참조하세요. For example:

- [Google Cloud Storage와 기본 통합을](https://www.mparticle.com/integration/google-cloud-storage/) 제공하는 mParticle
- [Twilio 세그먼트](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe 경험 플랫폼](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

이것이 가능한 경우 고객 데이터를 내보낼 수 있는 GCS 버킷을 제공하여 Decisioning Studio에 격리할 수 있습니다.

{% endtab %}
{% endtabs %}

## Best practices

- **설명이 포함된 열 이름입니다**: 고객 데이터에는 명확하고 설명적인 열 이름이 있어야 합니다. 이상적으로는 데이터 사전이 제공되어야 합니다.
- **점진적 업데이트**: 증분 파일은 매일 전체 고객 기록의 스냅샷보다 선호됩니다.
- **일관된 식별자**: 각 레코드에는 모든 데이터 자산에서 일관된 고유 고객 식별자가 포함되어야 합니다.
- **타임스탬프 포함**: 정확한 기여도 및 상담원 교육을 위해 기록에 관련 타임스탬프가 있어야 합니다.

## 커스텀 통합

다른 옵션이나 완전히 커스텀된 데이터 파이프라인도 가능합니다. 이러한 경우 팀의 추가 서비스 작업 또는 엔지니어링 작업이 필요할 수 있습니다. 실현 가능하고 최적의 방법을 결정하려면 AI 의사 결정 서비스 팀과 협력하세요.

{% alert important %}
이 가이드에서는 가장 일반적인 통합 패턴에 대해 설명합니다. 정보 보안팀은 여전히 모든 연결 지점을 검토해야 하며 솔루션 컨설턴트가 구현에 대한 조언을 제공할 수 있습니다.
{% endalert %}

## 다음 단계

데이터 소스를 연결한 후 오케스트레이션 설정을 진행합니다:

- [오케스트레이션 설정하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

