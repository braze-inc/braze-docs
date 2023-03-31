---
nav_title: Overview and Best Practices
article_title: Cloud Data Ingestion overview and best practices
page_order: 0
page_type: reference
description: "This reference article provides an overview of Cloud Data Ingestion, best practices, and product limitations."

---

# Braze Cloud Data Ingestion

## What is Cloud Data Ingestion?

Braze Cloud Data Ingestion allows you to set up a direct connection from your data warehouse to Braze to sync relevant user attributes, events, and purchases. Once synced to Braze, this data can be leveraged for use cases such as personalization or segmentation. Cloud Data Ingestion can connect to Snowflake and Redshift data warehouses.

{% alert important %}
Braze Cloud Data Ingestion for Redshift is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

### How it works

With Braze Cloud Data Ingestion, you set up an integration between your data warehouse instance and Braze app group to sync data on a recurring basis. This sync runs on a schedule you set, and each integration can have a different schedule. Syncs can run as frequently as every 15 minutes or as infrequently as once per month. For customers who need syncs to occur more frequently than 15 minutes, please speak with your customer success manager, or consider using REST API calls for real-time data ingestion.

When a sync runs, Braze will directly connect to your data warehouse instance, retrieve all new data from the specified table, and update the corresponding user profiles on your Braze dashboard. Each time the sync runs, any updated data will be reflected on the user profiles.

### Supported data types 

Sync user attributes, custom events, and purchases through Cloud Data Ingestion. Data for a user can be updated by external ID, user alias, or Braze ID. 

### What gets synced

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Any rows where `UPDATED_AT` is later than the last synced row will be selected and pulled into Braze.

In your data warehouse, you add the following users and attributes to your table, setting the `UPDATED_AT` time to the time you add this data:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |

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

Each attribute sent for a user will consume one data point. It's up to you to only send the required data. Data point tracking for Cloud Data Ingestion is equivalent to tracking through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track) endpoint. Refer to [Data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) for more information.

## Data setup recommendations

#### Only write new or updated attributes to minimize consumption

We will sync all attributes in a given row, regardless of whether they are the same as what's currently on the user profile. Given that, we recommend only syncing attributes you want to add or update.

#### Use a UTC timestamp for the UPDATED_AT column

The `UPDATED_AT` column should be in UTC to prevent issues with daylight savings time. Prefer UTC-only functions, such as `SYSDATE()` instead of `CURRENT_DATE()` whenever possible.

#### Separate EXTERNAL_ID from PAYLOAD column 
The PAYLOAD object should not include an external id or other id type. 

#### Removing an attribute

You can set it to' null' if you want to completely remove an attribute from a user's profile. If you want an attribute to remain unchanged, don't send it to Braze until it's been updated.

#### Create JSON string from another table

If you prefer to store each attribute in its own column internally, you need to convert those columns to a JSON string to populate the sync with Braze. To do that, you can use a query like:

{% tabs %}
{% tab Snowflake %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    SELECT JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% endtabs %}

#### Using the UPDATED_AT timestamp

We use the `UPDATED_AT` timestamp to track what data has been synced successfully to Braze. If many rows are written with the same timestamp while a sync is running, this may lead to duplicate data being synced to Braze. Some suggestions to avoid duplicate data:
- If you are setting up a sync against a `VIEW`, do not use `CURRENT_TIMESTAMP` as the default value. This will cause all data to sync every time the sync runs because the `UPDATED_AT` field will evaluate to the time our queries are run. 
- If you have very long-running pipelines or queries writing data to your source table, avoid running these concurrently with a sync, or avoid using the same timestamp for every row inserted.
- Use a transaction to write all rows that have the same timestamp.

#### Example table configuration

We have a public [GitHub repository](https://github.com/braze-inc/braze-examples/tree/main/data-ingestion) for customers to share best practices or code snippets. To contribute your own snippets, create a pull request!

## Product limitations

| Limitations | Description |
| --- | --- |
| Number of integrations | There is no limit on how many integrations you can set up. However, you will only be able to set up one integration per table or view.
| Number of rows | There is no limit on the number of rows you can sync. Each row will only be synced once, based on the `UPDATED` column. |
| Attributes per row | Each row should contain a single user ID and a JSON object with up to 50 attributes. Each key in the JSON object counts as one attribute (i.e., an array counts as one attribute). |
| Data type | You can sync user attributes, events, and purchases through Cloud Data Ingestion. |
| Braze region | This product is available in all Braze regions. Any Braze region can connect to any Snowflake region |
| Snowflake region | You can connect your Snowflake instance in any region or cloud to Braze using this product. |
{: .reset-td-br-1 .reset-td-br-2}

<br><br>
