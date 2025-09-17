---
nav_title: Sync and delete catalog data
article_title: Sync and Delete Catalog Data
page_order: 4
page_type: reference
description: "This page provides an overview of how to sync catalog data."

---

# Sync and delete catalog data

> This page discusses how to sync catalog data.
 
## Step 1: Create a new catalog

Before creating a new Cloud Data Ingestion (CDI) integration for [catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/), you need to create a new catalog or identify an existing catalog you want to use for the integration. There are a few ways to create a new catalog and any of these will work for the CDI integration:
- Upload a [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv)
- Create a catalog in the [Braze dashboard]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) or during CDI setup.
- Create a catalog using the [Create catalog endpoint]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Any changes to the catalog schema (for example, adding new fields or changing field type) must be made through the catalog dashboard before updated data is synced through CDI. We recommend making these updates when the sync is paused or not scheduled to run to avoid conflicts between your data warehouse data and the schema in Braze.

## Step 2: Integrate Cloud Data Ingestion with catalog data
The setup for a catalog sync closely follows the process for [user-data CDI integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Set up a source table in Snowflake. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
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

Create one or more tables to use for your CDI integration with the following fields:

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| FIELD NAME | TYPE | MODE |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | JSON | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | OPTIONAL |

{:start="2"}

2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse those&#8212;but make sure to extend access to the catalog source table. 
The service account should have the below permissions:
- BigQuery Connection User: This will allow Braze to make connections.
- BigQuery User: This will provide Braze access to run queries, read dataset metadata, and list tables.
- BigQuery Data Viewer: This will provide Braze access to view datasets and their contents.
- BigQuery Job User: This will provide Braze access to run jobs<br><br>After creating the service account and granting permissions, generate a JSON key. Refer to [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) for more information. You'll update this to the Braze dashboard later.

{:start="3"}
3. If you have network policies in place, you must give Braze network access to your BigQuery instance. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Set up a source table in Databricks. You can use the names in the following example or choose your catalog, schema, and table names. You can also use a view or a materialized view instead of a table.

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

| FIELD NAME | TYPE | MODE |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | STRING, STRUCT, or MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |

{:start="2"}

2. Create a personal access token in your Databricks workspace.

- a. Select your Databricks username, then select **User Settings** from the dropdown menu.
- b. On the **Access tokens** tab, select **Generate new token**.
- c. Enter a comment that helps you to identify this token, such as "Braze CDI". 
- d. Change the token’s lifetime to no lifetime by leaving the **Lifetime (days)** box blank. Select **Generate**.
- e. Copy the displayed token, and then select **Done**. 
- f. Keep the token in a safe place until you need to enter it during the credential creation step in the Braze dashboard.

{:start="3"}
3. If you have network policies in place, you must give Braze network access to your Databricks instance. For a list of IPs, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) page.

{% endtab %}
{% tab Microsoft Fabric %}

Create one or more tables to use for your CDI integration with the following fields:

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

2. Set up a service principal and grant proper permissions. If you already have credentials from an existing sync, you can reuse those&#8212;just make sure to extend access to the catalog source table. To learn more about how to create a new service principal and credentials, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) page. 

{:start="3"}
3. If you have network policies in place, you must give Braze network access to your Microsoft Fabric instance. For a list of IPs, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}

- No `UPDATED_AT` column for S3 files
- Optional `DELETED` boolean to delete items

JSON Example:
```json
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

CSV Example:
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
1,"{""product_name"": ""Product 1"", ""price"": 1.01}"
```

For S3 setup details, see [File Storage Integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## How the integration works

Each time the sync runs, Braze will pull in all rows where `UPDATED_AT` is equal to or after the last timestamp synced. We recommend creating a view in your data warehouse from your catalog data to set up a source table that will fully refresh each time a sync runs. With views, you won't need to rewrite the query each time.

For example, if you have a table of product data (`product_catalog_1`) with `product_id` and three additional attributes, you could sync the below view:

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

- The data fetched from the integration will be used to create or update items in the target catalog based on the `id` provided.
- If DELETED is set to `true`, the corresponding catalog item will be deleted.
- The sync won't log data points, but all data synced will count toward your total catalog usage; this usage is measured based on the total data stored, so you don’t need to worry about only syncing changed data.
