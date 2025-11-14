---
nav_title: Cloud Data Ingestion
article_title: Braze Cloud Data Ingestion
alias: /cloud_ingestion/
description: "This reference article covers Braze Cloud Data Ingestion sources and data setup recommendations."
page_order: 0.1
toc_headers: h2
---

# Braze Cloud Data Ingestion

> Braze Cloud Data Ingestion (CDI) allows you to set up a direct connection from your data storage solution to sync relevant user data and other non-user data to Braze. This data can then be used for personalization or segmentation to power your marketing use cases. Cloud Data Ingestion’s flexible integration supports complex data structures, including nested JSON and arrays of objects.

## How it works

With Braze Cloud Data Ingestion (CDI), you set up an integration between your data warehouse instance and Braze workspace to sync data on a recurring basis. This sync runs on a schedule you set, and each integration can have a different schedule. Syncs can run as frequently as every 15 minutes or as infrequently as once per month. If you need syncs to occur more frequently than 15 minutes, contact your customer success manager or consider using REST API calls for real-time data ingestion.

When a sync runs, Braze directly connects to your data warehouse instance, retrieves all new data from the specified table, and updates the corresponding data on your Braze dashboard. Each time the sync runs, any updated data will be reflected in Braze.

## Use cases

With Braze Cloud Data Ingestion capabilities, you can:

- Create a simple integration directly from your data warehouse or file storage solution to Braze in just a few minutes.
- Securely sync user data, including attributes, events, and purchases from your data warehouse to Braze.
- Close the data loop with Braze by combining Cloud Data Ingestion with Currents or Snowflake Data Sharing.

In addition, [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) are a zero-copy alternative. You can have Braze directly query your data warehouse or file storage solution to construct CDI segments &#8212;all without copying the underlying data to Braze.

## Supported data sources

Cloud Data Ingestion can sync data from:

   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Supported data types 

Cloud Data Ingestion supports the following data types:

### User data
- User attributes, including:
   - Nested custom attributes
   - Arrays of objects
   - Subscription statuses
- Custom events
- Purchase events
- User deletion requests

### Non-user objects
- Catalog items

### Zero-copy messaging
- Connected Sources

## Data point usage

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

