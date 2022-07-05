---
nav_title: Braze Cloud Ingestion 
permalink: /cloud_ingestion/
description: "This reference article covers Braze Cloud Ingestion and how to sync relevant user data to your Snowflake integration."
hidden: true
---

# Braze Cloud Ingestion - Snowflake integration

{% alert important %}
Braze Cloud Ingestion is currently in beta. Contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

## What is Braze Cloud Ingestion?

Braze Cloud Ingestion allows you to set up a direct connection from your Snowflake instance to Braze to sync relevant user data. Once synced to Braze, these attributes can be used for personalization or segmentation.

### How it works

With Braze Cloud Ingestion, you set up an integration between your Snowflake instance and Braze app group to sync data on a recurring basis. This sync runs on a schedule you set, and each integration can have a different schedule. 

When a sync runs, Braze will directly connect to your Snowflake and pull all new data from the table, and update the corresponding user profiles on your Braze dashboard. Each time the sync runs, any updated data will be reflected on the user profiles.

### What gets synced

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Any rows where `UPDATED_AT` is later than the last synced row will be selected and pulled into Braze.

### Data point usage 

Each attribute sent for a user will consume one data point. It’s up to you to only send the required data. Data point tracking for Cloud Ingestion is equivalent to tracking through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track) endpoint. Refer to [Data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) for more information.

## Data setup recommendations

### Only write new or updated attributes to minimize consumption

We will sync all attributes in a given row, regardless of whether they are the same as what’s currently on the user profile. Given that, we recommend that you only sync attributes that you want to add or update.

### Removing an attribute

If you want to completely remove an attribute from a user’s profile, you can set it to `null`. If you want an attribute to remain unchanged, don't send it to Braze until it’s been updated.

### Create JSON string from another table

If you prefer to store each attribute in its own column internally, you need to convert those columns to a JSON string to populate the sync with Braze. To do that, you can use a query like: 
```json
CREATE TABLE "PURCHASE_DATA" 
    (purchase_date datetime,
     purchase_amount number,
     quantity number,
     address string);

SELECT TO_JSON(OBJECT_CONSTRUCT (*)) FROM "PURCHASE_DATA";
```

## Product setup

During the beta phase, onboarding to Cloud Ingestion requires some manual integration steps managed by Braze. Follow these steps to set up the integration: 
1. In your Snowflake instance, set up the table(s) or view(s) you want to sync to Braze.
2. Submit a form to Braze with the relevant integration information.
3. Braze will send you a public key to [append to the Snowflake user](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) for authentication.
4. Sync starts.

### Set up tables or views

#### Step 1: Set up the table

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT datetime not null, 
     EXTERNAL_ID string not null,
     PAYLOAD string not null)
;
```

You can name the database, schema, and table as you’d like, but the column names should match the above definition.

- `UPDATED_AT` - The time this row was updated in or added to the table. We will only sync rows that have been added or updated since the last sync.
- `EXTERNAL_ID` - This identifies the user you want to update. You can use one of `external_id`, `user_alias`, or `braze_id`.
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
The warehouse will need to have the **auto-resume** flag on. If not, you will need to grant us additional `OPERATE` privileges on the warehouse for us to turn it on when it’s time to run the query.
{% endalert %}

#### Step 4: Set up the user

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

After this step, you will share connection information with Braze and receive a public key to append to the user. 

#### Step 5: Allow Braze IPs in Snowflake network policy (optional)

Allow the following IP addresses in your Snowflake network policy. For more information on enabling this, see the relevant Snowflake documentation on [modifying a network policy](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies). 

| Braze IPs |
| -------- |
| 23.21.118.191 |
| 34.206.23.173 |
| 50.16.249.9 |
| 52.4.160.214 |
| 54.87.8.34 |
| 54.156.35.251 |
| 52.54.89.238 |
| 18.205.178.15 |

### Share connection information with Braze 

Set up your integration by sharing the connection information with Braze through [this form](https://docs.google.com/forms/d/1df0dbw4G_XBkSD_ikT0-zJGg5K6OTOKKe-ARUx9j21M/edit). When you fill out the form, we will ask for the following information:

- Snowflake connection information
  - Account name 
  - Warehouse 
  - Database
  - Table 
  - User 
  - Role
- Braze integration information
  - App group ID - The ID of the app group where the data should be synced (you can find this ID in the URL if you go to your app group settings page). If you need help, please ask
  - API key - Submit an existing API key to use, or we can create a new one for you
- Sync information
  - Integration name - A label you can use to identify the integration(s) you set up with your Snowflake instance.
  - Sync schedule - To start, we will ask for a time to run the sync daily. After verifying the connection works as expected for a few days, we can increase the sync frequency.

### Add public key to Snowflake user

After submitting the form with connection details, Braze will generate an SSH key pair and securely store the private key. You will add the public key to the Braze user, and we’ll use this key pair to authenticate with your Snowflake instance. 

Alter your Braze user set up earlier with the public key:

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

Add the public key to the Braze user. For additional information on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). If you want to rotate the keys at any point, we can generate a new key pair and provide you with the new public key. 

### Verify the connection and start sync

Braze will verify that we can select from the table you provided earlier using the user, role, warehouse, and key pair. Assuming everything works, we’ll start the recurring sync. 

### Set up additional integrations (optional)

You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. To do this, submit the [onboarding form](https://docs.google.com/forms/d/1df0dbw4G_XBkSD_ikT0-zJGg5K6OTOKKe-ARUx9j21M/edit) again. 

Note that if you reuse the same user and role across integrations, you will not need to go through the step of adding the public key again. 

## Product limitations

| Limitations | Description |
| --- | --- |
| Number of integrations | There is no limit on how many integrations you can set up. However, you will only be able to set up one integration per table or view. 
| Number of rows | There is no limit on the number of rows you can sync. Each row will only be synced once, based on the `UPDATED` column. |
| Attributes per row | Each row should contain a single user ID and a JSON object with up to 50 attributes. Each key in the JSON object counts as one attribute (i.e., an array counts as one attribute). |
| Data type | Currently, the product only supports user attributes. In the future, you’ll also be able to sync events and purchases. |
| Braze region | The beta product is only available to Braze customers in the US region (Dashboard is in one of `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`)
| Snowflake region | You can connect your Snowflake instance in any region or cloud to Braze using this product. |
{: .reset-td-br-1 .reset-td-br-2}
