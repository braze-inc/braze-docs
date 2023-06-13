---
nav_title: Sync Catalogs Data
article_title: Cloud Data Ingestion Sync Catalogs Data
page_order: 2.1
page_type: reference
description: "This reference article provides an overview of how to sync catalogs data."

---

# Sync Catalogs data
 
## Step 1: Create a new catalog

Before creating a new Cloud Data Ingestion (CDI) integration for [Catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/), you will need to create a new catalog or identify an existing catalog you want to use for the integration. There are a few ways to create a new catalog and any of these will work for the CDI integration:
- Upload a [CSV]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-1-upload-csv)
- Create a catalog in the [Braze dashboard]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-2-create-in-browser)
- Create a catalog through the [API]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

The key things to note when creating this catalog are:
- You should use the same name for the catalog and CDI integration 
- Any changes to the catalog schema (e.g., adding new fields, changing field type) must be made through the catalogs dashboard or API before updated data is synced through CDI. We recommend making these updates when the sync is paused or not scheduled to run to avoid conflicts between your Snowflake data and the schema in Braze.

## Step 2: Integrate Cloud Data Ingestion with Snowflake
The Snowflake setup for a catalogs sync closely follows the process for [user-data CDI integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

1. Set up a source table in Snowflake. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
  ```json
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216),
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL
    );
    ```
2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, just make sure to extend access to the catalog source table.
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
3. If your Snowflake account has network policies, whitelist the Braze IPs so the CDI service can connect. For a list of IPs, see the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, navigate to **Technology Partners > Snowflake**, and create a new sync.
5. Enter connection details (or reuse existing credentials) and the source table.
6. Proceed to step 2 of the setup flow, select the “Catalogs” sync type, and input the integration name and schedule. Note that the name of the integration should **exactly match** the name of the catalog you previously created.
7. Choose a sync frequency and proceed to the next step.
8. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake. To complete this step, you will need someone with `SECURITYADMIN` access or higher in Snowflake. 
9. Click **Test Connection** to ensure everything works as expected. 
10. Save the sync, and use the synced catalog data for all your personalization use cases. 

## How the integration works
- Each time the sync runs, we will pull in all rows where `UPDATED_AT` is after the last timestamp synced. 
- To set up a source table that will fully refresh each time a sync runs, we’d recommend creating a view from your catalog data. For example, if you have a table of product data (`product_catalog_1`) with `product_id`, `price`, and three additional attributes, you could sync the below view:
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
- The data fetched from the integration will be used to create or update items in the target catalog based on the `id` provided. 
- The sync will not consume data points, but all data synced will count towards your total catalog usage; this usage is measured based on total data stored, so you don’t need to worry about only syncing changed data. 