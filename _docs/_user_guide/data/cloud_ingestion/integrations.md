---
nav_title: Data Warehouse Integrations
article_title: Data Warehouse Integrations
description: "This page covers how to use Braze Cloud Data Ingestion to sync relevant data with your Snowflake, Redshift, BigQuery, and Databricks integration."
page_order: 2
page_type: reference

---

# Data warehouse storage integrations

> This page covers how to use Braze Cloud Data Ingestion (CDI) to sync relevant data with your Snowflake, Redshift, BigQuery, and Databricks integration.

## Setting up data warehouse integrations

Cloud Data Ingestion integrations require some setup on the Braze side and in your data warehouse instance. Follow these steps to set up the integration:

{% tabs %}
{% tab Snowflake %}
1. In your Snowflake instance, set up the tables or views you want to sync to Braze.
2. Create a new integration in the Braze dashboard.
3. Retrieve the public key provided in the Braze dashboard and [append it to the Snowflake user for authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Test the integration and start the sync.

{% alert tip %}
The [Snowflake quickstart guide](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) provides sample code and walks through the required steps to create an automated pipeline using Snowflake Streams and CDI to sync data to Braze. 
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Make sure Braze access is allowed to the Redshift tables you want to sync. Braze will connect to Redshift over the internet.
2. In your Redshift instance, set up the tables or views you want to sync to Braze.
3. Create a new integration in the Braze dashboard.
4. Test the integration and start the sync.
{% endtab %}
{% tab BigQuery %}
1. Create a service account and allow access to the BigQuery project(s) and dataset(s) that contain the data you want to sync.  
2. In your BigQuery account, set up the tables or views you want to sync to Braze.   
3. Create a new integration in the Braze dashboard.  
4. Test the integration and start the sync.  
{% endtab %}
{% tab Databricks %}
1. Create a service account and allow access to the Databricks project(s) and dataset(s) that contain the data you want to sync.  
2. In your Databricks account, set up the tables or views you want to sync to Braze.   
3. Create a new integration in the Braze dashboard.  
4. Test the integration and start the sync.

{% alert important %}
There may be two to five minutes of warm-up time when Braze connects to Classic and Pro SQL instances, which will lead to delays during connection setup and testing, as well as at the beginning of scheduled syncs. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Create a service principal and allow access to the Fabric workspace that will be used for your integration.   
2. In your Fabric workspace, set up the tables or views you want to sync to Braze.   
3. Create a new integration in the Braze dashboard.  
4. Test the integration and start the sync.
{% endtab %}
{% endtabs %}

### Step 1: Set up tables or views

{% tabs %}
{% tab Snowflake %}

#### Step 1.1: Set up the table

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

You can name the database, schema, and table as you'd like, but the column names should match the preceding definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- **User identifier columns** - Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, `braze_id`, `email` or `phone`). A source table may have columns for one, two, three, four, or all five identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias.
    - `EMAIL` - The user's email address. If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates. If you include both email and phone, we will use the email as the primary identifier.
    - `PHONE` - The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. 
- `PAYLOAD` - This is a JSON string of the fields you want to sync to the user in Braze.

#### Step 1.2: Set up the role and database permissions

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Update the names as needed, but the permissions should match the preceding example.

#### Step 1.3: Set up the warehouse and give access to Braze role

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
The warehouse needs to have the **auto-resume** flag on. If not, you will need to grant Braze additional `OPERATE` privileges on the warehouse for us to turn it on when it's time to run the query.
{% endalert %}

#### Step 1.4: Set up the user

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

After this step, you will share connection information with Braze and receive a public key to append to the user.

{% alert note %}
When connecting different workspaces to the same Snowflake account, you must create a unique user for each Braze workspace where you are creating an integration. Within a workspace, you can reuse the same user across integrations, but integration creation will fail if a user on the same Snowflake account is duplicated across workspaces.
{% endalert %}

#### Step 1.5: Allow Braze IPs in Snowflake network policy (optional)

Depending on the configuration of your Snowflake account, you may need to allow the following IP addresses in your Snowflake network policy. For more information on enabling this, see the relevant Snowflake documentation on [modifying a network policy](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Step 1.1: Set up the table 

Optionally, set up a new Database and Schema to hold your source table
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Create a table (or view) to use for your CDI integration
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

You can name the database, schema, and table as you'd like, but the column names should match the preceding definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- **User identifier columns** - Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, `braze_id`, `email` or `phone`). A source table may have columns for one, two, three, four, or all five identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias.
    - `EMAIL` - The user's email address. If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates. If you include both email and phone, we will use the email as the primary identifier.
    - `PHONE` - The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. 
- `PAYLOAD` - This is a JSON string of the fields you want to sync to the user in Braze.
 
#### Step 1.2: Create user and grant permissions 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

These are the minimum required permissions for this user. If creating multiple CDI integrations, you may want to grant permissions to a schema or manage permissions using a group. 

#### Step 1.3: Allow access to Braze IPs

If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. An example of the Redshift URL endpoint is "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Some important things to know:
- You may also need to change your security groups to allow Braze to access your data in Redshift.
- Make sure to explicitly allow inbound traffic on the IPs in the table and on the port used to query your Redshift cluster (default is 5439). You should explicitly allow Redshift TCP connectivity on this port even if the inbound rules are set to “allow all”.
- The endpoint for the Redshift cluster must be publicly accessible for Braze to connect to your cluster.
     - If you don't want your Redshift cluster to be publicly accessible, you can set up a VPC and EC2 instance to use an SSH tunnel to access the Redshift data. Check out this [AWS Knowledge Center post](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) for more information.
 
Allow access from the following IPs corresponding to your Braze dashboard’s region.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Step 1.1: Set up the table 

Optionally, set up a new project or dataset to hold your source table.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Create one or more tables to use for your CDI integration with the following fields:

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Field Name | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

You can name the project, dataset, and table as you'd like, but the column names should match the preceding definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- **User identifier columns** - Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, `braze_id`, `email` or `phone`). A source table may have columns for one, two, three, four, or all five identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias.
    - `EMAIL` - The user's email address. If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates. If you include both email and phone, we will use the email as the primary identifier.
    - `PHONE` - The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. 
   email varchar,
   phone_number varchar,
- `PAYLOAD` - This is a JSON string of the fields you want to sync to the user in Braze.

#### Step 1.2: Create a Service Account and grant permissions 

Create a service account in GCP for Braze to use to connect and read data from your table(s). The service account should have the below permissions: 

- **BigQuery Connection User:** This will allow Braze to make connections
- **BigQuery User:** This will provide Braze access to run queries, read dataset metadata, and list tables.
- **BigQuery Data Viewer:** This will provide Braze access to view datasets and their contents.
- **BigQuery Job User:** This will provide Braze access to run jobs

After creating the service account and granting permissions, generate a JSON key. See more information on how to do this [here](https://cloud.google.com/iam/docs/keys-create-delete). You will update this to the Braze dashboard later. 

#### Step 1.3: Allow access to Braze IPs    

If you have network policies in place, you must give Braze network access to your Big Query instance. Allow access from the below IPs corresponding to your Braze dashboard's region.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Step 1.1: Set up the table 

Optionally, set up a new Catalog or Schema to hold your source table.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Create one or more tables to use for your CDI integration with the following fields:


```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Field Name | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

You can name the schema and table as you'd like, but the column names should match the preceding definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- **User identifier columns** - Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, `braze_id`, `email` or `phone`). A source table may have columns for one, two, three, four, or all five identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias. 
    - `EMAIL` - The user's email address. If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates. If you include both email and phone, we will use the email as the primary identifier.
    - `PHONE` - The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. 
- `PAYLOAD` - This is a string or struct of the fields you want to sync to the user in Braze.

#### Step 1.2: Create an Access Token  

For Braze to access Databricks, a personal access token needs to be created.

1. In your Databricks workspace, select your Databricks username in the top bar, and then select **User Settings** from the dropdown.
2. On the Access tokens tab, select **Generate new token**.
3. Enter a comment that helps you to identify this token, such as "Braze CDI", and change the token’s lifetime to no lifetime by leaving the Lifetime (days) box empty (blank).
4. Select **Generate**.
5. Copy the displayed token, and then select **Done**.

Keep the token in a safe place until you need to enter it on the Braze dashboard during the credential creation step.

#### Step 1.3: Allow access to Braze IPs    

If you have network policies in place, you must give Braze network access to your Databricks instance. Allow access from the below IPs corresponding to your Braze dashboard's region.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Step 1.1: Set up the service principal and grant access
Braze will connect to your Fabric warehouse using a service principal with Entra ID authentication. You will create a new service principal for Braze to use, and grant access to Fabric resources as needed. Braze will need the following details to connect:    

* Tenant ID (also called directory) for your Azure account 
* Principal ID (also called application ID) for the service principal 
* Client secret for Braze to authenticate

1. In the Azure portal, navigate to Microsoft Entra admin center, and then App Registrations 
2. Select **+ New registration** under **Identity** > **Applications** > **App registrations**.
3. Enter a name, and then select `Accounts in this organizational directory only` as the supported account type. Then, select **Register**. 
4. Select the application (service principal) you just created, then navigate to **Certificates & secrets** > **+ New client secret**.
5. Enter a description for the secret, and set an expiry period for the secret. Then, select **Add**. 
6. Note the client secret created to use in the Braze setup. 

{% alert note %}
Azure doesn't allow unlimited expiry on service principal secrets. Remember to refresh the credentials before they expire to maintain the flow of data to Braze.
{% endalert %}

#### Step 1.2: Grant access to Fabric resources 
You will provide access for Braze to connect to your Fabric instance. In your Fabric admin portal, navigate to **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.    

* In **Developer settings** enable "Service principals can use Fabric APIs" so Braze can connect using Microsoft Entra ID.
* In **OneLake settings** enable "Users can access data stored in OneLake with apps external to Fabric" so that the service principal can access data from an external app.


#### Step 1.3: Set up the table
Braze supports both tables and views in Fabric Warehouses. If you need to create a new warehouse, go to **Create > Data Warehouse > Warehouse** in the Fabric console. 

```json
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

You can name the warehouse, schema, and table or view as you'd like, but the column names should match the preceding definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- **User identifier columns** - Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, `braze_id`, `email` or `phone`). A source table may have columns for one, two, three, four, or all five identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias.
    - `EMAIL` - The user's email address. If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates. If you include both email and phone, we will use the email as the primary identifier.
    - `PHONE` - The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. 
- `PAYLOAD` - This is a JSON string of the fields you want to sync to the user in Braze.


#### Step 1.4: Get warehouse connection string 
You will need the SQL endpoint for your warehouse in order for Braze to connect. In order to retrieve this, go to the **workspace** in Fabric, and in the list of items, hover over the warehouse name and select **Copy SQL connection string**.

![The "Fabric Console" page in Microsoft Azure, where users should retrieve the SQL Connection String.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Step 1.5: Allow Braze IPs in Firewall (Optional)

Depending on the configuration of your Microsoft Fabric account, you may need to allow the following IP addresses in your firewall to allow traffic from Braze. For more information on enabling this, see the relevant documentation on [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Step 2: Create a new integration in the Braze dashboard

{% tabs %}
{% tab Snowflake %}

In the Braze Dashbord, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and then select **Snowflake Import**.

#### Step 2.1: Add Snowflake connection information and source table

Input the information for your Snowflake data warehouse and source table, then proceed to the next step.

![The "Create new import sync" page for Snowflake in the Braze dashboard with example data entered into Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Step 2.2: Configure sync details

Next, choose a name for your sync and input contact emails. We'll use this contact information to notify you of any integration errors, such as unexpected removal of access to the table.

Contact emails will only receive notifications of global or sync-level errors such as missing tables, permissions, and others. They will not receive row-level issues. Global errors indicate critical problems with the connection that prevent syncs from running. Such problems can include the following:

- Connectivity issues
- Lack of resources
- Permissions issues
- (For catalogs syncs only) Catalog tier is out of space

![The "Create new import sync" page for Snowflake in the Braze dashboard with example data added to Step 2: "Set up sync details".]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

You will also choose the data type and sync frequency. Frequency can be anywhere from every 15 minutes to once per month. We'll use the time zone configured in your Braze dashboard to schedule the recurring sync. Supported data types are Custom Attributes, Custom Events, and Purchase Events, and the data type for a sync cannot be changed after creation. 

#### Add a public key to the Braze user

At this point, you must go back to Snowflake to complete the setup. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake.

For additional information on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). If you want to rotate the keys at any point, we can generate a new key pair and provide you with the new public key.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

In the Braze Dashbord, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and then select **Amazon Redshift Import**.

#### Step 2.1: Add Redshift connection information and source table

Input the information for your Redshift data warehouse and source table. If you're using a private network tunnel, toggle the slider and input the tunnel information. Then proceed to the next step.

![The "Create new import sync" page for Redshift in the Braze dashboard, set to Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Step 2.2: Configure sync details

Next, choose a name for your sync and input contact emails. We'll use this contact information to notify you of any integration errors, such as unexpected removal of access to the table.

Contact emails will only receive notifications of global or sync-level errors such as missing tables, permissions, and others. They will not receive row-level issues. Global errors indicate critical problems with the connection that prevent syncs from running. Such problems can include the following:

- Connectivity issues
- Lack of resources
- Permissions issues
- (For catalogs syncs only) Catalog tier is out of space

![The "Create new import sync" page for Redshift in the Braze dashboard with some example data added to Step 2: "Set up sync details".]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

You will also choose the data type and sync frequency. Frequency can be anywhere from every 15 minutes to once per month. We'll use the time zone configured in your Braze dashboard to schedule the recurring sync. Supported data types are Custom Attributes, Custom Events, and Purchase Events, and the data type for a sync cannot be changed after creation. 
{% endtab %}
{% tab BigQuery %}

In the Braze Dashbord, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and then select **Google BigQuery Import**.

#### Step 2.1: Add BigQuery connection information and source table

Upload the JSON key and provide a name for the service account, then input the details of your source table.

![The "Create new import sync" page for BigQuery in the Braze dashboard, set to Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Step 2.2: Configure sync details

Next, choose a name for your sync and input contact emails. We'll use this contact information to notify you of any integration errors, such as unexpected removal of access to the table.

Contact emails will only receive notifications of global or sync-level errors such as missing tables, permissions, and others. They won't receive row-level issues. Global errors indicate critical problems with the connection that prevent syncs from running. Such problems can include the following:

- Connectivity issues
- Lack of resources
- Permissions issues
- (For catalogs syncs only) Catalog tier is out of space

![The "Create new import sync" page for BigQuery in the Braze dashboard, set to Step 2: "Set up sync details".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

You will also choose the data type and sync frequency. Frequency can be anywhere from every 15 minutes to once per month. We'll use the time zone configured in your Braze dashboard to schedule the recurring sync. Supported data types are Custom Attributes, Custom Events, Purchase Events, and User Deletes. The data type for a sync cannot be changed after creation. 

{% endtab %}
{% tab Databricks %}

In the Braze Dashbord, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and then select **Databricks Import**.

#### Step 2.1: Add Databricks connection information and source table

Input the information for your Databricks data warehouse and source table, then proceed to the next step.

![The "Create new import sync" page for Databricks in the Braze dashboard, set to Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Step 2.2: Configure sync details

Next, choose a name for your sync and input contact emails. We'll use this contact information to notify you of any integration errors, such as unexpected removal of access to the table.

Contact emails will only receive notifications of global or sync-level errors such as missing tables, permissions, and others. They will not receive row-level issues. Global errors indicate critical problems with the connection that prevent syncs from running. Such problems can include the following:

- Connectivity issues
- Lack of resources
- Permissions issues
- (For catalogs syncs only) Catalog tier is out of space

![The "Create new import sync" page for Databricks in the Braze dashboard, set to Step 2: "Set up sync details".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

You will also choose the data type and sync frequency. Frequency can be anywhere from every 15 minutes to once per month. We'll use the time zone configured in your Braze dashboard to schedule the recurring sync. Supported data types are custom attributes, custom events, purchase events, and user deletes. The data type for a sync cannot be changed after creation. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Step 2.1: Set up a Cloud Data Ingestion sync

You will create a new data sync for Microsoft Fabric. In the Braze dashbord, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and then select **Microsoft Fabric Import**.

#### Step 2.2: Add Microsoft Fabric connection information and source table

Input the information for your Microsoft Fabric warehouse credentials and source table, then proceed to the next step.

- Credentials Name is a label for these credentials in Braze, you can set a helpful value here
- See steps in section 1 for details on how to retrieve Tenant ID, Principal ID, Client Secret, and Connection String

![The "Create new import sync" page for Microsoft in the Braze dashboard, set to Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### Step 2.3: Configure sync details

Next, configure the following details for your sync: 

- Sync name 
- Data type - Supported data types are custom attributes, custom events, purchase events, catalogs, and user deletes. The data type for a sync cannot be changed after creation. 
- Sync Frequency - Frequency can be anywhere from every 15 minutes to once per month. We'll use the time zone configured in your Braze dashboard to schedule the recurring sync. 
  - Non-recurring syncs can be triggered manually or via the [API]({{site.baseurl}}/api/endpoints/cdi) 

![The "Create new import sync" page for Microsoft Fabric in the Braze dashboard, set to Step 2: "Set up sync details".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### Step 2.4: Configure notification preferences

Next, input contact emails. We'll use this contact information to notify you of any integration errors, such as unexpected removal of access to the table, or alert when specific rows fail to update .

By default, contact emails will only receive notifications of global or sync-level errors such as missing tables, permissions, and others. Global errors indicate critical problems with the connection that prevent syncs from running. Such problems can include the following:

- Connectivity issues
- Lack of resources
- Permissions issues
- (For catalogs syncs only) Catalog tier is out of space

You may also configure alerts for row-level issues, or choose to receive an alert every time a sync runs successfully. 

![The "Create new import sync" page for Microsoft Fabric in the Braze dashboard, set to Step 3: "Set up notification preferences".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### Step 3: Test connection

{% tabs %}
{% tab Snowflake %}

Return to the Braze dashboard and select **Test connection**. If successful, you'll see a preview of the data. If, for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![The "Create new import sync" page for Snowflake in the Braze dashboard with Step 3: "Test connection" displaying an RSA public key.]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Return to the Braze dashboard and select **Test connection**. If successful, you'll see a preview of the data. If, for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![The "Create new import sync" page for Redshift in the Braze dashboard, set to Step 3: "Test connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Return to the Braze dashboard and select **Test connection**. If successful, you'll see a preview of the data. If, for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![The "Create new import sync" page for Redshift Private Network in the Braze dashboard, with Step 4: "Test connection" displaying an RSA public key.]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

After all configuration details for your sync are entered, select **Test connection**. If successful, you'll see a preview of the data. If, for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![The "Create new import sync" page for BigQuery in the Braze dashboard, set to Step 3: "Test connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

After all configuration details for your sync are entered, select **Test connection**. If successful, you'll see a preview of the data. If, for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![The "Create new import sync" page for Databricks in the Braze dashboard, set to Step 3: "Test connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

After all configuration details for your sync are entered, select **Test connection**. If successful, you'll see a preview of the data. If, for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![The "Create new import sync" page for Microsoft Fabric in the Braze dashboard, set to Step 4: "Test connection".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
You must successfully test an integration before it can move from Draft to Active state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}

## Set up additional integrations or users (optional)

{% tabs %}
{% tab Snowflake %}
You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the Snowflake account.

![The "Create new import sync" page for Snowflake in the Braze dashboard, with the "Select credentials" dropdown open in Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

If you reuse the same user and role across integrations, you will **not** need to go through the step of adding the public key again.
{% endtab %}
{% tab Redshift %}
You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the same Snowflake or Redshift account.

![The "Create new import sync" page for Redshift in the Braze dashboard, with the "Select credentials" dropdown open in Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

If you reuse the same user across integrations, you cannot delete the user in the Braze dashboard until it's removed from all active syncs.
{% endtab %}
{% tab BigQuery %}

You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the same BigQuery account.

![The "Create new import sync" page for BigQuery in the Braze dashboard, with the "Select credentials" dropdown open in Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

If you reuse the same user across integrations, you cannot delete the user in the Braze dashboard until it's removed from all active syncs.

{% endtab %}
{% tab Databricks %}

You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the same Databricks account.

![The "Create new import sync" page for Databricks in the Braze dashboard, with the "Select credentials" dropdown open in Step 1: "Set up connection".]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

If you reuse the same user across integrations, you cannot delete the user in the Braze dashboard until it's removed from all active syncs.

{% endtab %}
{% tab Microsoft Fabric %}

You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the same Fabric account.

If you reuse the same user across integrations, you cannot delete the user in the Braze dashboard until it's removed from all active syncs.

{% endtab %}
{% endtabs %}

## Running the sync

{% tabs %}
{% tab Snowflake %}
When activated, your sync will run on the schedule configured during setup. If you want to run the sync outside the normal testing schedule or to fetch the most recent data, select **Sync Now**. This run will not impact regularly scheduled future syncs.

![The "Data Import" page for Snowflake in the Braze dashboard displaying the option to "Sync now" from the vertical ellipses menu.]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
When activated, your sync will run on the schedule configured during setup. If you want to run the sync outside the normal testing schedule or to fetch the most recent data, select **Sync Now**. This run will not impact regularly scheduled future syncs.

![The "Data Import" page for Redshift in the Braze dashboard displaying the option to "Sync now" from the vertical ellipses menu.]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

When activated, your sync will run on the schedule configured during setup. If you want to run the sync outside the normal testing schedule or to fetch the most recent data, select **Sync Now**. This run will not impact regularly scheduled future syncs.

![The "Data Import" page for BigQuery in the Braze dashboard displaying the option to "Sync now" from the vertical ellipses menu.]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

When activated, your sync will run on the schedule configured during setup. If you want to run the sync outside the normal testing schedule or to fetch the most recent data, select **Sync Now**. This run will not impact regularly scheduled future syncs.

![The "Data Import" page for Databricks in the Braze dashboard displaying the option to "Sync now" from the vertical ellipses menu.]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

When activated, your sync will run on the schedule configured during setup. If you want to run the sync outside the normal testing schedule or to fetch the most recent data, select **Sync Now**. This run will not impact regularly scheduled future syncs.

{% endtab %}

{% endtabs %}

