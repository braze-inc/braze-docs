---
nav_title: 계정 데이터 동기화 및 삭제
article_title: CDI를 사용하여 계정 데이터 동기화
page_order: 4
page_type: reference
description: "CDI를 사용하여 Braze 계정 데이터를 동기화하는 방법을 알아보세요."

---

# CDI를 사용하여 계정 데이터 동기화

> CDI를 사용하여 Braze 계정 데이터를 동기화하는 방법을 알아보세요.

{% alert important %}
[계정 오브젝트](https://braze.com/unlisted_docs/account_opportunity_object/)는 베타 버전이며, 이 기능을 사용하려면 필수입니다. 베타 참여에 관심이 있으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 필수 조건

CDI를 사용하여 계정 데이터를 동기화하려면 먼저 [계정 스키마를 구성](https://braze.com/unlisted_docs/account_opportunity_object/)해야 합니다.

{% alert note %}
데이터 웨어하우스 데이터와 Braze의 스키마 간 충돌을 방지하려면, 동기화가 일시 중지되었거나 스케줄되지 않은 상태에서만 계정 스키마를 업데이트하세요.
{% endalert %}

## 동기화 작동 방식

- 각 동기화는 `UPDATED_AT`이 마지막으로 동기화된 타임스탬프보다 늦은 행을 가져옵니다. 정확한 경계 타임스탬프의 행은 동일한 타임스탬프를 가진 새 행이 있을 경우 다시 동기화될 수 있습니다. 자세한 내용은 [중복 타임스탬프가 있는 행의 재동기화 방지]({{site.baseurl}}/user_guide/data/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps)를 참조하세요.
- 통합에서 가져온 데이터는 제공된 `id`를 기반으로 계정을 생성하거나 업데이트합니다.
- `DELETED`가 `true`이면 해당 계정이 삭제됩니다.
- 동기화는 데이터 포인트를 기록하지 않지만, 모든 동기화된 데이터는 총 저장 데이터로 측정되는 총 계정 사용량에 포함됩니다. 변경된 데이터만으로 제한할 필요는 없습니다.
- 계정 스키마에 없는 필드는 삭제됩니다. 새 필드를 동기화하기 전에 스키마를 업데이트하세요.
- 동기화 이름 위에 마우스를 올리고 관련 동작을 선택하여 동기화를 새로고침, 재개 또는 일시 중지할 수 있습니다.

## 계정 데이터 동기화

데이터 웨어하우스 또는 파일 스토리지를 통해 CDI를 사용하여 계정 데이터를 동기화할 수 있습니다.

{% tabs local %}
{% tab Data Warehouse %}
데이터 소스를 데이터 웨어하우스와 통합하려면:

{% subtabs %}
{% subtab Snowflake %}

1. Snowflake에서 소스 테이블을 생성합니다. 예제의 이름을 사용하거나 자체 데이터베이스, 스키마 및 테이블 이름을 선택하세요. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the account to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Name of the account to be created or updated
         NAME VARCHAR(16777216) NOT NULL,
         --Account fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The account associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. 역할, 웨어하우스, 사용자를 생성하고 권한을 부여합니다. 다른 동기화에서 사용하는 자격 증명이 이미 있다면 재사용할 수 있습니다. 계정 테이블에 대한 접근 권한이 있는지 확인하세요.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. 네트워크 정책을 사용하는 경우, CDI 서비스가 연결할 수 있도록 Braze IP를 허용 목록에 추가하세요. IP 목록은 [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.
4. Braze 대시보드에서 **데이터 설정** > **Cloud Data Ingestion**으로 이동하여 새 동기화를 생성합니다.
5. 연결 세부 정보를 입력하거나 기존 정보를 재사용한 다음 소스 테이블을 추가합니다.
6. **Accounts** 동기화 유형을 선택한 다음 통합 이름과 스케줄을 입력합니다.
7. 동기화 빈도를 선택합니다.
8. 대시보드에서 공개 키를 생성한 사용자에게 추가합니다. Snowflake에서 `SECURITYADMIN` 이상의 접근 권한을 가진 사용자가 필요합니다.
9. **Test Connection**을 선택하여 설정을 확인합니다.
10. 완료되면 동기화를 저장합니다.

{% endsubtab %}
{% subtab Redshift %}

1. Redshift에서 소스 테이블을 생성합니다. 예제의 이름을 사용하거나 자체 데이터베이스, 스키마 및 테이블 이름을 선택하세요. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the account to be created or updated
       id varchar not null,
       --Name of the account to be created or updated
       name varchar not null,
       --Account fields and values that should be added or updated
       payload varchar(max),
       --The account associated with this ID should be deleted
       deleted boolean
    )
    ```
2. 사용자를 생성하고 권한을 부여합니다. 다른 동기화에서 사용하는 자격 증명이 이미 있다면 재사용할 수 있습니다. 계정 테이블에 대한 접근 권한이 있는지 확인하세요.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. 방화벽 또는 네트워크 정책이 있는 경우, Braze가 Redshift 인스턴스에 접근할 수 있도록 허용하세요. IP 목록은 [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endsubtab %}
{% subtab BigQuery %}

1. (선택 사항) 소스 테이블을 위한 새 프로젝트 또는 데이터셋을 생성합니다.
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. CDI 통합을 위한 소스 테이블을 생성합니다:
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp,
      id STRING,
      name STRING,
      payload JSON,
      deleted BOOLEAN
    );
    ```

    소스 테이블을 생성할 때 다음을 참조하세요:

    | 필드 이름 | 유형 | 필수 여부 |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | 예 |
    | `PAYLOAD` | JSON | 예 |
    | `ID` | String | 예 |
    | `NAME` | String | 예 |
    | `DELETED` | Boolean | 선택 사항 |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. 사용자를 생성하고 권한을 부여합니다. 다른 동기화에서 사용하는 자격 증명이 이미 있다면 계정 테이블에 대한 접근 권한이 있는 한 재사용할 수 있습니다.

    | 권한 | 용도 |
    |------------|---------|
    | BigQuery Connection User | Braze가 연결할 수 있도록 허용합니다. |
    | BigQuery User | Braze가 쿼리를 실행하고, 메타데이터를 읽고, 테이블을 나열할 수 있도록 허용합니다. |
    | BigQuery Data Viewer | Braze가 데이터셋과 콘텐츠를 볼 수 있도록 허용합니다. |
    | BigQuery Job User | Braze가 작업을 실행할 수 있도록 허용합니다. |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

    권한을 부여한 후 JSON 키를 생성합니다. 자세한 방법은 [키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 나중에 Braze 대시보드에서 업로드하게 됩니다.

{:start="4"}
4. 네트워크 정책을 사용하는 경우, Braze IP가 BigQuery 인스턴스에 접근할 수 있도록 허용하세요. IP 목록은 [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endsubtab %}
{% subtab Databricks %}

1. 소스 테이블을 위한 카탈로그 또는 스키마를 생성합니다.
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. CDI 통합을 위한 소스 테이블을 생성합니다:
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      payload STRING, STRUCT, or MAP,
      deleted BOOLEAN
    );
    ```

    소스 테이블을 생성할 때 다음을 참조하세요:

    | 필드 이름 | 유형 | 필수 여부 |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | 예 |
    | `PAYLOAD` | String, Struct, or Map | 예 |
    | `ID` | String | 예 |
    | `NAME` | String | 예 |
    | `DELETED` | Boolean | 선택 사항 |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Databricks에서 개인 액세스 토큰을 생성합니다:
    1. 사용자 이름을 선택한 다음 **User Settings**를 선택합니다.
    2. **Access tokens** 탭에서 **Generate new token**을 선택합니다.
    3. 토큰을 식별할 수 있는 코멘트를 추가합니다(예: "Braze CDI").
    4. 만료 없이 설정하려면 **Lifetime (days)**를 비워두고 **Generate**를 선택합니다.
    5. 토큰을 복사하여 Braze 대시보드에서 사용할 수 있도록 안전하게 저장합니다.

{:start="4"}
4. 네트워크 정책을 사용하는 경우, Braze IP가 Databricks 인스턴스에 접근할 수 있도록 허용하세요. IP 목록은 [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. 다음 필드를 사용하여 CDI 통합을 위한 테이블을 하나 이상 생성합니다:
    ```sql
    CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
    (
      UPDATED_AT DATETIME2(6) NOT NULL,
      PAYLOAD VARCHAR NOT NULL,
      ID VARCHAR NOT NULL,
      NAME VARCHAR NOT NULL,
      DELETED BIT
    )
    GO
    ```

{:start="2"}
2. 서비스 주체를 생성하고 권한을 부여합니다. 다른 동기화에서 사용하는 자격 증명이 이미 있다면 재사용할 수 있습니다. 계정 테이블에 대한 접근 권한이 있는지 확인하세요.

{:start="3"}
3. 네트워크 정책을 사용하는 경우, Braze IP가 Microsoft Fabric 인스턴스에 접근할 수 있도록 허용하세요. IP 목록은 [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab File Storage %}
파일 스토리지에서 계정 데이터를 동기화하려면 다음 필드를 포함하는 소스 파일을 생성하세요.

| 필드 | 필수 여부 | 설명 |  
| --- | --- | --- |  
| `ID` | 예 | 업데이트하거나 생성할 계정의 ID |  
| `NAME` | 예 | 계정의 이름 |  
| `PAYLOAD` | 예 | Braze의 계정에 동기화할 필드의 JSON 문자열 |  
| `DELETED` | 선택 사항 | Braze에서 계정을 삭제할지 여부를 나타내는 부울 값 |  
| `UPDATED_AT` | _*지원되지 않음_ | 파일 스토리지는 `UPDATED_AT` 열을 지원하지 않습니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
파일 이름은 AWS 규칙을 따르고 고유해야 합니다. 고유성을 보장하기 위해 타임스탬프를 추가하세요. Amazon S3 동기화에 대한 자세한 내용은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/cloud_ingestion/file_storage_integrations)을 참조하세요.
{% endalert %}

다음 예제는 파일 스토리지에서 계정 데이터를 동기화하기 위한 유효한 JSON 및 CSV 형식을 보여줍니다.

{% subtabs %}
{% subtab JSON Accounts %}
```jsonl  
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```  

{% alert important %}
소스 파일의 각 행은 유효한 JSON을 포함해야 하며, 그렇지 않으면 파일이 건너뛰어집니다.
{% endalert %}
{% endsubtab %}
{% subtab CSV Accounts with Delete %}
```plaintext  
ID,NAME,PAYLOAD,DELETED
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}",TRUE 
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}",FALSE
```
{% endsubtab %}
{% subtab CSV Accounts without Delete %}
```plaintext  
ID,NAME,PAYLOAD
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}"
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}"
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 동기화 뷰 생성

데이터 웨어하우스에서 동기화 뷰를 생성하면 추가 쿼리를 다시 작성할 필요 없이 소스가 자동으로 새로고침됩니다.

예를 들어, `account_id`, `account_name` 및 세 개의 추가 속성이 있는 `account_details_1`이라는 계정 데이터 테이블이 있는 경우 다음과 같은 동기화 뷰를 생성할 수 있습니다:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [BRAZE_CLOUD_PRODUCTION].[INGESTION].[ACCOUNTS_SYNC]
AS SELECT 
    account_id as ID,
    account_name as NAME,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[account_details_1] ;
```
{% endtab %}
{% endtabs %}