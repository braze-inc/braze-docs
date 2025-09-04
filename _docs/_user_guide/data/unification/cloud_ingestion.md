---
nav_title: Cloud Data Ingestion
article_title: Braze Cloud Data Ingestion
alias: /cloud_ingestion/
description: "This reference article covers Braze Cloud Data Ingestion sources and data setup recommendations."
page_order: 0.1
---

# Braze Cloud Data Ingestion

> Braze Cloud Data Ingestion (CDI) allows you to set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data. When synced to Braze, this data can be leveraged for use cases such as personalization, triggering, or segmentation. 

## About Braze CDI

With Braze Cloud Data Ingestion (CDI), you set up an integration between your data warehouse instance and Braze workspace to sync data on a recurring basis. This sync runs on a schedule you set, and each integration can have a different schedule. Syncs can run as frequently as every 15 minutes or as infrequently as once per month. If you need syncs to occur more frequently than 15 minutes, contact your customer success manager or consider using REST API calls for real-time data ingestion.

When a sync runs, Braze directly connects to your data warehouse instance, retrieves all new data from the specified table, and updates the corresponding data on your Braze dashboard. Each time the sync runs, any updated data will be reflected in Braze.

## How syncing works

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the `UPDATED_AT` column in your table or view. Any rows where `UPDATED_AT` is equal to or later than the last `UPDATED_AT` timestamp from the last successful sync job will be selected and pulled into Braze.

For example, let's say you add the following data to a table in your data warehouse: 

<table>
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_1234</code></td>
      <td>
        <pre>{
  "attribute_1":"abcdefg",
  "attribute_2":{
    "attribute_a":"example_value_2",
    "attribute_b":"example_value_2"
  },
  "attribute_3":"2019-07-16T19:20:30+1:00"
}</pre>
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
        <pre>{
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_5":"testing"
}</pre>
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
        <pre>{
  "attribute_1":"abcdefg",
  "attribute_4":true,
  "attribute_5":"testing_123"
}</pre>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

During the next scheduled sync, all rows with a `UPDATED_AT` timestamp equal to or later than the most recent timestamp will be synced to the Braze user profiles. Fields will be updated or added, so you do not need to sync the full user profile each time.

After the sync, your users will receive the following updates:

<table>
  <thead>
    <tr>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>customer_1234</code></td>
      <td>
        <pre>{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":{
    "attribute_a":"example_value_1",
    "attribute_b":"example_value_2"
  },
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}</pre>
      </td>
    </tr>
    <tr>
      <td><code>customer_3456</code></td>
      <td>
        <pre>{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}</pre>
      </td>
    </tr>
    <tr>
      <td><code>customer_5678</code></td>
      <td>
        <pre>{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}</pre>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Supported sources

CDI supports syncing from the following sources to Braze:

| Source type | Supported sources |
|---|---|
| Data warehouse | Amazon Redshift, Databricks, Google BigQuery, Microsoft Fabric, Snowflake |
| File storage | Amazon S3 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Supported data types

The following data types can be synced:

| Data type | Description |
|---|---|
| User attributes | Key-value properties that describe a user, such as name or location. Example: `"first_name": "Jane"` |
| Nested custom attributes | Structured data within attributes, useful for grouping. Example: `"preferences": {"color":"blue","size":"M"}` |
| Arrays of objects | Lists of structured values tied to a user. Example: `"orders": [{"id":1,"item":"shirt"},{"id":2,"item":"shoes"}]` |
| Subscription statuses | Flags for opt-in/opt-out states for channels like email or SMS. Example: `"email_subscribe": "unsubscribed"` |
| Custom events | Track user actions or interactions. Example: `"event_name": "button_click"` |
| Purchase events | Transactions tied to users. Example: `"product_id": "123", "price": 19.99` |
| Catalog items | Items stored in Braze catalogs for personalization. Example: `"sku": "ABC123", "name": "Winter Jacket"` |
| User delete requests | Remove user records from Braze. Example: `"external_id": "customer_1234"` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Example queries

We provide a [GitHub repository](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) with sample queries and snippets for Cloud Data Ingestion. You can use these examples to model your own setup or contribute new ones by opening a pull request.

## CDI rate limits {#rate-limit}

Data point billing for Cloud Data Ingestion is equivalent to billing for updates through the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Refer to [Data points]({{site.baseurl}}/user_guide/data/data_points/) for more information. 

{% alert important %}
Braze Cloud Data Ingestion counts toward the available rate limit, so if you're sending data using another method, the rate limit is combined between the Braze API and Cloud Data Ingestion.
{% endalert %}

## Product limitations

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of integrations | There is no limit on how many integrations you can set up. However, you will only be able to set up one integration per table or view.                                             |
| Number of rows         | By default, each run can sync up to 500 million rows. Any syncs with more than 500 million new rows will be stopped. If you need a higher limit than this, contact your Braze customer success manager or Braze Support. |
| Attributes per row     | Each row should contain a single user ID and a JSON object with up to 250 attributes. Each key in the JSON object counts as one attribute (that is, an array counts as one attribute). |
| Payload size           | Each row can contain a payload of up to 1 MB. Payloads greater than 1&nbsp;MB will be rejected, and the error "Payload was greater than 1MB" will be logged to the sync log along with the associated external ID and truncated payload. |
| Data type              | You can sync user attributes, events, and purchases through Cloud Data Ingestion.                                                                                                  |
| Braze region           | This product is available in all Braze regions. Any Braze region can connect to any source data region.                                                                              |
| Source region       | Braze will connect to your data warehouse or cloud environment in any region or cloud provider.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
