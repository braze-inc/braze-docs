---
nav_title: Cloud Data Ingestion
article_title: Braze Cloud Data Ingestion
alias: /cloud_ingestion/
description: "This reference article covers Braze Cloud Data Ingestion and how to sync relevant user data to your Snowflake integration."
page_order: 6.1
page_type: reference

---

# Braze Cloud Data Ingestion - Snowflake integration

{% alert important %}
Braze Cloud Data Ingestion is currently in early access. Contact your Braze account manager if you are interested in participating in the Early Access.
{% endalert %}

## What is Braze Cloud Data Ingestion?

Braze Cloud Data Ingestion allows you to set up a direct connection from your Snowflake instance to Braze to sync relevant user data. Once synced to Braze, these attributes can be used for personalization or segmentation.

### How it works

With Braze Cloud Data Ingestion, you set up an integration between your Snowflake instance and Braze app group to sync data on a recurring basis. This sync runs on a schedule you set, and each integration can have a different schedule. Syncs can run as frequently as every 15 minutes or as infrequently as once per month. For customers who need syncs to occur more frequently than 15 minutes, please speak with your customer success manager, or consider using REST API calls for real-time data ingestion.

When a sync runs, Braze will directly connect to your Snowflake instance, retrieve all new data from the specified table, and update the corresponding user profiles on your Braze dashboard. Each time the sync runs, any updated data will be reflected on the user profiles.

### What gets synced

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Any rows where `UPDATED_AT` is later than the last synced row will be selected and pulled into Braze.

In Snowflake, you add the following users and attributes to your table, setting the `UPDATED_AT` time to the time you add this data:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| '2022-07-19 09:07:23' | 'customer_1234' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| '2022-07-19 09:07:23' | 'customer_3456' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| '2022-07-19 09:07:23' | 'customer_5678' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |

During the next scheduled sync, all rows with a `UPDATED_AT` timestamp later than the most recent timestamp will be synced to the Braze user profiles. Fields will be updated or added, so you do not need to sync the full user profile each time. After the sync, users will reflect the new updates:

```json
{
  "external_id":"customer_1234",
  "email":"jane@exaple.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@exaple.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@exaple.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Data point usage

Each attribute sent for a user will consume one data point. It’s up to you to only send the required data. Data point tracking for Cloud Data Ingestion is equivalent to tracking through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track) endpoint. Refer to [Data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) for more information.

## Data setup recommendations

#### Only write new or updated attributes to minimize consumption

We will sync all attributes in a given row, regardless of whether they are the same as what’s currently on the user profile. Given that, we recommend you only sync attributes you want to add or update.

#### Use a UTC timestamp for the UPDATED_AT column

The `UPDATED_AT` column should be in UTC to prevent issues with daylight savings time.  Prefer UTC-only functions, such as `SYSDATE()` instead of `CURRENT_DATE()` whenever possible.

#### Removing an attribute

If you want to completely remove an attribute from a user’s profile, you can set it to `null`. If you want an attribute to remain unchanged, don't send it to Braze until it’s been updated.

#### Create JSON string from another table

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

New Cloud Data Ingestion integrations require some setup on the Braze side and in your Snowflake instance. Follow these steps to set up the integration:
1. In your Snowflake instance, set up the table(s) or view(s) you want to sync to Braze.
2. Create a new integration in the Braze dashboard.
3. Retrieve the public key provided in the Braze dashboard and [append it to the Snowflake user for authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Test the integration and start the sync.

### Set up tables or views

#### Step 1: Set up the table

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     EXTERNAL_ID VARCHAR(16777216) NOT NULL,
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

You can name the database, schema, and table as you’d like, but the column names should match the preceding definition.

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

1. Add Snowflake connection information and source table
Input the information for your Snowflake account and source table, then proceed to the next step.<br>![][1]<br><br>
2. Name sync and set frequency
Next, choose a name for your sync and input contact emails. We’ll use this contact information to notify you of any integration errors (e.g., access to the table was removed unexpectedly).<br>![][2]<br><br>You will also choose the sync frequency. Frequency can be anywhere in the range of every 15 minutes to once per month. We’ll use the time zone configured in your Braze dashboard to schedule the recurring sync.

### Add a public key to the Braze user
At this point, you will need to go back to Snowflake to complete the setup. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake.

For additional information on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). If you want to rotate the keys at any point, we can generate a new key pair and provide you with the new public key.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

### Test connection

Once the user is updated with the public key, return to the Braze dashboard and click **Test connection**. If successful, you’ll see a preview of the data. If for some reason, we can’t connect, we’ll display an error message to help you troubleshoot the issue.

![][3]

{% alert note %}
You must successfully test an integration before it can move from Draft into Active state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}

### Set up additional integrations or users (optional)

You may set up multiple integrations with Braze, but each integration should be configured to sync a different table. When creating additional syncs, you may reuse existing credentials if connecting to the snowflake account.
![][4]

If you reuse the same user and role across integrations, you will **not** need to go through the step of adding the public key again.


## Product limitations

| Limitations | Description |
| --- | --- |
| Number of integrations | There is no limit on how many integrations you can set up. However, you will only be able to set up one integration per table or view.
| Number of rows | There is no limit on the number of rows you can sync. Each row will only be synced once, based on the `UPDATED` column. |
| Attributes per row | Each row should contain a single user ID and a JSON object with up to 50 attributes. Each key in the JSON object counts as one attribute (i.e., an array counts as one attribute). |
| Data type | You can sync user attributes through Cloud Data Ingestion. |
| Braze region | This product is avialable in all Braze regions. Any Braze region can connect to any Snowflake region |
| Snowflake region | You can connect your Snowflake instance in any region or cloud to Braze using this product. |
{: .reset-td-br-1 .reset-td-br-2}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
