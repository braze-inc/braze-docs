---
nav_title: Zero copy personalization
article_title: Zero-copy personalization using CDI (syncing canvas triggers)
page_order: 4
page_type: reference
description: "This page provides an overview of how to trigger Braze Canvases using CDI."

---


# Zero-copy personalization using CDI (syncing canvas triggers)

Learn how to sync canvas triggers using CDI for zero-copy personalization. This feature accesses user-specific information from your data storage solution and passes it to a destination canvas. Canvas steps can optionally include personalization fields that are not persisted on Braze user profiles.

Important:  
CDI canvas triggers are currently in early access. Contact your Braze account manager for access.

## Syncing canvas triggers

### Quick start guide

If you’re already familiar with Braze CDI, note that the setup for a canvas trigger sync closely follows the process for [user-data CDI integrations](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup), with the following caveats:

* Only external ID or user alias identifiers are supported. Email and phone numbers are not supported identifiers.  
* Only existing Braze users can be synced. New users cannot be created.  
* **`properties`** replaces the **`payload`** column. This is a JSON string of the fields you want to use as canvas entry properties for personalization.

To get started, simply choose the 'Canvas Triggers' data type when creating a new sync.

If needed, a step-by-step guide on how to use this new data type is provided below.

### Step 1: Set up data source for canvas triggers

{% tabs %}
{% tab Snowflake %}
1. Set up your source table in Snowflake. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.  

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

You can name the database, schema, and table as you’d like, but the column names should match the preceding definition.

* UPDATED_AT - The time this row was updated or added to the table. Only rows added or updated since the last sync will be synced.  
* Either external_id or alias_name and alias_label as user identifier column(s). These identify the users for whom you want to trigger canvas messaging.  
  * EXTERNAL_ID - Identifies the user to enter into the canvas. This should match the external_id value used in Braze.  
  * ALIAS_NAME and ALIAS_LABEL - These columns create a user alias object. alias_name should be a unique identifier, and alias_label specifies the alias type. Users may have multiple aliases with different labels, but only one alias_name per alias_label.  
* PROPERTIES - A JSON string of fields to make available as personalization properties in your canvas. This should contain user-specific information.

Note: Properties are not required for every row or user. However, properties values must be a valid JSON string. Input an empty {} string if there are no properties for the row.

2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the canvas triggers source table.  

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

3. If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).  

{% endtab %}
{% tab Redshift %}

1. Set up your source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

You can name the database, schema, and table as you’d like, but the column names should match the preceding definition.

* UPDATED_AT - The time this row was updated or added to the table. Only rows added or updated since the last sync will be synced.  
* Either external_id or alias_name and alias_label as user identifier column(s). These identify the users for whom you want to trigger canvas messaging.  
  * EXTERNAL_ID - Identifies the user to enter into the canvas. This should match the external_id value used in Braze.  
  * ALIAS_NAME and ALIAS_LABEL - These columns create a user alias object. alias_name should be a unique identifier, and alias_label specifies the alias type. Users may have multiple aliases with different labels, but only one alias_name per alias_label.  
* PROPERTIES - A JSON string of fields to make available as personalization properties in your canvas. This should contain user-specific information.

Note: Properties are not required for every row or user. However, properties values be a valid JSON string. Input an empty {} string if there are no properties for the row.

2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the canvas triggers source table.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

3. If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. (Optional) Create a new project or dataset for your source table.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

2. Set up your source table in BigQuery.

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

Refer to the following when creating your source table:

| Field Name | Type | Required? |
| :---- | :---- | :---- |
| **`UPDATED_AT`** | Timestamp | Yes |
| **`PROPERTIES`** | JSON | Yes |
| **`EXTERNAL_ID`** | STRING | NULLABLE |
| **`ALIAS_NAME`** | STRING | NULLABLE |
| **`ALIAS_LABEL`** | STRING | NULLABLE |

Note: Properties are not required for every row or user. However, properties values be a valid JSON string. Input an empty {} string if there are no properties for the row.

3. Create a user and grant permissions. If you already have credentials from another sync, you can reuse them as long as they have access to the canvas triggers table.

| Permission | Purpose |
| :---- | :---- |
| BigQuery Connection User | Allows Braze to connect. |
| BigQuery User | Allows Braze to run queries, read metadata, and list tables. |
| BigQuery Data Viewer | Allows Braze to view datasets and contents. |
| BigQuery Job User | Allows Braze to run jobs. |

After granting permissions, generate a JSON key. See [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) for instructions. You’ll upload it in the Braze dashboard later.

4. If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Create a catalog or schema for your source table.

**CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;**

2. Set up your source table in Databricks.

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

Refer to the following when creating your source table:

| Field Name | Type | Required? |
| :---- | :---- | :---- |
| **`UPDATED_AT`** | Timestamp | Yes |
| **`PROPERTIES`** | JSON | Yes |
| **`EXTERNAL_ID`** | STRING | NULLABLE |
| **`ALIAS_NAME`** | STRING | NULLABLE |
| **`ALIAS_LABEL`** | STRING | NULLABLE |

You can name the schema and table as you’d like, but the column names should match the preceding definition.

* UPDATED_AT - The time this row was updated or added to the table. Only rows added or updated since the last sync will be synced.  
* Either external_id or alias_name and alias_label as user identifier column(s). These identify the users for whom you want to trigger canvas messaging.  
  * EXTERNAL_ID - Identifies the user to enter into the canvas. This should match the external_id value used in Braze.  
  * ALIAS_NAME and ALIAS_LABEL - These columns create a user alias object. alias_name should be a unique identifier, and alias_label specifies the alias type. Users may have multiple aliases with different labels, but only one alias_name per alias_label.  
* PROPERTIES - A string or struct of fields to make available as personalization properties in your canvas. This should contain user-specific information.

Note: Properties are not required for every row or user. However, properties values must be valid JSON strings. Input an empty {} string if there are no properties for the row.

3. Create a personal access token in Databricks:

* Select your username, then select **User Settings.**  
* On the **Access tokens** tab, select **Generate new token.**  
* Add a comment to identify the token, such as “Braze CDI”.  
* Leave **Lifetime (days)** blank for no expiration, then select **Generate**.  
* Copy and save the token securely for use in the Braze dashboard.

4. If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Fabric %}
1. Set up your source table in Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

2. Create a service principal and grant permissions. If you already have credentials from another sync, you can reuse them—just make sure they have access to the accounts table.

3. If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab File Storage %}
To sync canvas triggers from file storage, create a source file with the following fields.

| Field | Required? | Description |
| :---- | :---- | :---- |
| **`EXTERNAL_ID`** | Yes, one of external_id or alias_name and alias_label | This identifies the user you want to update. This should match the **`external_id`** value used in Braze. |
| **`ALIAS_NAME` and `ALIAS_LABEL`** | Yes, one of external_id or alias_name and alias_label | These two columns create a user alias object. **`alias_name`** should be a unique identifier, and **`alias_label`** specifies the type of alias. Users may have multiple aliases with different labels, but only one **`alias_name`** per **`alias_label`**. |
| **`PROPERTIES`** | Yes | JSON string of fields to make available as personalization properties in your canvas. This should contain user-specific information. |

note:  
Filenames must follow AWS rules and be unique. Append timestamps to help ensure uniqueness. For more on Amazon S3 syncing, see [File Storage Integrations](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).


{% endtab %}
{% endtabs %}

### Step 2: Configure your destination canvas

Next, set up your destination canvas for canvas triggers. Create a new or select an existing API-triggered canvas. See [here](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) for instructions on how to create a canvas with an API-triggered delivery schedule type.

After selecting the API-triggered delivery schedule type, continue with canvas setup and build your canvas. Canvases can range from simple single-message sends to complex customer workflows with multiple steps.

Within your canvas steps, use [canvas entry properties](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) to personalize messages with properties fields from your source table in Step 1.

For example, if in Step 1 you instrumented a properties field for account__balance, you would use the following Liquid templating to personalize your message: {{canvas_entry_properties.${account_balance}}}.

Once you've built your canvas, launch it and proceed to Step 3.

### Step 3: Create your zero copy sync

With your source setup complete and destination canvas launched, navigate to **Data Settings > Cloud Data Ingestion** in Braze to create a new data sync.

* 1. Set up connection: Enter connection details (or reuse existing credentials) and the source table from Step 1.  
* 2. Set up sync details:   
  * Name the integration.  
  * Choose the ‘Canvas triggers’ data type.  
  * Choose your destination canvas (from Step 2).  
  * Choose a sync frequency  
* 3. Set up notification preferences  
* 4. Test connection:  
  * If connecting to Snowflake, first add the public key displayed on the dashboard to the user created for Braze to connect to Snowflake. To complete this step, you will need someone with SECURITYADMIN access or higher in Snowflake.  
  * Click 'Test Connection' to ensure everything works as expected.  
* Save the sync to begin syncing canvas triggers.

Once the sync runs, users in your source table will begin to enter the canvas. Use canvas analytics and the Cloud Data Ingestion sync logs page to monitor performance.

Important:  
Review your entire configuration (from sync behavior to canvas setup) to avoid unexpected sends. Canvas settings such as rate limiting, frequency capping, and segmentation filters can further refine message delivery.

It is recommended to conduct a trial run with a small or test audience before implementing production use cases.

### Product Limits

CDI canvas triggers utilize your REST API rate limit for /canvas/trigger/send. If you are using this endpoint simultaneously with CDI canvas triggers and your REST API integration, expect the combined usage to count towards your rate limit.

While CDI canvas triggers are in EA, note the following product limits:

* Up to 5 active canvas trigger syncs per workspace  
* Each sync run will enter users into its respective destination canvas at a maximum rate of approximately 3.75M users per hour.  
  * Be prepared for longer source-to-canvas entry times when:  
    * Syncing more than 3.75M users per sync run.  
    * Using CDI canvas triggers when already saturating your REST API’s [rate limit for /canvas/trigger/send](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).