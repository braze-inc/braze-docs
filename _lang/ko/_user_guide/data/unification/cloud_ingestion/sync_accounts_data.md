---
nav_title: 계정 데이터 동기화 및 삭제하기
article_title: CDI를 사용하여 계정 데이터 동기화하기
page_order: 4
page_type: reference
description: "CDI를 사용하여 Braze 계정 데이터를 동기화하는 방법을 알아보세요."

---

# CDI를 사용하여 계정 데이터 동기화하기

> CDI를 사용하여 Braze 계정 데이터를 동기화하는 방법을 알아보세요.

{% alert important %}
[계정 개체는](https://braze.com/unlisted_docs/account_opportunity_object/) 현재 베타 버전으로, 이 기능을 사용하려면 [계정 개체가](https://braze.com/unlisted_docs/account_opportunity_object/) 필요합니다. 베타 버전 참여에 관심이 있으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 전제 조건

CDI를 사용하여 계정 데이터를 동기화하려면 먼저 [계정 스키마를 구성해야](https://braze.com/unlisted_docs/account_opportunity_object/) 합니다.

{% alert note %}
동기화가 일시 중지되었거나 예약되지 않은 경우에만 계정 스키마를 업데이트하여 데이터 웨어하우스 데이터와 Braze의 스키마 간에 충돌이 발생하지 않도록 하세요.
{% endalert %}

## 동기화 작동 방식

- 각 동기화는 `UPDATED_AT` 이 마지막 동기화 타임스탬프보다 늦은 행을 가져옵니다.
- 통합의 데이터는 제공된 `id` 을 기반으로 계정을 생성하거나 업데이트합니다.
- `DELETED` 이 `true` 인 경우 계정이 삭제됩니다.
- 동기화는 데이터 포인트를 기록하지는 않지만, 동기화된 모든 데이터는 총 저장된 데이터로 측정되는 총 계정 사용량에 포함되므로 변경된 데이터로만 제한할 필요가 없습니다.
- 계정 스키마에 없는 필드는 삭제되므로 새 필드를 동기화하기 전에 스키마를 업데이트하세요.

## 계정 데이터 동기화하기

데이터 웨어하우스 또는 파일 저장소를 통해 CDI를 사용하여 계정 데이터를 동기화할 수 있습니다.

{% tabs local %}
{% tab Data Warehouse %}
데이터 소스를 데이터 웨어하우스와 통합하려면:

{% subtabs %}
{% subtab Snowflake %}

1. Snowflake에서 소스 테이블을 만듭니다. 예제의 이름을 사용하거나 고유한 데이터베이스, 스키마 및 테이블 이름을 선택합니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
  ```json
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
2. Create a role, warehouse, and user, and grant permissions. If you already have credentials from another sync, you can reuse them—just make sure they have access to the accounts table.
    ```json
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. If you use network policies, allowlist the Braze IPs so the CDI service can connect. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, go to **Data Settings** > **Cloud Data Ingestion** and create a new sync.
5. Enter connection details (or reuse existing ones), then add the source table.
6. Select the **Accounts** sync type, then enter the integration name and schedule. 
7. Choose the sync frequency.
8. Add the public key from the dashboard to the user you created. This requires a user with `SECURITYADMIN` access or higher in Snowflake. 
9. Select **Test Connection** to confirm the setup. 
10. When you're finished, save the sync.

{% endsubtab %}
{% subtab Redshift %}

1. Create a source table in Redshift. Use the names in the example or choose your own database, schema, and table names. You can also use a view or materialized view instead of a table.
    ```json
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
2. Create a user and grant permissions. If you already have credentials from another sync, you can reuse them—just make sure they have access to the accounts table.
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. If you have a firewall or network policies, allow Braze access to your Redshift instance. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab BigQuery %}

1. (Optional) Create a new project or dataset for your source table.  
    ```json
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Create the source table for your CDI integration:  
    ```json
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp,
      id STRING,
      name STRING,
      payload JSON,
      deleted BOOLEAN
    );
    ```

    Refer to the following when creating your source table:

    | Field Name | Type | Required? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Yes |
    | `PAYLOAD` | JSON | Yes |
    | `ID` | String | Yes |
    | `NAME` | String | Yes |
    | `DELETED` | Boolean | Optional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Create a user and grant permissions. If you already have credentials from another sync, you can reuse them as long as they have access to the accounts table.

    | Permission | Purpose |
    |------------|---------|
    | BigQuery Connection User | Allows Braze to connect. |
    | BigQuery User | Allows Braze to run queries, read metadata, and list tables. |
    | BigQuery Data Viewer | Allows Braze to view datasets and contents. |
    | BigQuery Job User | Allows Braze to run jobs. |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

    After granting permissions, generate a JSON key. See [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) for instructions. You’ll upload it in the Braze dashboard later.

{:start="4"}
4. If you use network policies, allow Braze IPs to access your BigQuery instance. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Databricks %}

1. Create a catalog or schema for your source table.  
    ```json
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Create the source table for your CDI integration:  
    ```json
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      payload STRING, STRUCT, or MAP,
      deleted BOOLEAN
    );
    ```

    Refer to the following when creating your source table:

    | Field Name | Type | Required? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Yes |
    | `PAYLOAD` | String, Struct, or Map | Yes |
    | `ID` | String | Yes |
    | `NAME` | String | Yes |
    | `DELETED` | Boolean | Optional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Create a personal access token in Databricks:
    1. Select your username, then select **User Settings**.  
    2. On the **Access tokens** tab, select **Generate new token**.  
    3. Add a comment to identify the token, such as "Braze CDI".  
    4. Leave **Lifetime (days)** blank for no expiration, then select **Generate**.  
    5. Copy and save the token securely for use in the Braze dashboard.

{:start="4"}
4. If you use network policies, allow Braze IPs to access your Databricks instance. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. Create one or more tables for your CDI integration with these fields:
    ```json
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
2. Create a service principal and grant permissions. If you already have credentials from another sync, you can reuse them—just make sure they have access to the accounts table.

{:start="3"}
3. If you use network policies, allow Braze IPs to access your Microsoft Fabric instance. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab File Storage %}
To sync account data from file storage, create a source file with the following fields.

| Field | Required? | Description |  
| --- | --- | --- |  
| `ID` | Yes | ID of the Account to update or create |  
| `NAME` | Yes | Name of the Account |  
| `PAYLOAD` | Yes | JSON string of the fields to sync to the account in Braze |  
| `DELETED` | Optional | Boolean indicating to delete the account from Braze |  
| `UPDATED_AT` | _*Unsupported_ | File storage doesn't support `UPDATED_AT` columns |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Filenames must follow AWS rules and be unique. Append timestamps to help ensure uniqueness. For more on Amazon S3 syncing, see [File Storage Integrations]({{site.baseurl}}/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

The following examples show valid JSON and CSV formats for syncing account data from file storage.

{% subtabs %}
{% subtab JSON Accounts %}
```json  
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```  

{% alert important %}
소스 파일의 각 줄에는 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다.
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

## 동기화 보기 만들기

데이터 웨어하우스에서 동기화 보기를 만들면 추가 쿼리를 다시 작성할 필요 없이 소스를 자동으로 새로고침할 수 있습니다.

예를 들어 `account_id`, `account_name`, 그리고 3개의 추가 속성이 있는 `account_details_1` 라는 계정 데이터 테이블이 있는 경우 다음과 같은 동기화 보기를 만들 수 있습니다:

{% tabs %}
{% tab Snowflake %}
```json
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
```json
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
```json
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
```json
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
```json
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
