---
nav_title: FAQ
article_title: Currents FAQ
page_order: 9
page_type: reference
description: "This article addresses some of the most frequently asked questions that arise when setting up Braze Currents."
tool: Currents
---

# Frequently asked questions

> This page provides answers to some frequently asked questions about Currents.

### How do I get historical data?

Currents is a real-time, live data stream, which means that events can't be replayed. However, you can store Currents data in a data warehouse such as [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) or [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), so you can act on past events as you see fit. Data is retained for 30 days, but for more historical data, you can query [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### Why does Currents output data in the Avro format, not JSON?

Avro, unlike schema-less JSON, natively supports schema evolution. You'll also benefit from the ability to send Avro files with less bandwidth and saved storage space because Avro is highly compressible.

### How does Braze handle file overhead?

We build out an Extract, Transform, Load (ETL) process, which lets you pull large amounts of data from one database to place and store in another.

### Where should I store this data for querying?

Braze is partnered with several data warehouses you can store your data in for querying. We recommend using:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).