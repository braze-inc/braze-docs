---
nav_title: CDI로 사용자 삭제
article_title: 클라우드 데이터 수집으로 사용자 삭제하기
page_order: 30
page_type: reference
description: "이 페이지에서는 클라우드 데이터 수집을 통해 사용자를 삭제하는 프로세스에 대한 개요를 제공합니다."

---

# 클라우드 데이터 수집으로 사용자 삭제하기

> 이 페이지에서는 클라우드 데이터 수집을 통해 사용자를 삭제하는 프로세스에 대해 설명합니다.

사용자 삭제 동기화는 사용 가능한 모든 클라우드 데이터 수집 데이터 소스에 대해 지원됩니다. 

## 통합 구성하기 

표준 프로세스에 따라 연결하려는 데이터 웨어하우스에 대해 [Braze 대시보드에서 새 통합을 생성하세요]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 삭제 테이블에 액세스할 수 있는 역할을 포함해야 합니다. 사용자 **가져오기 동기화 만들기** 페이지에서 **데이터 유형을** **사용자 삭제로** 설정하여 통합 실행 중에 적절한 조치를 취하여 사용자를 삭제할 수 있도록 합니다.

\![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## 소스 데이터 구성하기

사용자 삭제에 대한 소스 테이블에는 하나 이상의 사용자 식별자 유형과 `UPDATED_AT` 타임스탬프가 포함되어야 합니다. 페이로드 열은 사용자 삭제 데이터에 대해 지원되지 않습니다.

### `UPDATED_AT`

소스 테이블에 `UPDATED_AT` 타임스탬프를 추가합니다. 이 타임스탬프는 이 행이 테이블에 업데이트되거나 추가된 시간을 나타냅니다. Braze는 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화합니다.

### 사용자 식별자 열

테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 `external_id`, `alias_name` 과 `alias_label` 의 조합 또는 `braze_id` 중 하나의 식별자만 포함해야 합니다. 소스 테이블에는 하나, 둘 또는 세 가지 식별자 유형 모두에 대한 열이 포함될 수 있습니다.
- `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. 
- `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정합니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 은 하나만 지정할 수 있습니다.
- `BRAZE_ID` - Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며 클라우드 데이터 수집을 통해 신규 사용자를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다. 

{% alert important %}
사용자 제거를 위해 테이블에 `PAYLOAD` 열을 포함하지 마세요. 사용자의 우발적이고 영구적인 제거를 방지하기 위해 소스 테이블에 페이로드 열이 제공되면 동기화가 실패합니다. 다른 열은 허용되지만 Braze에서는 무시됩니다.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```json
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
다음 필드가 포함된 테이블을 만듭니다:

| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| 타임스탬프 | 필수 |
| `EXTERNAL_ID`| 문자열 | NULLABLE |
| `ALIAS_NAME`| 문자열 | NULLABLE |
| `ALIAS_LABEL`| 문자열 | NULLABLE |
| `BRAZE_ID`| 문자열 | NULLABLE |
{% endtab %}

{% tab Databricks %}
다음 필드가 포함된 테이블을 만듭니다:

| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| 타임스탬프 | 필수 |
| `EXTERNAL_ID`| 문자열 | NULLABLE |
| `ALIAS_NAME`| 문자열 | NULLABLE |
| `ALIAS_LABEL`| 문자열 | NULLABLE |
| `BRAZE_ID`| 문자열 | NULLABLE |
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### 작동 방식

Braze Cloud 데이터 수집을 사용하면 데이터 웨어하우스 인스턴스와 Braze 워크스페이스 간의 통합을 설정하여 반복적으로 데이터를 동기화할 수 있습니다. 이 동기화는 설정한 일정에 따라 실행되며 각 통합마다 다른 일정을 가질 수 있습니다. 동기화는 15분마다 자주 실행하거나 한 달에 한 번처럼 드물게 실행할 수 있습니다. 동기화가 15분보다 더 자주 수행되어야 하는 고객의 경우 고객 성공 매니저와 상담하거나 실시간 데이터 수집을 위해 REST API 호출을 사용하는 것을 고려하세요.

동기화가 실행되면, Braze는 데이터 웨어하우스 인스턴스에 직접 연결하여 지정된 테이블에서 모든 새 데이터를 검색하고, Braze 대시보드에서 해당 사용자 프로필을 삭제합니다. 

{% alert warning %}
고객 프로필 삭제는 되돌릴 수 없습니다. 데이터에 불일치를 일으킬 수 있는 사용자를 영구적으로 제거합니다. 자세한 내용은 [고객 프로필 삭제를]({{site.baseurl}}/help/help_articles/api/delete_user/) 참조하세요.
{% endalert %}

<br><br>