---
nav_title: Sync and Delete Account Data
article_title: Sync and Delete Account Data
page_order: 4
page_type: reference
description: "This page provides an overview of how to sync account data."

---

# Syncing account data using CDI

> Learn how to sync your Braze account data using CDI.

{% alert important %}
[Account objects](https://braze.com/unlisted_docs/account_opportunity_object/) are currently in beta, and only beta particpants can configure an Accounts sync through CDI. Contact your Braze account manager if you’re interested in participating in this beta.
{% endalert %}

## How syncing works

- Each time the sync runs, Braze will pull in all rows where `UPDATED_AT` is after the last timestamp synced. 
- The data fetched from the integration will be used to create or update accounts based on the `id` provided.
- If `DELETED` is set to `true`, the corresponding account item will be deleted.
- The sync won't consume data points, but all data synced will count toward your total accounts usage; this usage is measured based on the total data stored, so you don’t need to worry about only syncing changed data.
- Any fields that exist in your source data but not in the accounts schema will be dropped before they're synced to Braze; to add new fields, update the accounts schema and then sync the new data

## Syncing your account data
 
### Step 1: Configure your accounts schema

Any changes to the accounts schema in your workspace (such as, adding new fields or changing field type) must be made through the accounts dashboard before updated data is synced through CDI.

{% alert important %}
Only make updates to your account schema when the sync is paused or not scheduled, so you can avoid conflicts between your data warehouse data and the schema in Braze.
{% endalert %}

### Step 2: Integrate your data source

{% tabs local %}
{% tab Data Warehouse Integrations %}
To integrate your data source with your data warehouse:

{% subtabs %}
{% subtab Snowflake %}

1. Create a source table in Snowflake. Use the names in the example or choose your own database, schema, and table names. You can also use a view or materialized view instead of a table.
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

{% tab File Storage Integration %}
There are no additional filename requirements other than what's enforced by AWS. Filenames must be unique, so we recommend appending timestamps to your filenames. For more information about Amazon S3 syncing, see [File Storage Integrations]({{site.baseurl}}/user_guide/data/cloud_ingestion/file_storage_integrations).

Refer to the following table when integrating with a file storage:

| Field | Required? | Description |  
| --- | --- | --- |  
| `ID` | Yes | ID of the Account to update or create |  
| `NAME` | Yes | Name of the Account |  
| `PAYLOAD` | Yes | This is a JSON string of the fields you want to sync to the user in Braze. |  
| `DELETED` | Optional | Boolean indicating to delete the Account from Braze. |  
| `UPDATED_AT` | _*Unsupported_ | Unlike data warehouses, file storage doesn't support `UPDATED_AT` columns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

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
Every line in your source file must contain valid JSON, or the file will be skipped. 
{% endalert %}
{% endsubtab %}
{% subtab CSV Accounts with Delete  %}
```plaintext  
ID,NAME,PAYLOAD,DELETED
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}",TRUE 
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}",FALSE
```
{% endsubtab %}
{% subtab CSV Accounts without Delete  %}
```plaintext  
ID,NAME,PAYLOAD
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}"
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}"
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Creating a sync view

Creating a sync view in your data warehouse lets the source refresh automatically without needing to rewrite additional queries.

For example, if you have a table of account data called `account_details_1` with `account_id`, `account_name`, and three additional attributes, you could create a sync view like the following:

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
