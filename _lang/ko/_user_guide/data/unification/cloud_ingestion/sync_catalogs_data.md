---
nav_title: 카탈로그 데이터 동기화 및 삭제
article_title: 카탈로그 데이터 동기화 및 삭제
page_order: 4
page_type: reference
description: "이 페이지에서는 카탈로그 데이터를 동기화하는 방법에 대한 개요를 제공합니다."

---

# 카탈로그 데이터 동기화 및 삭제

> 이 페이지에서는 카탈로그 데이터를 동기화하는 방법에 대해 설명합니다.
 
## 1단계: 새 카탈로그 생성

[카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/)에 대한 새로운 클라우드 데이터 수집(CDI) 통합을 생성하기 전에 새 카탈로그를 생성하거나 통합에 사용할 기존 카탈로그를 식별해야 합니다. 새 카탈로그를 생성하는 방법에는 몇 가지가 있으며, 이 중 어느 것이든 CDI 통합에 사용할 수 있습니다:
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv) 업로드
- [Braze 대시보드]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser)에서 또는 CDI 설정 중에 카탈로그를 생성합니다.
- [카탈로그 생성 엔드포인트]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)를 사용하여 카탈로그 생성

카탈로그 스키마에 대한 모든 변경 사항(예: 새 필드 추가 또는 필드 유형 변경)은 업데이트된 데이터가 CDI를 통해 동기화되기 전에 카탈로그 대시보드를 통해 수행해야 합니다. 데이터 웨어하우스 데이터와 Braze의 스키마 간의 충돌을 방지하기 위해 동기화가 일시 중지되었거나 실행이 예약되어 있지 않을 때 이러한 업데이트를 수행하는 것이 좋습니다.

## 2단계: 클라우드 데이터 수집과 카탈로그 데이터 통합
카탈로그 동기화 설정은 [사용자 데이터 CDI 통합]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup) 프로세스와 매우 유사합니다. 

{% tabs %}
{% tab Snowflake %}

1. Snowflake에서 소스 테이블을 설정합니다. 다음 예제의 이름을 사용하거나 고유한 데이터베이스, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. 역할, 웨어하우스, 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화의 자격 증명이 이미 있는 경우 재사용할 수 있지만, 카탈로그 소스 테이블에 대한 액세스 권한을 확장해야 합니다.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Snowflake 계정에 네트워크 정책이 있는 경우, CDI 서비스가 연결할 수 있도록 Braze IP를 허용 목록에 추가하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.
4. Braze 대시보드에서 **기술 파트너** > **Snowflake**로 이동하여 새 동기화를 생성합니다.
5. 연결 세부 정보(또는 기존 자격 증명 재사용)와 소스 테이블을 입력합니다.
6. 설정 흐름의 2단계로 진행하여 "Catalogs" 동기화 유형을 선택하고 통합 이름과 스케줄을 입력합니다. 통합 이름은 이전에 생성한 카탈로그 이름과 **정확히 일치**해야 합니다.
7. 동기화 빈도를 선택하고 다음 단계로 진행합니다.
8. 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결하기 위해 생성한 사용자에게 추가합니다. 이 단계를 완료하려면 Snowflake에서 `SECURITYADMIN` 이상의 액세스 권한을 가진 사용자가 필요합니다. 
9. **연결 테스트**를 선택하여 모든 것이 예상대로 작동하는지 확인합니다. 
10. 동기화를 저장하고, 동기화된 카탈로그 데이터를 모든 개인화 사용 사례에 활용합니다. 
{% endtab %}
{% tab Redshift %}

1. Redshift에서 소스 테이블을 설정합니다. 다음 예제의 이름을 사용하거나 고유한 데이터베이스, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화의 자격 증명이 이미 있는 경우 재사용할 수 있지만, 카탈로그 소스 테이블에 대한 액세스 권한을 확장해야 합니다.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. 방화벽 또는 기타 네트워크 정책이 있는 경우, Braze에 Redshift 인스턴스에 대한 네트워크 액세스 권한을 부여해야 합니다. Braze 대시보드 리전에 해당하는 아래 IP에서의 액세스를 허용하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% tab BigQuery %}

1. 선택적으로, 소스 테이블을 보관할 새 프로젝트 또는 데이터세트를 설정합니다. 

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 생성합니다:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| 필드 이름 | TYPE | 모드 |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | 필수 |
| PAYLOAD | JSON | 필수 |
| ID | STRING | 필수 |
| DELETED | BOOLEAN | 선택 사항 |

{:start="2"}

2. 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화의 자격 증명이 이미 있는 경우 재사용할 수 있지만&#8212;카탈로그 소스 테이블에 대한 액세스 권한을 확장해야 합니다. 
서비스 계정에는 아래 권한이 있어야 합니다:
- BigQuery Connection User: Braze가 연결할 수 있도록 합니다.
- BigQuery User: Braze가 쿼리를 실행하고, 데이터세트 메타데이터를 읽고, 테이블을 나열할 수 있는 액세스 권한을 제공합니다.
- BigQuery Data Viewer: Braze가 데이터세트와 그 콘텐츠를 볼 수 있는 액세스 권한을 제공합니다.
- BigQuery Job User: Braze가 작업을 실행할 수 있는 액세스 권한을 제공합니다.<br><br>서비스 계정을 생성하고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 내용은 [키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 이 키는 나중에 Braze 대시보드에 업로드하게 됩니다.

{:start="3"}
3. 네트워크 정책이 있는 경우 Braze에 BigQuery 인스턴스에 대한 네트워크 액세스 권한을 부여해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% tab Databricks %}

1. Databricks에서 소스 테이블을 설정합니다. 다음 예제의 이름을 사용하거나 카탈로그, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| 필드 이름 | TYPE | 모드 |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | 필수 |
| PAYLOAD | STRING, STRUCT, or MAP | 필수 |
| ID | STRING | 필수 |
| DELETED | BOOLEAN | NULLABLE |

{:start="2"}

2. Databricks 워크스페이스에서 개인 액세스 토큰을 생성합니다.

- a. Databricks 사용자 이름을 선택한 다음 드롭다운 메뉴에서 **사용자 설정**을 선택합니다.
- b. **액세스 토큰** 탭에서 **새 토큰 생성**을 선택합니다.
- c. 이 토큰을 식별하는 데 도움이 되는 코멘트(예: "Braze CDI")를 입력합니다. 
- d. **수명(일)** 상자를 비워두면 토큰의 수명을 무제한으로 변경할 수 있습니다. **생성**을 선택합니다.
- e. 표시된 토큰을 복사한 다음 **완료**를 선택합니다. 
- f. Braze 대시보드에서 자격 증명 생성 단계에서 입력해야 할 때까지 토큰을 안전한 곳에 보관하세요.

{:start="3"}
3. 네트워크 정책이 설정되어 있는 경우, Databricks 인스턴스에 대한 Braze 네트워크 액세스 권한을 부여해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) 페이지를 참조하세요.

{% endtab %}
{% tab Microsoft Fabric %}

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 생성합니다:

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. 서비스 주체를 설정하고 적절한 권한을 부여합니다. 기존 동기화의 자격 증명이 이미 있는 경우 재사용할 수 있으며&#8212;카탈로그 소스 테이블에 대한 액세스 권한을 확장하기만 하면 됩니다. 새 서비스 주체 및 자격 증명을 생성하는 방법에 대해 자세히 알아보려면 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) 페이지를 참조하세요. 

{:start="3"}
3. 네트워크 정책이 설정되어 있는 경우 Braze에 Microsoft Fabric 인스턴스에 대한 네트워크 액세스 권한을 부여해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% tab S3 %}
JSON 또는 CSV 파일을 제공하여 S3에 소스 파일을 설정합니다. 다음 사항을 유의하세요:

- 파일에는 `UPDATED_AT` 열을 포함할 수 없습니다  
- 선택적으로 제거할 항목을 표시하는 `DELETED` 필드를 포함할 수 있습니다 

{% subtabs %}
{% subtab JSON %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```
{% endsubtab %}

{% subtab CSV %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% endsubtabs %}

설정에 대한 자세한 내용은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/)을 참조하세요.

{% endtab %}
{% endtabs %}

## 통합 작동 방식

동기화가 실행될 때마다 Braze는 `UPDATED_AT`이 마지막으로 동기화된 값보다 이후인 모든 행을 가져옵니다. 경계 타임스탬프가 정확히 동일한 행은 새 행이 동일한 타임스탬프를 공유하는 경우 다시 동기화될 수 있습니다. 데이터 웨어하우스에서 카탈로그 데이터를 기반으로 뷰를 생성하여 동기화가 실행될 때마다 완전히 새로고침되는 소스 테이블을 설정하는 것이 좋습니다. 뷰를 사용하면 매번 쿼리를 다시 작성할 필요가 없습니다.

예를 들어 `product_id`와 3개의 추가 속성이 있는 제품 데이터 테이블(`product_catalog_1`)이 있는 경우 아래 뷰를 동기화할 수 있습니다:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- 통합에서 가져온 데이터는 제공된 `id`를 기반으로 대상 카탈로그에서 항목을 생성하거나 업데이트하는 데 사용됩니다.
- DELETED가 `true`로 설정되어 있으면 해당 카탈로그 항목이 삭제됩니다.
- 동기화는 데이터 포인트를 소비하지 않지만, 동기화된 모든 데이터는 총 카탈로그 사용량에 포함됩니다. 이 사용량은 저장된 총 데이터량을 기준으로 측정되므로 변경된 데이터만 동기화하는 것에 대해 걱정할 필요가 없습니다.