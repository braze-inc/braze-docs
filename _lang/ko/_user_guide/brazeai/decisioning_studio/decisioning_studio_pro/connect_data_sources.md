---
nav_title: 데이터 소스 연결
article_title: 데이터 소스 연결
page_order: 1
description: "고객 데이터 소스를 BrazeAI Decisioning Studio Pro에 연결하여 개인화된 AI 의사 결정을 수행하는 방법을 배우십시오."
---

# 데이터 소스 연결

> BrazeAI Decisioning Studio™ Pro 에이전트는 효과적인 결정을 내리기 위해 고객 컨텍스트를 완전히 이해해야 합니다. 이 문서에서는 고객 데이터 소스를 Decisioning Studio Pro에 연결하는 방법을 설명합니다.

{% alert tip %}
AI 의사 결정 서비스 팀이 최적의 성능을 위한 데이터 연결 구성에서 지원합니다.
{% endalert %}

## 지원되는 통합 패턴

Decisioning Studio Pro는 고객 데이터를 연결하기 위한 여러 통합 패턴을 지원합니다:

| 통합 패턴 | Best for | 설정 복잡성 |
|---------------------|----------|------------------|
| **Braze 데이터 플랫폼** | 이미 Braze를 사용하고 있는 고객 | 낮음 |
| **Braze 클라우드 데이터 수집 (CDI)** | 외부 데이터 웨어하우스 연결 | 미디엄 |
| **클라우드 스토리지 (GCS, AWS, Azure)** | 다른 플랫폼에서의 직접 데이터 내보내기 | 미디엄 |
| **CEP 통합** | SFMC, Klaviyo 데이터 확장 | 미디엄 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 고객 데이터 유형

다음의 고객 데이터 자산은 에이전트가 더 효과적으로 개인화하는 데 도움을 줍니다:

| 데이터 유형 | 설명 | 예시 |
|-----------|-------------|----------|
| **고객 프로필** | 정적이고 천천히 변화하는 속성 | 고객으로서의 연수, 지리, 획득 채널, 만족도, 생애주기 가치 추정 |
| **고객 행동** | 활동 및 참여 패턴 | 계정 로그인, 기기 유형, 고객 서비스 상호작용, 제품 사용 |
| **트랜잭션 기록** | 구매 및 전환 데이터 | 구매한 제품, 트랜잭션 금액, 결제 방법, 구매 채널 |
| **마케팅 참여** | 커뮤니케이션에 대한 응답 | 이메일 열기/클릭, SMS 참여, 웹 및 모바일 활동, 설문조사 응답 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
에이전트가 고객에 대한 정보를 많이 가질수록 더 잘 수행할 것입니다. 비즈니스에 특히 중요한 통찰력에 대한 데이터를 포함하는 것을 고려하세요 (예를 들어, AI가 로열티 고객을 다르게 대하는 방식을 보고 싶으신가요?) 로열티 상태가 고객 데이터에 포함되어 있는지 확인하세요).
{% endalert %}

## 플랫폼별 데이터 연결

{% tabs %}
{% tab Braze %}

### Braze를 통해 고객 데이터 전송

BrazeAI 의사결정 스튜디오는 이미 Braze 데이터 플랫폼에 전송하고 있는 모든 데이터를 사용할 수 있습니다.

의사결정 스튜디오에서 사용하고 싶은 고객 데이터가 현재 사용자 프로필이나 커스텀 속성에 저장되어 있지 않은 경우, 추천하는 접근 방식은 [Braze 클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 사용하여 다른 출처에서 데이터를 수집하는 것입니다.

CDI는 다음과 같은 직접 통합을 지원합니다:

- Snowflake
- Redshift
- 빅쿼리
- Databricks
- Microsoft Fabric
- AWS S3

지원되는 소스의 전체 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 참조하십시오.

Braze 데이터 플랫폼에 전송할 데이터에 만족하면, AI 의사결정 서비스 팀에 연락하여 사용자 프로필 또는 커스텀 속성에서 어떤 필드를 AI 의사결정에 사용할지 논의하십시오.

이 프로세스를 간소화하기 위해, 의사결정 스튜디오에서 사용해야 할 고객 행동을 가장 잘 나타내는 Braze 사용자 프로필 속성 목록을 작성하십시오(사용 가능한 필드 목록은 [여기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)을 참조하십시오). 귀하의 서비스 팀은 AI 의사결정에 가장 적합한 필드를 결정하기 위한 탐색 세션을 진행하는 데 도움을 줄 수 있습니다.

데이터를 전송하는 다른 옵션은 다음과 같습니다:

- SDK를 통해 Braze 커스텀 이벤트 전송
- REST 엔드포인트([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))를 사용하여 이벤트 전송

이러한 패턴은 더 많은 엔지니어링 노력이 필요하지만, 현재 Braze 구성에 따라 때때로 더 바람직할 수 있습니다. AI 의사결정 서비스 팀에 연락하여 자세한 내용을 알아보십시오.

{% endtab %}
{% tab SFMC %}

### SFMC를 통해 고객 데이터 전송

세일즈포스 마케팅 클라우드 통합의 경우:

1. 고객 데이터를 위한 SFMC 데이터 확장 구성
2. 의사결정 스튜디오에서 필요한 적절한 권한으로 API 통합을 위한 SFMC 설치 패키지 설정
3. 데이터 확장이 매일 새로 고쳐지도록 하십시오. 의사결정 스튜디오는 최신 증분 데이터에서 가져옵니다.

확장 ID와 API 키를 AI 의사결정 서비스 팀에 제공하십시오. 그들은 고객 데이터 수집의 다음 단계에 도움을 줄 것입니다.

{% endtab %}
{% tab Klaviyo %}

### 클라비요를 통해 고객 데이터 전송

클라비요 통합의 경우:

1. 클라비요 프로필에서 고객 프로필 데이터가 사용 가능한지 확인하십시오.
2. 전체 액세스 권한이 있는 개인 API 키를 생성하십시오.
3. AI 의사 결정 서비스 팀에 API 키를 제공하십시오.

API 키 설정에 대한 자세한 내용은 [Klaviyo 설명서](https://help.klaviyo.com/hc/en-us/articles/115005237908)를 참조하십시오.

{% endtab %}
{% tab Cloud Storage %}

### 기타 클라우드 솔루션 (Google Cloud Storage, Azure, AWS)

고객 데이터가 현재 Braze, SFMC 또는 Klaviyo에 저장되어 있지 않은 경우, 다음 단계는 Braze가 제어하는 Google Cloud Storage 버킷으로 자동 내보내기를 구성하는 것입니다. AWS 또는 Azure로의 내보내기도 지원할 수 있습니다 (GCS가 더 바람직하지만). 이 플랫폼의 경우, 해당 클라우드 플랫폼의 내부 클라우드 스토리지로 내보내고 Braze가 그 데이터를 가져올 수 있습니다.

이것이 가능한지 확인하려면 Martech 플랫폼의 설명서를 참조하십시오. For example:

- mParticle은 [Google Cloud Storage와의 네이티브 통합](https://www.mparticle.com/integration/google-cloud-storage/)을 제공합니다.
- [Twilio 세그먼트](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

이것이 가능하다면, 의사 결정 스튜디오에 격리된 고객 데이터 내보내기를 위한 GCS 버킷을 제공할 수 있습니다.

{% endtab %}
{% endtabs %}

## Best practices

- **설명적인 열 이름**: 고객 데이터는 명확하고 설명적인 열 이름을 가져야 합니다. 이상적으로는 데이터 사전이 제공되어야 합니다.
- **증분 업데이트**: 증분 파일이 매일 전체 고객 기록의 스냅샷보다 바람직합니다.
- **일관된 식별자**: 각 레코드는 모든 데이터 자산에서 일관된 고유 고객 식별자를 포함해야 합니다.
- **타임스탬프 포함**: 기록에는 정확한 기여도와 에이전트 교육을 위한 관련 타임스탬프가 있어야 합니다.

## 커스텀 통합

다른 옵션이나 완전히 커스텀 데이터 파이프라인도 가능합니다. 이것은 귀하의 팀에서 추가 서비스 작업이나 엔지니어링 작업이 필요할 수 있습니다. 무엇이 실행 가능하고 최적인지 결정하기 위해 AI 의사결정 서비스 팀과 협력하십시오.

{% alert important %}
이 가이드는 가장 일반적인 통합 패턴을 설명합니다. 정보 보안은 여전히 모든 연결 지점을 검토해야 하며 솔루션 컨설턴트가 구현에 대해 조언할 수 있습니다.
{% endalert %}

## 다음 단계

데이터 소스를 연결한 후 오케스트레이션 설정을 진행하십시오:

- [오케스트레이션 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

