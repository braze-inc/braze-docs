---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "이 참조 문서에서는 모든 데이터와 사용자를 위해 특별히 빌드된 SQL 클라우드 데이터 웨어하우스인 Snowflake와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html)는 SaaS(software-as-a-service)로 제공되는 특별히 빌드된 SQL 클라우드 데이터 웨어하우스입니다. Snowflake는 기존 데이터 웨어하우스 제품보다 더 빠르고 사용하기 쉬우며 훨씬 더 유연한 데이터 웨어하우스를 제공합니다. 특허를 받은 Snowflake의 고유한 아키텍처를 사용하면 모든 데이터를 쉽게 수집하고, 신속한 분석을 가능하게 하며, 모든 사용자를 위한 데이터 중심 인사이트를 도출할 수 있습니다.

개인화된 관련 마케팅 캠페인에는 즉각적인 데이터 액세스가 필요합니다. 그것이 Braze가 Snowflake와 협력하여 데이터 공유를 시작한 이유입니다. 이 공동 제공을 통해 마케터는 고객 참여 및 캠페인 데이터의 잠재력을 그 어느 때보다 빠르게 활용할 수 있도록 합니다.

[Braze와 Snowflake 통합](https://www.braze.com/perspectives/article/snowflake-partner-announcement)은 Snowflake의 데이터 교환을 활용하여 존재감을 구축하고, 새로운 고객을 찾으며, 계속해서 성장하는 Snowflake 고객 기반을 통해 도달 범위를 확장합니다.

{% alert tip %}
**Snowflake 계정 없이 Snowflake 수준의 데이터에 액세스하는 데 관심이 있나요?**<br>[Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)을 확인하세요. 리더 계정을 사용하면 Braze에서 데이터를 생성하여 계정으로 공유하고 로그인하여 데이터에 액세스할 수 있는 자격 증명을 제공합니다. 이로 인해 모든 데이터 공유 및 사용 청구가 Braze에 의해 완전히 처리됩니다.
{% endalert %}

## 데이터 공유란 무엇입니까?

Snowflake의 [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) 기능을 사용하면 Braze가 일반적인 데이터 제공자 관계에서 발생하는 워크플로 마찰이나 지연, 실패 지점 및 불필요한 비용에 대해 걱정할 필요 없이 Snowflake 포털에서 데이터에 안전하게 액세스할 수 있습니다. 데이터 공유는 다음 통합 또는 [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)을 통해 설정할 수 있습니다.

- **인사이트로 시간 절약**<br>몇 주가 걸리던 ETL 프로세스와는 작별을 고하세요. Braze와 Snowflake의 독특한 아키텍처는 모든 고객 참여 및 캠페인 데이터를 데이터 레이크에 도착하는 즉시 접근 가능하고 쿼리할 수 있게 합니다. 데이터가 복사되거나 이동되지 않으므로 가장 관련성이 높고 최신 정보에 기반한 고객 경험을 제공할 수 있습니다.
- **데이터 사일로를 분해하다**<br>채널과 플랫폼 전반에 걸쳐 고객에 대한 전체적인 관점을 만드십시오. 데이터 공유로 어느 때보다 더 쉽게 다른 모든 Snowflake 데이터와 Braze 고객 참여 데이터를 결합하여, 신뢰할 수 있는 단일 소스에 기반하여 더 풍부한 인사이트를 창출합니다.
- **인게이지먼트의 누적 효과 확인**<br>Braze 벤치마크로 고객 참여 전략을 최적화하세요. 이 인터랙티브 도구는 Braze와 Snowflake에 의해 구동되며, 귀하의 브랜드 참여 데이터를 채널, 산업 및 기기 플랫폼 전반의 벤치마크와 비교할 수 있게 해줍니다.

데이터 공유를 통해 실제 데이터는 계정 간에 복사되거나 전송되지 않습니다. 모든 공유는 Snowflake의 고유한 서비스 계층 및 메타데이터 저장소를 통해 수행됩니다. 이것은 중요한 개념입니다. 공유된 데이터는 소비자 계정에 저장 공간을 차지하지 않으므로 소비자의 월간 데이터 스토리지 요금이 발생하지 않기 때문입니다. 소비자에게 부과되는 **유일한** 요금은 공유 데이터 쿼리에 사용되는 컴퓨팅 리소스(예: 가상 웨어하우스)에 대한 요금입니다.

또한, Snowflake의 내장된 역할 및 권한 기능을 사용하여 Braze에서 공유된 데이터에 대한 접근을 Snowflake 계정 및 그 안의 데이터에 대해 이미 설정된 접근 제어를 사용하여 제어하고 관리할 수 있습니다. 액세스는 사용자 데이터와 동일한 방식으로 제한되고 모니터링될 수 있습니다.

To learn more about Snowflake's data sharing, see [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## 전제 조건

Before you can use this feature, you'll need to complete the following:

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze access | To access this feature in Braze, you'll need to reach out to your Braze account or customer success manager. |
| Snowflake 계정 | A Snowflake account with `admin` permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Setting up Secure Data Sharing

For Snowflake, data sharing happens between a [data provider](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) and [data consumer](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Within this context, your Braze account is the data provider because it creates and sends the datashare—whereas your Snowflake account is the data consumer because it uses the datashare to create a database. For more details, see [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### 1단계: Send the datashare from Braze

1. In Braze, go to **Partner Integrations** > **Data Sharing**.
2. Enter your Snowflake account details and locator. To get your account locator, run `SELECT CURRENT_ACCOUNT()` in the destination account.
3. CRR 공유를 사용하는 경우 클라우드 제공자와 지역을 지정하십시오.
4. When you're finished, select **Create Datashare**. This will send the datashare to your Snowflake account.

### 2단계: Create the database in Snowflake

1. After a few minutes, you should receive the inbound datashare in your Snowflake acccount.
2. Using the inbound datashare, create a database to view and query the tables. For example:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Grant priviliges to query the new database.

{% alert warning %}
If you delete and recreate a share in the Braze dashboard, you must drop the previously-created database and recreate it using `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` to query the inbound share.
{% endalert %}

## 사용 및 시각화

After the data share is provisioned, you will need to create a database from the incoming data share, making all the tables shared appear in your Snowflake instance and be queryable just like any other data you're storing in your instance. 그러나 공유된 데이터는 읽기 전용이며 쿼리만 가능하고 수정하거나 삭제할 수 없습니다.

커런츠와 마찬가지로, Snowflake 보안 데이터 공유를 사용하여 다음을 수행할 수 있습니다.

- 복잡한 보고서 작성
- 기여도 모델링 수행
- 회사 내에서 보안 공유
- 원시 이벤트 또는 사용자 데이터를 CRM(예: Salesforce)에 매핑합니다
- 기타 등등

[여기에서 원시 테이블 스키마를 다운로드합니다.][schemas]

### 사용자 ID 스키마

Braze 및 Snowflake 사용자 ID 명명 규칙의 다음 차이점을 참고하십시오.

| Braze 스키마 | Snowflake 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze에서 자동으로 할당하는 고유 식별자. |
| `external_id` | `"EXTERNAL_USER_ID"` | 고객이 설정한 사용자의 프로필의 고유 식별자. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 중요한 정보 및 제한 사항

### 파괴적 변경 사항 및 비파괴적 변경 사항

#### 비파괴적 변경 사항

비파괴적 변경 사항은 언제든지 발생할 수 있으며 일반적으로 추가 기능을 제공합니다. 비파괴적 변경 사항의 예:
- 새 테이블 또는 뷰 추가
- 기존 테이블 또는 뷰에 열 추가하기

{% alert important %}
새 열은 비파괴적 변경으로 간주되므로 Braze는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 적극 권장합니다. 또는 열 이름을 명시적으로 지정하는 보기를 생성한 다음, 테이블을 직접 쿼리하는 대신 해당 보기를 쿼리할 수 있습니다.
{% endalert %}

#### 파괴적 변경 사항

가능한 경우, 파괴적 변경 사항은 공지와 마이그레이션 기간이 선행됩니다. 파괴적 변경 사항의 예:
- 테이블 또는 뷰 제거
- 기존 테이블 또는 뷰에서 열 제거하기
- 기존 열의 유형 또는 null 가능성을 변경

### Snowflake 리전

Braze는 현재 모든 사용자 수준 데이터를 Snowflake AWS US East-1 및 EU-Central(프랑크푸르트) 리전에 호스팅합니다. 해당 리전 외부의 사용자에 대해 Braze는 모든 AWS, Azure 또는 GCP 리전에서 Snowflake 인프라를 호스팅하는 공동 고객에게 데이터 공유를 제공할 수 있습니다.

### 데이터 보존

#### 보존 정책

2년이 넘는 모든 데이터는 아카이브되어 장기 스토리지로 이동됩니다. 아카이브 과정 중에 모든 이벤트는 익명화되고 모든 개인 식별 정보(PII) 민감 필드는 제거됩니다(여기에는 선택적으로 `properties` 같은 PII 필드가 포함됨). 아카이브된 데이터는 여전히 `user_id` 필드를 포함하며 모든 이벤트 데이터에서 사용자별 분석이 가능합니다.

해당되는 `USERS_*_SHARED` 보기에서 각 이벤트에 대한 최근 2년간의 데이터를 쿼리할 수 있습니다. 또한 각 이벤트에는 익명화된 데이터와 익명화되지 않은 데이터를 모두 반환하도록 쿼리할 수 있는 `USERS_*_SHARED_ALL` 보기가 있습니다.

#### 역사적 데이터

Snowflake의 과거 이벤트 데이터 아카이브는 2019년 4월로 거슬러 올라갑니다. Braze가 Snowflake에 데이터를 저장한 첫 몇 달 동안, 제품 변경이 발생하고 이로 인해 일부 데이터가 약간 다르게 보이거나 일부 null 값이 포함될 수 있습니다(이 시점에서는 사용 가능한 모든 필드에 데이터를 전달하지 않았기 때문임). 2019년 8월 이전의 데이터를 포함하는 결과는 예상과 약간 다를 수 있다고 가정하는 것이 좋습니다.

### 일반 데이터 보호 규정 (GDPR) 준수

Braze가 저장하는 거의 모든 이벤트 레코드에는 사용자의 개인 식별 정보(PII)를 나타내는 몇 가지 필드가 포함되어 있습니다. 일부 이벤트에는 이메일 주소, 전화번호, 기기 ID, 언어, 성별 및 위치 정보가 포함될 수 있습니다. 사용자가 Braze에 정보 지우기를 요청하면 해당 사용자에 속하는 이벤트에 대한 PII 필드를 무효화합니다. 이렇게 하면 이벤트의 과거 레코드를 제거하지 않지만 이제 이벤트를 특정 개인에게 다시 연결할 수 없습니다.

### 속도, 성능/성과, 쿼리 비용

데이터를 쿼리하는 데 사용하는 웨어하우스 크기에 따라 데이터에 대해 실행되는 모든 쿼리의 속도, 성능 및 비용이 결정됩니다. 일부 경우 분석을 위해 액세스하는 데이터의 양에 따라 쿼리가 성공적으로 실행되기 위해 더 큰 웨어하우스 크기를 사용해야 할 수도 있습니다. Snowflake는 [개요](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) 및 [창고 고려 사항](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)을 포함하여 어떤 크기를 사용할지 가장 잘 결정하는 방법에 대한 훌륭한 리소스를 제공합니다.

## Braze 벤치마크

Benchmarks, [a data tool built by Braze](https://www.braze.com/perspectives/benchmarks), allows Braze prospects and customers to see how they compare to top players in their industry by comparing their metrics against Braze industry benchmarks.

초기 산업에는 다음이 포함됩니다:

- 전달 서비스
- eCommerce
- 교육
- 엔터테인먼트
- 재무
- 게임
- 건강
- 라이프스타일
- 레스토랑
- 소매
- 기술
- 교통
- 여행

우리의 벤치마킹 데이터는 [Snowflake 데이터 교환](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR)에서 직접 사용할 수 있습니다.

> Snowflake 설정 시 참조할 예제 쿼리 세트를 보려면 [샘플 쿼리][SQ] 및 [ETL 이벤트 파이프라인 설정][ETL] 예제를 확인하세요.

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
