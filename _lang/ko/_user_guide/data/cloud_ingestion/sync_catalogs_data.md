---
nav_title: 카탈로그 데이터 동기화 및 삭제
article_title: 카탈로그 데이터 동기화 및 삭제
page_order: 4
page_type: reference
description: "이 페이지에서는 카탈로그 데이터를 동기화하는 방법에 대한 개요를 제공합니다."

---

# 카탈로그 데이터 동기화 및 삭제

> 이 페이지에서는 카탈로그 데이터를 동기화하는 방법에 대해 설명합니다.
 
## 1단계: 새 카탈로그 만들기

[카탈로그에]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) 대한 새로운 클라우드 데이터 수집(CDI) 통합을 만들기 전에 새 카탈로그를 만들거나 통합에 사용할 기존 카탈로그를 식별해야 합니다. 새 카탈로그를 만드는 방법에는 몇 가지가 있으며, 이 중 어느 것이든 CDI 통합에 사용할 수 있습니다:
- [CSV]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-1-upload-csv) 업로드
- [Braze 대시보드에서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-2-create-in-browser) 또는 CDI 설정 중에 카탈로그를 생성합니다.
- [카탈로그 만들기 엔드포인트]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)를 사용하여 카탈로그 만들기

카탈로그 스키마에 대한 모든 변경 사항(예: 새 필드 추가 또는 필드 유형 변경)은 업데이트된 데이터가 CDI를 통해 동기화되기 전에 카탈로그 대시보드를 통해 수행해야 합니다. 데이터 웨어하우스 데이터와 Braze의 스키마 간의 충돌을 방지하기 위해 동기화가 일시 중지되었거나 실행이 예약되어 있지 않을 때 이러한 업데이트를 수행하는 것이 좋습니다.

## 2단계: 클라우드 데이터 수집과 카탈로그 데이터 통합
카탈로그 동기화를 위한 설정은 [사용자 데이터 CDI 통합]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup) 프로세스와 매우 유사합니다. 

{% tabs %}
{% tab Snowflake %}

1. Snowflake에서 소스 테이블을 설정합니다. 다음 예제의 이름을 사용하거나 고유한 데이터베이스, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
  ```json
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
2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    ```json
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. If your Snowflake account has network policies, allowlist the Braze IPs so the CDI service can connect. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, navigate to **Technology Partners** > **Snowflake**, and create a new sync.
5. Enter connection details (or reuse existing credentials) and the source table.
6. Proceed to step 2 of the setup flow, select the “Catalogs” sync type, and input the integration name and schedule. Note that the name of the integration should **exactly match** the name of the catalog you previously created.
7. Choose a sync frequency and proceed to the next step.
8. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake. To complete this step, you will need someone with `SECURITYADMIN` access or higher in Snowflake. 
9. Select **Test Connection** so that everything works as expected. 
10. Save the sync, and use the synced catalog data for all your personalization use cases. 
{% endtab %}
{% tab Redshift %}

1. Set up a source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
    ```json
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
2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the below IPs corresponding to your Braze dashboard’s region. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Optionally, set up a new project or dataset to hold your source table. 

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 만드세요.

```json
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
| UPDATED_AT | 타임스탬프 | 필수 |
| PAYLOAD | JSON | 필수 |
| ID | STRING | 필수 |
| 삭제됨 | BOOLEAN | 선택 사항 |

{:start="2"}

2. 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화의 자격 증명이 이미 있는 경우 이를 재사용할 수 있지만 카탈로그 소스 테이블에 대한 액세스 권한을 확장해야 합니다.
서비스 계정에는 아래 권한이 있어야 합니다:
- BigQuery 연결 사용자: 이렇게 하면 Braze가 연결할 수 있습니다.
- BigQuery 사용자: 이렇게 하면 Braze에서 쿼리를 실행하고, 데이터 세트 메타데이터를 읽고, 테이블을 나열할 수 있는 액세스 권한이 제공됩니다.
- BigQuery 데이터 Viewer: 이렇게 하면 Braze가 데이터 세트와 그 내용을 볼 수 있는 접근 권한을 제공합니다.
- BigQuery 작업 사용자: 이렇게 하면 작업을 실행할 수 있는 Braze 액세스 권한이 제공됩니다<br><br>서비스 계정을 만들고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 내용은 [키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 나중에 Braze 대시보드에 업데이트할 예정입니다.

{:start="3"}
3\. 네트워크 정책이 있는 경우 Braze 네트워크에 Big Query 인스턴스에 대한 액세스 권한을 부여해야 합니다. IP 목록은 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) 참조하세요.

{% endtab %}
{% tab Databricks %}

1. Databricks에서 소스 테이블을 설정합니다. 다음 예제의 이름을 사용하거나 카탈로그, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```json
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
| UPDATED_AT | 타임스탬프 | 필수 |
| PAYLOAD | STRING, STRUCT, or MAP | 필수 |
| ID | STRING | 필수 |
| 삭제됨 | BOOLEAN | NULLABLE |

{:start="2"}

2. Databricks 워크스페이스에서 개인 액세스 토큰을 생성합니다.

- a. Databricks 사용자 아이디를 선택한 다음 드롭다운 메뉴에서 **사용자 설정**을 선택합니다.
- b. **액세스 토큰** 탭에서 **새 토큰 생성**을 선택합니다.
- c. 이 토큰을 식별하는 데 도움이 되는 댓글(예: "Braze CDI")을 입력합니다. 
- d. **수명(일)** 상자를 비워두면 토큰의 수명을 수명 없음으로 변경할 수 있습니다. **생성**을 선택합니다.
- e. 표시된 토큰을 복사한 다음 **완료**를 선택합니다. 
- f. Braze 대시보드에서 자격증명 생성 단계에서 토큰을 입력해야 할 때까지 토큰을 안전한 곳에 보관하세요.

{:start="3"}
3\. 네트워크 정책이 설정되어 있는 경우, Databricks 인스턴스에 대한 Braze 네트워크 액세스 권한을 부여해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) 페이지를 참조하세요.

{% endtab %}
{% tab Microsoft Fabric %}

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 만드세요.

```json
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

2. 서비스 주체를 설정하고 적절한 권한을 부여하세요. 기존 동기화의 자격 증명이 이미 있는 경우 이를 재사용할 수 있으며, 카탈로그 소스 테이블에 대한 액세스 권한을 확장하기만 하면 됩니다. 새 서비스 계정 및 자격 증명을 만드는 방법에 대해 자세히 알아보려면 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) 페이지를 참조하세요. 

{:start="3"}
3\. 네트워크 정책이 설정되어 있는 경우 Braze 네트워크에 Microsoft 패브릭 인스턴스에 대한 액세스 권한을 부여해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% endtabs %}

## 통합 작동 방식

동기화가 실행될 때마다 Braze는 마지막 타임스탬프 동기화 이후 `UPDATED_AT`이 있는 모든 행을 가져옵니다. 데이터 웨어하우스에서 카탈로그 데이터로 뷰를 만들어 동기화가 실행될 때마다 완전히 새로 고쳐지는 원본 테이블을 설정하는 것이 좋습니다. 조회를 사용하면 매번 쿼리를 다시 작성할 필요가 없습니다.

예를 들어 `product_id` 및 3개의 추가 속성이 있는 제품 데이터 테이블(`product_catalog_1`)이 있는 경우 아래 보기를 동기화할 수 있습니다.

{% tabs %}
{% tab Snowflake %}
```json
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
```json
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
```json
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
```json
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
```json
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- 통합에서 가져온 데이터는 제공된 `id`에 따라 대상 카탈로그에서 항목을 생성하거나 업데이트하는 데 사용됩니다.
- 삭제됨이 `true`로 설정되어 있으면 해당 카탈로그 항목이 삭제됩니다.
- 동기화는 데이터 포인트를 소비하지 않지만 동기화된 모든 데이터는 총 카탈로그 사용량에 포함되며, 이 사용량은 저장된 총 데이터를 기준으로 측정되므로 변경된 데이터만 동기화하는 것에 대해 걱정할 필요가 없습니다.
