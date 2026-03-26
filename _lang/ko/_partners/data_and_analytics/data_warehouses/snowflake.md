---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "이 문서에서는 데이터 공유(Braze에서 Snowflake로)와 클라우드 데이터 수집(Snowflake에서 Braze로)을 포함하여 Braze와 Snowflake 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html)는 SaaS(software-as-a-service)로 제공되는 전용 SQL 클라우드 데이터 웨어하우스입니다. Snowflake는 기존 데이터 웨어하우스 제품보다 더 빠르고, 사용하기 쉬우며, 훨씬 유연한 데이터 웨어하우스를 제공합니다. Snowflake의 고유하고 특허받은 아키텍처를 통해 모든 데이터를 쉽게 수집하고, 빠른 분석을 수행하며, 모든 사용자를 위한 데이터 중심 인사이트를 도출할 수 있습니다.

Braze는 Snowflake와 두 가지 통합을 제공합니다. 이 두 가지를 함께 사용하면 Braze와 Snowflake 환경 간에 완전한 양방향 데이터 파이프라인을 구축할 수 있습니다.

## 통합 선택

### 데이터 공유 (Braze에서 Snowflake로)

Snowflake [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/)을 사용하면 Snowflake 인스턴스에서 직접 Braze 참여 및 캠페인 데이터에 안전하게 실시간으로 접근할 수 있습니다. 계정 간에 데이터가 복사되거나 전송되지 않으며, 모든 공유는 Snowflake의 고유한 서비스 레이어와 메타데이터 저장소를 통해 이루어집니다.

**데이터 공유를 사용하면 좋은 경우:**
- Snowflake SQL을 사용하여 Braze 이벤트 및 캠페인 데이터를 쿼리하고 싶을 때
- 복잡한 보고서를 생성하고 기여도 모델링을 수행하고 싶을 때
- Braze 데이터를 Snowflake 웨어하우스의 다른 데이터와 결합하고 싶을 때
- 채널, 산업, 기기 플랫폼 전반에 걸쳐 참여 데이터를 벤치마크하고 싶을 때

설정 방법은 [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/)를 참조하세요.

### 클라우드 데이터 수집 (Snowflake에서 Braze로)

[클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)을 사용하면 Snowflake 인스턴스의 데이터를 Braze로 직접 동기화할 수 있습니다. 이를 통해 Braze의 사용자 속성, 이벤트, 구매 데이터를 신뢰할 수 있는 소스인 데이터 웨어하우스와 최신 상태로 유지할 수 있습니다.

**클라우드 데이터 수집을 사용하면 좋은 경우:**
- Snowflake의 사용자 속성을 Braze 고객 프로필에 동기화하고 싶을 때
- Snowflake의 이벤트 또는 구매 데이터를 Braze로 전송하고 싶을 때
- 웨어하우스에서 발생하는 데이터 변환과 Braze를 동기화 상태로 유지하고 싶을 때
- Snowflake에서 Braze로의 커스텀 ETL 파이프라인 구축 및 유지 관리를 피하고 싶을 때

Snowflake의 데이터 공유에 대해 자세히 알아보려면 [Secure Data Sharing 소개](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)를 참조하세요.

## 필수 조건

이 기능을 사용하기 전에 다음을 완료해야 합니다:

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze 접근 권한 | Braze에서 이 기능에 접근하려면 Braze 계정 매니저 또는 고객 성공 매니저에게 문의해야 합니다. |
| Snowflake 계정 | `admin` 권한이 있는 Snowflake 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Secure Data Sharing 설정

Snowflake에서 데이터 공유는 [데이터 공급자](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)와 [데이터 소비자](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) 간에 이루어집니다. 이 컨텍스트에서 Braze 계정은 데이터 공유를 생성하고 전송하는 데이터 공급자이며&#8212;Snowflake 계정은 데이터 공유를 사용하여 데이터베이스를 생성하는 데이터 소비자입니다. 자세한 내용은 [Snowflake: 공유 데이터 사용](https://docs.snowflake.com/en/user-guide/data-share-consumers)을 참조하세요.

### 1단계: Braze에서 데이터 공유 전송

1. Braze에서 **파트너 통합** > **데이터 공유**로 이동합니다.
2. Snowflake 계정 세부 정보와 로케이터를 입력합니다. 계정 로케이터를 얻으려면 대상 계정에서 `SELECT CURRENT_ACCOUNT()`를 실행하세요.
3. CRR 공유를 사용하는 경우 클라우드 공급자와 리전을 지정합니다.
4. 완료되면 **데이터 공유 생성**을 선택합니다. 그러면 데이터 공유가 Snowflake 계정으로 전송됩니다.

### 2단계: Snowflake에서 데이터베이스 생성

1. 몇 분 후, 인바운드 데이터 공유가 Snowflake 계정에 수신됩니다.
2. 인바운드 데이터 공유를 사용하여 테이블을 조회하고 쿼리할 데이터베이스를 생성합니다. 예시:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. 새 데이터베이스를 쿼리할 수 있는 권한을 부여합니다.

{% alert warning %}
Braze 대시보드에서 공유를 삭제하고 다시 생성하는 경우, 이전에 생성한 데이터베이스를 삭제하고 `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>`을 사용하여 다시 생성해야 인바운드 공유를 쿼리할 수 있습니다.
여러 워크스페이스가 동일한 Snowflake 계정으로 데이터를 공유하는 경우, 다중 워크스페이스 구성 관리에 대한 안내는 [Snowflake 데이터 공유 FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/)를 참조하세요.
{% endalert %}

## 사용 및 시각화

데이터 공유가 프로비저닝된 후, 수신 데이터 공유에서 데이터베이스를 생성해야 합니다. 그러면 공유된 모든 테이블이 Snowflake 인스턴스에 나타나며, 인스턴스에 저장된 다른 데이터와 마찬가지로 쿼리할 수 있습니다. 다만, 공유 데이터는 읽기 전용이며 쿼리만 가능하고 어떤 방식으로도 수정하거나 삭제할 수 없다는 점을 유의하세요.

커런츠와 마찬가지로, Snowflake Secure Data Sharing을 사용하여 다음을 수행할 수 있습니다:

- 복잡한 보고서 생성
- 기여도 모델링 수행
- 회사 내 안전한 공유
- 원시 이벤트 또는 사용자 데이터를 CRM(예: Salesforce)에 매핑
- 기타 다양한 활용

사용 가능한 테이블 및 열의 전체 목록은 [SQL 테이블 참조]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)를 참조하세요. Snowflake 데이터 공유에는 해당 참조의 모든 테이블과 스냅샷, 캠페인 및 Canvas 체인지로그, 에이전트 콘솔 이벤트, 메시지 재시도 이벤트에 대한 추가 Snowflake 전용 테이블이 포함됩니다.

[원시 테이블 스키마를 다운로드]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})하여 텍스트 파일로 확인할 수도 있습니다.

### 사용자 ID 스키마

사용자 ID에 대한 Braze와 Snowflake 명명 규칙의 다음 차이점에 유의하세요.

| Braze 스키마 | Snowflake 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze에서 자동으로 할당하는 고유 식별자입니다. |
| `external_id` | `"EXTERNAL_USER_ID"` | 고객이 설정하는 고객 프로필의 고유 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 중요 정보 및 제한 사항

### 호환성을 깨는 변경과 깨지 않는 변경

#### 호환성을 깨지 않는 변경

호환성을 깨지 않는 변경은 언제든지 발생할 수 있으며, 일반적으로 추가 기능을 제공합니다. 호환성을 깨지 않는 변경의 예시:
- 새 테이블 또는 뷰 추가
- 기존 테이블 또는 뷰에 열 추가

{% alert important %}
새 열은 호환성을 깨지 않는 변경으로 간주되므로, Braze는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 강력히 권장합니다. 또는 열을 명시적으로 지정하는 뷰를 생성한 다음 테이블 대신 해당 뷰를 쿼리하는 것도 좋은 방법입니다.
{% endalert %}

#### 호환성을 깨는 변경

가능한 경우, 호환성을 깨는 변경은 사전 공지와 마이그레이션 기간이 선행됩니다. 호환성을 깨는 변경의 예시:
- 테이블 또는 뷰 제거
- 기존 테이블 또는 뷰에서 열 제거
- 기존 열의 유형 또는 null 허용 여부 변경

### Snowflake 리전

Braze는 현재 Snowflake AWS 미국 동부-1, 유럽 중부(프랑크푸르트), AP 동남부-2(시드니), AP 동남부-3(자카르타) 리전에서 모든 사용자 수준 데이터를 호스팅하고 있습니다. 해당 리전 외부의 사용자에 대해서는, Braze가 AWS, Azure 또는 GCP 리전에서 Snowflake 인프라를 호스팅하는 공동 고객에게 데이터 공유를 제공할 수 있습니다.

### 데이터 보존

#### 보존 정책

2년이 지난 데이터는 아카이브되어 장기 스토리지로 이동됩니다. 아카이브 프로세스의 일환으로 모든 이벤트가 익명화되며, 개인 식별 정보(PII) 민감 필드가 제거됩니다(`properties`와 같은 선택적 PII 필드 포함). 아카이브된 데이터에는 여전히 `user_id` 필드가 포함되어 있어 모든 이벤트 데이터에 대한 사용자별 분석이 가능합니다.

각 이벤트에 대해 해당 `USERS_*_SHARED` 뷰에서 최근 2년간의 데이터를 쿼리할 수 있습니다. 또한 각 이벤트에는 익명화된 데이터와 익명화되지 않은 데이터를 모두 반환하도록 쿼리할 수 있는 `USERS_*_SHARED_ALL` 뷰가 있습니다.

#### 과거 데이터

Snowflake의 과거 이벤트 데이터 아카이브는 2019년 4월까지 거슬러 올라갑니다. Braze가 Snowflake에 데이터를 저장하기 시작한 초기 몇 달 동안 제품 변경이 이루어져, 일부 데이터가 약간 다르게 보이거나 null 값이 있을 수 있습니다(당시 모든 사용 가능한 필드에 데이터를 전달하지 않았기 때문입니다). 2019년 8월 이전의 데이터를 포함하는 결과는 예상과 약간 다를 수 있다고 가정하는 것이 좋습니다.

### 일반 데이터 보호 규정(GDPR) 준수

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### 쿼리 속도, 성능, 비용

데이터에 대해 실행하는 모든 쿼리의 속도, 성능 및 비용은 데이터를 쿼리하는 데 사용하는 웨어하우스 크기에 따라 결정됩니다. 경우에 따라 분석을 위해 접근하는 데이터 양에 따라 쿼리가 성공하려면 더 큰 웨어하우스 크기를 사용해야 할 수 있습니다. Snowflake는 [웨어하우스 개요](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) 및 [웨어하우스 고려 사항](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)을 포함하여 최적의 크기를 결정하는 방법에 대한 훌륭한 리소스를 제공합니다.

> Snowflake 설정 시 참조할 수 있는 예시 쿼리 세트는 [샘플 쿼리]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) 및 [ETL 이벤트 파이프라인 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/) 예시를 확인하세요.

설정 방법은 [클라우드 데이터 수집: 데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)을 참조하세요.