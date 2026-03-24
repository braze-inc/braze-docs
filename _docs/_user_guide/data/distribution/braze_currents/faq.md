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

### How reliable is Currents data?

Currents guarantees "at-least-once" delivery, meaning duplicate events can occasionally be written to your storage bucket. If your use case requires exactly-once delivery, you can deduplicate events using the unique identifier field (`id`) sent with every event. For more details, refer to [Event delivery semantics]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### How often is data synced to Currents?

Data is continuously streamed. Braze sends a batch of events every time there is a full batch to send, or every 5 minutes, whichever comes first. For high-volume connectors, data arrives close to real-time. For low-volume connectors, expect data to arrive within 5 to 30 minutes. For more details, refer to [Avro write threshold]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
If a device isn't connected to the internet, there may be a delay in creating the event. This is most common for in-app message events, since in-app messages can be triggered offline.
{% endalert %}

### How do I find which events are available for Currents?

For a full list of events that Currents logs, refer to the [Customer behavior events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) and [Message engagement events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) glossaries. You can filter these glossaries by event type (such as sends, deliveries, or opens).

### Are all send events logged to Currents?

All events are logged to Currents. There are no scenarios where an event would be intentionally suppressed from the Currents stream.

### Can data be corrupted in Currents?

Under normal circumstances, Currents data is not corrupted. While there is always a possibility of a rare issue, there are no known conditions under which data would be systematically corrupted.

### Why do I see custom event data dated before my Currents integration was set up?

Braze does not backfill events to Currents. However, custom events can be logged with a past timestamp (for example, if a device was offline when the event occurred and synced later). In these cases, the event timestamp reflects when the event originally occurred, which may be before the Currents integration was configured.

### Can I include custom attributes in Currents send events?

No. Currents does not include custom attributes in send events. Currents logs custom events and message engagement events. For a complete list of available fields, refer to the [event glossaries]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/).

### Does Currents include campaign tags or key-value pairs?

No. Currents does not include campaign tags or message-level key-value pairs. As a workaround, you can use a webhook channel in the campaign to send this information to your own endpoint, using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) to template the tag and key-value pair data.

### How does Braze notify customers of changes to Currents?

When Currents changes occur (such as new event fields or event types), Braze sends an email to all customers with active Currents integrations who have used the dashboard within the past 30 days. You can also refer to the [Currents changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) for latest changes.

### How much storage do I need for Currents data?

Storage requirements depend on your event volume and the types of events you're exporting. Braze provides [sample events in Avro format](https://github.com/braze-inc/currents-examples/tree/master/sample-data) that you can use to estimate file sizes for your use case.

### Why is the campaign name or Canvas step name `NULL` in my Currents data?

When you create a new campaign or Canvas, the name may take some time to propagate through all Braze systems. Events sent through Currents during this window may have `NULL` in the name fields (such as `campaign_name` or `canvas_step_name`). This is also expected if the name was modified shortly before the events were logged. To avoid this, allow some time after creating or renaming a campaign or Canvas step before sending.

### What happens if my storage bucket is unavailable when Currents tries to write data?

If your storage bucket is unavailable at the time of data transfer, that data is lost. Braze is not able to backfill events that were not successfully delivered. To avoid data loss, ensure your storage bucket is available and properly configured at all times.

### How often does the schema ID update?

Schema IDs are global across all event types and increment sequentially. Updates can occur at any time, and Braze will notify customers by email about upcoming changes. Each time a schema update occurs for any event type, the next available global ID is assigned. We recommend reading files recursively from the root path to handle schema ID changes. For more details, refer to [Avro schema changes]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-schema-changes).