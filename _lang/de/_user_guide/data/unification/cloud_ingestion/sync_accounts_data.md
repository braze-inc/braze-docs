---
nav_title: Kontodaten synchronisieren und löschen
article_title: Synchronisierung von Kontodaten mit CDI
page_order: 4
page_type: reference
description: "Erfahren Sie, wie Sie die Daten Ihres Braze-Kontos mit CDI synchronisieren können."

---

# Synchronisierung von Kontodaten mit CDI

> Erfahren Sie, wie Sie die Daten Ihres Braze-Kontos mit CDI synchronisieren können.

{% alert important %}
[Kontoobjekte](https://braze.com/unlisted_docs/account_opportunity_object/) befinden sich derzeit in der Beta-Phase, die für die Nutzung dieses Features erforderlich ist. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an einer Teilnahme an der Beta interessiert sind.
{% endalert %}

## Voraussetzungen

Bevor Sie Ihre Kontodaten mit CDI synchronisieren können, müssen Sie [Ihr Kontenschema konfigurieren](https://braze.com/unlisted_docs/account_opportunity_object/).

{% alert note %}
Nehmen Sie Updates an Ihrem Kontenschema nur dann vor, wenn die Synchronisierung pausiert oder nicht geplant ist, um Konflikte zwischen Ihren Data Warehouse Daten und dem Schema in Braze zu vermeiden.
{% endalert %}

## So funktioniert die Synchronisierung

- Bei jeder Synchronisierung werden Zeilen importiert, bei denen `UPDATED_AT` später als der letzte synchronisierte Zeitstempel liegt.
- Die Daten aus der Integration erstellen oder aktualisieren Konten auf der Grundlage der bereitgestellten `id`.
- Wenn `DELETED` auf `true` steht, wird das Konto gelöscht.
- Bei der Synchronisierung werden keine Datenpunkte protokolliert, aber alle synchronisierten Daten werden auf die Gesamtnutzung Ihres Kontos angerechnet, gemessen an der Gesamtzahl der gespeicherten Daten - Sie müssen sich nicht auf geänderte Daten beschränken.
- Felder, die nicht in Ihrem Kontenschema enthalten sind, werden gelöscht. Aktualisieren Sie das Schema, bevor Sie neue Felder synchronisieren.

## Daten Ihres Kontos synchronisieren

Sie können Ihre Kontodaten mit CDI über ein Data Warehouse oder einen Dateispeicher synchronisieren.

{% tabs local %}
{% tab Data Warehouse %}
So integrieren Sie Ihre Datenquelle mit Ihrem Data Warehouse:

{% subtabs %}
{% subtab Snowflake %}

1. Erstellen Sie eine Quelltabelle in Snowflake. Verwenden Sie die Namen aus dem Beispiel oder wählen Sie Ihre eigenen Datenbank-, Schema- und Tabellennamen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.
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
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, sonst wird die Datei übersprungen.
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

## Erstellen einer Synchronisationsansicht

Wenn Sie eine Synchronisationsansicht in Ihrem Data Warehouse erstellen, wird die Quelle automatisch aktualisiert, ohne dass Sie zusätzliche Abfragen neu schreiben müssen.

Wenn Sie z.B. eine Tabelle mit Kontodaten namens `account_details_1` mit `account_id`, `account_name` und drei zusätzlichen Attributen haben, könnten Sie eine Sync-Ansicht wie die folgende erstellen:

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
