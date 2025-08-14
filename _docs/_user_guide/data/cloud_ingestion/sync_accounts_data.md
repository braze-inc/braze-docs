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

1. Set up a source table in Snowflake. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
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
2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the accounts source table.
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
3. If your Snowflake account has network policies, allowlist the Braze IPs so the CDI service can connect. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, go to **Data Settings** > **Cloud Data Ingestion**, and create a new sync.
5. Enter connection details (or reuse existing credentials), then enter the source table.
6. For the sync type, select **Accounts**, then enter the integration name and schedule. 
7. Choose a sync frequency.
8. Add the public key shown in the dashboard to the user you previously created. Note that you'll need to choose a user with `SECURITYADMIN` access or higher in Snowflake. 
9. Select **Test Connection** and verify the sync. 
10. When you're finished, save your sync. 
{% endsubtab %}
{% subtab Redshift %}

1. Set up a source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
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
2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the accounts source table.
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the below IPs corresponding to your Braze dashboard’s region. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab BigQuery %}

1. Optionally, set up a new project or dataset to hold your source table. 
    ```json
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

    Create one or more tables to use for your CDI integration with the following fields:

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

    | FIELD NAME | TYPE | MODE |
    | --- | --- | --- |
    | UPDATED_AT | TIMESTAMP | REQUIRED |
    | PAYLOAD | JSON | REQUIRED |
    | ID | STRING | REQUIRED |
    | NAME | STRING | REQUIRED |
    | DELETED | BOOLEAN | OPTIONAL |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="2"}

2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse those&#8212;but make sure to extend access to the accounts source table.

    | Permission | Purpose |
    |------------|---------|
    | BigQuery Connection User | Allows Braze to make connections. |
    | BigQuery User | Provides Braze access to run queries, read dataset metadata, and list tables. |
    | BigQuery Data Viewer | Provides Braze access to view datasets and their contents. |
    | BigQuery Job User | Provides Braze access to run jobs. |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

    After creating the service account and granting permissions, generate a JSON key. Refer to [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) for more information. You'll update this to the Braze dashboard later.

{:start="3"}
3. If you have network policies in place, you must give Braze network access to your BigQuery instance. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Databricks %}

1. Set up a source table in Databricks. You can use the names in the following example or choose your catalog, schema, and table names. You can also use a view or a materialized view instead of a table.
    ```json
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

    ```json
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      deleted BOOLEAN,
      payload STRING, STRUCT, or MAP
    );
    ```

    | FIELD NAME | TYPE | MODE |
    | --- | --- | --- |
    | UPDATED_AT | TIMESTAMP | REQUIRED |
    | PAYLOAD | STRING, STRUCT, or MAP | REQUIRED |
    | ID | STRING | REQUIRED |
    | NAME | STRING | REQUIRED |
    | DELETED | BOOLEAN | NULLABLE |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="2"}
2. Create a personal access token in your Databricks workspace:
    1. Select your Databricks username, then select **User Settings** from the dropdown menu.  
    2. On the **Access tokens** tab, select **Generate new token**.  
    3. Enter a comment that helps you to identify this token, such as "Braze CDI".  
    4. Change the token’s lifetime to no lifetime by leaving the **Lifetime (days)** box blank. Select **Generate**.  
    5. Copy the displayed token, and then select **Done**.  
    6. Keep the token in a safe place until you need to enter it during the credential creation step in the Braze dashboard.

{:start="3"}
3. If you have network policies in place, you must give Braze network access to your Databricks instance. For a list of IPs, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) page.

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. Create one or more tables to use for your CDI integration with the following fields:
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
2. Set up a service principal and grant proper permissions. If you already have credentials from an existing sync, you can reuse those&#8212;just make sure to extend access to the accounts source table. To learn more about how to create a new service principal and credentials, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) page. 

{:start="3"}
3. If you have network policies in place, you must give Braze network access to your Microsoft Fabric instance. For a list of IPs, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
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
