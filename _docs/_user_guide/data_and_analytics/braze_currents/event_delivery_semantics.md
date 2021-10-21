---
nav_title: Event Delivery Semantics
article_title: Event Delivery Semantics
page_order: 3
page_type: reference
description: "This reference article outlines how Currents manages flat file event data we send to Data Warehouse partners."
tool: Currents

---

# Event delivery semantics

> This article outlines how Currents manages flat file event data we send to Data Warehouse partners.

Currents for Data Storage is a continuous streams of data from our platform to a storage bucket on one of our [data warehouse partner connections]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

Currents writes Avro files to your storage bucket at regular thresholds, allowing you to process and analyze the event data using your own Business Intelligence toolset.

{% alert important %}
Please note that this content **only applies to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage)**. For content that applies to the other partners, please check [their respective pages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).
{% endalert %}


## At-Least-Once Delivery

As a high-throughput system, Currents guarantees "at-least-once" delivery of events, meaning that duplicate events can occasionally be written to your storage bucket. This can happen when events are reprocessed from our queue for any reason.

If your use cases require exactly-once delivery, you can use the unique identifier field that is sent with every event (`id`) to deduplicate events. Since the file leaves our control once it's written to your storage bucket, we have no way to guarantee deduplication from our end.

## Timestamps

all timestamps exported by currents are sent in the utc time zone. for some events where it is available, a time zone field is also included, which delivers the iana format of the user's local time zone at the time of the event.

## Avro

the braze currents data storage integrations output data in the `.avro` format. we chose [avro](https://avro.apache.org/) because it is a flexible data format that natively supports schema evolution and is supported by a wide variety of data products:

-   Avro is supported by nearly every major data warehouse.
-   In the event that you desire to leave your data in S3, Avro compresses better than CSV and JSON, so you pay less for storage and potentially can use less CPU to parse the data.
-   Avro requires schemas when data is written or read. Schemas can be evolved over time to handle the addition of fields without breaking.

Currents will create a file for each event type using the format below:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

_Can't see the code because of the scroll bar? See how to fix that [here]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._

|Filename Segment |Definition|
|---|---|
| `<your-bucket-prefix>` | The prefix set for this Currents integration. |
| `<cluster-identifier>` | For internal use by Braze. Will be a string such as "prod-01", "prod-02", "prod-03", or "prod-04". All files will have the same cluster identifier.|
| `<connection-type-identifier>` | The identifier for type of connection. Options are "S3", "AzureBlob", or "GCS". |
| `<integration-id>` | The unique ID for this Currents integration. |
| `<event-type>` | The type of the event in the file (see event list below). |
| `<date>` | The hour that events are queued in our system for processing. Formatted YYYY-MM-DD-HH. |
| `<schema-id>` | Used to version `.avro` schemas for backward-compatibility and schema evolution. Integer. |
| `<zone>` | For internal use by Braze. Single letter. |
| `<partition>` | For internal use by Braze. Integer. |
| `<offset>`| For internal use by Braze. Integer. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
File naming conventions may change in the future, Braze recommends searching all keys in your bucket that have a prefix of &lt;your-bucket-prefix&gt;.
{% endalert %}

### Avro write threshold

Data files will be written to your storage bucket once you hit _any of the set thresholds_, whichever happens first:

| Partner | Write Threshold |
|---|---|
| Amazon AWS S3 | Every 5 minutes. <br> Every 15,000 events. |
| Microsoft Azure Blob Storage | Every 5 minutes. <br> Every 15,000 events. |
| Google Cloud Storage | Every 5 minutes. <br> Every 15,000 events. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Currents will never write empty files.
{% endalert %}

### Avro schema changes

From time to time, Braze may make changes to the Avro schema when fields are added, changed, or removed. For our purposes here, there are two types of changes: breaking and non-breaking. In all cases, the `<schema-id>` will be advanced to indicate the schema was updated.

#### Non-breaking Changes

When a field is added to the Avro schema, we consider this a non-breaking change. Added fields will always be "optional" Avro fields (i.e. with a default value of `null`), so they will "match" older schemas according to the [Avro schema resolution spec](http://avro.apache.org/docs/current/spec.html#schema+resolution). These additions should not affect existing ETL processes as the field will simply be ignored until it is added to your ETL process. 

{% alert important %}
We recommend that your ETL setup is explicit about the fields it processes to avoid breaking the flow when new fields are added.
{% endalert %}

While we will strive to give advance warning in the case of all changes, we may include non-breaking changes to the schema at any time.

#### Breaking changes

When a field is removed from or changed in the Avro schema, we consider this a breaking change. Breaking changes may require modifications to existing ETL processes as fields that were in use may no longer be recorded as expected.

All breaking changes to the schema will be communicated in advance of the change.
