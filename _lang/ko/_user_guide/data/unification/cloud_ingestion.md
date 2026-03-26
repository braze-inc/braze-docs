---
nav_title: 클라우드 데이터 수집
article_title: Braze 클라우드 데이터 수집
alias: /cloud_ingestion/
description: "이 참조 문서에서는 Braze 클라우드 데이터 수집 소스 및 데이터 설정 권장 사항을 다룹니다."
page_order: 0.1
toc_headers: h2
---

# Braze 클라우드 데이터 수집

> Braze Cloud 데이터 수집(CDI)은 데이터 저장 솔루션에서 Braze로 관련 사용자 데이터 및 기타 비사용자 데이터를 동기화하기 위한 직접 연결을 설정할 수 있게 해줍니다. 이 데이터는 개인화 또는 세분화를 위해 사용되어 마케팅 사용 사례를 지원할 수 있습니다. Cloud 데이터 수집의 유연한 통합은 중첩된 JSON 및 객체 배열을 포함한 복잡한 데이터 구조를 지원합니다.

## 작동 방식

Braze 클라우드 데이터 수집(CDI)을 사용하면 데이터 웨어하우스 인스턴스와 Braze 워크스페이스 간의 통합을 설정하여 데이터를 정기적으로 동기화할 수 있습니다. 이 동기화는 사용자가 설정한 일정에 따라 실행되며, 각 통합은 다른 일정을 가질 수 있습니다. 동기화는 15분마다 자주 실행되거나 한 달에 한 번씩 드물게 실행될 수 있습니다. 15분보다 더 자주 동기화를 수행해야 하는 경우에는 고객 성공 관리자에게 문의하거나 실시간 데이터 수집을 위해 REST API 호출을 사용하는 것을 고려하세요.

동기화가 실행되면 Braze는 데이터 웨어하우스 인스턴스에 직접 연결하여 지정된 테이블에서 모든 새 데이터를 검색하고 Braze 대시보드에서 해당 데이터를 업데이트합니다. 동기화가 실행될 때마다 업데이트된 데이터가 Braze에 반영됩니다.

### 통합 ID 찾기

Braze 대시보드에서 통합을 볼 때 URL에서 통합 ID를 찾을 수 있습니다. **데이터 설정** > **Cloud 데이터 수집**로 이동하여 통합을 선택합니다. 통합 ID는 `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]` 형식의 URL에 나타납니다. 예를 들어, URL이 `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`인 경우 통합 ID는 `abc123xyz`입니다. API 호출을 할 때 이 ID를 사용하여 동기화를 트리거하거나 동기화 상태를 확인할 수 있습니다.

## 사용 사례

Braze Cloud 데이터 수집 기능을 사용하면:

- 몇 분안에 데이터 웨어하우스 또는 파일 스토리지 솔루션에서 Braze로 직접 단순 통합을 생성합니다.
- 데이터 웨어하우스에서 Braze로 사용자 데이터(속성, 이벤트 및 구매 포함)를 안전하게 동기화할 수 있습니다.
- Cloud 데이터 수집을 Currents 또는 Snowflake 데이터 공유와 결합하여 Braze와 데이터 루프를 닫을 수 있습니다.

또한, [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)는 제로 복사 대안입니다. Braze가 데이터 웨어하우스 또는 파일 저장 솔루션을 직접 쿼리하여 CDI 세그먼트를 구성할 수 있습니다. — 모든 기본 데이터를 Braze로 복사하지 않고도 가능합니다.

## 지원되는 데이터 소스

Cloud 데이터 수집은 다음에서 데이터를 동기화할 수 있습니다:

   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## 지원되는 데이터 유형 

클라우드 데이터 수집은 다음 데이터 유형을 지원합니다.

### 사용자 데이터
- 사용자 속성, 포함:
   - 중첩된 커스텀 속성
   - 객체 배열
   - 구독 상태
- 사용자 지정 이벤트
- 구매 이벤트
- 사용자 삭제 요청

### 비사용자 객체
- 카탈로그 항목

### 제로 복사 메시징
- 연결된 소스

## 데이터 수집을 위한 사용자 식별자

Cloud Data Ingestion을 통해 사용자 데이터를 동기화할 때, 다음 식별자 유형 중 하나 이상을 사용하여 사용자를 식별할 수 있습니다. 소스 테이블의 각 행은 한 번에 하나의 식별자 유형에 대한 값만 포함해야 하지만, 테이블에는 하나, 둘, 셋, 넷 또는 모든 다섯 개의 식별자 유형에 대한 열을 포함할 수 있습니다.

| 식별자 | 설명 |
|------------|-------------|
| `EXTERNAL_ID` | 생성하거나 업데이트할 사용자 프로필을 식별하는 외부 ID입니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. |
| `ALIAS_NAME` and `ALIAS_LABEL` | `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정해야 하며, 이 두 열은 사용자 별칭 개체를 만듭니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
| `BRAZE_ID` | Braze SDK에 의해 생성된 Braze 사용자 식별자입니다. 새 사용자는 Cloud Data Ingestion을 통해 Braze ID를 사용하여 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다. |
| `EMAIL` | 사용자의 이메일 주소입니다. 같은 이메일 주소를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트를 위해 우선시됩니다. 이메일과 전화번호를 모두 포함하는 경우, 이메일이 기본 식별자로 사용됩니다. |
| `PHONE` | 사용자의 전화번호입니다. 같은 전화번호를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트를 위해 우선시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 식별자를 사용하여 테이블을 설정하는 방법에 대한 자세한 정보는 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) 설명서를 참조하십시오.

## 데이터 포인트 사용량

데이터 포인트 기반 청구를 사용하는 고객의 경우, Cloud Data Ingestion에 대한 데이터 포인트 청구는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)를 통한 업데이트에 대한 청구와 동일합니다. [데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)에 대한 자세한 내용은 참조하세요. 

{% alert important %}
Braze 클라우드 데이터 수집은 사용 가능한 속도 제한에 포함되므로 다른 방법으로 데이터를 전송하는 경우 Braze API와 클라우드 데이터 수집 간에 사용량 제한이 결합됩니다.
{% endalert %}

## 제품 제한

| Limitation            | 설명                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 통합 수 | 통합 설정의 수에는 제한이 없습니다. 그러나 테이블이나 뷰당 하나의 통합만 설정할 수 있습니다.                                             |
| 행 수         | By default, each run can sync up to 500 million rows. 500백만 개 이상의 새 행이 포함된 모든 동기화는 중단됩니다. If you need a higher limit than this, contact your Braze customer success manager or Braze Support. |
| 행별 속성     | 각 행에는 단일 사용자 ID와 최대 250개의 속성을 포함하는 JSON 객체가 포함되어야 합니다. JSON 객체의 각 키는 하나의 속성으로 간주됩니다 (즉, 배열은 하나의 속성으로 간주됩니다). |
| 페이로드 크기           | 각 행에는 최대 1MB의 페이로드가 포함될 수 있습니다. 1MB를 초과하는 페이로드는 거부되며, "페이로드가 1MB를 초과했습니다"라는 오류가 동기화 로그에 기록되고 관련된 외부 ID 및 잘린 페이로드와 함께 기록됩니다. |
| 데이터 유형              | 클라우드 데이터 수집을 통해 사용자 속성, 이벤트 및 구매를 동기화할 수 있습니다.                                                                                                  |
| Braze 지역           | 이 제품은 모든 Braze 지역에서 사용할 수 있습니다. 어떤 Braze 지역이든 어떤 소스 데이터 지역에든 연결할 수 있습니다.                                                                              |
| 출처 지역       | Braze는 모든 지역 또는 클라우드 제공자의 데이터 웨어하우스 또는 클라우드 환경에 연결됩니다.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
