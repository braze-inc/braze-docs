---
nav_title: Event Delivery Semantics
article_title: Event Delivery Semantics
page_order: 3
page_type: reference
description: "This reference article outlines and defines how Currents manages flat file event data we send to Data Warehouse Storage partners."
tool: Currents

---

# Event delivery semantics

> This page outlines and defines how Currents manages the flat file event data we send to Data Warehouse Storage partners.

Currents for Data Storage is a continuous stream of data from our platform to a storage bucket on one of our data warehouse [partner connections]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/). Currents writes Avro files to your storage bucket at regular thresholds, allowing you to process and analyze the event data with your own Business Intelligence (BI) toolset.

{% alert important %}
This content **only applies to the flat file event data we send to Data Warehouse Storage partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage)**. <br><br>For content that applies to other partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) and check their respective pages.
{% endalert %}

## At-least-once delivery

As a high-throughput system, Currents provides an "at-least-once" delivery of events, meaning that duplicate events can occasionally be written to your storage bucket. This can happen when events are reprocessed from our queue for any reason.

If your use cases require "exactly-once" delivery, you can use the unique identifier field that is sent with every event (`id`) to deduplicate events. Because the file leaves our control when it's written to your storage bucket, we have no way to guarantee deduplication from our end.

## Timestamps

All timestamps exported by Currents are sent in the UTC time zone. For some events where it is available, a time zone field is also included, which delivers the Internet Assigned Numbers Authority (IANA) format of the user's local time zone at the time of the event.

### Latency

Events sent to Braze through SDK or API can include a timestamp from the past. The most notable example is when SDK data gets queued, such as when there isn't mobile connectivity. In that case, the event timestamp will reflect when the event was generated. This means a percentage of events will appear to have high latency.

## Apache Avro format

The Braze Currents data storage integrations output data in the `.avro` format. We chose [Apache Avro](https://avro.apache.org/) because it is a flexible data format that natively supports schema evolution and is supported by a wide variety of data products: 

- Avro is supported by nearly every major data warehouse.
- In the event that you desire to leave your data in S3, Avro compresses better than CSV and JSON, so you pay less for storage and potentially can use less CPU to parse the data.
- Avro requires schemas when data is written or read. Schemas can be evolved over time to handle the addition of fields without breaking.

Currents will create a file for each event type using the following format:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Can't see the code because of the scroll bar? Learn how to fix that [here]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/).
{% endalert %}

|Filename Segment |Definition|
|---|---|
| `<your-bucket-prefix>` | The prefix set for this Currents integration. |
| `<cluster-identifier>` | For internal use by Braze. Will be a string such as "prod-01", "prod-02", "prod-03", or "prod-04". All files will have the same cluster identifier.|
| `<connection-type-identifier>` | The identifier for type of connection. Options are "S3", "AzureBlob", or "GCS". |
| `<integration-id>` | The unique ID for this Currents integration. |
| `<event-type>` | The type of the event in the file. |
| `<date>` | The hour that events are queued in our system for processing in the UTC time zone. Formatted YYYY-MM-DD-HH. |
| `<schema-id>` | Used to version `.avro` schemas for backward-compatibility and schema evolution. Integer. |
| `<zone>` | For internal use by Braze. |
| `<partition>` | For internal use by Braze. Integer. |
| `<offset>`| For internal use by Braze. Integer. Note that different files sent within the same hour will have a different `<offset>` parameter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
File naming conventions may change in the future. Braze recommends searching all keys in your bucket that have a prefix of &lt;your-bucket-prefix&gt;.
{% endalert %}

### Avro write threshold

Under normal circumstances, Braze will write data files to your storage bucket every 5 minutes or 15,000 events, whichever is sooner. Under heavy load, we may write larger data files with as many as 100,000 events per file.

{% alert important %}
Currents will never write empty files.
{% endalert %}

### Avro schema changes

From time to time, Braze may make changes to the Avro schema when fields are added, changed, or removed. For our purposes here, there are two types of changes: breaking and non-breaking. In all cases, the `<schema-id>` will be advanced to indicate the schema was updated. Currents events written to Azure Blob Storage, Google Cloud Storage, and Amazon S3 will write the `<schema-id>` in the path. For example `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`.

#### Non-breaking changes

When a field is added to the Avro schema, we consider this a non-breaking change. Added fields will always be "optional" Avro fields (such as with a default value of `null`), so they will "match" older schemas according to the [Avro schema resolution spec](http://avro.apache.org/docs/current/spec.html#schema+resolution). These additions should not affect existing Extract, Transform, and Load (ETL) processes as the field will simply be ignored until it is added to your ETL process. 

{% alert important %}
We recommend that your ETL setup is explicit about the fields it processes to avoid breaking the flow when new fields are added.
{% endalert %}

While we will strive to give advance warning in the case of all changes, we may include non-breaking changes to the schema at any time.

#### Breaking changes

When a field is removed from or changed in the Avro schema, we consider this a breaking change. Breaking changes may require modifications to existing ETL processes as fields that were in use may no longer be recorded as expected.

All breaking changes to the schema will be communicated in advance of the change.
