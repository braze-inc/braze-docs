---
nav_title: Working with payloads
article_title: Working with payloads
description: "TODO"
page_order: 0.3
---

# Working with payloads

> TODO

## Updating arrays of objects

This example shows how to update a field in an existing array of objects. Let's say we have a source table with the following definition:

```json 
Create table BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list (
    pet_id int IDENTITY(1,1), 
    breed VARCHAR, 
    type VARCHAR, 
    name VARCHAR, 
    owner_id VARCHAR, 
    age int
);
```

In this example, we want to add an array of pets owned by each user, which corresponds to `owner_id`. Specifically, we want to include identification, breed, type, and name. We can use the following query to populate a table or view:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$add', ARRAY_AGG( OBJECT_CONSTRUCT(
                'id',
                pet_id,
                'breed',
                breed,
                'type',
                type,
                'name',
                name
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID;
```

The expected output would look like this:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

Next, to send an updated name field and new age field for each owner, we can use the following query to populate a table or view:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$update', ARRAY_AGG( OBJECT_CONSTRUCT(
                '$identifier_key','id',
                '$identifier_value',pet_id,
                '$new_object',OBJECT_CONSTRUCT(
                    'name',name,
                    'age',age
                )
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID; 
```

The expected output would look like this:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## Removing attributes

To omit an attribute from a user's profile, set the attribute to `null`. Avoid sending it to Braze until it's been updated to prevent accidental updates.

To completely remove an attribute, use `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

## Storing attributes as separate columns

If you prefer to store each attribute in its own column internally, you need to convert those columns to a JSON string to populate the sync with Braze.

To create a JSON string from another table, use a query similar to the following:

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

## Payload templates

Any operations that are possible through the Braze `/users/track` endpoint are supported through Cloud Data Ingestion, including updating nested custom attributes, adding subscription status, and syncing custom events or purchases. 

Fields within the payload should follow the same format as the corresponding `/users/track` endpoint. For detailed formatting requirements, refer to the following:

| Data type | Formatting specifications |
| --------- | ---------| --------- | ----------- |
| `attributes` | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |

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
To sync events, an event name is required. The `time` field should be formatted as an ISO 8601 string or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. If the `time` field is not present, the `UPDATED_AT` column value is used as the event time. Other fields including `app_id` and `properties` are optional. 

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
To sync purchase events, `product_id`, `currency`, and `price` are required. The `time` field, which is optional, should be formatted as an ISO 8601 string or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. If the `time` field is not present, the `UPDATED_AT` column value is used as the event time. Other fields, including `app_id`, `quantity` and `properties` are optional.

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

## Best practices

### Make incremental updates

Make incremental updates to your data so you can prevent unintentional overwrites when simultaneous updates are made.

### Only write new or updated attributes

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Any rows where `UPDATED_AT` is equal to or later than the last `UPDATED_AT` timestamp from the last successful sync job will be selected and pulled into Braze, regardless of whether they are the same as what's currently on the user profile. Given that, we recommend only syncing attributes you want to add or update.

Data point usage is identical using CDI as for other ingestion methods like REST APIs or SDKs, so it is up to you to make sure that you're only adding new or updated attributes into your source tables.

### Use UTC timestamps for `UPDATED_AT`

The `UPDATED_AT` column should be in UTC to prevent issues with daylight savings time. Prefer UTC-only functions, such as `SYSDATE()` instead of `CURRENT_DATE()` whenever possible.

### Set `UPDATED_AT` to after the last sync

Your CDI sync might have duplicate data if any `UPDATED_AT` fields are at the exact same time as the last `UPDATED_AT` timestamp of the previous successful sync job. This is because CDI will choose an "inclusive boundary" when it identifies any row that is the same time as the previous sync, and will make the rows able to sync. CDI will re-ingest those rows and create duplicate data.
 
### Use `UPDATED_AT` timestamps

We use the `UPDATED_AT` timestamp to track what data has been synced successfully to Braze. If many rows are written with the same timestamp while a sync is running, this may lead to duplicate data being synced to Braze. Some suggestions to avoid duplicate data:

- If you're setting up a sync against a `VIEW`, don't use `CURRENT_TIMESTAMP` as the default value. This will cause all data to sync every time the sync runs because the `UPDATED_AT` field will evaluate to the time our queries are run. 
- If you have very long-running pipelines or queries writing data to your source table, avoid running these concurrently with a sync, or avoid using the same timestamp for every row inserted.
- Use a transaction to write all rows that have the same timestamp.

### Separate `EXTERNAL_ID` and `PAYLOAD`

The `PAYLOAD` object should not include an external ID or other ID type.

### Avoid query timeouts

For optimal performance, ensure that queries to your data warehouse are completed within one hour. If queries exceed this timeframe, consider reviewing your data warehouse configuration. Optimizing resources allocated to your warehouse can help improve query execution speed.
