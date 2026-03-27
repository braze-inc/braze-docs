---
nav_title: "데이터 공유"
article_title: Snowflake 데이터 공유
page_order: 0
description: "이 참조 문서에서는 Snowflake 보안 데이터 공유 통합에 대해 다루며, 이를 통해 Snowflake 인스턴스에서 직접 Braze 참여 및 캠페인 데이터에 액세스할 수 있습니다."
page_type: partner
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake 데이터 공유

> Snowflake [보안 데이터 공유](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)를 사용하면 일반적인 데이터 공급자 관계에서 발생하는 워크플로 마찰이나 지연, 장애 지점, 불필요한 비용에 대한 걱정 없이 Braze가 Snowflake 포털의 데이터에 대한 안전한 액세스를 제공할 수 있습니다. 데이터 공유는 다음 통합을 통해 또는 [Snowflake 리더 계정]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)을 통해 설정할 수 있습니다.

{% alert tip %}
**Snowflake 계정 없이도 Snowflake 수준의 데이터에 액세스하고 싶으신가요?**<br>[Snowflake 리더 계정]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)을 확인해 보세요. 리더 계정을 사용하면 Braze가 계정을 생성하고 데이터를 공유하며, 로그인하여 데이터에 액세스할 수 있는 자격 증명을 제공합니다. 이 경우 모든 데이터 공유 및 사용 요금은 전적으로 Braze에서 처리합니다.
{% endalert %}

## 보안 데이터 공유 소개

데이터 공유에서는 실제 데이터가 계정 간에 복사되거나 전송되지 않습니다. 모든 공유는 Snowflake의 고유한 서비스 레이어와 메타데이터 저장소를 통해 이루어집니다. 이는 공유 데이터가 계정의 스토리지를 차지하지 않으므로 월별 데이터 스토리지 요금에 기여하지 않는다는 점에서 중요한 개념입니다. **유일한** 요금은 공유 데이터를 쿼리하는 데 사용되는 컴퓨팅 리소스(예: 가상 웨어하우스)에 대한 것입니다.

또한 Snowflake의 기본 제공 역할 및 권한 기능을 사용하면 Braze에서 공유된 데이터에 대한 액세스를 Snowflake 계정 및 해당 데이터에 이미 적용된 액세스 제어를 사용하여 제어하고 관리할 수 있습니다. 자체 데이터와 동일한 방식으로 액세스를 제한하고 모니터링할 수 있습니다.

- **인사이트 도출 시간 단축**<br>구축하는 데 몇 주가 걸리는 ETL 프로세스에 작별을 고하세요. Braze와 Snowflake의 고유한 아키텍처 덕분에 모든 고객 참여 및 캠페인 데이터가 데이터 레이크에 도착하는 즉시 액세스하고 쿼리할 수 있습니다. 데이터가 복사되거나 이동되지 않으므로 가장 관련성 높고 최신의 정보만을 기반으로 고객 경험을 제공할 수 있습니다.
- **데이터 사일로 해소**<br>채널과 플랫폼 전반에 걸쳐 고객에 대한 전체적인 뷰를 만드세요. 데이터 공유를 통해 Braze 고객 참여 데이터를 다른 모든 Snowflake 데이터와 결합하는 것이 그 어느 때보다 쉬워져, 단일하고 신뢰할 수 있는 소스에서 더 풍부한 인사이트를 얻을 수 있습니다.
- **참여 성과 비교**<br>Braze 벤치마크로 고객 참여 전략을 최적화하세요. Braze와 Snowflake가 제공하는 이 인터랙티브 도구를 사용하면 채널, 산업 및 기기 플랫폼 전반의 벤치마크와 브랜드의 참여 데이터를 비교할 수 있습니다.

Snowflake의 데이터 공유에 대해 자세히 알아보려면 [보안 데이터 공유 소개](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)를 참조하세요.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze 액세스 | 데이터 공유를 설정하려면 Braze 계정 또는 고객 성공 매니저에게 문의하세요. |
| Snowflake 계정 | `admin` 권한이 있는 Snowflake 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 보안 데이터 공유 설정

Snowflake에서 데이터 공유는 [데이터 공급자](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)와 [데이터 소비자](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) 간에 이루어집니다. 이 컨텍스트에서 Braze 계정은 데이터 공유를 생성하고 전송하는 데이터 공급자이며, Snowflake 계정은 데이터 공유를 사용하여 데이터베이스를 생성하는 데이터 소비자입니다. 자세한 내용은 [Snowflake: 공유 데이터 사용](https://docs.snowflake.com/en/user-guide/data-share-consumers)을 참조하세요.

### 1단계: Braze에서 데이터 공유 전송

1. Braze에서 **파트너 통합** > **데이터 공유**로 이동합니다.
2. Snowflake 계정 세부 정보와 로케이터를 입력합니다. 계정 로케이터를 가져오려면 대상 계정에서 `SELECT CURRENT_ACCOUNT()`를 실행하세요.
3. CRR 공유를 사용하는 경우 클라우드 공급자와 리전을 지정합니다.
4. 완료되면 **데이터 공유 생성**을 선택합니다. 그러면 Snowflake 계정으로 데이터 공유가 전송됩니다.

### 2단계: Snowflake에서 데이터베이스 생성

1. 몇 분 후 Snowflake 계정에서 인바운드 데이터 공유를 수신해야 합니다.
2. 인바운드 데이터 공유를 사용하여 테이블을 보고 쿼리할 데이터베이스를 생성합니다. 예시:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. 새 데이터베이스를 쿼리할 수 있는 권한을 부여합니다.

{% alert warning %}
Braze 대시보드에서 공유를 삭제하고 다시 생성하는 경우, 이전에 생성한 데이터베이스를 삭제하고 `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>`을 사용하여 다시 생성해야 인바운드 공유를 쿼리할 수 있습니다.
동일한 Snowflake 계정에 데이터를 공유하는 여러 워크스페이스가 있는 경우, 다중 워크스페이스 구성 관리에 대한 안내는 [Snowflake 데이터 공유 FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/)를 참조하세요.
{% endalert %}

## 사용 및 시각화

데이터 공유가 프로비저닝된 후 수신 데이터 공유에서 데이터베이스를 생성하면 공유된 모든 테이블이 Snowflake 인스턴스에 나타나며 인스턴스에 저장된 다른 데이터와 마찬가지로 쿼리할 수 있습니다. 다만 공유 데이터는 읽기 전용이며 쿼리만 가능하고 어떤 방식으로든 수정하거나 삭제할 수 없다는 점에 유의하세요.

커런츠와 마찬가지로 Snowflake 보안 데이터 공유를 사용하여 다음을 수행할 수 있습니다:

- 복잡한 보고서 생성
- 기여도 모델링 수행
- 회사 내 안전한 공유
- 원시 이벤트 또는 사용자 데이터를 CRM(예: Salesforce)에 매핑
- 기타 다양한 활용

[여기에서 원시 테이블 스키마를 다운로드하세요.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### 사용자 ID 스키마

사용자 ID에 대한 Braze와 Snowflake 명명 규칙의 다음 차이점에 유의하세요.

| Braze 스키마 | Snowflake 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze에서 자동으로 할당하는 고유 식별자입니다. |
| `external_id` | `"EXTERNAL_USER_ID"` | 고객이 설정한 사용자 프로필의 고유 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 중요 정보 및 제한 사항

### 호환성을 깨는 변경과 깨지 않는 변경

#### 호환성을 깨지 않는 변경

호환성을 깨지 않는 변경은 언제든지 발생할 수 있으며 일반적으로 추가 기능을 제공합니다. 호환성을 깨지 않는 변경의 예:
- 새 테이블 또는 뷰 추가
- 기존 테이블 또는 뷰에 열 추가

{% alert important %}
새 열은 호환성을 깨지 않는 변경으로 간주되므로, Braze는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 강력히 권장합니다. 또는 열을 명시적으로 지정하는 뷰를 생성한 다음 테이블 대신 해당 뷰를 쿼리할 수도 있습니다.
{% endalert %}

#### 호환성을 깨는 변경

가능한 경우 호환성을 깨는 변경에는 사전 공지와 마이그레이션 기간이 제공됩니다. 호환성을 깨는 변경의 예:
- 테이블 또는 뷰 제거
- 기존 테이블 또는 뷰에서 열 제거
- 기존 열의 유형 또는 null 허용 여부 변경

### Snowflake 리전

Braze는 현재 다음 Snowflake AWS 리전에서 모든 사용자 수준 데이터를 호스팅합니다:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)
 
해당 리전 외부의 사용자에 대해 Braze는 AWS, Azure 또는 GCP 리전에서 Snowflake 인프라를 호스팅하는 공동 고객에게 데이터 공유를 제공할 수 있습니다.

### 데이터 보존

#### 보존 정책

2년이 지난 데이터는 아카이브되어 장기 스토리지로 이동됩니다. 아카이브 프로세스의 일환으로 모든 이벤트가 익명화되고 개인 식별 정보(PII)에 해당하는 민감한 필드가 제거됩니다(여기에는 `properties`와 같은 선택적 PII 필드도 포함됩니다). 아카이브된 데이터에는 여전히 `user_id` 필드가 포함되어 있어 모든 이벤트 데이터에 대한 사용자별 분석이 가능합니다.

각 이벤트에 대해 해당 `USERS_*_SHARED` 뷰에서 최근 2년간의 데이터를 쿼리할 수 있습니다. 또한 각 이벤트에는 익명화된 데이터와 익명화되지 않은 데이터를 모두 반환하는 `USERS_*_SHARED_ALL` 뷰가 있습니다.

#### 과거 데이터

Snowflake의 과거 이벤트 데이터 아카이브는 2019년 4월까지 거슬러 올라갑니다. Braze가 Snowflake에 데이터를 저장하기 시작한 초기 몇 달 동안 제품 변경이 이루어져 일부 데이터가 약간 다르게 보이거나 일부 null 값이 있을 수 있습니다(당시 모든 사용 가능한 필드에 데이터를 전달하지 않았기 때문입니다). 2019년 8월 이전의 데이터를 포함하는 결과는 예상과 약간 다를 수 있다고 가정하는 것이 좋습니다.

### 일반 데이터 보호 규정(GDPR) 준수

{% include partners/snowflake_pii_gdpr.md %}

### 쿼리 속도, 성능 및 비용

데이터에 대해 실행하는 쿼리의 속도, 성능 및 비용은 데이터를 쿼리하는 데 사용하는 웨어하우스 크기에 따라 결정됩니다. 경우에 따라 분석을 위해 액세스하는 데이터 양에 따라 쿼리가 성공하려면 더 큰 웨어하우스 크기를 사용해야 할 수 있습니다. Snowflake는 [웨어하우스 개요](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) 및 [웨어하우스 고려 사항](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)을 포함하여 적절한 크기를 결정하는 방법에 대한 훌륭한 리소스를 제공합니다.

{% alert tip %}
Snowflake 설정 시 참조할 수 있는 예제 쿼리 세트는 [샘플 쿼리]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries/) 및 [ETL 이벤트 파이프라인 설정]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup/) 예제를 확인하세요.
{% endalert %}