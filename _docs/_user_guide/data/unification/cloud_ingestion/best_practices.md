---
nav_title: Best practices
article_title: Cloud Data Ingestion Best Practices
toc_headers: h2
page_order: 0
page_type: reference
description: "This page provides an overview of Cloud Data Ingestion, best practices, and product limitations."

---

# Best practices

> Braze Cloud Data Ingestion allows you to set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data. When you sync this data to Braze, you can leverage it for use cases such as personalization, triggering, or segmentation. 

## Understanding the `UPDATED_AT` column

{% alert note %}
`UPDATED_AT` is relevant for data warehouse integrations only, not for S3 syncs.
{% endalert %}

When a sync runs, Braze directly connects to your data warehouse instance, retrieves all new data from the specified table, and updates the corresponding data on your Braze dashboard. Each time the sync runs, Braze reflects any updated data.

{% alert important %}
Braze CDI will sync rows strictly based on the `UPDATED_AT` value, regardless of whether the row content is the same as what’s currently in Braze. Given that, we recommend using `UPDATED_AT` properly to only sync new or updated data to avoid unnecessary data point usage.
{% endalert %}

### Example: Recurring sync

To illustrate how `UPDATED_AT` is used in a CDI sync, consider this example recurring sync for updating user attributes:

- File storage sources 
   - Amazon S3

## Supported data types 

Cloud Data Ingestion supports the following data types: 
- User attributes, including:
   - Nested custom attributes
   - Arrays of objects
   - Subscription statuses
- Custom events
- Purchase events
- Catalog items
- User delete requests

You can update user data by external ID, user alias, Braze ID, email, or phone number. You can delete users by external ID, user alias, or Braze ID. 

## What gets synced

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Braze selects and imports any rows where `UPDATED_AT` is equal to or later than the last `UPDATED_AT` timestamp from the last successful sync job.

In your data warehouse, add the following users and attributes to your table, setting the `UPDATED_AT` time to the time you add this data:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2": {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_a":"example_value_1",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_b":"example_value_1"<br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

During the next scheduled sync, Braze syncs all rows with a `UPDATED_AT` timestamp equal to or later than the most recent timestamp to user profiles. Braze updates or adds fields, so you do not need to sync the full user profile each time. After the sync, user profiles reflect the new updates:

**Recurring sync, second run on July 20, 2022 at 12 pm**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2": {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_a":"example_value_2",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_b":"example_value_2"<br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":false,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

A row was added, but the `UPDATED_AT` value is earlier than `2022-07-19 09:07:23` (stored from the first run). As a result, none of these rows will be synced in this run. The last `UPDATED_AT` for the sync is unchanged by this run, and remains as  `2022-07-19 09:07:23`.

**Recurring sync, third run on July 21, 2022 at 12 pm**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2": {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_a":"example_value_1",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_b":"example_value_1"<br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"xyz",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":false,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |
| `2022-07-21 08:30:00` | `customer_1234` | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2": {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_a":"example_value_2",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"attribute_b":"example_value_2"<br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3”:”2019-07-20T19:20:30+1:00"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In this third run, another new row was added. Now, one row has an `UPDATED_AT` value later than `2022-07-19 09:07:23`, which means only one row will sync. The last `UPDATED_AT` is now set as `2022-07-21 08:30:00`.

{% alert note %}
`UPDATED_AT` values are allowed to be even later than the run start time for a given sync. However, this is not recommended as it pushes the last `UPDATED_AT` timestamp "into the future" and subsequent syncs will not sync earlier values.
{% endalert %}

## Use a UTC timestamp for the `UPDATED_AT` column

The `UPDATED_AT` column should be in UTC to prevent issues with daylight savings time. Prefer UTC-only functions, such as `SYSDATE()` instead of `CURRENT_DATE()` whenever possible.

## Make sure the `UPDATED_AT` time isn’t the same time as your sync

Your CDI sync might have duplicate data if any `UPDATED_AT` fields are at the exact same time as the last `UPDATED_AT` timestamp of the previous successful sync job. This is because CDI will choose an "inclusive boundary" when it identifies any row that is the same time as the previous sync, and will make the rows able to sync. CDI will re-ingest those rows and create duplicate data.

Here are some suggestions to avoid duplicate data:

- If you’re setting up a sync against a `VIEW`, don’t use `CURRENT_TIMESTAMP` as the default value. This will cause all data to sync every time the sync runs because the `UPDATED_AT` field will evaluate to the time our queries are run.
- If you have very long-running pipelines or queries writing data to your source table, avoid running these concurrently with a sync, or avoid using the same timestamp for every row inserted.
- Use a transaction to write all rows that have the same timestamp.

### Example: Managing subsequent updates

This example shows the general process for syncing data for the first time, then only updating changing data (deltas) in the subsequent updates. Let's say we have a table `EXAMPLE_DATA` with some user data. On day 1, it has the following values:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

To get this data into the format that CDI expects, you could run the following query:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

None of this has synced to Braze before, so add all of it to the source table for CDI:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

A sync runs, and Braze records that you synced all available data up until “2023-03-16 15:00:00”. Then, on the morning of day 2, you have an ETL that runs and some fields in your users table are updated (highlighted):

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">red</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Now you need to add only the changed values into the CDI source table. These rows can be appended rather than updating the old rows. That table now looks like this:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 12345       | { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} |
| 2023-03-17 09:30:00 | 23456       | { "ATTRIBUTE_1": "15"} |
| 2023-03-17 09:30:00 | 34567       | { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 45678       | { "ATTRIBUTE_2":"green"} |
| 2023-03-17 09:30:00 | 56789       | { "ATTRIBUTE_3":"693"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

CDI will only sync the new rows, so the next sync that runs will only sync the last five rows.

## Additional tips

### Only write new or updated attributes to minimize consumption

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Braze selects and imports any rows where `UPDATED_AT` is equal to or later than the last `UPDATED_AT` timestamp from the last successful sync job, regardless of whether they are the same as what's currently on the user profile. Given that, we recommend only syncing attributes you want to add or update.

Data point usage is identical using CDI as for other ingestion methods like REST APIs or SDKs, so it is up to you to make sure that you're only adding new or updated attributes into your source tables.

### Separate `EXTERNAL_ID` from `PAYLOAD` column

The `PAYLOAD` object should not include an external ID or other ID type. 

### Remove an attribute

You can set it to `null` if you want to omit an attribute from a user's profile. If you want an attribute to remain unchanged, don't send it to Braze until it's been updated. To completely remove an attribute, use `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Make incremental updates

Make incremental updates to your data so you can prevent unintentional overwrites when simultaneous updates are made.

In the following example, a user has two attributes:
- Color: "Green"
- Size: "Large"

Then Braze receives the following two updates to that user simultaneously:
- Request 1: Change color to "Red"
- Request 2: Change size to "Medium"

Because Request 1 occurs first, the user's attributes are updated to the following:
- Color: "Red"
- Size: "Large"

However, when Request 2 occurs, Braze starts with the original attribute values ("Green" and "Large"), then updates the user's attributes to the following:
- Color: "Green"
- Size: "Medium"

When the requests are finished, Request 2 will overwrite the update from Request 1, so it's best to stagger your updates so you can prevent requests from being overwritten.

### Create a JSON string from another table

If you prefer to store each attribute in its own column internally, you need to convert those columns to a JSON string to populate the sync with Braze. To do that, you can use a query like:

{% tabs local %}
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
    JSON_SERIALIZE(
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
{% tab BigQuery %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Use the `UPDATED_AT` timestamp

We use the `UPDATED_AT` timestamp to track what data has been synced successfully to Braze. If many rows are written with the same timestamp while a sync is running, this may lead to duplicate data being synced to Braze. Some suggestions to avoid duplicate data:
- If you're setting up a sync against a `VIEW`, don't use `CURRENT_TIMESTAMP` as the default value. This will cause all data to sync every time the sync runs because the `UPDATED_AT` field will evaluate to the time our queries are run. 
- If you have very long-running pipelines or queries writing data to your source table, avoid running these concurrently with a sync, or avoid using the same timestamp for every row inserted.
- Use a transaction to write all rows that have the same timestamp.

### Table configuration

We have a public [GitHub repository](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) for customers to share best practices or code snippets. To contribute your own snippets, create a pull request!

### Data formatting

Any operations that are possible through the Braze `/users/track` endpoint are supported through Cloud Data Ingestion, including updating nested custom attributes, adding subscription status, and syncing custom events or purchases. 

Fields within the payload should follow the same format as the corresponding `/users/track` endpoint. For detailed formatting requirements, refer to the following:

| Data type | Formatting specifications |
| --------- | ---------| --------- | ----------- |
| `attributes` | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Note the special requirement for [capturing dates]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) in nested attributes. 

{% tabs local %}
{% tab Nested Custom Attributes %}
You may include nested custom attributes in the payload column for a custom attributes sync. 

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Event %}
To sync events, an event name is required. Format the `time` field as an ISO 8601 string or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. If the `time` field is not present, Braze uses the `UPDATED_AT` column value as the event time. Other fields including `app_id` and `properties` are optional. 

Note that you can only sync one event per row.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab Purchase %}
To sync purchase events, `product_id`, `currency`, and `price` are required. Format the `time` field, which is optional, as an ISO 8601 string or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. If the `time` field is not present, Braze uses the `UPDATED_AT` column value as the event time. Other fields, including `app_id`, `quantity` and `properties` are optional.

Note that you can only sync one purchase event per row.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
    }
}
```

{% endtab %}
{% tab Subscription Groups %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### Avoid timeouts for data warehouse queries

We recommend that queries be completed within one hour for optimal performance and to avoid potential errors. If queries exceed this timeframe, consider reviewing your data warehouse configuration. Optimizing resources allocated to your warehouse can help improve query execution speed.

## Product limitations

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of integrations | There is no limit on how many integrations you can set up. However, you will only be able to set up one integration per table or view.                                             |
| Number of rows         | By default, each run can sync up to 500 million rows. Braze stops any syncs with more than 500 million new rows. If you need a higher limit than this, contact your Braze customer success manager or Braze Support. |
| Attributes per row     | Each row should contain a single user ID and a JSON object with up to 250 attributes. Each key in the JSON object counts as one attribute (that is, an array counts as one attribute). |
| Payload size           | Each row can contain a payload of up to 1 MB. Braze rejects payloads greater than 1&nbsp;MB and logs the error "Payload was greater than 1MB" to the sync log along with the associated external ID and truncated payload. |
| Data type              | You can sync user attributes, events, and purchases through Cloud Data Ingestion.                                                                                                  |
| Braze region           | This product is available in all Braze regions. Any Braze region can connect to any source data region.                                                                              |
| Source region       | Braze will connect to your data warehouse or cloud environment in any region or cloud provider.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
