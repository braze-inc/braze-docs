---
nav_title: Connected Sources
article_title: Connected Sources
description: "This page covers how to use Braze Cloud Data Ingestion to sync relevant data with your Snowflake, Redshift, BigQuery, and Databricks integration."
page_order: 2
page_type: reference

---

# Connected Sources

> Connected sources are a zero-copy alternative to directly syncing data with Braze’s Cloud Data Ingestion (CDI) feature. A connected source directly queries your data warehouse to create new segments without copying any of the underlying data to Braze. 

After adding a connected source to your Braze workspace, you can create a CDI segment within Segment Extensions. CDI Segment Extensions let you write SQL that directly queries your data warehouse (using data there that’s made available through your CDI Connected Source), and creates and maintains a group of users that can be targeted within Braze. 

For more information on creating a segment with this source, refer to [CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert warning %}
Because connected sources run on your data warehouse directly, you will incur all costs associated with running these queries in your data warehouse. If your Braze pricing includes data points, connected sources don't log data points, and CDI Segment Extensions don't consume SQL segment credits.
{% endalert %}

## Integrating connected sources

### Step 1: Connect your resources

Cloud Data Ingestion connected sources require some setup on Braze and in your instance. Follow these steps to set up the integration&#8722;some steps will be done in your data warehouse and some steps will be done in your Braze dashboard.

{% tabs %}
{% tab Snowflake %}
**In your data warehouse**
1. Create a role and grant permissions to query and create tables in a schema.
2. Set up your warehouse and give access to that role.
3. Create a user for that role.
4. Depending on your configuration, you may need to allow Braze IPs in your Snowflake network policy.

**In the Braze dashboard**

{: start="5"} 
5. Create a new connected source in the Braze dashboard.
6. Configure the sync details for the connected source.
7. Retrieve the public key provided in the Braze dashboard.

**In your data warehouse**

{: start="8"} 
8. Append the public key from the Braze dashboard to the [Snowflake user for authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). When you're finished, you can use the connected source to create one or more CDI Segment Extensions. 
{% endtab %}

{% tab Redshift %}
1. Set up the source data and required resources in your Redshift environment.
2. Create a new connected source in the Braze dashboard.
4. Test the integration.
5. Use the connected source to create one or more CDI Segment Extensions.
{% endtab %}

{% tab BigQuery %}
1. Set up the source data and required resources in your BigQuery environment.
2. Create a service account and allow access to the BigQuery project(s) and dataset(s) that contain the data you want to sync.  
3. Create a new connected source in the Braze dashboard.
4. Test the integration.
5. Use the connected source to create one or more CDI Segment Extensions.
{% endtab %}

{% tab Databricks %}
1. Set up the source data and required resources in your Databricks environment.
2. Create a service account and allow access to the Databricks project(s) and dataset(s) that contain the data you want to sync.  
3. Create a new connected source in the Braze dashboard.
4. Test the integration.
5. Use the connected source to create one or more CDI Segment Extensions.

{% alert important %}
There may be two to five minutes of warm-up time when Braze connects to Classic and Pro SQL instances, which will lead to delays during connection setup and testing, as well as during CDI Segment Extension creation and refresh. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Create a service principal and allow access to the Fabric workspace that will be used for your integration.   
2. In your Fabric workspace, set up the source data and grant permissions to your service principal 
3. Create a new connected source in the Braze dashboard.
4. Test the integration.
5. Use the connected source to create one or more CDI Segment Extensions.
{% endtab %}

{% endtabs %}

### Step 2: Set up your data warehouse

Set up the source data and required resources in your data warehouse environment. The connected source may reference one or more tables, so ensure your Braze user has permission to access all tables you want in the connected source.

{% tabs %}
{% tab Snowflake %}
#### Step 2.1: Create a role and grant permissions

Create a role for your connected source to use. This role will be used to generate the list of tables available in your CDI Segment Extensions, and to query source tables to create new segments. After the connected source is created, Braze will discover the names and description of all tables available to the user in the source schema.

You may choose to grant access to all tables in a schema, or grant privileges only to specific tables. Whichever tables the Braze role has access to will be available to query in the CDI Segment Extension.

The `create table` permission is required so Braze can create a table with your CDI Segment Extension query results before updating the segment in Braze. Braze will create a temporary table per segment, and the table will only persist while Braze is updating the segment.

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Step 2.2: Set up the warehouse and give access to Braze role

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
The warehouse needs to have the **auto-resume** flag turned on. If it's not, you'll need to grant Braze additional `OPERATE` privileges on the warehouse for Braze to turn it on when it's time to run the query.
{% endalert %}

#### Step 2.3: Set up the user
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

You will share connection information with Braze and receive a public key to append to the user in a later step.

{% alert note %}
When connecting different workspaces to the same Snowflake account, you must create a unique user for each Braze workspace where you are creating an integration. Within a workspace, you can reuse the same user across integrations, but integration creation will fail if a user on the same Snowflake account is duplicated across workspaces.
{% endalert %}

#### Step 2.4: Allow Braze IPs in your Snowflake network policy (optional)

Depending on the configuration of your Snowflake account, you may need to allow the following IP addresses in your Snowflake network policy. For more information on doing this, refer to the relevant Snowflake documentation on [modifying a network policy](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Step 2.1: Create user and grant permissions 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Create a user for your connected source to use. This user will be used to generate the list of tables available in your CDI Segment Extensions, and to query source tables to create new segments. After the connected source is created, Braze will discover the names and description of all tables available to the user in the source schema. If creating multiple CDI integrations, you may want to grant permissions to a schema or manage permissions using a group. 

You may choose to grant access to all tables in a schema, or grant privileges only to specific tables. Whichever tables the Braze role has access to will be available to query in the CDI Segment Extension. Be sure to grant access to any new tables to the user when they're created, or set default permissions for the user. 

The `create table` permission is required so Braze can create a table with your CDI Segment Extension query results before updating the segment in Braze. Braze will create a temporary table per segment, which will only persist while Braze updates the segment.


#### Step 2.2: Allow access to Braze IPs    

If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the below IPs corresponding to your Braze dashboard's region. 

You may also need to change your security groups to allow Braze access to your data in Redshift. Make sure to explicitly allow inbound traffic on the IPs below and on the port used to query your Redshift cluster (default is 5439). You should explicitly allow Redshift TCP connectivity on this port even if the inbound rules are set to "allow all". In addition, it is important that the endpoint for the Redshift cluster be publicly accessible in order for Braze to connect to your cluster.

If you don't want your Redshift cluster to be publicly accessible, you can set up a VPC and EC2 instance to use an ssh tunnel to access the Redshift data. For more information, refer to [AWS: How do I access a private Amazon Redshift cluster from my local machine?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Step 2.1: Create a Service Account and grant permissions 

Create a service account in GCP for Braze to use to connect and read data from your table(s). The service account should have the below permissions: 

- **BigQuery Connection User:** Allows Braze to make connections.
- **BigQuery User:** Provides Braze access to run queries, read dataset metadata, and list tables.
- **BigQuery Data Viewer:** Provides Braze access to view datasets and their contents.
- **BigQuery Job User:** Provides Braze access to run jobs.
- **bigquery.tables.create** Provides Braze access to create temporary tables during segment refresh.

Create a service account for your connected source to use. This user will be used to generate the list of tables available in your CDI Segment Extensions, and to query source tables to create new segments. After the connected source is created, Braze will discover the names and description of all tables available to the user in the source schema. 

You may choose to grant access to all tables in a dataset, or grant privileges only to specific tables. Whichever tables the Braze role has access to will be available to query in the CDI Segment Extension. 

The `create table` permission is required so Braze can create a table with your CDI Segment Extension query results before updating the segment in Braze. Braze will create a temporary table per segment, and the table will only persist while Braze is updating the segment. 

After creating the service account and granting permissions, generate a JSON key. For more information, refer to [Google Cloud: Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete). You'll upload this to the Braze dashboard later.

#### Step 2.2: Allow access to Braze IPs    

If you have network policies in place, you must give Braze network access to your Big Query instance. Allow access from the below IPs corresponding to your Braze dashboard's region.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Step 2.1: Create an access token  

For Braze to access Databricks, a personal access token needs to be created.

1. In your Databricks workspace, select your Databricks username in the top bar, then select **User Settings** from the dropdown.
2. Make sure the service account has `CREATE TABLE` priviliges on the schema used for the connected souce. 
3. On the **Access tokens** tab, select **Generate new token**.
4. Enter a comment that helps you to identify this token, such as "Braze CDI", and change the token’s lifetime to no lifetime by leaving the Lifetime (days) box empty (blank).
5. Select **Generate**.
6. Copy the displayed token, and then select **Done**.

This token will be used to generate the list of tables available in your CDI Segment Extensions, and to query source tables to create new segments. After the connected source is created, Braze will discover the names and description of all tables available to the user in the source schema. 

You may choose to grant access to all tables in a schema, or grant privileges only to specific tables. Whichever tables the Braze role has access to will be available to query in the CDI Segment Extension.

The `create table` permission is required so Braze can create a table with your CDI Segment Extension query results before updating the segment in Braze. Braze will create a temporary table per segment, which will only persist while Braze updates the segment. 

Keep the token in a safe place until you need to enter it on the Braze dashboard during the credential creation step.

#### Step 2.2: Allow access to Braze IPs    

If you have network policies in place, you must give Braze network access to your Databricks instance. Allow access from the below IPs corresponding to your Braze dashboard's region.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Step 2.1: Grant access to Fabric resources 
Braze will connect to your Fabric warehouse using a service principal with Entra ID authentication. You will create a new service principal for Braze to use, and grant access to Fabric resources as needed. Braze will need the following details to connect:    

* Tenant ID (also called directory) for your Azure account 
* Principal ID (also called application ID) for the service principal 
* Client secret for Braze to authenticate

1. In the Azure portal, navigate to the Microsoft Entra admin center, and then **App Registrations**.
2. Select **+ New registration** under **Identity > Applications > App registrations** 
3. Enter a name, and select `Accounts in this organizational directory only` as the supported account type. Then, select **Register**. 
4. Select the application (service principal) you just created, then navigate to **Certificates & secrets > + New client secret**
5. Enter a description for the secret, and set an expiry period for the secret. Then, select **Add**. 
6. Note the client secret created to use in the Braze setup. 

{% alert note %}
Azure doesn't allow unlimited expiry on service principal secrets. Remember to refresh the credentials before they expire in order to maintain the flow of data to Braze.
{% endalert %}

#### Step 2.2: Grant access to Fabric resources 
You will provide access for Braze to connect to your Fabric instance. In your Fabric admin portal, navigate to **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.    

* In **Developer settings** enable "Service principals can use Fabric APIs" so Braze can connect using Microsoft Entra ID.
* In **OneLake settings** enable "Users can access data stored in OneLake with apps external to Fabric" so that the service principal can access data from an external app.

#### Step 2.3: Get warehouse connection string 

You will need the SQL endpoint for your warehouse in order for Braze to connect. To retrieve the SQL endpoint, go to the **workspace** in Fabric, and in the list of items, hover over the warehouse name and select **Copy SQL connection string**.

![The "Fabric Console" page in Microsoft Azure, where users should retrieve the SQL Connection String.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Step 2.4: Allow Braze IPs in Firewall (Optional)

Depending on the configuration of your Microsoft Fabric account, you may need to allow the following IP addresses in your firewall to allow traffic from Braze. For more information on enabling this, see the relevant documentation on [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Step 3: Create a connected source in the Braze dashboard

{% tabs %}
{% tab Snowflake %}
#### Step 3.1: Add Snowflake connection information and source table

Create a connected source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, and then select **Create new data sync** > **Snowflake Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Input the information for your Snowflake data warehouse and source schema, then proceed to the next step.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Step 3.2: Configure sync details

Choose a name for the connected source. This name will be used in the list of available sources when you create a new CDI Segment Extension. 

Configure a maximum runtime for this source. Braze will automatically abort any queries that exceed the maximum runtime when it's creating or refreshing a segment. The maximum runtime allowed is 60 minutes; a lower runtime will reduce costs incurred on your Snowflake account. 

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating a larger warehouse to the Braze user.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Step 3.3: Note the public key  

In the **Test connection** step, take note of the RSA public key. You'll need it to complete the integration in Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Step 3.1: Add Redshift connection information and source table

Create a connected source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, and then select **Create data connection** > **Amazon Redshift Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Input the information for your Redshift data warehouse and source schema, then proceed to the next step.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Step 3.2: Configure sync details

Choose a name for the connected source. This name will be used in the list of available sources when you create a new CDI Segment Extension. 

Configure a maximum runtime for this source. Braze will automatically abort any queries that exceed the maximum runtime when it's creating or refreshing a segment. The maximum runtime allowed is 60 minutes; a lower runtime will reduce costs incurred on your Redshift account. 

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating a larger warehouse to the Braze user.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Step 3.3: Note the public key (optional)

If your credentials have **Connect with SSH Tunnel** selected, take note of the RSA public key in the **Test connection** step. You'll need it to complete the integration in Redshift.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Step 3.1: Add BigQuery connection information and source table

Create a connected source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, and then select **Create new data sync** > **Google BigQuery Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Input the information for your BigQuery project and dataset, then proceed to the next step.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Step 3.2: Configure sync details

Choose a name for the connected source. This name will be used in the list of available sources when you create a new CDI Segment Extension. 

Configure a maximum runtime for this source. Braze will automatically abort any queries that exceed the maximum runtime when it's creating or refreshing a segment. The maximum runtime allowed is 60 minutes; a lower runtime will reduce costs incurred on your BigQuery account. 

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating a larger warehouse to the Braze user.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Step 3.3: Test the connection

Select **Test Connection** to verify that the list of tables visible to the user is what you expect, then select **Done**. Your connected source is now created and ready to use in CDI Segment Extensions.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Step 3.1: Add Databricks connection information and source table

Create a connected source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, and then select **Create new data sync** > **Databricks Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Input the information for your Databricks credentials and, optional catalog and source schema, then proceed to the next step.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Step 3.2: Configure sync details

Choose a name for the connected source. This name will be used in the list of available sources when you create a new CDI Segment Extension. 

Configure a maximum runtime for this source. Braze will automatically abort any queries that exceed the maximum runtime when it's creating or refreshing a segment. The maximum runtime allowed is 60 minutes; a lower runtime will reduce costs incurred on your Databricks account. 

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating a larger warehouse to the Braze user.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Step 3.3: Test the connection

Select **Test Connection** to verify that the list of tables visible to the user is what you expect, then select **Done**. Your connected source is now created and ready to use in CDI Segment Extensions.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Step 3.1: Add Microsoft Fabric connection information and source table

Create a connected source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, and then select **Create new data sync** > **Microsoft Fabric Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Input the information for your Microsoft Fabric credentials, as well as the source warehouse and schema, then proceed to the next step.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Step 3.2: Configure sync details

Choose a name for the connected source. This name will be used in the list of available sources when you create a new CDI Segment Extension. 

Configure a maximum runtime for this source. Braze will automatically abort any queries that exceed the maximum runtime when it's creating or refreshing a segment. The maximum runtime allowed is 60 minutes; a lower runtime will reduce costs incurred on your Microsoft Fabric account. 

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or scaling the Fabric capacity.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Step 3.3: Test the connection

Select **Test Connection** to verify that the list of tables visible to the user is what you expect, then select **Done**. Your connected source is now created and ready to use in CDI Segment Extensions.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Step 4: Finalize the data warehouse configuration

{% tabs %}
{% tab Snowflake %}
Add the public key you noted during the last step to your user in Snowflake. This will allow Braze to connect to Snowflake. For details on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

If you want to rotate the keys at any point, you can create a new public key by going to **Data Access Management** in **Cloud Data Ingestion** and selecting **Generate New Key** for the respective account.

![Data Access Management for Snowflake Data Access Credentials, with a button to Generate New Key.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

After you add the key to the user in Snowflake, select **Test Connection** in Braze, and then select **Done**. Your connected source is now created and ready to use in CDI Segment Extensions.
{% endtab %}

{% tab Redshift %}
If connecting with an SSH tunnel, add the public key you noted during the last step to the SSH tunnel user. 

After you add the key to the user, select **Test Connection** in Braze, and then select **Done**. Your connected source is now created and ready to use in CDI Segment Extensions.

{% endtab %}
{% tab BigQuery %}
This doesn't apply to BigQuery.

{% endtab %}
{% tab Databricks %}
This doesn't apply to Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
This doesn't apply to Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
You must successfully test a source before it can move from the "draft" to the "active" state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}

## Setting up additional integrations or users (optional)

{% tabs %}
{% tab Snowflake %}
You may set up multiple integrations with Braze, but each integration should be configured to connect a different schema. When creating additional connections, you may reuse existing credentials if connecting to the same Snowflake account.

If you reuse the same user and role across integrations, you won't need to add the public key again.
{% endtab %}

{% tab Redshift %}
You may set up multiple sources with Braze, but each source should be configured to connect a different schema. When creating additional sources, you may reuse existing credentials if connecting to the same Redshift account. 
{% endtab %}

{% tab BigQuery %}
You may set up multiple sources with Braze, but each source should be configured to connect a different dataset. When creating additional sources, you may reuse existing credentials if connecting to the same BigQuery account. 
{% endtab %}

{% tab Databricks %}
You may set up multiple sources with Braze, but each source should be configured to connect a different schema. When creating additional sources, you may reuse existing credentials if connecting to the same Databricks account.
{% endtab %}

{% tab Microsoft Fabric %}
You may set up multiple sources with Braze, but each source should be configured to connect a different schema. When creating additional sources, you may reuse existing credentials if connecting to the same Azure account.
{% endtab %}
{% endtabs %}

## Using the connected source

After the source is created, you can use it to create one or more CDI Segment Extensions. For more information on creating a segment with this source, refer to the [CDI Segment Extensions documentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating more compute resources (such as a larger warehouse) to the Braze user.
{% endalert %}
