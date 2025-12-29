---
nav_title: Zero-copy personalization
article_title: Zero-copy personalization using CDI
page_order: 4
page_type: reference
description: "This page provides an overview of how to trigger Braze Canvases using CDI."
---

# Zero-copy personalization using CDI

> Learn how to sync Canvas triggers using CDI for zero-copy personalization. This feature accesses user-specific information from your data storage solution and passes it to a destination Canvas. Canvas steps can optionally include personalization fields that are not persisted on Braze user profiles.

{% alert important %}
CDI Canvas triggers are currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Syncing Canvas triggers

### Quick start steps

If you’re already familiar with Braze CDI, note that the setup for a Canvas trigger sync closely follows the process for [user-data CDI integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), with the following caveats:

- Only external ID or user alias identifiers are supported. Email and phone numbers are not supported identifiers.  
- Only existing Braze users can be synced. New users cannot be created.  
- `properties` replaces the `payload` column. This is a JSON string of the fields you want to use as Canvas entry properties for personalization.

To get started, select the **Canvas Triggers** data type when creating a new sync.

### Using Canvas triggers 

#### Step 1: Set up data source for Canvas triggers

{% tabs %}
{% tab Snowflake %}

##### Step 1.1: Set up your source table in Snowflake

You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.  

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

* `UPDATED_AT`: The time this row was updated or added to the table. Only rows added or updated since the last sync will be synced.  
* Either `external_id` or `alias_name` and `alias_label` as the user identifier column. These identify the users for whom you want to trigger Canvas messaging.  
  * `EXTERNAL_ID`: Identifies the user to enter into the Canvas. This should match the `external_id` value used in Braze.  
  * `ALIAS_NAME` and `ALIAS_LABEL`: These columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the alias type. Users may have multiple aliases with different labels, but only one alias_name per `alias_label`.  
* `PROPERTIES`: A JSON string of fields to make available as personalization properties in your Canvas. This should contain user-specific information.

{% alert note %}
Properties are not required for every row or user. However, properties values must be a valid JSON string. Input an empty `{}` string if there are no properties for the row.
{% endalert %}

##### Step 1.2: Set up credentials

Set up a role, warehouse, and user, and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the Canvas triggers source table.  

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

##### Step 1.3: Configure network policies

If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Step 1.1: Set up your source table in Redshift

You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.

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

* `UPDATED_AT`: The time this row was updated or added to the table. Only rows added or updated since the last sync will be synced.  
* Either `external_id` or `alias_name` and `alias_label` as the user identifier column. These identify the users for whom you want to trigger Canvas messaging.  
  * `EXTERNAL_ID`: Identifies the user to enter into the Canvas. This should match the `external_id` value used in Braze.  
  * `ALIAS_NAME` and `ALIAS_LABEL`: These columns create a user alias object. `alias_name` should be a unique identifier, and alias_label specifies the alias type. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`.  
* `PROPERTIES`: A JSON string of fields to make available as personalization properties in your Canvas. This should contain user-specific information.

{% alert note %}
Properties are not required for every row or user. However, properties values be a valid JSON string. Input an empty `{}` string if there are no properties for the row.
{% endalert %}

##### Step 1.2: Set up credentials

Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the Canvas triggers source table.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Step 1.3: Configure network policies 

If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Step 1.1: Create a new project or dataset for your source table (optional)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Step 1.2: Set up your source table in BigQuery
Refer to the following when creating your source table:  

| Field Name | Type | Required? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Timestamp | Yes | 
| **`PROPERTIES`** | JSON | Yes | 
| **`EXTERNAL_ID`** | STRING | NULLABLE | 
| **`ALIAS_NAME`** | STRING | NULLABLE | 
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Properties are not required for every row or user. However, properties values be a valid JSON string. Input an empty `{}` string if there are no properties for the row.
{% endalert %}

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

##### Step 1.3: Set up credentials

Create a user and grant permissions. If you already have credentials from another sync, you can reuse them as long as they have access to the canvas triggers table.

| Permission | Purpose |
| :---- | :---- |
| BigQuery Connection User | Allows Braze to connect. |
| BigQuery User | Allows Braze to run queries, read metadata, and list tables. |
| BigQuery Data Viewer | Allows Braze to view datasets and contents. |
| BigQuery Job User | Allows Braze to run jobs. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

After granting permissions, generate a JSON key. See [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) for instructions. You’ll upload it in the Braze dashboard later.

##### Step 1.4: Configure network policies 
If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Step 1.1: Create a catalog or schema for your source table.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Step 1.2: Set up your source table in Databricks

Refer to the following when creating your source table:

| Field name | Type | Required |
| :---- | :---- | :---- |
| `UPDATED_AT` | Timestamp | Yes |
| `PROPERTIES` | JSON | Yes |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

You can name the schema and table as you’d like, but the column names should match the preceding definition.

* `UPDATED_AT`: The time this row was updated or added to the table. Only rows added or updated since the last sync will be synced.  
* Either `external_id` or `alias_name` and `alias_label` as the user identifier column. These identify the users for whom you want to trigger Canvas messaging.  
  * `EXTERNAL_ID`: Identifies the user to enter into the Canvas. This should match the `external_id` value used in Braze.  
  * `ALIAS_NAME` and `ALIAS_LABEL`: These columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the alias type. Users may have multiple aliases with different labels, but only one alias_name per `alias_label`.  
* `PROPERTIES`: A string or struct of fields to make available as personalization properties in your Canvas. This should contain user-specific information.

{% alert note %}
Properties are not required for every row or user. However, properties values must be valid JSON strings. Input an empty `{}` string if there are no properties for the row.
{% endalert %}

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

##### Step 1.3: Set up credentials 

Create a personal access token in Databricks:

1. Select your username, then select **User Settings.**  
2. On the **Access tokens** tab, select **Generate new token.**  
3. Add a comment to identify the token, such as “Braze CDI”.  
4. Leave **Lifetime (days)** blank for no expiration, then select **Generate**.  
5. Copy and save the token securely for use in the Braze dashboard.

##### Step 1.4: Configure network policies 

If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Step 1.1: Set up your source table in Fabric

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

##### Step 1.2: Set up credentials 

Create a service principal and grant permissions. If you already have credentials from another sync, you can reuse them—just make sure they have access to the accounts table.

##### Step 1.3: Configure network policies 

If your account has network policies, allowlist the Braze IPs to enable the CDI service connection. For the list of IPs, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

To sync Canvas triggers from file storage, create a source file with the following fields.

| Field | Required | Description |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Yes, one of `external_id` or `alias_name`, and `alias_label` | This identifies the user you want to update. This should match the `external_id` value used in Braze. |
| `ALIAS_NAME` and `ALIAS_LABEL` | Yes, one of `external_id` or `alias_name` and `alias_label` | These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`. |
| `PROPERTIES` | Yes | JSON string of fields to make available as personalization properties in your Canvas. This should contain user-specific information. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Filenames must follow AWS rules and be unique. Append timestamps to help ensure uniqueness. For more on Amazon S3 syncing, see [File Storage Integrations](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Step 2: Configure your destination Canvas

1. Set up your destination Canvas for Canvas triggers. Create a new or select an existing API-triggered Canvas. Refer to [Entry schedule types]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) for instructions on how to create a canvas with an API-triggered delivery schedule type.
2. After selecting the API-triggered delivery schedule type, continue with Canvas setup and build your Canvas. Canvases can range from simple single-message sends to complex customer workflows with multiple steps.
3. Within your Canvas steps, use [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) to personalize messages with properties fields that you plan to sync from your source table.
  * For example, if in Step 1 you instrumented a properties field for `account_balance`, you would use the following Liquid templating to personalize your message: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. After building your Canvas, launch it and proceed to [Step 3](#step-3-create-your-zero-copy-sync).

#### Step 3: Create your zero copy sync

With your source setup complete and destination Canvas launched, create a new data sync:

1. In Braze, go to **Data Settings** > **Cloud Data Ingestion** .
1. Set up the connection by entering connection details (or reuse existing credentials) and the source table from [Step 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Provide a name the integration.
3. Select the **Canvas triggers** data type.
4. Choose your destination Canvas (from [Step 2](#step-2-configure-your-destination-canvas)).
5. Choose a sync frequency.
6. Set up notification preferences.
7. Select **Test Connection** to confirm everything works as expected. If connecting to Snowflake, first add the public key displayed on the dashboard to the user created for Braze to connect to Snowflake. To complete this step, you'll need **SECURITYADMIN** access or higher in Snowflake. 
8. Save the sync to begin syncing Canvas triggers.

When the sync runs, users in your source table will begin to enter the Canvas. Use Canvas analytics and the Cloud Data Ingestion sync logs page to monitor performance.

{% alert tip %}  
Review your entire configuration (from sync behavior to Canvas setup) to avoid unexpected sends. Canvas settings such as rate limiting, frequency capping, and segmentation filters can further refine message delivery.<br><br>We recommend conducting a trial run with a small or test audience before implementing production use cases.
{% endalert %}

### Considerations

CDI Canvas triggers utilize your REST API rate limit for `/canvas/trigger/send`. If you're using this endpoint simultaneously with CDI Canvas triggers and your REST API integration, expect the combined usage to count towards your rate limit.

While CDI Canvas triggers are in early access, consider the following details:

* Up to 5 active Canvas trigger syncs per workspace  
* Each sync run will enter users into its respective destination Canvas at a maximum rate of approximately 3.75 million users per hour.  
  * Be prepared for longer source-to-Canvas entry times when:  
    * Syncing more than 3.75M users per sync run.  
    * Using CDI Canvas triggers when already saturating your REST API's [rate limit for `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).