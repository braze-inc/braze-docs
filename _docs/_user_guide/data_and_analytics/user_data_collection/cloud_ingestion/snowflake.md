---
nav_title: Snowflake
article_title: Braze Cloud Data Ingestion for Snowflake
description: "This reference article covers Braze Cloud Data Ingestion and how to sync relevant user data to your Snowflake integration."
page_order: 1
page_type: reference

---

# Cloud Data Ingestion for Snowflake

## Product setup

New Cloud Data Ingestion integrations require some setup on the Braze side and in your Snowflake instance. Follow these steps to set up the integration:
1. In your Snowflake instance, set up the table(s) or view(s) you want to sync to Braze
2. Create a new integration in the Braze dashboard
3. Retrieve the public key provided in the Braze dashboard and [append it to the Snowflake user for authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)
4. Test the integration and start the sync

### Set up tables or views

#### Step 1: Set up the table

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

You can name the database, schema, and table as you'd like, but the column names should match the preceding definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- User identifier columns. Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, or `braze_id`. A source table may columns for one, two, or all three identifier types. 
    - `EXTERNAL_ID` - This identifies the user you want to update.  This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` - these two columns together create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - the Braze user identifier. This is genereated by the Braze SDK and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an External User ID or User Alias. 
- `PAYLOAD` - This is a JSON string of the fields you want to sync to the user in Braze.

#### Step 2: Set up the role and database permissions

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Update the names as needed, but the permissions should match the preceding example.

#### Step 3: Set up the warehouse and give access to Braze role

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
The warehouse will need to have the **auto-resume** flag on. If not, you will need to grant us additional `OPERATE` privileges on the warehouse for us to turn it on when it's time to run the query.
{% endalert %}

#### Step 4: Set up the user

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

After this step, you will share connection information with Braze and receive a public key to append to the user.

{% alert note %}
When connecting different app groups to the same Snowflake account, you must create a unique user for each Braze app group where you are creating an integration. Within an app group, you can reuse the same user across integrations, but integration creation will fail if a user on the same Snowflake account is duplicated across app groups.
{% endalert %}

#### Step 5: Allow Braze IPs in Snowflake network policy (optional)

Depending on the configuration of your Snowflake account, you may need to allow the following IP addresses in your Snowflake network policy. For more information on enabling this, see the relevant Snowflake documentation on [modifying a network policy](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

| For Instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` | For Instances `EU-01` and `EU-02` |
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

### Create a new integration in the Braze dashboard

Navigate to the Snowflake page on Braze, under **Technology Partners**, and click **Create new import sync**.

1. **Add Snowflake connection information and source table**<br>
Input the information for your Snowflake account and source table, then proceed to the next step.<br>![][1]<br><br>
2. **Configure sync details**<br>
Next, choose a name for your sync and input contact emails. We'll use this contact information to notify you of any integration errors (e.g., access to the table was removed unexpectedly).<br>![][2]<br><br> You will also choose the data type and sync frequency. Frequency can be anywhere in the range of every 15 minutes to once per month. We'll use the time zone configured in your Braze dashboard to schedule the recurring sync. Supported data types are Custom Attributes, Custom Events, and Purchase Events and the data type for a sync cannot be changed after creation. 

### Add a public key to the Braze user
At this point, you will need to go back to Snowflake to complete the setup. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake.

For additional information on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). If you want to rotate the keys at any point, we can generate a new key pair and provide you with the new public key.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

### Test connection

Once the user is updated with the public key, return to the Braze dashboard and click **Test connection**. If successful, you'll see a preview of the data. If for some reason, we can't connect, we'll display an error message to help you troubleshoot the issue.

![][3]

{% alert note %}
You must successfully test an integration before it can move from Draft into Active state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}

### Set up additional integrations or users (optional)

You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the snowflake account.
![][4]

If you reuse the same user and role across integrations, you will **not** need to go through the step of adding the public key again.

### Running the sync

Once activated, your sync will run on the schedule configured during setup. If you want to run the sync outside of the normal schedule for testing or to fetch the most recent data, click **Sync Now**. This run will not impact regularly scheduled future syncs.  
![][5]

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
