---
nav_title: Connected Sources
article_title: Connected Sources
description: "This reference article covers how to use Braze Cloud Data Ingestion to sync relevant data with your Snowflake, Redshift, BigQuery, and Databricks integration."
page_order: 2
page_type: reference

---

# Connected Sources

> Connected sources are a zero-copy alternative to directly syncing data with Braze’s Cloud Data Ingestion (CDI) feature. With a connected source, directly query your data warehouse to create new segments–without copying any of the underlying data to Braze. 

Once a connected source is added to your Braze workspace, you can create a CDI segment within Segment Extensions. CDI Segments lets you write SQL that directly queries on your own data warehouse (using data there that’s made available via your CDI Connected Source), and creates and maintains a group of users that can be targeted within Braze. 

{% alert update %}
Note that this feature is currently in Early Access and available only for Snowflake sources.
{% endalert %}

{% alert important %}
Because connected sources run on your data warehouse directly, you will incur all costs associated with running these queries in your data warehouse. Connected sources do not consume data points, and CDI segments do not consume SQL Segment credits.
{% endalert %}


## Integration

Cloud Data Ingestion connected sources require some setup on the Braze side and in your instance. Follow these steps to set up the integration&#8722;some steps will be done in your data warehouse and some steps will be done in your Braze dashboard.

{% tabs %}
{% tab Snowflake %}
**In your data warehouse**
1. Create a role and grant permissions to query and create tables in a schema
2. Set up your warehouse and give access to that role
3. Create a user for that role
4. Depending on your configuration, you may need to allow Braze IPs in your Snowflake network policy 

**In the Braze dashboard**
{:start="5"}
5. Create a new connected source in the Braze dashboard
6. Configure the sync details for the connected source
7. Retrieve the public key provided in the Braze dashboard 

**In your data warehouse**
{:start="8"}
8. Append the public key from the Braze dashboard to the [Snowflake user for authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)

When complete, you can use the connected source to create one or more CDI Segments. 
{% endtab %}
{% endtabs %}

### Setting up your data warehouse

First, set up the source data and required resources in your data warehouse environment.  A connected source may reference one or more tables, so the user created for Braze to use should have permissions for all tables you want to be available in the connected source. 

{% tabs %}
{% tab Snowflake %}
#### Step 1: Create a role and grant permissions

Create a role for your connected source to use. This role will be used to generate the list of tables available in your CDI segments, and to query source tables to create new segments. Once the connected source is created, Braze will discover the names and description of all tables available to the user in the source schema.

You may choose to grant access to all tables in a schema, or grant privileges only to specific tables. Whichever tables the Braze role has access to will be available to query in the CDI segment.

The role must have the permission to create tables. This is because Braze will create a table with your CDI Segment query results before updating the segment in Braze. We will create one table per segment, and the same table will be recreated each time the segment is refreshed. 

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


#### Step 2: Set up the warehouse and give access to Braze role

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
The warehouse will need to have the **auto-resume** flag on. If not, you will need to grant Braze additional `OPERATE` privileges on the warehouse for Braze to turn it on when it's time to run the query.
{% endalert %}

#### Step 3: Set up the user
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

You will share connection information with Braze and receive a public key to append to the user in a later step.

{% alert note %}
When connecting different workspaces to the same Snowflake account, you must create a unique user for each Braze workspace where you are creating an integration. Within a workspace, you can reuse the same user across integrations, but integration creation will fail if a user on the same Snowflake account is duplicated across workspaces.
{% endalert %}

#### Step 4: Allow Braze IPs in Snowflake network policy (optional)
Depending on the configuration of your Snowflake account, you may need to allow the following IP addresses in your Snowflake network policy. For more information on enabling this, see the relevant Snowflake documentation on [modifying a network policy](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

| For Instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | For Instances `EU-01` and `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% endtabs %}

### Creating a connected source in the Braze dashboard

Next, create a connected source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion**. Navigate to the **Connected Sources** tab and click **Create data connection**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), go to **Cloud Data Ingestion** under **Data**.
{% endalert %}


{% tabs %}
{% tab Snowflake %}

#### Step 5: Add Snowflake connection information and source table
Input the information for your Snowflake data warehouse and source schema, then proceed to the next step.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Step 6: Configure sync details
Next, choose a name for connected source. This name will be used in the list of available sources when you create a new CDI Segment. 

Configure a max runtime for this source. Braze will automatically abort any queries that exceed the max runtime when we are creating or refreshing a segment. The maximum runtime allowed is 60 minutes; a lower runtime will reduce costs incurred on your Snowflake account. 

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating a larger warehouse to the Braze user.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})


#### Step 7: Note the public key  

In the **Test connection** page, you will see a RSA public key. Note this down. You will need it complete the integration in Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% endtabs %}

### Finalize configuring the data warehouse

{% tabs %}
{% tab Snowflake %}

#### Step 8: Add a public key to the Braze user

Add the public key you noted during the last step to your user in Snowflake. This will allow Braze to connect to Snowflake. For details on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

If you want to rotate the keys at any point, Braze can generate a new key pair and provide you with the new public key.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Once you have added the key to the user in Snowflake, select **Test Connection** in Braze, and then select **Done**. Your connected source is now created and ready to use in CDI Segments.

{% endtab %}
{% endtabs %}

{% alert note %}
You must successfully test a source before it can move from Draft to Active state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}

## Setting up additional integrations or users (optional)
{% tabs %}
{% tab Snowflake %}
You may set up multiple integrations with Braze, but each integration should be configured to connect a different schema. When creating additional connections, you may reuse existing credentials if connecting to the same Snowflake account.

If you reuse the same user and role across integrations, you will not need to add the public key again.
{% endtab %}
{% endtabs %}

## Using the connected source
Once the source is created, it can be used to create one or more CDI Segments. For more information on creating a segment with this source, see the [CDI Segments documentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating a larger warehouse to the Braze user.
{% endalert %}
